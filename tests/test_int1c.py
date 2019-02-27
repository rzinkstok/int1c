import pytest
from int1c import Int1C


def test_values():
    x = Int1C(12)
    assert x.value == 12
    assert x.bits == "0000000000001100"

    x = Int1C(-5)
    assert x.value == -5
    assert x.bits == "1111111111111010"

    x = Int1C("0000000001010101")
    assert x.value == 85
    assert x.bits == "0000000001010101"

    x = Int1C(4, 4)
    assert x.width == 4
    assert len(x.bits) == 4
    assert x.value == 4
    assert x.bits == "0100"

    with pytest.raises(ValueError):
        x = Int1C(11, 4)

    with pytest.raises(ValueError):
        x = Int1C("01010", 4)


def test_complement():
    x = Int1C(85)
    y = ~x
    assert y.value == -x.value


def test_negative():
    x = Int1C(-48)
    y = -x
    assert y.value == -x.value


def test_absolute():
    x = Int1C(-5)
    y = abs(x)
    assert y.value == -x.value

    x = Int1C(14)
    y = abs(x)
    assert y.value == x.value


def test_add():
    x = Int1C(3)
    y = Int1C(12)
    z = x + y
    assert z.value == 15

    x = Int1C(-36)
    y = Int1C(63)
    z = x + y
    assert z.value == 27

    x = Int1C(7, 4)
    y = Int1C(1, 4)
    with pytest.raises(OverflowError):
        z = x + y

    x = Int1C(-6, 4)
    y = Int1C(-3, 4)
    with pytest.raises(OverflowError):
        z = x + y


def test_lshift():
    x = Int1C(25)
    y = x.lshift(1)
    assert y.value == 50


def test_rshift():
    x = Int1C(25)
    y = x.rshift(1)
    assert y.value == 12


