
import pytest

def test_div_zero_exception():
    with pytest.raises(ZeroDivisionError):
        x = 10 / 0

def test_keyerror_details():
    my_map = {'foo': 'bar'}

    with pytest.raises(KeyError) as ke:
        baz = my_map['baz']

    assert "baz" in str(ke)

def test_approximate_matches():
    assert 0.1 + 0.2 == pytest.approx(0.3)
