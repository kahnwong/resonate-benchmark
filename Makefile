serve:
	resonate serve
start-api:
	uv run uvicorn resonate_benchmark.server:app --port 8081 --reload
