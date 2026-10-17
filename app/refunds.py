"""Refund amount handling for the test application."""

from decimal import ROUND_HALF_UP, Decimal


def refund_amount(amount: str) -> Decimal:
    """Return the refundable amount in whole cents.

    Values with more than two decimals are rounded half up, so "10.005" becomes 10.01.
    The rounded amount must be positive: an amount that rounds to zero cents, such as
    "0.004", is refused just like zero or a negative amount.
    """
    value = Decimal(amount).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    if value <= 0:
        raise ValueError("refund must be positive")
    return value
