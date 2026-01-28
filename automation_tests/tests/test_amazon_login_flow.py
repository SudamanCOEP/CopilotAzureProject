"""
Test Suite for Amazon Login Flow
Work Item ID: 1
Description: This task involves automating the testing of Amazon login flow using Playwright and pytest. 
Test cases cover email validation, password field visibility, button functionality, and error handling.
"""

import pytest
from playwright.async_api import Page, expect


class TestAmazonLoginFlow:
    """Test cases for Amazon login functionality."""

    async def test_login_page_loads(self, page: Page, amazon_url: str):
        """Test that the Amazon login page loads successfully."""
        await page.goto(f"{amazon_url}/ap/signin")
        await expect(page).to_have_url(f"{amazon_url}/ap/signin")
        
    async def test_email_field_exists(self, page: Page, amazon_url: str):
        """Test that the email input field exists on login page."""
        await page.goto(f"{amazon_url}/ap/signin")
        email_field = page.locator('input[type="email"]')
        await expect(email_field).to_be_visible()

    async def test_email_field_accepts_input(self, page: Page, amazon_url: str):
        """Test that email field accepts user input."""
        await page.goto(f"{amazon_url}/ap/signin")
        email_field = page.locator('input[type="email"]')
        await email_field.fill("test@example.com")
        await expect(email_field).to_have_value("test@example.com")

    async def test_email_validation_empty_field(self, page: Page, amazon_url: str):
        """Test email validation with empty field."""
        await page.goto(f"{amazon_url}/ap/signin")
        continue_button = page.locator('input#continue')
        await continue_button.click()
        
        # Check for error message
        error_message = page.locator('[role="alert"]')
        await expect(error_message).to_be_visible()

    async def test_password_field_visibility(self, page: Page, amazon_url: str):
        """Test that password field appears after valid email entry."""
        await page.goto(f"{amazon_url}/ap/signin")
        email_field = page.locator('input[type="email"]')
        continue_button = page.locator('input#continue')
        
        # Enter valid email
        await email_field.fill("testuser@example.com")
        await continue_button.click()
        
        # Wait for password field to appear
        password_field = page.locator('input[type="password"]')
        await expect(password_field).to_be_visible(timeout=5000)

    async def test_password_field_accepts_input(self, page: Page, amazon_url: str):
        """Test that password field accepts input."""
        await page.goto(f"{amazon_url}/ap/signin")
        email_field = page.locator('input[type="email"]')
        continue_button = page.locator('input#continue')
        
        # Enter email
        await email_field.fill("testuser@example.com")
        await continue_button.click()
        
        # Enter password
        password_field = page.locator('input[type="password"]')
        await expect(password_field).to_be_visible(timeout=5000)
        await password_field.fill("TestPassword123!")
        await expect(password_field).to_have_value("TestPassword123!")

    async def test_sign_in_button_visible(self, page: Page, amazon_url: str):
        """Test that Sign-in button is visible on login page."""
        await page.goto(f"{amazon_url}/ap/signin")
        email_field = page.locator('input[type="email"]')
        continue_button = page.locator('input#continue')
        
        await email_field.fill("testuser@example.com")
        await continue_button.click()
        
        password_field = page.locator('input[type="password"]')
        await expect(password_field).to_be_visible(timeout=5000)
        await password_field.fill("TestPassword123!")
        
        signin_button = page.locator('input[type="submit"]')
        await expect(signin_button).to_be_visible()

    async def test_invalid_email_format(self, page: Page, amazon_url: str):
        """Test email validation with invalid format."""
        await page.goto(f"{amazon_url}/ap/signin")
        email_field = page.locator('input[type="email"]')
        continue_button = page.locator('input#continue')
        
        # Enter invalid email format
        await email_field.fill("invalidemail")
        await continue_button.click()
        
        # Check for validation error
        error_message = page.locator('[role="alert"]')
        await expect(error_message).to_be_visible(timeout=5000)

    async def test_remember_me_checkbox(self, page: Page, amazon_url: str):
        """Test that 'Remember me' checkbox is present."""
        await page.goto(f"{amazon_url}/ap/signin")
        remember_me_checkbox = page.locator('input[type="checkbox"]')
        await expect(remember_me_checkbox).to_be_visible()
