import os
from threading import Event

from resonate import Resonate

from resonate_benchmark.utils.logger import init_logger

log = init_logger(__name__)

resonate = Resonate.remote(group="foo_nodes", host=os.environ["RESONATE_HOST"])


@resonate.register
def foo(_, v):
    print("running foo")
    return f"{v} world"


def main():
    log.info("Starting node: foo")
    resonate.start()
    Event().wait()


if __name__ == "__main__":
    main()
