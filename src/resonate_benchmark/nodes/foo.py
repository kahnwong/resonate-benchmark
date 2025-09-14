import os
from threading import Event

from resonate import Resonate

from resonate_benchmark.utils import simulation
from resonate_benchmark.utils.logger import init_logger

log = init_logger(__name__)

resonate = Resonate.remote(group="foo_nodes", host=os.environ["RESONATE_HOST"])


@resonate.register
def foo_str(_, identifier: str):
    if not simulation.random_failure():
        return f"id: {identifier}"
    else:
        log.error("Random failure")
        raise Exception("Random failure")


@resonate.register
def foo(_, identifier: str) -> str:
    return identifier


def main():
    log.info("Starting node: foo")
    resonate.start()
    Event().wait()


if __name__ == "__main__":
    main()
