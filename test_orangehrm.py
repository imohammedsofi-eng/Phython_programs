from playwright.sync_api import sync_playwright
with sync_playwright() as a:
    browser = a.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    page.locator("//input[@name='username']").fill("Admin")  #Username
    page.wait_for_timeout(3000)
    page.locator("//input[@placeholder='Password']").fill("admin123")  #Password
    page.wait_for_timeout(3000)
    page.locator("//button[@type='submit']").click()  #Submit Button
    page.wait_for_timeout(2000)
    page.go_back()
    page.wait_for_timeout(2000)
    page.go_forward()
    page.wait_for_timeout(2000)
    page.reload()
    page.wait_for_timeout(3000)