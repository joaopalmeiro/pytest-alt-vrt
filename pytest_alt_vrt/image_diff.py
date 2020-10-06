import math

import pytest
from PIL import Image
from skimage.metrics import mean_squared_error

from .utils import pil2np


class ImageDiffEngine:
    def __init__(self, baseline_file, output_file, threshold):
        self.baseline_file = baseline_file
        self.output_file = output_file
        self.threshold = threshold

        self.baseline_image = Image.open(baseline_file).convert("RGB")
        self.output_image = Image.open(output_file).convert("RGB")

    def assert_same_images(self):
        diff = self.root_mean_squared_error()

        if diff > self.threshold:
            pytest.fail(f"New screenshot did not match the baseline ({diff})")

    # Version that uses Pillow and Python:
    # def root_mean_squared_error(self):
    #     diff = ImageChops.difference(self.baseline_image, self.output_image)

    #     squared_values = [d ** 2 for d in flatten(diff.getdata())]
    #     mse = mean(squared_values)
    #     rmse = math.sqrt(mse)

    #     return rmse

    # Version that uses NumPy, scikit-image, and Python:
    def root_mean_squared_error(self):
        rmse = math.sqrt(
            mean_squared_error(pil2np(self.baseline_image), pil2np(self.output_image))
        )

        return rmse
