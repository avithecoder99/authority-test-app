from decimal import Decimal

import pytest

from app.refunds import refund_amount


def test_two_decimals_pass_through():
    assert refund_amount("10.25") == Decimal("10.25")


def test_whole_number():
    assert refund_amount("3") == Decimal("3.00")


def test_zero_or_negative_rejected():
    with pytest.raises(ValueError):
        refund_amount("0")
    with pytest.raises(ValueError):
        refund_amount("-1")

def test_three_decimals_round_half_up():
    assert refund_amount("10.005") == Decimal("10.01")
    assert refund_amount("10.004") == Decimal("10.00")


def test_amount_rounding_to_zero_cents_rejected():
    with pytest.raises(ValueError):
        refund_amount("0.004")
    with pytest.raises(ValueError):
        refund_amount("0.001")


def test_amount_rounding_to_one_cent_accepted():
    assert refund_amount("0.005") == Decimal("0.01")
    assert refund_amount("0.01") == Decimal("0.01")
