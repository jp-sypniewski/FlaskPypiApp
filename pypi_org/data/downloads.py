import datetime

import sqlalchemy as sa

from pypi_org.data.modelbase import SqlAlchemyBase

class Download(SqlAlchemyBase):
    __tablename__ = 'downloads'

    id = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_date = sa.Column(sa.DateTime, default=datetime.datetime.now, index=True)

    package_id = sa.Column(sa.String, index=True)
    release_id = sa.Column(sa.BigInteger, index=True)

    ip_address = sa.Column(sa.String)
    user_agent = sa.Column(sa.String)