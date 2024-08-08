from ..context import AlistUser
from ..request import authenticated_client


async def dirs(
        alist_user: AlistUser,
        path: str = None,
        password: str = None,
        force_root: bool = False
):
    async with await authenticated_client(alist_user) as client:
        resp = await client.post(
            "/api/fs/dirs",
            json={
                "path": path,
                "password": password,
                "force_root": force_root
            }
        )
        return resp.json()


async def fs_list(
        alist_user: AlistUser,
        path: str,
        password: str = "",
        page: int = 1,
        per_page: int = 10,
        refresh: bool = False
):
    async with await authenticated_client(alist_user) as client:
        resp = await client.post(
            "/api/fs/list",
            json={
                "path": path,
                "password": password,
                "page": page,
                "per_page": per_page,
                "refresh": refresh
            }
        )
        return resp.json()
