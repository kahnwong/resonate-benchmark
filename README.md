# resonate-benchmark

Ref: <https://docs.resonatehq.io/get-started/existing-project>

## Pre-reqs

```bash
go install github.com/resonatehq/resonate@latest
```

## Start server

```bash
make serve
make start-node  # start foo node
```

## Run

```bash
# single call
make test

# api call
make start
make get
```

## Benchmark

```bash
make load-test
```


## Results

```bash
# 1 node
iteration_duration.............: avg=3.35s min=1.8s  med=3.52s max=9.25s p(90)=3.69s p(95)=3.73s
iterations.....................: 315   19.123229/s

# 2 nodes
iteration_duration.............: avg=3.31s min=1.91s med=3.41s max=5.37s p(90)=3.48s p(95)=3.49s
iterations.....................: 322   24.32773/s

# 4 nodes
iteration_duration.............: avg=3.25s min=1.93s med=3.28s max=6.23s p(90)=3.39s p(95)=4.32s
iterations.....................: 390   26.489844/s

# 6 nodes
iteration_duration.............: avg=3.4s  min=2.14s med=3.27s max=6.16s p(90)=4.8s p(95)=4.8s
iterations.....................: 376   25.406649/s

# 8 nodes
iteration_duration.............: avg=3.14s min=2s    med=3.29s max=8.32s p(90)=3.96s p(95)=3.98s
iterations.....................: 357   26.773127/s

# 12 nodes
iteration_duration.............: avg=3.5s min=1.94s med=3.64s max=16.64s p(90)=4.19s p(95)=5.14s
iterations.....................: 325   8.12486/s
```

## Remarks

- Runs with the same ID are cached
