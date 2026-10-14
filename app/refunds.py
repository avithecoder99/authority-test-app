"""Refund amount handling for the test application."""

from decimal import Decimal


def refund_amount(amount: str) -> Decimal:
    """Return the refundable amount in whole cents.

    Known defect (PAY-1): values with more than two decimals are truncated,
    so "10.005" becomes 10.00 instead of 10.01.
    """
    value = Decimal(amount)
    if value <= 0:
        raise ValueError("refund must be positive")
    cents = int(value * 100)
    return Decimal(cents) / Decimal(100)
