import nox

ALL_PYTHONS = ["3.6", "3.7", "3.8", "3.9", "3.10"]

nox.options.sessions = ["lint", "tests"]


@nox.session(python=ALL_PYTHONS)
def tests(session: nox.Session) -> None:
    """
    Run the unit and regular tests.
    """
    session.install(".[test]")
    session.run("pytest", *session.posargs)


@nox.session
def docs(session: nox.Session) -> None:
    """
    Build the docs. Pass "serve" to serve.
    """

    session.chdir("docs")
    session.install("-r", "requirements.txt")
    session.run("sphinx-build", "-M", "html", ".", "_build")

    if session.posargs:
        if "serve" in session.posargs:
            session.log("Launching docs at http://localhost:8000/ - use Ctrl-C to quit")
            session.run("python", "-m", "http.server", "8000", "-d", "_build/html")
        else:
            session.error("Unsupported argument to docs")


@nox.session
def lint(session: nox.Session) -> None:
    """
    Run the linter.
    """
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session
def make_pickle(session: nox.Session) -> None:
    """
    Make a pickle file for this version
    """
    session.install(".[dev]")
    session.run("python", "tests/pickles/make_pickle.py", *session.posargs)
