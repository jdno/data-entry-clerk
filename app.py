"""
Data Entry Clerk.

The Data Entry Clerk (DEC) accepts data on your behalf and stores it in a
database for later processing. The data is delivered to the DEC by external
services via webhooks, for which it implements an HTTP endpoint.
"""
from flask import Flask, jsonify

app = Flask(__name__)


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
