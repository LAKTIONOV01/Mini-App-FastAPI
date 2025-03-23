import pytest
import asyncio
from httpx import AsyncClient, ASGITransport

from main import app

@pytest.mark.asyncio
async def test_get_books():
    async with AsyncClient(transport=ASGITransport(app=app), base_url='http://test') as ac:
        response = await ac.get('/books')
        print(response)

