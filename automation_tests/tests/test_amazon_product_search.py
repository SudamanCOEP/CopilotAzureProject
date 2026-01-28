"""
Test Suite for Amazon Product Search
Work Item ID: 2
Description: Automation to search for a product on amazon
"""

import pytest
from playwright.async_api import Page, expect


class TestAmazonProductSearch:
    """Test cases for Amazon product search functionality."""

    async def test_search_page_loads(self, page: Page, amazon_url: str):
        """Test that Amazon homepage loads successfully."""
        await page.goto(amazon_url)
        await expect(page).to_have_url(amazon_url)

    async def test_search_bar_visible(self, page: Page, amazon_url: str):
        """Test that search bar is visible on homepage."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await expect(search_box).to_be_visible()

    async def test_search_bar_accepts_input(self, page: Page, amazon_url: str):
        """Test that search bar accepts user input."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await search_box.fill("laptop")
        await expect(search_box).to_have_value("laptop")

    async def test_search_product_by_name(self, page: Page, amazon_url: str):
        """Test searching for a product by name."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await search_box.fill("iPhone 15")
        
        search_button = page.locator('input[type="submit"]')
        await search_button.click()
        
        # Wait for results page to load
        await page.wait_for_url("**/s?k=*", timeout=10000)

    async def test_search_results_display(self, page: Page, amazon_url: str):
        """Test that search results are displayed."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await search_box.fill("wireless headphones")
        
        search_button = page.locator('input[type="submit"]')
        await search_button.click()
        
        # Wait for results
        await page.wait_for_url("**/s?k=*", timeout=10000)
        
        # Check for product results
        products = page.locator('[data-component-type="s-search-result"]')
        await expect(products.first).to_be_visible()

    async def test_search_result_count(self, page: Page, amazon_url: str):
        """Test that search results count is displayed."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await search_box.fill("books")
        
        search_button = page.locator('input[type="submit"]')
        await search_button.click()
        
        await page.wait_for_url("**/s?k=*", timeout=10000)
        
        # Check for results count
        results_count = page.locator('h2 span')
        await expect(results_count).to_be_visible()

    async def test_product_details_clickable(self, page: Page, amazon_url: str):
        """Test that product results are clickable and navigate to product page."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await search_box.fill("USB cable")
        
        search_button = page.locator('input[type="submit"]')
        await search_button.click()
        
        await page.wait_for_url("**/s?k=*", timeout=10000)
        
        # Click on first product
        first_product = page.locator('[data-component-type="s-search-result"] a[href*="/dp/"]').first
        initial_url = page.url
        await first_product.click()
        
        # Wait for navigation
        await page.wait_for_load_state('networkidle')
        await expect(page).not_to_have_url(initial_url)

    async def test_search_with_empty_query(self, page: Page, amazon_url: str):
        """Test search behavior with empty query."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        search_button = page.locator('input[type="submit"]')
        
        # Try to search without entering text
        await search_button.click()
        
        # Page should remain on homepage or show results
        await page.wait_for_load_state('networkidle')

    async def test_search_filters_available(self, page: Page, amazon_url: str):
        """Test that search filters are available on results page."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await search_box.fill("smartphone")
        
        search_button = page.locator('input[type="submit"]')
        await search_button.click()
        
        await page.wait_for_url("**/s?k=*", timeout=10000)
        
        # Check for filter section
        filter_section = page.locator('[data-feature-name="sb-filter-refinements"]')
        await expect(filter_section).to_be_visible()

    async def test_search_sorting_option(self, page: Page, amazon_url: str):
        """Test that sorting options are available."""
        await page.goto(amazon_url)
        search_box = page.locator('#twotabsearchtextbox')
        await search_box.fill("monitor")
        
        search_button = page.locator('input[type="submit"]')
        await search_button.click()
        
        await page.wait_for_url("**/s?k=*", timeout=10000)
        
        # Check for sorting dropdown
        sort_dropdown = page.locator('[data-feature-name="cr-sort-select"]')
        await expect(sort_dropdown).to_be_visible()
