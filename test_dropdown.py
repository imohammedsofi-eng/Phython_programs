from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.tranktechnologies.com/")

#Web Development

    Web_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/web-development-company"])[2]')
    CMS_Website_Development = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
    eCommerce_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
    Arrow_head_One = page.locator('(//i[@aria-hidden="true"])[3]')
    Website_Development = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]') 
    Custom_Web_Portal_Development = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
    Web_Development_List = [Web_Development, CMS_Website_Development, Custom_Web_Portal_Development]

    for i in Web_Development_List:
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    Arrow_head_One.click()
    page.wait_for_timeout(1000)
    Website_Development.click()
    page.wait_for_load_state("load")
    page.wait_for_timeout(5000)
    page.go_back()