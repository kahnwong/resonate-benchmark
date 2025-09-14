# resonate-benchmark

Ref: <https://docs.resonatehq.io/get-started/existing-project>

## Start server

```bash
make serve
uv run foo  # start foo node
```

## Run

```bash
# single call
uv run main

# api call
uv run start-api
make get
```

## Benchmark

```bash
make benchmark
```


## Results

```bash
# 1 node - 70 interrupted iterations
avg=20.2s min=2.03s med=21.36s max=39.68s p(90)=29.91s p(95)=30.72s

# 2 node - 77 interrupted iterations
avg=20.47s min=1.01s med=22.3s max=38.55s p(90)=33.69s p(95)=36.32s

# 4 node - 70 interrupted iterations
avg=21.32s min=2.04s med=21.35s max=39.66s p(90)=36s p(95)=37.83s
```

## Remarks

- Runs with the same ID are cached
