import pytest
from playwright.async_api import async_playwright, Browser, BrowserContext, Page
import asyncio


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def browser():
    """Create a Playwright browser instance for the test session."""
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set to True for headless mode
        yield browser
        await browser.close()


@pytest.fixture
async def context(browser: Browser) -> BrowserContext:
    """Create a new browser context for each test."""
    context = await browser.new_context()
    yield context
    await context.close()


@pytest.fixture
async def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = await context.new_page()
    yield page
    await page.close()


@pytest.fixture
def amazon_url():
    """Amazon base URL."""
    return "https://www.amazon.com"


@pytest.fixture
def amazon_in_url():
    """Amazon India URL."""
    return "https://www.amazon.in"


@pytest.fixture
def google_url():
    """Google base URL."""
    return "https://www.google.com"
