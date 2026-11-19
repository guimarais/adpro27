"""No test may reach a real HTTP service; explicit MockTransport remains usable."""

import httpx
import pytest


@pytest.fixture(autouse=True)
def block_real_http(monkeypatch):
    def blocked(*args, **kwargs):
        raise AssertionError("Real HTTP is forbidden in the default test suite.")

    monkeypatch.setattr(httpx.HTTPTransport, "handle_request", blocked)
