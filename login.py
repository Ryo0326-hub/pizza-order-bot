# login.py
def launch_browser(playwright, headless=True):
    browser = playwright.chromium.launch(headless=headless)
    context = browser.new_context(
        geolocation={"latitude": 43.6532, "longitude": -79.3832},
        permissions=["geolocation"],
        locale="en-CA",
        viewport={"width": 1280, "height": 800},
    )
    page = context.new_page()
    return browser, page


