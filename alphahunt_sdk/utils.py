from urllib3.util import Retry
from requests.adapters import HTTPAdapter
from requests import Session
from .constants import RETRIES_BACKOFF, RETRIES


def requests_retry_session(
    retries=RETRIES,
    backoff_factor=RETRIES_BACKOFF,
    status_forcelist=[504],
    session=None,
):

    session = session or Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session
