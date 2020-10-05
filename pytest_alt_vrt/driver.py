import base64
from io import BytesIO
from pathlib import Path

from PIL import Image

from .image_diff import ImageDiffEngine

DEFAULT_BASELINE_DIR = Path.cwd() / "screenshots" / "baseline"
DEFAULT_OUTPUT_DIR = Path.cwd() / "screenshots"
DEFAULT_VIEWPORT_SIZE = "1024x768"


class AltVRTDriver:
    def __init__(self, driver, **options):

        self.driver = driver
        self.options = options

        self.driver.set_window_position(0, 0)
        self.set_viewport()

    def set_viewport(self):
        viewport_dimensions = DEFAULT_VIEWPORT_SIZE.split("x")

        self.driver.set_window_size(
            *[int(dimension) for dimension in viewport_dimensions]
        )

    def get_screenshot(self):
        stream = BytesIO(
            base64.b64decode(self.driver.get_screenshot_as_base64().encode("ascii"))
        )
        image = Image.open(stream).convert("RGB")

        return image

    @staticmethod
    def _create_dir(directory):
        Path(directory).mkdir(parents=True, exist_ok=True)

    def assert_screenshot(self, file_path, threshold=0):
        self._create_dir(self.baseline_dir)

        baseline_image = self.baseline_dir / f"{file_path}.png"

        if self.save_baseline:
            self.get_screenshot().save(baseline_image)
            return

        self._create_dir(self.output_dir)

        fresh_image = self.get_screenshot()

        fresh_image_file = self.output_dir / f"{file_path}.png"
        fresh_image.save(fresh_image_file)

        engine = ImageDiffEngine(baseline_image, fresh_image_file, threshold)
        engine.assertSameFiles()

    @property
    def baseline_dir(self):
        return self.options["baseline_dir"]

    @baseline_dir.setter
    def baseline_dir(self, value):
        self.options["baseline_dir"] = value

    @property
    def output_dir(self):
        return self.options["output_dir"]

    @output_dir.setter
    def output_dir(self, value):
        self.options["output_dir"] = value

    @property
    def save_baseline(self):
        return self.options["save_baseline"]

    @save_baseline.setter
    def save_baseline(self, value):
        self.options["save_baseline"] = value
