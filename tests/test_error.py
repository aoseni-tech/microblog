from flask import Flask, json
from flask.testing import FlaskClient

def test_error(app : Flask, client: FlaskClient):
    """Test for request error handling for client/server error

    Args:
        app (Flask)
        client (FlaskClient)
    """
    response = client.get("/unknown_url")
    response_data = json.loads(response.data.decode())
    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert response_data["description"] == "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    assert response_data["name"] == "Not Found"