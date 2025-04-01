# login.py
def launch_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        geolocation={"latitude": 43.6532, "longitude": -79.3832},
        permissions=["geolocation"],
        locale="en-CA"
    )
    page = context.new_page()
    return browser, page


