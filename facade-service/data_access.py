"""
This module is responsible for getting the data for the facade service.
"""
import httpx


class DataAccess:
    async def post(self, url, msg):
        async with httpx.AsyncClient() as client:
            return await client.post(url, json=msg)

    async def get(self, url):
        async with httpx.AsyncClient() as client:
            return await client.get(url)
