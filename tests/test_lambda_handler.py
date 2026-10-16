from app.lambda_handler import handler


def test_handler_rounds_like_the_http_service():
    assert handler({"queryStringParameters": {"amount": "10.005"}}, None) == {"statusCode": 200, "body": "10.01"}


def test_handler_refuses_a_non_positive_amount():
    assert handler({"queryStringParameters": {"amount": "0"}}, None)["statusCode"] == 400
    assert handler({}, None)["statusCode"] == 400
