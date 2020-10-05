def test_example_page(local_vrt):
    local_vrt.driver.get("https://www.example.com")
    local_vrt.assert_screenshot("static_page")
