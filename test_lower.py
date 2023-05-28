import pytest

from lower import lowercase_string

def test_lower_string():
    assert lowercase_string('HELLO WORLD') == 'hello world'