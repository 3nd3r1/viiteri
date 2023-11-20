""" tasks.py """

import sys
from invoke.tasks import task


@task
def start(ctx):
    if sys.platform.startswith("win"):
        ctx.run("py viiteri/index.py")
    else:
        ctx.run("python viiteri/index.py")


@task
def test(ctx):
    ctx.run("pytest .")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest .")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html -d ./docs/coverage")


@task
def lint(ctx):
    ctx.run("pylint viiteri", warn=True)
