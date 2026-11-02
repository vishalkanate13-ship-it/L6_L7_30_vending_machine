
import pytest

from vending_machine import select_item, make_change, purchase


# select_item: test all decision outcomes

def test_select_item_invalid():
    assert select_item("water", {}, 200) == "invalid"


def test_select_item_sold_out():
    assert select_item("cola", {"cola": 0}, 200) == "sold_out"


def test_select_item_insufficient():
    assert select_item("cola", {"cola": 5}, 100) == "insufficient"


def test_select_item_exact_price():
    assert select_item("cola", {"cola": 5}, 150) == "ok"


# make_change: test different branches

def test_make_change_negative():
    with pytest.raises(ValueError):
        make_change(-5)


def test_make_change_zero():
    assert make_change(0) == []


def test_make_change_exact_coins():
    assert make_change(185) == [100, 50, 25, 10]


def test_make_change_unavailable_change():
    assert make_change(3) is None


# purchase: test all decision outcomes

def test_purchase_invalid():
    stock = {"cola": 5}
    assert purchase("water", stock, 200) == ("invalid", [])


def test_purchase_sold_out():
    stock = {"cola": 0}
    assert purchase("cola", stock, 200) == ("sold_out", [])


def test_purchase_insufficient():
    stock = {"cola": 5}
    assert purchase("cola", stock, 100) == ("insufficient", [])


def test_purchase_no_exact_change():
    stock = {"cola": 5}
    assert purchase("cola", stock, 151) == ("no_exact_change", [])


def test_purchase_success():
    stock = {"cola": 5}
    result = purchase("cola", stock, 200)

    assert result == ("dispensed", [50])
    assert stock["cola"] == 4
