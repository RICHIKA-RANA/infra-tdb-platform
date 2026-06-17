#!/usr/bin/env python3

from pathlib import Path

from common import (
    load_repos,
    clone_repository,
    run_python,
    commit_if_needed,
    temporary_workspace,
)


def sync_dependencies(repo_path: Path):
    """
    Execute the repository's sync_git_deps.py script if present.
    """
    script = repo_path / "sync_git_deps.py"

    if not script.exists():
        print(f"Skipping {repo_path.name}: sync_git_deps.py not found.")
        return

    run_python(
        str(script),
        "--mode",
        "git",
        cwd=repo_path,
    )


def process_repo(repo_path, repo_name):
    print("\n" + "=" * 80)
    print(f"Processing {repo_name}")
    print("=" * 80)

    try:
        sync_dependencies(repo_path)
    except Exception as ex:
        print(f"Dependency sync failed: {ex}")

    committed = commit_if_needed(
        repo_path,
        f"chore: sync deps ({repo_name})",
    )

    if committed:
        print(f"✅ {repo_name}: changes committed")
    else:
        print(f"ℹ️  {repo_name}: no changes")


def main():
    repos = load_repos()

    print(f"Found {len(repos)} repositories.\n")

    workspace = temporary_workspace()

    cloned_repos = [clone_repository(workspace, repo) for repo in repos]

    for repo_path, repo_name in cloned_repos:
        process_repo(repo_path, repo_name)

    print("\nRepository synchronization complete.")

    workspace.cleanup()  # Clean up the temporary workspace


if __name__ == "__main__":
    main()
