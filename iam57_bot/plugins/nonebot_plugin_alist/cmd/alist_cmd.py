from nonebot import require

require("nonebot_plugin_alconna")
from arclet.alconna import Alconna, Subcommand
from nonebot_plugin_alconna import on_alconna

alist_cmd = on_alconna(
    Alconna(
        "alist",
        Subcommand("logout"),
        Subcommand("relogin"),
        Subcommand(
            "account",
            Subcommand("add"),
            Subcommand("del"),
            Subcommand("list"),
            Subcommand("switch")
        )
    ),
    use_cmd_sep=True,
    use_cmd_start=True
)
