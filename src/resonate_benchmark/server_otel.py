import os
from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.propagate import inject
from resonate import Resonate

from resonate_benchmark.model.response import ResponseItem
from resonate_benchmark.utils.logger import init_logger

tracer = trace.get_tracer("resonate.tracer")

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

    headers = {}
    inject(headers)

    with tracer.start_as_current_span("server"):
        with tracer.start_as_current_span("server-promise"):
            identifier = str(uuid4())
            result = await resonate.options(
                target="poll://any@foo_nodes",
                tags={"traceparent": headers["traceparent"]},
            ).begin_rpc(id=identifier, func="foo", identifier=identifier)

            return ResponseItem(time=datetime.now(), message=result)
