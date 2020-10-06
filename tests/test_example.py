import altair as alt
import pytest


@pytest.fixture
def example_chart():
    source = alt.pd.DataFrame(
        {
            "a": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
            "b": [28, 55, 43, 91, 81, 53, 19, 87, 52],
        }
    )

    chart = alt.Chart(source).mark_bar().encode(x="a", y="b")

    return chart


def test_example_chart(alt_vrt, example_chart):
    name = "example_chart"

    uri = alt_vrt.generate_html(name, example_chart)

    alt_vrt.driver.get(uri)
    alt_vrt.assert_screenshot(name)
