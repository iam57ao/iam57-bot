from httpx import AsyncClient, Response
from nonebot import get_plugin_config

from ..common.auth_service.logout_service import logout_and_switch_main_account
from ..config import Config
from ..context import AlistUser

plugin_config = get_plugin_config(Config)


def async_client(site_url: str) -> AsyncClient:
    return AsyncClient(
        base_url=site_url,
        timeout=plugin_config.alist_request_timeout,
    )


async def async_client_with_au(alist_user: AlistUser) -> AsyncClient:
    user = alist_user.user
    account = await user.get_main_account()
    token = account.token if account else ""
    client = AsyncClient(
        base_url=account.site_url,
        headers={"Authorization": token},
        timeout=plugin_config.alist_request_timeout,
    )

    async def auto_logout(resp: Response):
        await resp.aread()
        if resp.json()["code"] == 401:
            await logout_and_switch_main_account(alist_user)

    client.event_hooks['response'] = [auto_logout]
    return client
