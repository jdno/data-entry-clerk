"""
Default configuration.

This module contains the default configuration for the Data Entry Clerk. It can
be overwritten in environment specific configuration files, or through the use
of environment variables.
"""

# Enable debug mode for Flask
DEBUG = True

# Leave empty to use default DynamoDB endpoint in current region
DYNAMODB_ENDPOINT = None

# Leave empty to use default region
DYNAMODB_REGION = None

# Overwrite this in environment specific configuration files
DYNAMODB_TABLE = "automatiqa-dec"
