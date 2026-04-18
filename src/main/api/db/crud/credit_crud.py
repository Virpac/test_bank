from sqlalchemy.orm import Session
from src.main.api.db.models.credit_table import Credit

class CreditCrudDb(Credit):
    @staticmethod
    def get_credit_id(db: Session, account_id: int) -> Credit:
         return db.query(Credit).filter_by(account_id = account_id).first()