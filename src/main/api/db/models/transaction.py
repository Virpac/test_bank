from sqlalchemy import Column,Integer,Float,ForeignKey,DateTime,String
from src.main.api.db.base import Base

class Transaction(Base):
    __tablename__ = "transaction"
    id = Column(Integer,primary_key=True,nullable=False)
    to_account_id = Column(Integer,nullable=False,ForeignKey="account.account_id")
    from_account_id = Column(Integer,nullable=False,ForeignKey="account.account_id")
    amount = Column(Float,nullable=False)
    credit_id = Column(Integer,nullable=False,ForeignKey="credit.id")
    amount = Column(Float,nullable=False)
    created_at = Column(DateTime,nullable=False)
    transaction_type = Column(String,nullable=False)