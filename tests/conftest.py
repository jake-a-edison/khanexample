import khan
import asyncio
import pytest

LOOP = asyncio.get_event_loop()
khan.context.install_task_factory(LOOP)


@pytest.yield_fixture(scope="session")
def event_loop():
    global LOOP
    yield LOOP


@pytest.yield_fixture(scope="session")
def loop(event_loop):
    yield event_loop
