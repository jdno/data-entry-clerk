"""
Data Entry Clerk's API.

This module implements the API that our Data Entry Clerk provides. The API
consists of two endpoints: one health check for monitoring or load balancing,
and the endpoint that processes and stores webhooks.
"""
from datetime import datetime
from uuid import uuid4

import boto3
import pytz
from botocore.exceptions import ClientError
from decimal import Decimal
from flask import jsonify, request, json

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


@app.route("/incoming", methods=["POST"])
def process():
    """
    Process an incoming webhook.

    Incoming webhooks contain data that should be stored in a database. The
    data is extracted by parsing the request body, and written to the database.
    If both operations are successful, HTTP 200 is returned. Otherwise, HTTP
    400 or 500 are returned, depending on the cause of the failure.

    :return: HTTP 200 if successful, HTTP 400 or 500 in case of an error
    """
    data = json.loads(request.data, parse_float=Decimal)

    if not data:
        return jsonify({"errors": ["Empty request"]}), 400

    data["dec_id"] = str(uuid4())
    data["dec_created_at"] = str(datetime.utcnow().replace(tzinfo=pytz.utc))

    dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url=app.config['DYNAMODB_ENDPOINT'],
        aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
        region_name=app.config['AWS_REGION']
    )
    table = dynamodb.Table(app.config['DYNAMODB_TABLE'])

    try:
        table.put_item(Item=data)
    except ClientError as e:
        print(str(e))
        return jsonify({"errors": [str(e)]}), 500

    return jsonify(data), 200
