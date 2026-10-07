from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://demo.automationtesting.in/Register.html")   
     # First Name
    page.locator("//input[@placeholder='First Name']").fill("Iqbal")
    # Last Name
    page.locator("//input[@placeholder='Last Name']").fill("Sofi")
    # Address
    page.locator("//textarea[@ng-model='Adress']").fill("Hyderabad")
    # Email
    page.locator("//input[@ng-model='EmailAdress']").fill("i.mohammed.sofi@gmail.com")
    # Phone number
    page.locator("//input[@ng-model='Phone']").fill("+919398649944")
    # Gender
    page.locator("//input[@value='Male']").click()
    # Hobbies
    page.locator("//input[@id='checkbox1']").click()

    page.locator("//select[@id='Skills']").select_option("Adobe InDesign")
    page.locator("//select[@id='yearbox']").select_option("1918")
    page.locator("//select[@ng-model='monthbox']").select_option("April")
    page.locator("//select[@id='daybox']").select_option("3")

    page.locator('//span[@aria-labelledby="select2-country-container"]').click()
    page.locator('//input[@type="search"]').fill('India')
    page.locator('//input[@type="search"]').press('Enter')

    page.locator('//div[@id="msdd"]').click()
    Arabic = page.locator('//a[contains(text(),"Arabic")]')
    Urdu = page.locator('//a[contains(text(),"Urdu")]')
    English = page.locator('//a[contains(text(),"English")]')
    all_language = [Arabic,Urdu,English]
    for language in all_language:
        language.click()

    page.locator('//label[contains(text(),"Country*")]').click()

    page.set_input_files('//input[@id="imagesrc"]',"C://Users//azams//Downloads//Screenshot 2026-08-29 124244.png")

    page.wait_for_timeout(5000)