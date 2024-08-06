from ..util.request import async_client


async def login_hash(site_url: str, username: str, password_hash: str):
    async with async_client(site_url) as client:
        resp = await client.post(
            "/api/auth/login/hash",
            json={
                "username": username,
                "password": password_hash
            }
        )
        return resp.json()
