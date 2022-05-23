from flask import Flask, g, json
from flask.testing import FlaskClient
import pytest


@pytest.fixture
def test_home_get(client: FlaskClient, app: Flask):
    """GIVEN a Flask application configured for testing
        WHEN the '/' page is requested (GET)
        THEN check that the response is valid

    Args:
        client (FlaskClient): FlaskClient
        app (Flask): Our Flask app object

    Returns:
        : _AppCtxGlobals
    """
    #strings to check for in the response html body
    get_data_to_check = ["Recent", "Add Content", "Recent posts"]

    response = client.get("/")
    response_json = client.get("/", headers={"Content-Type": "application/json"})
    #response data when content type is set to application/json
    response_json_data = json.loads(response_json.data.decode())
    response_json_contents = response_json_data["entries"]
    #The default response data, an html rendered
    get_datas = response.data.decode()
    assert response.status_code == 200
    assert response_json.status_code == 200

    #check to make sure json response content data count is the same as entries collection count returned from the database
    assert len(response_json_contents) == app.db.entries.count_documents({})

    #check for strings in html body
    for data in get_data_to_check:
        assert data in get_datas
    #save the request url in g.location
    g.location = response.request.url
    g.coll_count = len(response_json_contents)
    return g


def test_home_post(client: FlaskClient, app: Flask, test_home_get):
    """When a data is posted to "/" route
        Check that the respone status code is redirect(302) to
        the get "/" page.
        And also test for appropriate behaviours to make sure it matches the way our app should behave

    Args:
        client (FlaskClient)
        app (Flask)
        test_home_get (PytestFixture)
    """
    post_data = {
        "csrf_token": test_home_get.pop("csrf_token"),
        "content": "This is a new test content",
        "first_name": "Vinicius",
        "last_name": "Jnr",
    }
    get_url = test_home_get.location
    prev_count = test_home_get.coll_count

    response = client.post("/", data=post_data)
    form = app.entry_form()
    post_compare = [post_data[data] == form.data[data] for data in post_data]

    get_data_to_check = ["Recent", "Add Content", "Recent posts", post_data["first_name"], post_data["content"],form.data["date_posted"].astimezone().strftime("%d-%m-%Y")]

    #get the "/" url to confirm new data has been added through posting

    get_response_json = client.get("/", headers={"Content-Type": "application/json"})

    #response data when content type is set to aapplication/json
    get_response_data = json.loads(get_response_json.data.decode())

    #default response data
    get_response_html = client.get("/").data.decode()

    #get entries collection count to know if new documents has been added through post
    collection_count = app.db.entries.count_documents({})
    

    #check that the response status code is a redirect
    assert response.status_code == 302

    #check that the datas being posted are the right one
    assert not False in post_compare

    #check that redirect url is the "/" url
    assert response.location == get_url

    #check that collection count increases by one
    assert (collection_count - prev_count) == 1
    
    #check that the length of response["contents"] returned when the content type is json is the same as the new collection count
    assert len(get_response_data["entries"]) == collection_count
    
    #check for strings in html body
    for data in get_data_to_check:
        assert data in get_response_html
