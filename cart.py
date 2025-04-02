# cart.py

def add_pizza_to_cart(page):
    # Wait for any deal that contains the phrase "Any Crust"
    page.wait_for_selector("text=Any Crust", timeout=10000)

    # Click the deal card's "Select" button
    deal_card = page.locator("text=Any Crust").first
    deal_card.scroll_into_view_if_needed()
    deal_card.locator("..").locator("text=Select").click()

    page.wait_for_timeout(3000)
    print("🍕 Deal selected: Any Crust, Any Size")

    # Open pizza chooser
    page.wait_for_selector("text=Choose a pizza", timeout=10000)
    page.locator("text=Choose a pizza").click()
    page.wait_for_timeout(1000)

    # Select "Create your Own"
    page.locator("text=Create your Own").click()
    page.wait_for_timeout(2000)

    # ✅ More specific selector to wait for the customization modal
    page.wait_for_selector("text=Pan", timeout=10000)

    # Choose crust
    crust_button = page.locator('[data-synth="add--12-medium--12-medium-1P2.crusts.pan"]')
    crust_button.scroll_into_view_if_needed()
    crust_button.click()

    page.wait_for_timeout(1000)
    print("🍞 Selected crust: 12\" Medium Pan")

    # Add toppings
    def add_topping(page, topping_name):
        print(f"🔍 Looking for topping: {topping_name}")

        topping_element = page.locator(f"text={topping_name}").first
        topping_element.scroll_into_view_if_needed()
        page.wait_for_timeout(500)
        topping_element.click()

        print(f"✅ Clicked topping: {topping_name}")
        page.wait_for_timeout(1000)

    for topping in ["Pepperoni", "Mushroom"]:
        add_topping(page, topping)

    # Final add to deal
    page.locator("button:has-text('Add to my deal')").click()
    page.wait_for_timeout(3000)
    # Final add to deal
    page.locator("button:has-text('Add deal to basket')").click()
    page.wait_for_timeout(3000)
    print("🛒 Deal added to basket")




