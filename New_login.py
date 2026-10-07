from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://automationexercise.com/")   

    page.locator("//a[@href='/login']").click()
    page.wait_for_timeout(2000)
    page.locator("//input[@data-qa='login-email']").fill("i.mohammed.sofi@gmail.com")
    page.wait_for_timeout(2000)
    page.locator("//input[@data-qa='login-password']").fill("Password")
    page.locator("//button[@data-qa='login-button']").click()
    page.wait_for_timeout(5000)
    