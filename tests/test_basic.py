"""Test basic gfql package imports and metadata."""

import gfql


def test_import():
    """Test that gfql can be imported."""
    assert gfql is not None


def test_version():
    """Test that version is defined."""
    assert hasattr(gfql, "__version__")
    assert isinstance(gfql.__version__, str)
    assert gfql.__version__ == "0.1.0"


def test_author():
    """Test that author is defined."""
    assert hasattr(gfql, "__author__")
    assert isinstance(gfql.__author__, str)


def test_license():
    """Test that license is defined."""
    assert hasattr(gfql, "__license__")
    assert isinstance(gfql.__license__, str)
    assert gfql.__license__ == "BSD-3-Clause"
