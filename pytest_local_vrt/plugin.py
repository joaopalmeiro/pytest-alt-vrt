import pytest

from .driver import DEFAULT_BASELINE_DIR, DEFAULT_OUTPUT_DIR, LocalVRTDriver


def pytest_addoption(parser):
    """
    :param parser:
    :return:
    """

    group = parser.getgroup("needle")

    group.addoption(
        "--local-vrt-save-baseline", action="store_true",
    )

    group.addoption(
        "--local-vrt-baseline-dir",
        action="store",
        dest="baseline_dir",
        metavar="dir",
        default=DEFAULT_BASELINE_DIR,
    )

    group.addoption(
        "--local-vrt-output-dir",
        action="store",
        dest="output_dir",
        metavar="dir",
        default=DEFAULT_OUTPUT_DIR,
    )


@pytest.fixture()
def local_vrt(request, selenium):
    options = {
        "save_baseline": request.config.getoption("local_vrt_save_baseline"),
        "baseline_dir": request.config.getoption("baseline_dir"),
        "output_dir": request.config.getoption("output_dir"),
    }

    return LocalVRTDriver(selenium, **options)
