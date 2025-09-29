import os
import sys
from threading import Event

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from resonate import Resonate

from resonate_benchmark.utils import simulation
from resonate_benchmark.utils.logger import init_logger

provider = TracerProvider()
exporter = ConsoleSpanExporter(out=sys.stdout)

processor = SimpleSpanProcessor(exporter)
provider.add_span_processor(processor)

trace.set_tracer_provider(provider)
tracer = trace.get_tracer("resonate.tracer")

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
def foo(context, identifier: str) -> str:
    ctx = TraceContextTextMapPropagator().extract(
        {"traceparent": context.info.tags["traceparent"]}
    )

    with tracer.start_as_current_span("node", context=ctx):
        print(f"id: {identifier}")

        if not simulation.random_failure():
            return identifier
        else:
            log.error("Random failure")
            raise Exception("Random failure")


def main():
    log.info("Starting node: foo")

    with tracer.start_as_current_span("root"):
        resonate.start()
        Event().wait()


if __name__ == "__main__":
    main()
