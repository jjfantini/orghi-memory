"""Test orghi-memory REST API."""

import httpx
from fastapi.testclient import TestClient

from orghi_memory.api import app

client = TestClient(app)


def test_read_root() -> None:
    """Test that reading the root is successful."""
    response = client.get("/")
    assert httpx.codes.is_success(response.status_code)
