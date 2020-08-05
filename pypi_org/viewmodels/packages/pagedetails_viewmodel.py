from pypi_org.services import package_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class PackageDetailsViewModel(ViewModelBase):
    def __init__(self, package_name: str):
        super().__init__()

        # create package_name and package fields for use immediately below
        self.package_name = package_name
        self.package = None

        # if a package_name is passed, make that the field,
        # then find the package from the database service
        if package_name:
            self.package_name = package_name.strip().lower()
            self.package = package_service.get_package_by_id(self.package_name)

        # create latest_version, latest_release, and is_latest
        # fields for class
        self.latest_version = "0.0.0"
        self.latest_release = None
        self.is_latest = True

        # check if we found a package earlier and if there
        # are releases attached to it
        # if so, update the release related fields
        if self.package:
            self.latest_release = package_service.get_latest_release_for_package(self.package.id)
            if self.latest_release:
                self.latest_version = self.latest_release.version_text

        self.release_version = self.latest_release
