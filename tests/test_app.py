"""
Test the app module.

The app module defines and implements the application's endpoints. The tests in
this module ensure that the endpoints process requests correctly.
"""
import json

import time


def test_status_ok(app):
    """
    Test the status check under normal conditions.

    Under normal conditions, the status check is supposed to return HTTP 200
    OK.

    :param app: The Flask dec
    """
    response = app.test_client().get('/')
    body = json.loads(response.get_data())

    assert '200 OK' == response.status
    assert 'ok' == body['status']


def test_process(app):
    data = {
        "name": "Data Entry Clerk",
        "message": "Running tests",
        "timestamp": time.time()
    }

    response = app.test_client().post('/incoming',
                                      data=json.dumps(data),
                                      content_type='application/json')
    assert '200 OK' == response.status

    body = json.loads(response.get_data())
    assert 'dec_id' in body
    assert 'dec_created_at' in body
