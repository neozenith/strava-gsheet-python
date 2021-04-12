#!/usr/bin/env python3
# Standard Library
import inspect
import os
import sys
from subprocess import run


def _inspect_tasks(prefix):
    return {
        f[0].replace(prefix, ""): f[1]
        for f in inspect.getmembers(sys.modules["__main__"], inspect.isfunction)
        if f[0].startswith(prefix)
    }


def _cmd(command, args=[]):
    return run(command.split(" ") + args)


def _exit_handler(status):
    statuses = status if type(status) == list else [status]
    bad_statuses = [s for s in statuses if s.returncode != 0]
    if bad_statuses:
        sys.exit(bad_statuses)


def task_install(args):
    return _cmd("python -m pip install -r requirements.txt -r requirements-dev.txt --upgrade", args)


def task_qa(args):
    targets = ["core/", "api/", "cli/", "tasks.py"]
    return [_cmd(f"{tool} {' '.join(targets)}") for tool in ["black", "isort", "flake8"]]


def task_test(args):
    return _cmd("python3 -m pytest", args)


def task_dev(args):
    return _cmd("uvicorn api.v1:app", args)


def task_logs(args):
    # Third Party Libraries
    from dotenv import load_dotenv

    load_dotenv()
    return _cmd(f"heroku logs -a {os.getenv('APP_NAME')}", args)


if __name__ == "__main__":
    tasks = _inspect_tasks("task_")

    if len(sys.argv) >= 2 and sys.argv[1] in tasks.keys():
        _exit_handler(tasks[sys.argv[1]](sys.argv[2:]))
    else:
        print(f"Must provide a task from the following: {list(tasks.keys())}")
