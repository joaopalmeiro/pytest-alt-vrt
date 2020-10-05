from itertools import chain

import pytest
from PIL import Image


class ImageDiffEngine:
    def __init__(self, baseline_file, output_file, threshold):
        self.baseline_file = baseline_file
        self.output_file = output_file
        self.threshold = threshold

    def assertSameFiles(self):
        baseline_image = Image.open(self.baseline_file).convert("RGB")
        output_image = Image.open(self.output_file).convert("RGB")

        distance = self.get_distance(baseline_image, output_image)

        if distance > self.threshold:
            pytest.fail("New screenshot did not match the baseline")

    @staticmethod
    def get_distance(baseline_image, output_image):
        baseline_values = chain(*baseline_image.getdata())
        output_values = chain(*output_image.getdata())

        band_len = len(output_image.getbands())

        distance = 0

        for output_value, baseline_value in zip(output_values, baseline_values):
            distance += (
                abs(float(output_value) / band_len - float(baseline_value) / band_len)
                / 255
            )

        return distance
