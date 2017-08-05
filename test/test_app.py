"""
Test the app module.

The app module defines and implements the application's endpoints. The tests in
this module ensure that the endpoints process requests correctly.
"""
import json


def test_status_ok(app):
    """
    Test the status check under normal conditions.

    Under normal conditions, the status check is supposed to return HTTP 200
    OK.

    :param app: The Flask app
    """
    response = app.test_client().get('/')
    body = json.loads(response.get_data())

    assert '200 OK' == response.status
    assert 'ok' == body['status']
