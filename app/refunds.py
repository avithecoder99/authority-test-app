"""Refund amount handling for the test application."""

from decimal import ROUND_HALF_UP, Decimal


def refund_amount(amount: str) -> Decimal:
    """Return the refundable amount in whole cents.

    Values with more than two decimals are rounded half up, so "10.005" becomes 10.01.
    """
    value = Decimal(amount)
    if value <= 0:
        raise ValueError("refund must be positive")
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
