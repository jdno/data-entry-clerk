"""
Data Entry Clerk.

The Data Entry Clerk (DEC) accepts data on your behalf and stores it in a
database for later processing. The data is delivered to the DEC by external
services via webhooks, for which it implements an HTTP endpoint.

Following Flask's best practices, we initialize the app here and load its
configuration. The API itself is implemented in `api.py`.
"""
import os

from flask import Flask

app = Flask(__name__)

# Load the default configuration
app.config.from_object('dec.config.default')

# Load environment specific configuration
app.config.from_object(
    f"dec.config.{os.getenv('FLASK_ENV', 'development').lower()}")

from dec import api  # noqa
