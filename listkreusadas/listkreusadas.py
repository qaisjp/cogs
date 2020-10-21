from datetime import date
from collections import Counter

from instantcmd.utils import listener
from redbot.core.utils.chat_formatting import pagify
from tabulate import tabulate


async def sth(after):
    l = sorted(
        [
            [m.display_name.strip("\ua9c1\ua9c2 "), m.name.strip("\ua9c1\ua9c2 ")]
            for m in bot.get_guild(133049272517001216).members
            if (
                Counter(m.display_name.strip("\ua9c1\ua9c2 ").lower()[:6]) == Counter("twenty")
                or Counter(m.name.strip("\ua9c1\ua9c2 ").lower()[:6]) == Counter("twenty")
            )
        ],
        key=lambda x: x[0].lower(),
    )
    table = pagify(
        tabulate(l, headers=["Twentysix Edition", "Bearer of this edition"]).replace("```", r"`​`​`"),
        page_length=1850,
    )
    c = bot.get_channel(171665724262055936)
    await c.send(
        f"<@176070082584248320> new Twentysix ({after.display_name}) arrived!"
        f" <:aha:350653489044652052> We have {len(l)} Twentysixes now! "
        f"```asciidoc\n{next(table)}\n```"
    )
    for p in table:
        await c.send(f"```asciidoc\n{p}\n```")


@listener(name="on_member_update")
async def on26_member_update(before, after):
    if (
        before.display_name.strip("\ua9c1\ua9c2 ") != after.display_name.strip("\ua9c1\ua9c2 ")
        and Counter(before.display_name.strip("\ua9c1\ua9c2 ").lower()[:6]) != Counter("twenty")
        and Counter(after.display_name.strip("\ua9c1\ua9c2 ").lower()[:6]) == Counter("twenty")
    ):
        await sth(after)


return on26_member_update
