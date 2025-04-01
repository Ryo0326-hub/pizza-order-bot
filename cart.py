# cart.py
def add_pizza_to_cart(page):
    page.wait_for_selector("text=Deals")
    page.locator("text=Deals").click()
    page.wait_for_timeout(2000)

    # Click first deal
    page.locator("button:has-text('Order Now')").first.click()
    page.wait_for_timeout(3000)

    # Add to order
    page.locator("button:has-text('Add to Order')").click()
    page.wait_for_timeout(2000)
    print("🛒 Pizza added to cart")

