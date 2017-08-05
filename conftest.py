"""
Configuration for tests.

This module contains configuration and fixtures for all test cases. It is
automatically loaded by PyTest when running tests.
"""
import pytest

from app import app as flask_app


@pytest.fixture
def app():
    """
    Return the Flask app.

    To be able to test the application and its API, we need to pass it to the
    tests. Using the application's instance, tests can set up required
    resources (e.g. databases) and send requests to the application's
    endpoints.
    """
    return flask_app
