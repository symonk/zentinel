import pytest

from zentinel import main


@pytest.fixture(scope="function")
def run_zentinel():
    return lambda *args: main(*args)
