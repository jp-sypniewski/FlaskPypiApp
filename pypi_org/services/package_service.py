from typing import List, Optional
import sqlalchemy.orm as orm

import pypi_org.data.db_session as db_session
from pypi_org.data.package import Package
from pypi_org.data.releases import Release


def get_latest_releases(limit=10) -> List[Release]:
    session = db_session.create_session()

    releases = session.query(Release) \
        .options(orm.joinedload(Release.package)) \
        .order_by(Release.created_date.desc()) \
        .limit(limit) \
        .all()

    session.close()

    return releases


def get_package_count() -> int:
    session = db_session.create_session()
    return session.query(Package).count()


def get_release_count() -> int:
    session = db_session.create_session()
    return session.query(Release).count()


def get_package_by_id(package_id: str) -> Optional[Package]:
    if not package_id:
        return None

    package_id = package_id.strip().lower()
    session = db_session.create_session()
    package = session.query(Package) \
        .options(orm.joinedload(Package.releases)) \
        .filter(Package.id == package_id) \
        .first()

    session.close()

    return package


def all_packages(limit=10) -> List[Package]:
    session = db_session.create_session()
    packages = session.query(Package).limit(limit).all()

    return packages
