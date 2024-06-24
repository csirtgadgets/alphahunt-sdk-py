import pytest
import os


@pytest.fixture(autouse=True)
def setup():
    os.environ["ALPHAHUNT_TOKEN"] = "1234"
    os.environ["ALPHAHUNT_REMOTE"] = "https://localhost:3000"