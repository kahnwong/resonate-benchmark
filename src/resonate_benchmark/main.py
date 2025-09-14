import os
from uuid import uuid4

from resonate import Resonate

resonate = Resonate.remote(host=os.environ["RESONATE_HOST"])


def main():
    try:
        result = resonate.options(target="poll://any@foo_nodes").rpc(
            id=str(uuid4()), func="foo", v="baz"
        )

        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
