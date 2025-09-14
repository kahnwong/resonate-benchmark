# resonate server
serve:
	resonate serve

# api server
start-dev:
	uv run uvicorn resonate_benchmark.server:app --port 8081 --reload
start:
	uv run uvicorn resonate_benchmark.server:app --port 8081

# tests
get:
	hurl hurl/get.hurl

benchmark:
	oha http://localhost:8081 -n 100 -p 12 -o benchmark.json --output-format json
