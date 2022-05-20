from flask import Flask, json
from flask.testing import FlaskClient

def test_error(app : Flask, client: FlaskClient):
    """Test for request error handling for client/server error

    Args:
        app (Flask)
        client (FlaskClient)
    """
    response = client.get("/unknown_url")
    response_data = response.data
    assert response.status_code == 404
    assert response.content_type == "text/html; charset=utf-8"
    assert b"Calendar" in response_data
    assert b"The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again." in response_data
    assert b"Not Found</p>" in response_data
    assert b">404</h1>" in response_data