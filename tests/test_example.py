def test_example_page(alt_vrt):
    alt_vrt.driver.get("https://www.example.com")
    alt_vrt.assert_screenshot("static_page")
