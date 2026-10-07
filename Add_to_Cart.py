from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demoblaze.com/")   

    page.locator("//a[@id='login2']").click()
    page.locator("//input[@id='loginusername']").fill("Aug2708")
    page.locator("//input[@id='loginpassword']").fill("password")
    page.locator("//button[@onclick='logIn()']").click()
    page.wait_for_timeout(2000)

    page.locator("(//a[@href='prod.html?idp_=1'])[2]").click()
    page.locator("//a[@onclick='addToCart(1)']").click()
    page.locator("//a[@href='cart.html']").click()
    page.locator('//button[@data-target="#orderModal"]').click()

    page.locator('//input[@id="name"]').fill("Iqbal")
    page.locator('//input[@id="country"]').fill("India")
    page.locator('//input[@id="city"]').fill("Hyderabad")
    page.locator('//input[@id="card"]').fill("123-124")
    page.locator('//input[@id="month"]').fill("03")
    page.locator('//input[@id="year"]').fill("2031")
    page.locator('//button[@onclick="purchaseOrder()"]').click()
    page.wait_for_timeout(2000)
    page.locator('//button[@tabindex="1"]').click()
    page.wait_for_timeout(5000)