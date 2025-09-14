import pytest

from resonate_benchmark.utils import simulation


@pytest.mark.parametrize("event", list(range(100)))
def test_random_failure(event):
    print(f"id: {event}")

    assert not simulation.random_failure()
