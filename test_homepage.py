from playwright.sync_api import expect

def test_homepage_title(page):
	page.goto("https://example.com")
	assert page.title() == "Example Domain"


