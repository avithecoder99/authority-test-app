"""AWS Lambda entry point for the test application: the same refund calculation as the HTTP service."""

from app.refunds import refund_amount


def handler(event, context):
    query = (event or {}).get("queryStringParameters") or {}
    try:
        return {"statusCode": 200, "body": str(refund_amount(query.get("amount", "0")))}
    except (ValueError, ArithmeticError) as exc:
        return {"statusCode": 400, "body": f"error: {exc}"}
