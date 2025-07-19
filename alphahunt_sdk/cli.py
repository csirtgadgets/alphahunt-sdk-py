#!/usr/bin/env python3

import logging
import sys
import textwrap
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from json import dumps
from pprint import pprint

from alphahunt_sdk import (
    search,
    research,
    integrations,
    integration_enable,
    integration_disable,
    integrations_available,
    faq,
)

logger = logging.getLogger(__name__)


def main():  # pragma: no cover
    p = ArgumentParser(
        description=textwrap.dedent(
            """\
        example usage:
            $ alphahunt 173.249.0.199 | jq
            $ alphahunt 173.249.0.199 --wait | jq
        """
        ),
        formatter_class=RawDescriptionHelpFormatter,
        prog="alphahunt",
    )

    p.add_argument(
        "-q",
        "--query",
        help="search for an indicator against your intelligence providers",
    )
    p.add_argument(
        "-v",
        "--verbose",
        help="search in verbose mode",
        action="store_true",
        default=False,
    )
    p.add_argument("-r", "--research", help="search for research")
    p.add_argument(
        "-d",
        "--debug",
        help="debug mode",
        action="store_true",
    )

    p.add_argument("-w", "--wait", help="wait for results", action="store_true")

    p.add_argument("--integrations", help="list integrations", action="store_true")
    p.add_argument("--integration-enable", help="enable integration")
    p.add_argument("--integration-disable", help="disable integration")
    p.add_argument("--integration-token", help="integration token")
    p.add_argument("--integration-token-id", help="integration token id")
    p.add_argument(
        "--integrations-available",
        help="list available integrations",
        action="store_true",
    )

    p.add_argument("--tags", help="specify related tags to your search")

    p.add_argument("--insights", help="summarize the results", action="store_true")
    p.add_argument("--related", help="show related indicators", action="store_true")
    p.add_argument("--summary", help="show summary", action="store_true")
    p.add_argument("--faq", help="Ask a question related to the platform")

    if len(sys.argv) == 2 and not sys.argv[1].startswith("-"):
        sys.argv.append(sys.argv[1])
        sys.argv[1] = "-q"

    args = p.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)

    if args.query:
        data = search(
            args.query,
            wait=args.wait,
            verbose=args.verbose,
            tags=args.tags,
            insights=args.insights,
            related=args.related,
        )

    elif args.faq:
        print(faq(args.faq))
        raise SystemExit

    elif args.research:
        print(research(args.research, wait=args.wait))
        raise SystemExit

    elif args.integrations:
        data = integrations()

    elif args.integration_enable:
        data = integration_enable(args.integration_enable, args.integration_token)

    elif args.integration_disable:
        data = integration_disable(args.integration_disable)

    elif args.integrations_available:
        data = integrations_available()

    else:
        p.print_help()
        return

    indent = None
    if args.debug:
        indent = 4

    print(dumps(data, indent=indent))


if __name__ == "__main__":
    main()
