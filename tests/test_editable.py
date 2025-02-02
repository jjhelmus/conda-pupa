from pathlib import Path

import pytest

from conda_pupa.editable import editable, normalize


def test_editable():
    editable(Path(__file__).parents[1])


def test_normalize():
    assert normalize("flit_core") == "flit-core"


def pypa_build_packages():
    """
    Test packages from pypa/build repository.

    (Clone pypa/build into tests/)
    """
    here = Path(__file__).parent
    return list(p.name for p in Path(here, "build", "tests", "packages").glob("*"))


@pytest.fixture
def package_path():
    here = Path(__file__).parent
    return Path(here, "build", "tests", "packages")


@pytest.mark.parametrize("package", pypa_build_packages())
def test_build_wheel(package, package_path):
    # Some of these will not contain the editable hook; need to test building
    # regular wheels also. Some will require a "yes" for conda install
    # dependencies.
    editable(package_path / package)
