"""Thin UI over the supplied class-05 application; no server starts on import."""

import logging
import secrets

from openai import APIError
import streamlit as st

from report_app.analysis import summarize
from report_app.evaluation import EVALUATION_CASES
from report_app.harness import run
from report_app.provider import make_live_request, make_replay
from report_app.source import load_observations, read_fixture

APP_TITLE = "Saved population explorer"
RELEASE = "06.0"
logger = logging.getLogger("data_explorer")


def show_result(result):
    """Show only the application's safe result/trace, never provider history."""
    if result["outcome"] == "answered":
        st.write(result["answer"])
    else:
        st.warning(f"Run stopped: {result['outcome']}. Inspect the saved tests/logs.")
    st.caption(
        f"Mode: {result['mode']}; requests: {result['model_requests']}; "
        f"tools executed: {result['tool_executions']}"
    )
    with st.expander("Application events"):
        st.json(result["trace"])


def show_ai():
    """Replay is public; live use needs explicit private server configuration."""
    st.subheader("Optional AI examples")
    st.caption(
        "These examples query the whole saved snapshot, independently of the filter. "
        "Replay is a fixed illustrative script, not a model or a live recording."
    )
    case = st.selectbox("Example", EVALUATION_CASES)
    script = read_fixture(f"replays/{case}.json")
    st.write(script["prompt"])
    if st.button("Run saved example"):
        st.session_state.replay_case = case
        st.session_state.replay_result = run(script["prompt"], make_replay(case))
    if st.session_state.get("replay_case") == case:
        show_result(st.session_state.replay_result)

    try:
        settings = dict(st.secrets.get("ai", {}))
    except FileNotFoundError:
        settings = {}
    if settings.get("enabled") is not True:
        st.info("Live AI is disabled. The data explorer and saved examples still work.")
        return
    required = ("model", "api_key", "access_code")
    if (
        any(
            not isinstance(settings.get(name), str) or not settings[name].strip()
            for name in required
        )
        or len(settings["access_code"]) < 16
    ):
        logger.warning("live_ai_unavailable reason=incomplete_configuration")
        st.warning("Live AI configuration is incomplete. Use a saved example.")
        return

    # This classroom gate is not identity management or a global spending quota.
    # Host live demonstrations privately; see DEPLOYMENT.md before enabling them.
    with st.expander("Private instructor live demonstration"):
        code = st.text_input("Instructor access code", type="password")
        authorized = secrets.compare_digest(
            code.encode(), settings["access_code"].encode()
        )
        used = st.session_state.get("live_used", False)
        st.caption("One run per browser session; at most three model requests per run.")
        clicked = st.button("Run live example", disabled=not authorized or used)
        if clicked and authorized and not used:
            # Failures also consume this session's run; enforce the cap in Python.
            st.session_state.live_used = True
            try:
                request = make_live_request(
                    model=settings["model"], api_key=settings["api_key"]
                )
                result = run(script["prompt"], request, mode="live")
                st.session_state.live_case = case
                st.session_state.live_result = result
                logger.info(
                    "ai_finished outcome=%s requests=%d tools=%d",
                    result["outcome"],
                    result["model_requests"],
                    result["tool_executions"],
                )
            except (ValueError, APIError) as exc:
                logger.warning("live_ai_unavailable kind=%s", type(exc).__name__)
                st.warning("Live AI could not start. Use a saved example.")
        if st.session_state.get("live_case") == case:
            show_result(st.session_state.live_result)


def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s %(message)s")
    st.set_page_config(page_title=APP_TITLE)
    st.title(APP_TITLE)
    st.caption(f"Release {RELEASE} · Saved 2023 population data · Units: persons")
    try:
        records = load_observations()
    except (OSError, ValueError) as exc:
        logger.error("data_load_failed kind=%s", type(exc).__name__)
        st.error(
            "Saved data could not be loaded. Restore the supplied fixtures folder."
        )
        return
    selected = st.selectbox(
        "Country label", ["All countries", *(r.label for r in records), "FRA:2023"]
    )
    visible = [r for r in records if selected == "All countries" or r.label == selected]
    if visible:
        summary = summarize(visible)
        st.metric("Total population (persons)", f"{summary['total']:,.0f}")
        st.dataframe([r.model_dump() for r in visible], hide_index=True)
    else:
        st.info("No observation in this snapshot for that label. Missing is not zero.")
    logger.info("view release=%s rows=%d", RELEASE, len(visible))
    st.caption(
        "Source: World Bank, World Development Indicators, Population, total "
        "(SP.POP.TOTL), Spain and Portugal, 2023; retrieved 19 November 2026. "
        "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). "
        "[Data and terms](https://data.worldbank.org/indicator/SP.POP.TOTL). "
        "Values may be revised; this is not live data or a world total."
    )
    show_ai()


if __name__ == "__main__":
    main()
