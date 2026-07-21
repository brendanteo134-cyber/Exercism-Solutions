import json
from typing import Iterable
class User:
    def __init__(self, name, owed_by=None, owes=None, **kwargs):
        self.name = name
        self.ledger = {}
        for borrower, amount in (owed_by or {}).items():
            self.loan(borrower, amount)
        for lender, amount in (owes or {}).items():
            self.borrow(lender, amount)
    def borrow(self, borrower, amount):
        self.ledger[borrower] = self.ledger.get(borrower, 0) - amount
    def loan(self, lender, amount):
        self.ledger[lender] = self.ledger.get(lender, 0) + amount
    def to_dict(self) -> dict:
        return {"name": self.name, "owes": self.owes, "owed_by": self.owed_by, "balance": self.balance}
    @property
    def owes(self):
        return {name: -amount for name, amount in self.ledger.items() if amount < 0}
    @property
    def owed_by(self):
        return {name: amount for name, amount in self.ledger.items() if amount > 0}
    @property
    def balance(self):
        return sum(self.ledger.values())
class RestAPI:
    def __init__(self, database: Iterable[dict] = None):
        self.users = {user["name"]: User(**user) for user in (database or {}).get("users", [])}
    def get(self, url: str, payload: str = None) -> json:
        response = None
        if url == "/users":
            if payload:
                payload = json.loads(payload)
            response = self._users(payload)
        else:
            raise ValueError(f"{url} [GET] does not exist")
        return json.dumps(response, default=User.to_dict)
    def post(self, url: str, payload: str = None) -> json:
        response = None
        if url == "/add":
            response = self._add(json.loads(payload))
        elif url == "/iou":
            response = self._iou(json.loads(payload))
        else:
            raise ValueError(f"{url} [POST] does not exist")
        return json.dumps(response, default=User.to_dict)
    def _users(self, payload: dict = None) -> dict:
        if payload is None:
            return {"users": sorted([user.to_dict() for _, user in self.users.values()], key=lambda x: x.name)}
        else:
            return {"users": sorted([self.users[name] for name in payload["users"]], key=lambda x: x.name)}
    def _add(self, payload: dict) -> dict:
        if payload["user"] in self.users:
            raise ValueError("Name Exists in Database")
        else:
            self.users[payload["user"]] = User(name=payload["user"])
        return self.users[payload["user"]].to_dict()
    def _iou(self, payload: dict) -> dict:
        self.users[payload["borrower"]].borrow(payload["lender"], payload["amount"])
        self.users[payload["lender"]].loan(payload["borrower"], payload["amount"])
        return {"users": sorted([self.users[payload["lender"]], self.users[payload["borrower"]]], key=lambda x: x.name)}