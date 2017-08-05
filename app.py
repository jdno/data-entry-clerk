"""
Data Entry Clerk.

The Data Entry Clerk (DEC) accepts data on your behalf and stores it in a
database for later processing. The data is delivered to the DEC by external
services via webhooks, for which it implements an HTTP endpoint.
"""
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Load the default configuration
app.config.from_object('config.default')

# Load environment specific configuration
app.config.from_object(
    f"config.{os.getenv('FLASK_ENV', 'development').lower()}")


@app.route("/")
def root():
    """
    Endpoint for status checks.

    Depending on how and where the app is deployed, it might require an
    endpoint for status checks. The root path returns HTTP 200 and can be used
    for this purpose.

    :return: The status encoded as a JSON object and HTTP 200
    """
    return jsonify({"status": "ok"}), 200
