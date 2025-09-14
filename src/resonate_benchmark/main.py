import os
from datetime import datetime
from uuid import uuid4

from resonate import Resonate

resonate = Resonate.remote(host=os.environ["RESONATE_HOST"])


def main():
    identifier = str(uuid4())

    # try:
    start = datetime.now()
    result = resonate.options(target="poll://any@foo_nodes").rpc(
        id=identifier, func="foo_str", identifier=identifier
    )
    end = datetime.now()
    print(f"Time taken: {(end - start).total_seconds()}")

    print(result)
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    main()
