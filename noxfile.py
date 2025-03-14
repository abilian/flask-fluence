from __future__ import annotations

import nox

# nox.options.default_venv_backend = "uv"
nox.options.sessions = ["py", "lint"]
nox.options.reuse_existing_virtualenvs = True

# NB: first one is the default
PYTHON_VERSIONS = ["3.12", "3.11", "3.13"]


@nox.session(python=PYTHON_VERSIONS)
def py(session: nox.Session) -> None:
    """Run tests (using pytest)."""
    session.run("uv", "sync", "--active", external=True)
    session.run("pytest", "-v")


@nox.session(python=PYTHON_VERSIONS[0])
def lint(session: nox.Session) -> None:
    session.run("uv", "sync", "--active", external=True)
    session.run("make", "lint")
