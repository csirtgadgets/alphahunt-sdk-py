from unittest.mock import patch
from alphahunt_sdk import account, integrations, integration_enable, integration_disable


@patch("alphahunt_sdk.Client._get")
def test_account(mock_rv):
    mock_rv.return_value = {"username": "test"}

    response = account(token="token")
    assert response["username"] == "test"


@patch("alphahunt_sdk.Client._get")
def test_account_integrations(mock_rv):
    mock_rv.return_value = {
        "integrations": {
            "abusech_threatfox": {"name": "abusech_threatfox", "enabled": True}
        }
    }
    rv = integrations(token="token")
    assert rv["abusech_threatfox"]["name"] == "abusech_threatfox"


@patch("alphahunt_sdk.Client._put")
def test_account_integrations_enable(mock_rv):
    mock_rv.return_value = {"message": "success"}
    rv = integration_enable(token="token", integration="abusech_threatfox")
    assert rv["message"] == "success"


@patch("alphahunt_sdk.Client._delete")
def test_account_integrations_disable(mock_rv):
    mock_rv.return_value = {"message": "success"}

    rv = integration_disable(token="token", integration="abusech_threatfox")
    assert rv["message"] == "success"
