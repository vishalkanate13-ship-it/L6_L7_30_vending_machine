
import pytest

from vending_machine import select_item, make_change, purchase


# Test select_item function

def test_invalid_item():
    assert select_item("water", {"water": 5}, 200) == "invalid"


def test_sold_out_item():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_insufficient_credit():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"


def test_valid_item():
    assert select_item("cola", {"cola": 5}, 150) == "ok"


# Test make_change function

def test_negative_amount():
    with pytest.raises(ValueError):
        make_change(-10)


def test_exact_change():
    assert make_change(40) == [25, 10, 5]


def test_no_exact_change():
    assert make_change(3) is None


# Test purchase function

def test_purchase_invalid_item():
    stock = {"cola": 5}
    assert purchase("water", stock, 200) == ("invalid", [])


def test_purchase_sold_out():
    stock = {"cola": 0}
    assert purchase("cola", stock, 200) == ("sold_out", [])


def test_purchase_insufficient_credit():
    stock = {"cola": 5}
    assert purchase("cola", stock, 100) == ("insufficient", [])


def test_purchase_no_exact_change():
    stock = {"cola": 5}
    assert purchase("cola", stock, 151) == ("no_exact_change", [])
    assert stock["cola"] == 5


def test_successful_purchase():
    stock = {"cola": 5}
    result = purchase("cola", stock, 200)

    assert result == ("dispensed", [50])
    assert stock["cola"] == 4
