import pytest

from .driver import DEFAULT_BASELINE_DIR, DEFAULT_OUTPUT_DIR, AltVRTDriver


def pytest_addoption(parser):
    group = parser.getgroup("alt-vrt")

    group.addoption(
        "--alt-vrt-save-baseline", action="store_true",
    )

    group.addoption(
        "--alt-vrt-baseline-dir",
        action="store",
        dest="baseline_dir",
        metavar="dir",
        default=DEFAULT_BASELINE_DIR,
    )

    group.addoption(
        "--alt-vrt-output-dir",
        action="store",
        dest="output_dir",
        metavar="dir",
        default=DEFAULT_OUTPUT_DIR,
    )


@pytest.fixture
def alt_vrt(request, selenium):
    options = {
        "save_baseline": request.config.getoption("alt_vrt_save_baseline"),
        "baseline_dir": request.config.getoption("baseline_dir"),
        "output_dir": request.config.getoption("output_dir"),
    }

    return AltVRTDriver(selenium, **options)
