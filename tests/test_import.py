"""Test orghi-memory."""

import orghi_memory


def test_import() -> None:
    """Test that the package can be imported."""
    assert isinstance(orghi_memory.__name__, str)
