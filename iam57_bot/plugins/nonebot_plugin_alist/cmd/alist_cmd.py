from nonebot import require

require("nonebot_plugin_alconna")
from arclet.alconna import Alconna, Args, Subcommand
from nonebot_plugin_alconna import on_alconna

alist_cmd = on_alconna(
    Alconna(
        "alist",
        Subcommand(
            "cd",
            Args["path", str]
        ),
        Subcommand("logout"),
        Subcommand("me"),
        Subcommand("relogin"),
        Subcommand(
            "account",
            Subcommand("add"),
            Subcommand("del"),
            Subcommand("info"),
            Subcommand("list"),
            Subcommand("switch")
        )
    ),
    use_cmd_sep=True,
    use_cmd_start=True
)
