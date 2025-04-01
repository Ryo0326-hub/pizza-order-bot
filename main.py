from playwright.sync_api import sync_playwright
from login import launch_browser
from search import set_delivery_location
from cart import add_pizza_to_cart
from checkout import go_to_checkout

def run():
    with sync_playwright() as p:
        browser, page = launch_browser(p)
        set_delivery_location(page)
        add_pizza_to_cart(page)
        go_to_checkout(page)
        browser.close()

if __name__ == "__main__":
    run()


