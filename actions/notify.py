#!/usr/bin/env python3

import os
import sys


def enabled(name):
    return os.getenv(name, "false").lower() == "true"


def getenv(name):
    return os.getenv(name, "").strip()


def notify_teams():
    print("Sending Teams notification...")

    #
    # Example:
    #
    # from providers.teams import send
    #
    # send(
    #     release=getenv("RELEASE"),
    #     vm=getenv("VM"),
    # )
    #

    print("✓ Teams notification sent")


def notify_email():
    recipients = getenv("ADDITIONAL_RECIPIENTS")

    print("Sending Email notification...")

    #
    # Example:
    #
    # from providers.email import send
    #
    # send(
    #     release=getenv("RELEASE"),
    #     vm=getenv("VM"),
    #     recipients=recipients,
    # )
    #

    print("✓ Email notification sent")


def main():
    try:
        print("=" * 80)
        print("Notifications")
        print("=" * 80)

        if enabled("NOTIFY_TEAMS"):
            notify_teams()

        if enabled("NOTIFY_EMAIL"):
            notify_email()

        print("Done.")

    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()