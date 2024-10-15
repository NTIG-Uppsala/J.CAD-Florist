from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

class CompanyInformation(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    # companyPhoneNumber = db.Column(db.String(32))
    companyPhoneNumber: so.Mapped[str] = so.mapped_column(sa.String(32), index=True, unique=True)

    def __repr__(self):
        return '<CompanyInformation {}>'.format(self.id)