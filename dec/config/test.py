"""
Test configuration.

Tests are usually executed in Docker, so we configure the endpoint by its link
name. Make sure the hostname resolves to either localhost or a Docker container
running DynamoDB Local.
"""

# Must be set, but aren't used.
AWS_ACCESS_KEY_ID = "foo"
AWS_SECRET_ACCESS_KEY = "bar"

# Must be set, but isn't used.
AWS_REGION = "eu-west-1"

# Leave empty to use default DynamoDB endpoint in current region
DYNAMODB_ENDPOINT = "http://dynamodb:8000"
