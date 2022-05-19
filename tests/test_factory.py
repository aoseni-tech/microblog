from microblog import create_app
from microblog.config import ProdConfig


def test_config(app) -> None:
    """Test to check that app is in the right environment(development, test or production)
    The app should be in test mode when test config is passed to create app
    """
    #check to make sure default env is development and testing is true
    assert create_app().config["ENV"] == "development"
    assert create_app().testing

    #check to make sure current testing app is set with correct test config and environment is testing
    assert app.testing
    assert app.config["ENV"] == "testing"

    #check to make sure ProdConfig behaves as it should by setting env as production ,testing to false and debug to false.
    assert not create_app(ProdConfig).testing
    assert create_app(ProdConfig).config["ENV"] == "production"
    assert create_app(ProdConfig).config["DEBUG"] == False