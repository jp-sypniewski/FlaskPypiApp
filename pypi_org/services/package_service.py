from typing import List

import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def get_latest_releases(limit = 10) -> List[Release]:
    session = db_session.create_session()

    releases = session.query(Release).\
        order_by(Release.created_date.desc()).\
        limit(limit).\
        all()

    return releases

def get_package_count() -> int:
    return 200
    session = db_session.create_session()
    return session.query(Package).count()

def get_release_count() -> int:
    return 200
    session = db_session.create_session()
    return session.query(Release).count()