import os
from uuid import uuid4

from resonate import Resonate

resonate = Resonate.remote(host=os.environ["RESONATE_HOST"])


def main():
    identifier = str(uuid4())
    # try:
    result = resonate.options(target="poll://any@foo_nodes").rpc(
        id=identifier, func="foo_str", identifier=identifier
    )

    print(result)
    # except Exception as e:
    #     print(e)


if __name__ == "__main__":
    main()
