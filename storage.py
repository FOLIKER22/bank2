import json
import os
from models import User, Account

DATA_FILE = "database.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": [], "accounts": []}

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    users = [User.from_dict(u) for u in data["users"]]
    accounts = [Account.from_dict(a) for a in data["accounts"]]

    return {"users": users, "accounts": accounts}


def save_data(users, accounts):
    data = {
        "users": [u.to_dict() for u in users],
        "accounts": [a.to_dict() for a in accounts]
    }

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
