def go_to_checkout(page):
    # Go to checkout page
    page.locator("a[href*='/checkout']").click()
    page.wait_for_selector("text=First Name", timeout=10000)
    print("🧾 Reached checkout page")

    # Fill in the customer info
    print("✍️  Filling in customer details...")
    page.fill("input[placeholder='First Name']", "Ryo")
    page.fill("input[placeholder='Last Name']", "Kitano")
    page.fill("input[placeholder='So we can contact you']", "1234567890")  # use a real number if needed
    page.fill("input[placeholder='To send your confirmation']", "rkitano0326@gmail.com")

    page.wait_for_timeout(2000)
    page.screenshot(path="filled_checkout.png")
    print("✅ Customer info filled in")

