# checkout.py
def go_to_checkout(page):
    page.locator("a[href*='/checkout']").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="checkout.png")
    print("🧾 Reached checkout page")
