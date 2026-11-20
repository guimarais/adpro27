"""Exercise the real Streamlit script without a browser or live service."""

from pathlib import Path
from unittest.mock import Mock

from streamlit.testing.v1 import AppTest

from report_app import provider

APP = Path(__file__).resolve().parents[1] / "streamlit_app.py"


def test_default_app_filters_saved_data_and_keeps_absence_distinct(monkeypatch):
    forbidden = Mock(
        side_effect=AssertionError("Default UI must not construct a client")
    )
    monkeypatch.setattr(provider, "OpenAI", forbidden)
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception
    assert app.metric[0].value == "58,930,702"
    app.selectbox[0].select("PRT:2023").run()
    assert app.metric[0].value == "10,578,174"
    app.selectbox[0].select("FRA:2023").run()
    assert not app.metric
    assert any("Missing is not zero" in message.value for message in app.info)
    forbidden.assert_not_called()


def test_saved_ai_button_runs_shared_harness_without_enabling_live(monkeypatch):
    forbidden = Mock(side_effect=AssertionError("Replay must not construct a client"))
    monkeypatch.setattr(provider, "OpenAI", forbidden)
    app = AppTest.from_file(str(APP)).run()
    app.button[0].click().run()
    assert not app.exception
    result = app.session_state.replay_result
    assert result["mode"] == "replay"
    assert result["tool_executions"] == 1
    assert "10,578,174" in result["answer"]
    assert any("disabled" in message.value for message in app.info)
    app.selectbox[1].select("missing").run()
    assert not app.json  # Do not show the previous case's trace under a new prompt.
    app.button[0].click().run()
    assert "absent" in app.session_state.replay_result["answer"]
    forbidden.assert_not_called()


def test_missing_data_shows_recovery_and_safe_log(monkeypatch, caplog):
    from report_app import source

    monkeypatch.setattr(
        source, "load_observations", Mock(side_effect=ValueError("PRIVATE"))
    )
    app = AppTest.from_file(str(APP)).run()
    assert not app.exception
    assert "Restore the supplied fixtures" in app.error[0].value
    assert "data_load_failed kind=ValueError" in caplog.text
    assert "PRIVATE" not in caplog.text


def test_enabled_but_incomplete_ai_keeps_data_available():
    app = AppTest.from_file(str(APP))
    app.secrets["ai"] = {"enabled": True}
    app.run()
    assert not app.exception
    assert app.metric[0].value == "58,930,702"
    assert "incomplete" in app.warning[0].value
    assert len(app.button) == 1


def test_live_gate_and_one_run_limit_without_real_model(monkeypatch, caplog):
    def fake_live(**kwargs):
        assert kwargs == {"model": "test-model", "api_key": "PRIVATE-KEY"}
        return provider.make_replay("portugal")

    spy = Mock(side_effect=fake_live)
    monkeypatch.setattr(provider, "make_live_request", spy)
    app = AppTest.from_file(str(APP))
    app.secrets["ai"] = {
        "enabled": True,
        "model": "test-model",
        "api_key": "PRIVATE-KEY",
        "access_code": "private-code-123456",
    }
    app.run()
    assert app.button[1].disabled
    app.text_input[0].set_value("incorrect").run()
    assert app.button[1].disabled
    spy.assert_not_called()
    app.text_input[0].set_value("private-code-123456").run()
    assert not app.button[1].disabled
    app.button[1].click().run()
    assert not app.exception
    assert app.session_state.live_result["outcome"] == "answered"
    assert app.session_state.live_result["mode"] == "live"
    # Mode names describe application branches; this test uses an illustrative script.
    # A stale button event must not bypass the cap enforced in Python.
    app.button[1].click().run()
    assert spy.call_count == 1
    app.run()
    assert app.button[1].disabled
    assert spy.call_count == 1
    assert "PRIVATE-KEY" not in caplog.text
    assert "private-code-123456" not in caplog.text


def test_live_failure_consumes_run_and_does_not_expose_exception(monkeypatch, caplog):
    monkeypatch.setattr(
        provider, "make_live_request", Mock(side_effect=ValueError("PRIVATE-KEY"))
    )
    app = AppTest.from_file(str(APP))
    app.secrets["ai"] = {
        "enabled": True,
        "model": "test-model",
        "api_key": "PRIVATE-KEY",
        "access_code": "private-code-123456",
    }
    app.run()
    app.text_input[0].set_value("private-code-123456").run()
    app.button[1].click().run()
    app.run()
    assert not app.exception
    assert app.button[1].disabled
    assert "PRIVATE-KEY" not in caplog.text


def test_invalid_ai_flag_does_not_enable_live():
    app = AppTest.from_file(str(APP))
    app.secrets["ai"] = {"enabled": "true"}
    app.run()
    assert not app.exception
    assert len(app.button) == 1
