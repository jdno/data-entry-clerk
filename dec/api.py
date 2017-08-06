"""
Data Entry Clerk's API.

This module implements the API that our Data Entry Clerk provides. The API
consists of two endpoints: one health check for monitoring or load balancing,
and the endpoint that processes and stores webhooks.
"""
from flask import jsonify

from dec import app


@app.route("/")
def status():
    """
    Endpoint for status checks.

    Depending on how and where the dec is deployed, it might require an
    endpoint for status checks. The root path returns HTTP 200 and can be used
    for this purpose.

    :return: The status encoded as a JSON object and HTTP 200
    """
    return jsonify({"status": "ok"}), 200
