from time import sleep
import logging

from .utils import requests_retry_session
from .constants import REMOTE, TOKEN, HEADERS

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

__all__ = [
    "search",
    "research",
    "account",
    "integrations",
    "integration_enable",
    "integration_disable",
    "integrations_available",
    "Client",
    "faq",
]


def search(
    q,
    wait: bool = False,
    remote=REMOTE,
    token=TOKEN,
    verbose: bool = False,
    tags: list = None,
    insights: bool = False,
    related: bool = False,
):
    """Search for indicators

    :param q: indicator to search for
    :param wait: wait for results to be returned
    :param remote: remote to search
    :param token: token to use
    :param verbose: verbose mode
    :param context: provide additional context
    :param tags: specify related tags to your search
    :return: results
    """
    return Client(remote=remote, token=token).search(
        q,
        wait=wait,
        verbose=verbose,
        tags=tags,
        insights=insights,
        related=related,
    )


def faq(q, remote=REMOTE, token=TOKEN):
    """Ask a question

    :param q: question to ask
    :param remote: remote to search
    :param token: token to use
    :return: results
    """
    return Client(remote=remote, token=token).faq(q)


def research(
    q,
    keywords=None,
    remote=REMOTE,
    token=TOKEN,
    chat_history: list = None,
    retries: int = 20,
):
    """Research a broader topic

    :param q: indicator to search for
    :param keywords: keywords to search
    :param chat_history: chat history
    :param retries: number of retries
    :param remote: remote to search
    :param token: token to use
    :return: results
    """
    return Client(remote=remote, token=token).research(
        q, keywords=keywords, chat_history=chat_history, retries=retries
    )


def account(token=TOKEN, remote=REMOTE):
    """Get account information

    :param remote: remote to search
    :param token: token to use
    :return: results
    """
    return Client(remote=remote, token=token).account()


def integrations(token=TOKEN, remote=REMOTE):
    """Get account integrations

    :param remote: remote to search
    :param token: token to use
    :return: results
    """
    return Client(remote=remote, token=token).integrations()


def integration_enable(integration, integration_token=None, token=TOKEN, remote=REMOTE):
    """Enable an integration

    :param remote: remote to search
    :param token: token to use
    :param integration: integration to enable
    :param integration_token: integration token
    :return: results
    """
    return Client(remote=remote, token=token).integration_enable(
        integration, integration_token
    )


def integration_disable(integration, token=TOKEN, remote=REMOTE):
    """Disable an integration

    :param remote: remote to search
    :param token: token to use
    :param integration: integration to disable
    :return: results
    """
    return Client(remote=remote, token=token).integration_disable(integration)


def integrations_available(token=TOKEN, remote=REMOTE):
    """Get available integrations

    :return: results
    """
    return Client(token, remote).integrations_available()


class Client:
    session = requests_retry_session()
    token = None
    remote = None

    def __init__(self, token=TOKEN, remote=REMOTE, version=3):
        self.token = token
        self.remote = remote
        self.version = version

        if self.token in ["", None, False]:
            raise ValueError("token required")

        self.session.headers.update(HEADERS)
        self.session.headers.update({"x-api-key": self.token})

    def search(
        self,
        q,
        wait: bool = False,
        verbose: bool = False,
        tags: list = None,
        insights: bool = False,
        related: bool = False,
        retries: int = 20,
    ):
        params = {"q": q}
        for e in ["wait", "verbose", "insights", "related"]:
            if locals()[e]:
                params[e] = "1"

        if tags:  # pragma: no cover
            params["tags"] = ",".join(tags)

        return self._get(self.remote, params=params, retries=retries)

    def faq(self, q: str, retries: int = 5):
        rv = self.session.post(f"{self.remote}/faq", json={"q": q})

        if rv.status_code >= 300:
            raise IOError(rv.text)  # pragma: no cover

        data = rv.json()

        if rv.status_code == 200:
            return data["answer"]

        logger.info(f"waiting for {data['id']}")
        sleep_time = 5
        sleep(sleep_time)
        for _ in range(retries):
            rv = self.session.get(
                f"{self.remote}/faq", params={"tracking_id": data["id"]}
            )

            if rv.status_code >= 300:
                raise IOError(rv.text)

            data = rv.json()

            if rv.status_code == 200:
                return data["answer"]

            if rv.status_code == 202:
                sleep(sleep_time)
                if sleep_time > 15:
                    sleep_time = sleep_time * 0.75
                logger.info(f"re-checking: {data['id']}")
                continue

            raise IOError("Unable to get answer. Please try again later.")

        raise IOError("Unable to get answer. Please try again later.")

    def research(
        self, q, keywords: list = None, chat_history: list = None, retries: int = 20
    ):
        rv = self.session.post(
            f"{self.remote}/research",
            json={
                "q": q,
                "keywords": keywords or [],
                "chat_history": chat_history or [],
            },
        )

        if rv.status_code >= 300:
            raise IOError(rv.text)

        data = rv.json()

        if rv.status_code == 200:
            return data["answer"]

        logger.info(f"waiting for {data['id']}")
        sleep_time = 45
        sleep(sleep_time)
        for _ in range(retries):
            rv = self.session.get(
                f"{self.remote}/research", params={"tracking_id": data["id"]}
            )

            if rv.status_code >= 300:
                raise IOError(rv.text)

            data = rv.json()

            if rv.status_code == 200:
                return data["answer"]

            if rv.status_code == 202:
                sleep(sleep_time)
                if sleep_time > 15:
                    sleep_time = sleep_time * 0.75
                logger.info(f"re-checking: {data['id']}")
                continue

            raise IOError("Unable to get answer. Please try again later.")

        raise IOError("Unable to get answer. Please try again later.")

    def account(self):
        return self._get(f"{self.remote}/account")

    def integrations(self):
        return self.account().get("integrations", {})

    def integrations_available(self):
        return self._get(f"{self.remote}/integrations")

    def integration_enable(self, name, token=None):
        data = {"name": name, "token": token}
        return self._put(f"{self.remote}/account/integrations", data=data)

    def integration_disable(self, name):
        return self._delete(f"{self.remote}/account/integrations/{name}")

    def _get(self, url, params=None, retries: int = 20):
        rv = self.session.get(url, params=params)
        if rv.status_code == 403:
            raise PermissionError("Forbidden (HTTP403)")

        if rv.status_code == 200:
            return rv.json()

        if rv.status_code == 202:
            sleep_time = 5
            sleep(sleep_time)
            for _ in range(retries):
                rv = self.session.get(f"{self.remote}")

                if rv.status_code >= 300:
                    logger.error(rv.text)
                    raise IOError(rv.status_code)

                data = rv.json()

                if rv.status_code == 200:
                    return data

                if rv.status_code == 202:
                    sleep(sleep_time)
                    if sleep_time > 15:
                        sleep_time = sleep_time * 0.75
                    continue

                raise IOError("Unable to get answer. Please try again later.")

            raise IOError("Unable to get answer. Please try again later.")

        logger.error(rv.text)  # pragma: no cover
        raise IOError(rv.status_code)

    def _put(self, url, data=None):
        rv = self.session.put(url, json=data)
        if rv.status_code == 201:
            return rv.json()

        raise IOError(f"HTTP PUT failed: {rv.status_code} - {rv.text}")

    def _delete(self, url):
        rv = self.session.delete(url).json()
        if rv.status_code == 200:
            return rv.json()

        raise IOError(f"HTTP DELETE failed: {rv.status_code} - {rv.text}")
