import pytest

from babel.babel import Library


@pytest.fixture
def library():
	return Library()