## Contributing

Thanks for your interest in contributing to this project — contributions are welcome!

Getting started
- Create a virtual environment and activate it:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

- Install runtime dependencies (or use the lockfile workflow shown in README):

```bash
pip install -r requirements.txt
pip install -e .
# If you use the optional dev extras declared in pyproject.toml:
pip install -e .[dev]
```

Run tests

```bash
PYTHONPATH=src python -m pytest tests
```

Linting & formatting
- This repository does not enforce a specific formatter by default. If you add `black`/`isort`/`ruff`, run:

```bash
python -m pip install black isort
black .
isort .
```

Making changes
- Create a feature branch from `main`: `git checkout -b feat/my-change`
- Keep changes small and focused; add or update tests for new behavior.
- Run tests locally before opening a PR.

Pull request process
- Push your branch to your fork and open a Pull Request against `main`.
- In the PR description include: what the change does, why it is needed, and any notes about testing or migration.
- A maintainer will review the PR; be responsive to review comments and update the PR as requested.

Thank you for helping improve this project!
