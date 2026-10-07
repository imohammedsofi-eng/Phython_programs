from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demo.automationtesting.in/Alerts.html#google_vignette")  

    page.locator('//a[@href="#OKTab"]').click()
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('//button[@onclick="alertbox()"]').click()
    page.wait_for_timeout(1000)


    page.locator('//a[@href="#CancelTab"]').click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.locator('//button[@onclick="confirmbox()"]').click()
    page.wait_for_timeout(1000)

    page.locator('//a[@href="#CancelTab"]').click()
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('//button[@onclick="confirmbox()"]').click()
    page.wait_for_timeout(1000)

    page.locator('//a[@href="#Textbox"]').click()
    page.once("dialog", lambda dialog: dialog.accept("Iqbal"))
    page.locator('//button[@onclick="promptbox()"]').click()
    page.wait_for_timeout(1000)

    page.wait_for_timeout(3000)