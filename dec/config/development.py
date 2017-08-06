"""
Development configuration.

The configuration for local development ensures that the application uses local
or temporary resources, so that new features can be tested in isolation.
"""

# Use DynamoDB Local for development. See README for more information.
DYNAMODB_ENDPOINT = "http://localhost:8000"
