from environ import Env
import os
from fast_bitrix24 import Bitrix
from database import get_equal_name


def main():
    settings = Env()
    Env.read_env(os.path.join(os.getcwd(), ".settings"))
    webhook = settings("WEBHOOK")

    bx = Bitrix(webhook)

    leads = bx.get_all(
        'crm.lead.list',
        params={"select": ["ID", "Name"]}
    )

    for lead in leads["result"]:
        name = lead["Name"]
        gender = get_equal_name(name)
        contact_id = lead["ID"]
        bx.call("crm.lead.update", params={"ID": contact_id, "GENDER": gender})


if __name__ == "__main__":
    main()
