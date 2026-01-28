# Amazon Automation Test Suite

Automated test suite for Amazon using Playwright and Pytest framework.

## Project Structure

```
automation_tests/
├── tests/
│   ├── test_amazon_login_flow.py          # Work Item 1: Login flow tests
│   ├── test_amazon_product_search.py      # Work Item 2: Product search tests
│   ├── test_amazon_product_purchase.py    # Work Item 3: Product purchase tests
│   └── test_google_to_amazon_navigation.py # Work Item 4: Navigation tests
├── conftest.py                             # Pytest configuration and fixtures
├── pytest.ini                              # Pytest settings
├── requirements.txt                        # Python dependencies
└── README.md                               # This file
```

## Installation

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Setup

1. **Clone/Navigate to project directory:**
   ```bash
   cd automation_tests
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## Running Tests

### Run all tests
```bash
pytest
```

### Run specific test file
```bash
pytest tests/test_amazon_login_flow.py
```

### Run specific test class
```bash
pytest tests/test_amazon_login_flow.py::TestAmazonLoginFlow
```

### Run specific test
```bash
pytest tests/test_amazon_login_flow.py::TestAmazonLoginFlow::test_email_field_exists
```

### Run tests with verbose output
```bash
pytest -v
```

### Run tests in headless mode
Edit `conftest.py` and change:
```python
browser = await p.chromium.launch(headless=True)
```

### Run tests with custom markers
```bash
pytest -m smoke
pytest -m regression
```

## Test Files Overview

### 1. test_amazon_login_flow.py (Work Item 1)
Tests for Amazon login flow including:
- Login page loading
- Email field validation
- Email format validation
- Password field visibility
- Sign-in button functionality
- Remember me checkbox
- Error handling

**Key Test Cases:**
- `test_login_page_loads` - Verify login page URL
- `test_email_field_exists` - Check email input visibility
- `test_email_validation_empty_field` - Empty field validation
- `test_password_field_visibility` - Password field appears after email
- `test_invalid_email_format` - Invalid email detection

### 2. test_amazon_product_search.py (Work Item 2)
Tests for product search functionality:
- Search bar visibility and input
- Product search execution
- Search results display
- Result pagination
- Filter and sorting options

**Key Test Cases:**
- `test_search_bar_accepts_input` - Search field input
- `test_search_product_by_name` - Product search
- `test_search_results_display` - Results visibility
- `test_product_details_clickable` - Product navigation
- `test_search_filters_available` - Filter presence

### 3. test_amazon_product_purchase.py (Work Item 3)
Tests for product purchase workflow:
- Product page loading
- Add to cart functionality
- Quantity selection
- Cart management
- Checkout process
- Product details display

**Key Test Cases:**
- `test_add_to_cart_button_visible` - Add to cart button
- `test_add_product_to_cart` - Add product action
- `test_product_quantity_selector` - Quantity adjustment
- `test_remove_from_cart` - Remove functionality
- `test_product_price_displayed` - Price visibility

### 4. test_google_to_amazon_navigation.py (Work Item 4)
Tests for navigation from Google to Amazon:
- Google search functionality
- Amazon link discovery
- Link clicking and navigation
- Tab/window management
- Back button navigation
- Search suggestions

**Key Test Cases:**
- `test_google_homepage_loads` - Google page load
- `test_search_amazon_from_google` - Search execution
- `test_amazon_link_in_search_results` - Link visibility
- `test_click_amazon_link_from_search_results` - Link navigation
- `test_open_amazon_in_new_tab_from_google` - New tab opening

## Configuration

### conftest.py
Contains shared fixtures:
- `browser` - Playwright browser instance
- `context` - Browser context (isolated session)
- `page` - Browser page for each test
- `amazon_url` - Amazon base URL
- `google_url` - Google base URL

### pytest.ini
Configuration settings:
- `asyncio_mode = auto` - Enable async test support
- Custom markers for test organization
- Output formatting options

## Dependencies

- **playwright** (1.40.0) - Browser automation
- **pytest** (7.4.3) - Test framework
- **pytest-asyncio** (0.23.0) - Async test support
- **python-dotenv** (1.0.0) - Environment variables

## Notes

- Tests use async/await syntax with Playwright's async API
- All tests are browser-based and require internet connection to real websites
- Some tests may fail due to website layout changes or updates
- It's recommended to run tests during off-peak hours to avoid rate limiting
- Screenshots can be captured for failed tests by modifying fixtures

## Troubleshooting

### Common Issues

1. **Playwright browsers not installed:**
   ```bash
   playwright install chromium
   ```

2. **Tests timing out:**
   - Increase timeout values in tests
   - Check internet connection
   - Verify website is accessible

3. **Element not found errors:**
   - Website selectors may have changed
   - Update selectors in test files
   - Use browser dev tools to inspect elements

4. **Port already in use:**
   - Close other browser instances
   - Wait for previous test run to complete

## Best Practices

1. Keep tests independent - don't depend on other test results
2. Use meaningful test names that describe what is being tested
3. Include proper waits for dynamic content
4. Use fixtures for setup and teardown
5. Add comments for complex test logic
6. Review test results regularly and update selectors as needed

## Contributing

When adding new tests:
1. Follow existing naming conventions
2. Add descriptive docstrings
3. Use existing fixtures from conftest.py
4. Keep tests focused on single functionality
5. Update README.md with new test information

## License

This test suite is for educational and testing purposes.
