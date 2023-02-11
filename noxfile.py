"""nox configuration file."""
from pathlib import Path
from typing import List

import nox
from nox import Session
from nox_poetry import session

nox.options.sessions = [
    "check_format",
    "docs",
    "isort",
    "lint",
    "mypy",
    "tests",
]


# determine modules present in this repository
modules = [p.name for p in Path("src").iterdir() if p.is_dir()]
modules_str = ",".join(modules)


@session(python=False)
def lint(sess: Session):
    """Run pylint."""
    sess.run("pylint", "src", "tests")


@session(python=False)
def isort(sess: Session):
    """Check import sort order."""
    sess.run("isort", ".", "--check")


@session(python=False)
def check_format(sess: Session):
    """Check formatting with black."""
    sess.run("black", ".", "--check")


@session(python=False)
def mypy(sess: Session):
    """Run static analysis with mypy."""
    sess.run("mypy", ".", "--html-report", "html/mypy")


@session
def tests(sess: Session):
    """Run tests."""
    sess.run("pip", "install", ".", "pytest", "pytest-benchmark", "coverage")
    sess.run("coverage", "run", f"--source={modules_str}", "-m", "pytest", "tests")
    sess.run("coverage", "report", "-i")
    sess.run("coverage", "html", "-d", "html/testcov")


@session(python=False)
def docs(sess: Session):
    """Build documentation."""
    sess.run("mkdocs", "build", "-d", "html/docs")


@session(python=False)
def serve_docs(sess: Session):
    """Serve current documentation with live reloading."""
    sess.run("mkdocs", "serve")


@session
def pip_licenses(sess: Session):
    """Generate list of pip package licenses."""
    sess.install(".", "pip-licenses")
    html_root = Path("html/licenses")
    html_root.mkdir(parents=True, exist_ok=True)
    licenses_path = html_root / "licenses.html"
    summary_path = html_root / "summary.html"
    args_list: List[List[str]] = [
        ["--summary"],
        [],
        ["--format=html", "--summary", f"--output-file={summary_path}"],
        ["--with-urls", "--format=html", f"--output-file={licenses_path}"],
    ]
    for args in args_list:
        sess.run("pip-licenses", *args)
    style = (
        r"<style>* {font-family: Courier New, Courier; "  # mono space font
        r"tr:nth-child(even): background-color: #EEE;}</style>"  # alternate row styling
    )
    for html_fname in [summary_path, licenses_path]:
        with open(html_fname, "at", encoding="ascii") as f:
            f.write(style)


@session(python=False)
def serve(sess: Session):
    """Serve html folder."""
    sess.run("python", "-m", "http.server", "-d", "html")


@session
def freeze(sess: Session):
    """Pip freeze."""
    sess.run_always("poetry", "install", "--remove-untracked", external=True)
    sess.run("pip", "freeze")
