from typing import Dict, Optional
from pydantic import BaseModel, ConfigDict

from nonebot.adapters import Event
from nonebot_plugin_alconna import AlconnaMatcher, At, UniMessage

from ..enum import DeletePolicy, DownloadTool
from ..models import User


class AlistUser(BaseModel):
    default_path: str = "/"
    user_account: Optional[User] = None
    delete_policy: DeletePolicy = DeletePolicy.SUCCEED
    download_tool: DownloadTool = DownloadTool.QBITTORRENT

    model_config = ConfigDict(arbitrary_types_allowed=True)


class AlistUserManager:
    _alist_users: Dict[str, AlistUser] = dict()

    @classmethod
    async def get_by_user_id(cls, user_id: str) -> Optional[AlistUser]:
        user_account = await User.get_or_none(user_id=user_id)
        if user_account and user_account.main_account_id:
            alist_user = cls._alist_users.get(user_id)
            if not alist_user:
                alist_user = AlistUser(user_account=user_account)
                cls._alist_users[user_id] = alist_user
            else:
                alist_user.user_account = user_account
            return alist_user
        return None

    @classmethod
    def remove_by_user_id(cls, user_id: str) -> None:
        cls._alist_users.pop(user_id, None)


async def get_alist_user(matcher: AlconnaMatcher, event: Event) -> AlistUser:
    user_id = event.get_user_id()
    alist_user = await AlistUserManager.get_by_user_id(user_id)
    if not alist_user:
        await matcher.finish(
            UniMessage([At("user", event.get_user_id()), "【Alist】您未登录任何账号!"])
        )
    return alist_user
