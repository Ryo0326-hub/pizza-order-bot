# search.py

def set_delivery_location(page, address="250 Yonge St, Toronto, ON"):
    page.goto("https://www.pizzahut.ca", timeout=60000)
    page.wait_for_selector("input[placeholder='Your street number and name']", timeout=10000)

    # Type the address
    page.fill("input[placeholder='Your street number and name']", address)
    page.wait_for_timeout(500)
    page.keyboard.press(" ")

    # Wait for any element that contains "250 Yonge St"
    suggestion_locator = page.locator("text='250 Yonge St'").first
    suggestion_locator.wait_for(timeout=5000)
    suggestion_locator.click()

    page.wait_for_timeout(3000)
    print(f"📍 Clicked on address suggestion: {address}")




