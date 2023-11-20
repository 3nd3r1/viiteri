""" tasks.py """
# pylint:   disable-all

import sys
from invoke.tasks import task


@task
def start(ctx):
    if sys.platform.startswith("win"):
        ctx.run("py viiteri/index.py")
    else:
        ctx.run("python viiteri/index.py")


@task
def unittest(ctx):
    ctx.run("pytest ./tests/unit")


@task
def robottest(ctx):
    ctx.run("robot ./tests/integration")


@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest .")


@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html -d ./docs/coverage")


@task
def lint(ctx):
    ctx.run("pylint viiteri", warn=True)
