from sqlalchemy.orm import Session
from src.main.api.db.models.account_table import Account

class AccountCrudDb(Account):
    @staticmethod
    def get_account_by_id(db:Session, account_id:int):
        return db.query(Account).filter_by(id = account_id).first()

    @staticmethod
    def delete_account(db:Session, account_id:int) -> None:
        account = db.query(Account).filter_by(id = account_id).first()
        if account:
            db.delete(account)
            db.commit()
