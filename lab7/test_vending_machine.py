from hypothesis import given, strategies as st
from vending_machine import parse_coins, slot_position, change_due


@given(st.one_of(st.text(), st.none()))
def test_parse_coins_no_crash(s):
    result = parse_coins(s)
    assert isinstance(result, list)


@given(st.one_of(st.text(), st.none()))
def test_slot_position_no_crash(s):
    result = slot_position(s)
    assert result is None or (
        isinstance(result, tuple) and len(result) == 2
    )


@given(st.one_of(st.text(), st.none()))
def test_change_due_no_crash(s):
    result = change_due(s)
    assert isinstance(result, str)


def test_valid_inputs():
    assert parse_coins("5,10,25") == [5, 10, 25]
    assert slot_position("B7") == (1, 6)
    assert change_due("200/150") == "10 five-coins"