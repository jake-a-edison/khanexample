import run
import pytest


@pytest.mark.asyncio
async def test_external():
    result = await run.get_external()
    assert isinstance(result, str)
