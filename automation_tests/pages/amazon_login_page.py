"""
Page Object Model for Amazon Login Page
This module contains all selectors and methods for interacting with the Amazon login page.
"""

from playwright.async_api import Page, expect
from typing import Optional


class AmazonLoginPage:
    """Page Object Model for Amazon Login Page."""

    # Selectors
    LOGIN_PAGE_URL = "https://www.amazon.com/ap/signin"
    
    # Page Elements
    EMAIL_INPUT = 'input[type="email"]'
    CONTINUE_BUTTON = 'input#continue'
    PASSWORD_INPUT = 'input[type="password"]'
    SIGNIN_BUTTON = 'input[type="submit"]'
    REMEMBER_ME_CHECKBOX = 'input[type="checkbox"]'
    ERROR_MESSAGE = '[role="alert"]'
    LOGIN_HEADER = 'h1'
    FORGOT_PASSWORD_LINK = 'a[href*="forgot"]'
    CREATE_ACCOUNT_LINK = 'a[href*="register"]'
    ACCOUNT_NAME_FIELD = '[data-feature-name="ap_account_name_field"]'
    PHONE_NUMBER_FIELD = 'input[name="phoneNumber"]'
    OTP_INPUT = 'input[name="code"]'
    SECURITY_CHECK_CONTAINER = '[data-a-target="auth-status"]'

    def __init__(self, page: Page):
        """
        Initialize the Amazon Login Page object.
        
        Args:
            page: Playwright Page object
        """
        self.page = page

    async def navigate_to_login(self) -> None:
        """Navigate to Amazon login page."""
        await self.page.goto(self.LOGIN_PAGE_URL)
        await self.page.wait_for_load_state('networkidle')

    async def verify_login_page_loaded(self) -> None:
        """Verify that the login page has loaded successfully."""
        await expect(self.page).to_have_url(self.LOGIN_PAGE_URL)
        login_header = self.page.locator(self.LOGIN_HEADER)
        await expect(login_header).to_be_visible()

    async def get_email_field(self) -> object:
        """
        Get the email input field locator.
        
        Returns:
            Locator object for email field
        """
        return self.page.locator(self.EMAIL_INPUT)

    async def is_email_field_visible(self) -> bool:
        """
        Check if email field is visible.
        
        Returns:
            Boolean indicating visibility
        """
        email_field = self.page.locator(self.EMAIL_INPUT)
        return await email_field.is_visible()

    async def enter_email(self, email: str) -> None:
        """
        Enter email address into the email field.
        
        Args:
            email: Email address to enter
        """
        email_field = self.page.locator(self.EMAIL_INPUT)
        await email_field.fill(email)

    async def get_email_value(self) -> str:
        """
        Get the current value of the email field.
        
        Returns:
            Email value entered in the field
        """
        email_field = self.page.locator(self.EMAIL_INPUT)
        return await email_field.input_value()

    async def click_continue_button(self) -> None:
        """Click the Continue button to proceed."""
        continue_btn = self.page.locator(self.CONTINUE_BUTTON)
        await continue_btn.click()
        await self.page.wait_for_load_state('networkidle')

    async def is_continue_button_enabled(self) -> bool:
        """
        Check if Continue button is enabled.
        
        Returns:
            Boolean indicating if button is enabled
        """
        continue_btn = self.page.locator(self.CONTINUE_BUTTON)
        return await continue_btn.is_enabled()

    async def get_password_field(self) -> object:
        """
        Get the password input field locator.
        
        Returns:
            Locator object for password field
        """
        return self.page.locator(self.PASSWORD_INPUT)

    async def is_password_field_visible(self, timeout: int = 5000) -> bool:
        """
        Check if password field is visible.
        
        Args:
            timeout: Timeout in milliseconds
            
        Returns:
            Boolean indicating visibility
        """
        password_field = self.page.locator(self.PASSWORD_INPUT)
        try:
            await expect(password_field).to_be_visible(timeout=timeout)
            return True
        except:
            return False

    async def enter_password(self, password: str) -> None:
        """
        Enter password into the password field.
        
        Args:
            password: Password to enter
        """
        password_field = self.page.locator(self.PASSWORD_INPUT)
        await password_field.fill(password)

    async def get_password_value(self) -> str:
        """
        Get the current value of the password field.
        
        Returns:
            Password value entered in the field
        """
        password_field = self.page.locator(self.PASSWORD_INPUT)
        return await password_field.input_value()

    async def click_signin_button(self) -> None:
        """Click the Sign-in button to submit login form."""
        signin_btn = self.page.locator(self.SIGNIN_BUTTON)
        await signin_btn.click()
        await self.page.wait_for_load_state('networkidle')

    async def is_signin_button_visible(self) -> bool:
        """
        Check if Sign-in button is visible.
        
        Returns:
            Boolean indicating visibility
        """
        signin_btn = self.page.locator(self.SIGNIN_BUTTON)
        return await signin_btn.is_visible()

    async def login_with_credentials(self, email: str, password: str) -> None:
        """
        Complete login flow with email and password.
        
        Args:
            email: Email address
            password: Password
        """
        await self.enter_email(email)
        await self.click_continue_button()
        await self.is_password_field_visible()
        await self.enter_password(password)
        await self.click_signin_button()

    async def is_error_message_visible(self, timeout: int = 5000) -> bool:
        """
        Check if error message is displayed.
        
        Args:
            timeout: Timeout in milliseconds
            
        Returns:
            Boolean indicating if error message is visible
        """
        error_msg = self.page.locator(self.ERROR_MESSAGE)
        try:
            await expect(error_msg).to_be_visible(timeout=timeout)
            return True
        except:
            return False

    async def get_error_message_text(self) -> str:
        """
        Get the error message text.
        
        Returns:
            Error message text
        """
        error_msg = self.page.locator(self.ERROR_MESSAGE)
        return await error_msg.text_content()

    async def is_remember_me_checked(self) -> bool:
        """
        Check if 'Remember Me' checkbox is checked.
        
        Returns:
            Boolean indicating if checkbox is checked
        """
        remember_me = self.page.locator(self.REMEMBER_ME_CHECKBOX)
        return await remember_me.is_checked()

    async def check_remember_me(self) -> None:
        """Check the 'Remember Me' checkbox."""
        remember_me = self.page.locator(self.REMEMBER_ME_CHECKBOX)
        if not await remember_me.is_checked():
            await remember_me.click()

    async def uncheck_remember_me(self) -> None:
        """Uncheck the 'Remember Me' checkbox."""
        remember_me = self.page.locator(self.REMEMBER_ME_CHECKBOX)
        if await remember_me.is_checked():
            await remember_me.click()

    async def click_forgot_password_link(self) -> None:
        """Click the 'Forgot Password' link."""
        forgot_pwd_link = self.page.locator(self.FORGOT_PASSWORD_LINK)
        await forgot_pwd_link.click()
        await self.page.wait_for_load_state('networkidle')

    async def is_forgot_password_link_visible(self) -> bool:
        """
        Check if 'Forgot Password' link is visible.
        
        Returns:
            Boolean indicating visibility
        """
        forgot_pwd_link = self.page.locator(self.FORGOT_PASSWORD_LINK)
        return await forgot_pwd_link.is_visible()

    async def click_create_account_link(self) -> None:
        """Click the 'Create Account' link."""
        create_account_link = self.page.locator(self.CREATE_ACCOUNT_LINK)
        await create_account_link.click()
        await self.page.wait_for_load_state('networkidle')

    async def is_create_account_link_visible(self) -> bool:
        """
        Check if 'Create Account' link is visible.
        
        Returns:
            Boolean indicating visibility
        """
        create_account_link = self.page.locator(self.CREATE_ACCOUNT_LINK)
        return await create_account_link.is_visible()

    async def clear_email_field(self) -> None:
        """Clear the email field."""
        email_field = self.page.locator(self.EMAIL_INPUT)
        await email_field.clear()

    async def clear_password_field(self) -> None:
        """Clear the password field."""
        password_field = self.page.locator(self.PASSWORD_INPUT)
        await password_field.clear()

    async def wait_for_password_field(self, timeout: int = 5000) -> None:
        """
        Wait for password field to appear.
        
        Args:
            timeout: Timeout in milliseconds
        """
        password_field = self.page.locator(self.PASSWORD_INPUT)
        await expect(password_field).to_be_visible(timeout=timeout)

    async def wait_for_error_message(self, timeout: int = 5000) -> None:
        """
        Wait for error message to appear.
        
        Args:
            timeout: Timeout in milliseconds
        """
        error_msg = self.page.locator(self.ERROR_MESSAGE)
        await expect(error_msg).to_be_visible(timeout=timeout)

    async def get_login_page_title(self) -> str:
        """
        Get the page title.
        
        Returns:
            Page title text
        """
        return await self.page.title()

    async def is_two_fa_required(self) -> bool:
        """
        Check if Two-Factor Authentication is required.
        
        Returns:
            Boolean indicating if 2FA is required
        """
        otp_input = self.page.locator(self.OTP_INPUT)
        return await otp_input.is_visible()

    async def enter_otp(self, otp_code: str) -> None:
        """
        Enter OTP code for two-factor authentication.
        
        Args:
            otp_code: OTP code to enter
        """
        otp_input = self.page.locator(self.OTP_INPUT)
        await otp_input.fill(otp_code)

    async def submit_otp(self) -> None:
        """Submit OTP for authentication."""
        submit_btn = self.page.locator(self.SIGNIN_BUTTON)
        await submit_btn.click()
        await self.page.wait_for_load_state('networkidle')

    async def verify_on_homepage(self, homepage_url: str = "https://www.amazon.com") -> bool:
        """
        Verify that user is logged in and on homepage.
        
        Args:
            homepage_url: Expected homepage URL
            
        Returns:
            Boolean indicating if user is on homepage
        """
        try:
            await expect(self.page).to_have_url(homepage_url, timeout=5000)
            return True
        except:
            return False

    async def get_current_url(self) -> str:
        """
        Get the current page URL.
        
        Returns:
            Current page URL
        """
        return self.page.url
