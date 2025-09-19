import os
from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI
from resonate import Resonate

from resonate_benchmark.model.response import ResponseItem
from resonate_benchmark.utils.logger import init_logger

log = init_logger(__name__)

resonate = Resonate.remote(host=os.environ["RESONATE_HOST"])
app = FastAPI(title="resonate-benchmark")


#######################
# routes
#######################
@app.get("/version")
async def root():
    return {"version": "0.1.0"}


@app.get("/", response_model=ResponseItem)
async def main() -> ResponseItem:
    # log.info(f"Input: {request}")

    identifier = str(uuid4())
    result = await resonate.options(target="poll://any@foo_nodes").begin_rpc(
        id=identifier, func="foo", identifier=identifier
    )

    # result="foo"
    return ResponseItem(time=datetime.now(), message=result)
