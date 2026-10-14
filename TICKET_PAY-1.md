Title: Refund endpoint returns wrong amount for values with three decimals

Steps: call /?amount=10.005
Expected: 10.01
Actual: 10.00

Acceptance criteria:
- refund_amount("10.005") returns Decimal("10.01") (round half up to cents)
- existing tests still pass
- a new test covers the three-decimal case
