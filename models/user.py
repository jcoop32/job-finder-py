from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column
from sqlalchemy.dialects.mysql import TINYINT, VARCHAR, INTEGER
from app import app


db = SQLAlchemy(app)


class Investor(db.Model):
    id = Column(INTEGER, primary_key=True)
    email = Column(VARCHAR(length=45), nullable=False)
    f_name = Column(VARCHAR(length=45), nullable=False)
    l_name = Column(VARCHAR(length=45), nullable=True)
    description = Column(VARCHAR(length=256), nullable=True)
    contacted = Column(TINYINT, default=0)

    def __repr__(self):
        return "<Investor %r>" % self.id
