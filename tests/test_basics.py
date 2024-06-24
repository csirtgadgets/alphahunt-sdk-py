from unittest.mock import patch
from alphahunt_sdk import (
    search,
    faq,
    research,
    account,
    integrations,
    integrations_available,
    integration_disable,
    integration_enable,
)


@patch("requests.Session.get")
def test_search(mock_get):
    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {"nodes": []}

    rv = search("1.1.1.1", token="1234", wait=True)

    assert rv["nodes"] == []


@patch("requests.Session.get")
def test_search_fail(mock_get):
    mock_get.return_value.status_code = 403

    try:
        search(
            "nobody cares",
            token="1234",
        )

    except PermissionError:
        pass

    else:
        assert False, "Should have raised PermissionError"


# test faq function
@patch("requests.Session.post")
def test_faq(mock_post):
    mock_post.return_value.status_code = 200

    mock_post.return_value.json.return_value = {"answer": "rtfm"}

    rv = faq("how do i install the sdk", token="1234")

    assert rv == "rtfm"


# test research function
@patch("requests.Session.post")
def test_research(mock_get):
    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {"answer": "42"}

    rv = research("1234", token="1234")

    assert rv == "42"


# test account


@patch("requests.Session.get")
def test_account(mock_get):
    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {"integrations": {}}

    rv = account(token=1234)

    assert rv == {"integrations": {}}


# test integrations available
@patch("requests.Session.get")
def test_integrations(mock_get):
    mock_get.return_value.status_code = 200

    mock_get.return_value.json.return_value = {"integrations": {}}

    rv = integrations_available(token=1234)

    assert rv == {"integrations": {}}


# test integration enable
@patch("requests.Session.put")
def test_integration_enable(mock_put):
    mock_put.return_value.status_code = 201

    mock_put.return_value.json.return_value = {"integrations": {}}

    rv = integration_enable("abusech_threatfox", token=1234)

    assert rv == {"integrations": {}}

    mock_put.return_value.status_code = 500
    mock_put.return_value.text = "Internal Server Error"
    rv = integration_enable("abusech_threatfox", token=1234)
    assert rv == "Internal Server Error"


# test integration disable
@patch("requests.Session.delete")
def test_integration_disable(mock_delete):
    mock_delete.return_value.status_code = 200

    mock_delete.return_value.json.return_value = {"integrations": {}}

    rv = integration_disable("abusech_threatfox", token=1234)

    assert rv == {"integrations": {}}


# check self.token is None
def test_no_token():
    try:
        search("")

    except ValueError:
        pass

    else:
        assert False, "Should have raised ValueError"
