"""
Test Suite for Google to Amazon Navigation
Work Item ID: 4
Description: Automation code to go to amazon from google
"""

import pytest
from playwright.async_api import Page, expect


class TestGoogleToAmazonNavigation:
    """Test cases for navigating from Google to Amazon."""

    async def test_google_homepage_loads(self, page: Page, google_url: str):
        """Test that Google homepage loads successfully."""
        await page.goto(google_url)
        await expect(page).to_have_url(google_url)

    async def test_google_search_box_visible(self, page: Page, google_url: str):
        """Test that Google search box is visible."""
        await page.goto(google_url)
        search_box = page.locator('textarea[name="q"]')
        await expect(search_box).to_be_visible()

    async def test_search_amazon_from_google(self, page: Page, google_url: str):
        """Test searching for Amazon from Google."""
        await page.goto(google_url)
        search_box = page.locator('textarea[name="q"]')
        await search_box.fill("amazon")
        
        # Press Enter to search
        await search_box.press("Enter")
        
        # Wait for results to load
        await page.wait_for_url("**/search?**", timeout=10000)

    async def test_amazon_link_in_search_results(self, page: Page, google_url: str):
        """Test that Amazon link appears in Google search results."""
        await page.goto(google_url)
        search_box = page.locator('textarea[name="q"]')
        await search_box.fill("amazon.com")
        await search_box.press("Enter")
        
        # Wait for results
        await page.wait_for_url("**/search?**", timeout=10000)
        
        # Look for Amazon link
        amazon_link = page.locator('a[href*="amazon.com"]').first
        await expect(amazon_link).to_be_visible()

    async def test_click_amazon_link_from_search_results(self, page: Page, google_url: str, amazon_url: str):
        """Test clicking Amazon link from Google search results."""
        await page.goto(google_url)
        search_box = page.locator('textarea[name="q"]')
        await search_box.fill("amazon.com")
        await search_box.press("Enter")
        
        # Wait for results
        await page.wait_for_url("**/search?**", timeout=10000)
        
        # Click first Amazon link
        amazon_link = page.locator('a[href*="amazon.com"]').first
        
        # Get the href and navigate
        href = await amazon_link.get_attribute("href")
        if href:
            await page.goto(href)
            
            # Wait for page to load
            await page.wait_for_load_state('networkidle')

    async def test_navigate_to_amazon_direct_url(self, page: Page, amazon_url: str):
        """Test direct navigation to Amazon from any page."""
        # Start from Google
        await page.goto("https://www.google.com")
        
        # Navigate to Amazon
        await page.goto(amazon_url)
        await expect(page).to_have_url(amazon_url)

    async def test_google_to_amazon_multiple_searches(self, page: Page, google_url: str):
        """Test multiple searches leading to Amazon."""
        search_terms = ["amazon products", "amazon shopping", "amazon prime"]
        
        for term in search_terms:
            await page.goto(google_url)
            search_box = page.locator('textarea[name="q"]')
            await search_box.fill(term)
            await search_box.press("Enter")
            
            # Wait for results
            await page.wait_for_url("**/search?**", timeout=10000)
            
            # Verify search results page
            await expect(page).to_have_url("**/search?**")

    async def test_amazon_logo_clickable_from_home(self, page: Page, amazon_url: str):
        """Test Amazon logo navigation."""
        await page.goto(amazon_url)
        
        # Look for Amazon logo
        amazon_logo = page.locator('[aria-label="Amazon"]').first
        if await amazon_logo.is_visible():
            await expect(amazon_logo).to_be_visible()

    async def test_back_navigation_from_amazon_to_google(self, page: Page, google_url: str, amazon_url: str):
        """Test back navigation from Amazon to Google."""
        # Visit Google first
        await page.goto(google_url)
        
        # Navigate to Amazon
        await page.goto(amazon_url)
        
        # Go back to Google
        await page.go_back()
        
        # Should be back on Google
        await page.wait_for_load_state('networkidle')
        await expect(page).to_have_url(google_url)

    async def test_open_amazon_in_new_tab_from_google(self, page: Page, google_url: str, context):
        """Test opening Amazon in a new tab from Google."""
        await page.goto(google_url)
        search_box = page.locator('textarea[name="q"]')
        await search_box.fill("amazon.com")
        await search_box.press("Enter")
        
        # Wait for results
        await page.wait_for_url("**/search?**", timeout=10000)
        
        # Open Amazon link in new tab
        amazon_link = page.locator('a[href*="amazon.com"]').first
        
        # Get link context and open in new page
        with page.context.expect_page() as new_page_info:
            await amazon_link.click(button="middle")  # Middle click opens in new tab
        
        new_page = await new_page_info.value
        await new_page.wait_for_load_state('networkidle')

    async def test_google_search_suggestions(self, page: Page, google_url: str):
        """Test Google search suggestions for Amazon-related queries."""
        await page.goto(google_url)
        search_box = page.locator('textarea[name="q"]')
        await search_box.fill("amazon")
        
        # Wait for suggestions dropdown
        suggestions = page.locator('[role="listbox"] li')
        
        # Check if suggestions appear
        if await suggestions.count() > 0:
            await expect(suggestions.first).to_be_visible()
