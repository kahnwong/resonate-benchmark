# resonate server
serve:
	docker compose -f compose-db.yaml up -d
	resonate serve \
	    --aio-store-postgres-enable=true \
	    --aio-store-postgres-workers 8 \
	    --aio-store-postgres-host localhost \
	    --aio-store-postgres-port 5432 \
	    --aio-store-postgres-username postgres \
	    --aio-store-postgres-password postgrespassword \
	    --aio-store-postgres-database resonate \
	    --aio-store-postgres-query sslmode=disable

# api server
start-dev:
	uv run uvicorn resonate_benchmark.server:app --port 8081 --reload
start:
	uv run uvicorn resonate_benchmark.server:app --port 8081

# tests
get:
	hurl hurl/get.hurl

load-test:
	k6 run -u 100 -d 10s k6/load-test.js
