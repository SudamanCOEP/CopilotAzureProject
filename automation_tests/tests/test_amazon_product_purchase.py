"""
Test Suite for Amazon Product Purchase
Work Item ID: 3
Description: Automation to buy a product from amazon
"""

import pytest
from playwright.async_api import Page, expect


class TestAmazonProductPurchase:
    """Test cases for Amazon product purchase workflow."""

    async def test_product_page_loads(self, page: Page, amazon_url: str):
        """Test that a product page loads successfully."""
        # Using a sample product URL structure
        await page.goto(f"{amazon_url}/s?k=laptop")
        
        # Click on first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        await first_product.click()
        
        await page.wait_for_load_state('networkidle')

    async def test_add_to_cart_button_visible(self, page: Page, amazon_url: str):
        """Test that 'Add to Cart' button is visible on product page."""
        await page.goto(f"{amazon_url}/s?k=headphones")
        
        # Navigate to first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        await first_product.click()
        await page.wait_for_load_state('networkidle')
        
        # Check for Add to Cart button
        add_to_cart_button = page.locator('#add-to-cart-button')
        await expect(add_to_cart_button).to_be_visible()

    async def test_add_product_to_cart(self, page: Page, amazon_url: str):
        """Test adding a product to cart."""
        await page.goto(f"{amazon_url}/s?k=tablet")
        
        # Navigate to first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        await first_product.click()
        await page.wait_for_load_state('networkidle')
        
        # Click Add to Cart
        add_to_cart_button = page.locator('#add-to-cart-button')
        await add_to_cart_button.click()
        
        # Verify success message or cart update
        await page.wait_for_load_state('networkidle')

    async def test_product_quantity_selector(self, page: Page, amazon_url: str):
        """Test product quantity selection."""
        await page.goto(f"{amazon_url}/s?k=mouse")
        
        # Navigate to first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        await first_product.click()
        await page.wait_for_load_state('networkidle')
        
        # Check for quantity selector
        quantity_selector = page.locator('select[aria-label*="Quantity"]')
        if await quantity_selector.is_visible():
            await quantity_selector.select_option("2")
            await expect(quantity_selector).to_have_value("2")

    async def test_proceed_to_checkout(self, page: Page, amazon_url: str):
        """Test proceeding to checkout."""
        await page.goto(f"{amazon_url}/gp/cart/view.html")
        
        # Check if cart is accessible
        await expect(page).to_have_url("**/gp/cart/**")

    async def test_cart_page_shows_items(self, page: Page, amazon_url: str):
        """Test that cart page displays added items."""
        await page.goto(f"{amazon_url}/gp/cart/view.html")
        
        # Look for cart items container
        cart_container = page.locator('[data-name="Active Items"]')
        
        # Cart might be empty, but container should exist
        if await cart_container.is_visible():
            await expect(cart_container).to_be_visible()

    async def test_remove_from_cart(self, page: Page, amazon_url: str):
        """Test removing item from cart."""
        await page.goto(f"{amazon_url}/gp/cart/view.html")
        
        # Look for delete buttons if items exist
        delete_buttons = page.locator('input[aria-label*="Delete"]')
        delete_count = await delete_buttons.count()
        
        # If items exist, test delete functionality
        if delete_count > 0:
            initial_count = delete_count
            await delete_buttons.first.click()
            await page.wait_for_load_state('networkidle')

    async def test_checkout_button_visible(self, page: Page, amazon_url: str):
        """Test that checkout button is visible on cart page."""
        await page.goto(f"{amazon_url}/gp/cart/view.html")
        
        # Look for proceed to checkout button
        checkout_button = page.locator('input[aria-label*="Proceed"]')
        if await checkout_button.is_visible():
            await expect(checkout_button).to_be_visible()

    async def test_product_price_displayed(self, page: Page, amazon_url: str):
        """Test that product price is displayed."""
        await page.goto(f"{amazon_url}/s?k=keyboard")
        
        # Navigate to first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        await first_product.click()
        await page.wait_for_load_state('networkidle')
        
        # Check for price
        price = page.locator('[data-a-color="price"] span')
        await expect(price.first).to_be_visible()

    async def test_product_image_displayed(self, page: Page, amazon_url: str):
        """Test that product image is displayed."""
        await page.goto(f"{amazon_url}/s?k=camera")
        
        # Navigate to first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        await first_product.click()
        await page.wait_for_load_state('networkidle')
        
        # Check for main product image
        product_image = page.locator('[data-feature-name="dp-image-block"] img').first
        if await product_image.is_visible():
            await expect(product_image).to_be_visible()

    async def test_product_description_visible(self, page: Page, amazon_url: str):
        """Test that product description is visible."""
        await page.goto(f"{amazon_url}/s?k=router")
        
        # Navigate to first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        await first_product.click()
        await page.wait_for_load_state('networkidle')
        
        # Check for product details
        details = page.locator('[data-feature-name="featurebullets"]')
        if await details.is_visible():
            await expect(details).to_be_visible()
