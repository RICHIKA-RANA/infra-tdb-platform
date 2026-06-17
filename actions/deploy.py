#!/usr/bin/env python3

import json
import os
import sys


def getenv(name, default=""):
    return os.getenv(name, default).strip()


def resolve_vm():
    vm = getenv("VM")
    new_vm = getenv("NEW_VM_NAME")

    if vm == "create-new":
        if not new_vm:
            raise Exception("NEW_VM_NAME is required.")
        return new_vm

    return vm


def resolve_release():
    release = getenv("RELEASE")
    new_release = getenv("NEW_RELEASE_NAME")

    if release == "create-new":
        if not new_release:
            raise Exception("NEW_RELEASE_NAME is required.")
        return new_release

    return release


def load_repositories():
    repos = getenv("REPOS_JSON")

    if not repos:
        return []

    return json.loads(repos)


def print_summary(vm, release, repos):
    print("=" * 80)
    print("TalkingDB Deployment")
    print("=" * 80)

    print(f"Target VM      : {vm}")
    print(f"Release        : {release}")

    print("\nRepositories")

    for repo in repos:
        print(
            f"  • {repo['url']} ({repo.get('branch', 'main')})"
        )

    print("=" * 80)


def deploy(vm, release):
    """
    Replace this function with your actual deployment mechanism.

    Examples:
        - ansible-playbook
        - ssh
        - kubectl
        - terraform
        - invoke another workflow
    """

    print(f"Deploying {release} to {vm}")

    #
    # Example:
    #
    # subprocess.run([
    #     "ansible-playbook",
    #     "deploy.yml",
    #     "-e",
    #     f"vm={vm}",
    #     "-e",
    #     f"release={release}",
    # ], check=True)
    #

    print("Deployment completed.")


def main():
    try:
        vm = resolve_vm()
        release = resolve_release()
        repos = load_repositories()

        print_summary(vm, release, repos)

        deploy(vm, release)

    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()