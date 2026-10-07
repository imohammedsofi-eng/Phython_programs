from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto("https://www.tranktechnologies.com/")


#Verticals 
    Verticals = page.locator('(//a[@href="#"])[2]')

    Trading = page.locator("//strong[text()='Trading']")
    Stock_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
    Paper_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
    Cfd_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
    Stock_Trading_Mass = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
    Algo_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
    Custom_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
    Web_Portal_Trading = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')
    Trading_List = [Stock_Trading, Paper_Trading, Cfd_Trading, Stock_Trading_Mass, Algo_Trading, Custom_Trading, Web_Portal_Trading]

    Retail_Ecommerce = page.locator("//strong[text()='Retail and Ecommerce']")
    eCommerce_Website_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
    eCommerce_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')
    Retail_Ecom_List = [eCommerce_Website_Development, eCommerce_App_Development]

    Healthcare = page.locator('//strong[text()="Healthcare"]')
    Diet_Nutritions = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
    Health_tracking_App = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')
    Healthcare_List = [Diet_Nutritions, Health_tracking_App]

    Fintech = page.locator('//strong[text()="Fintech"]')
    Pos_Software = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
    Crypto = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')
    Fintech_List = [Pos_Software, Crypto]

    Custom_App = page.locator('//strong[text()="Custom App"]')
    Desktop_App = page.locator('(//a[@href="https://www.tranktechnologies.com/desktop-application-development-company"])[1]')
    HRM_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/hrm-application-development-company"])[1]')
    Travel = page.locator('(//a[@href="https://www.tranktechnologies.com/travel-mobile-app-development-company"])[1]')
    Dating_app_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/dating-app-development-company"])[1]')
    CRM_Dev_USA = page.locator('(//a[@href="https://www.tranktechnologies.com/usa/custom-crm-development-company-usa"])[1]')
    CRM_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-crm-development-company"])[1]')
    ERP_App_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/erp-app-development-company"])[1]')
    E_Learn = page.locator('(//a[@href="https://www.tranktechnologies.com/e-learning-mobile-app-development-company"])[1]')
    Real_Estate = page.locator('(//a[@href="https://www.tranktechnologies.com/real-estate-mobile-app-development-company"])[1]')
    Custom_App_List = [Desktop_App, HRM_Dev, Travel, Dating_app_Dev, CRM_Dev_USA, CRM_Dev, ERP_App_Dev, E_Learn, Real_Estate]

    # for i in Trading_List:
    #     Verticals.hover()
    #     Trading.hover()
    #     i.click()
    #     page.wait_for_load_state("load")
    #     page.go_back()

    for i in Retail_Ecom_List:
        Verticals.hover()
        Retail_Ecommerce.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    for i in Healthcare_List:
        Verticals.hover()
        Healthcare.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    for i in Fintech_List:
        Verticals.hover()
        Fintech.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    for i in Custom_App_List:
        Verticals.hover()
        Custom_App.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()


#Technologies 
    Technologies = page.locator('(//a[@href="#"])[5]')

    eCommerce_Development = page.locator('//strong[text()="eCommerce Development"]')
    Magneto_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
    Codeigniter_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
    Big_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
    CS_Cart_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
    Nop_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/nopcommerce-design-and-development-company"])[1]')
    Laravel_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
    Opencart_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
    WordPress_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
    Shopify_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
    NodeJS_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
    Woo_Commerce = page.locator('(//a[@href="https://www.tranktechnologies.com/woocommerce-development"])[1]')
    Prestashop_Dev = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
    eCommerce_Development_List = [Magneto_Dev, Codeigniter_Dev, Big_Commerce, CS_Cart_Dev, Nop_Commerce, Laravel_Dev, Opencart_Dev, WordPress_Dev, Shopify_Dev, NodeJS_Dev, Woo_Commerce, Prestashop_Dev]

    Mobile_App_Development = page.locator('//strong[text()="Mobile App Development"]')
    React_Native_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
    Enterprise_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
    Xamarin_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
    Kotlin_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
    Flutter_Mobile_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
    Ionic_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ionic-mobile-app-development"])[1]')
    Swift_App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/swift-mobile-app-development"])[1]')
    Appointment_Booking_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')
    Mobile_App_Development_List = [React_Native_Mobile_App_Development, Enterprise_Mobile_App_Development, Xamarin_Mobile_App_Development, Kotlin_Mobile_App_Development, Flutter_Mobile_App_Development, Ionic_App_Development, Swift_App_Development, Appointment_Booking_Development]

    Artificial_Intelligence = page.locator('//strong[text()="Artificial Intelligence"]')
    AI_list =[Artificial_Intelligence]

    for i in eCommerce_Development_List:
        Technologies.hover()
        eCommerce_Development.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    for i in Mobile_App_Development_List:
        Technologies.hover()
        Mobile_App_Development.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    for i in AI_list:
        Technologies.hover()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()


#Blog 
    Blog = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')

    #Categories 
    App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/app-development/"])[1]')
    Artificial_Intelligence = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/artificial-intelligence/"]')
    Content_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/content-marketing/"]')
    CRM_Development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/crm-development/"]')
    Digital_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/digital-marketing/"]')
    ECommerce_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ecommerce-development/"])[5]')
    Email_Marketing = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/email-marketing/"]')
    Graphic_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/graphic-design/"])[3]')
    Software_IT_Company = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-it-company/"]')
    Software_Development = page.locator('//a[@href="https://www.tranktechnologies.com/blog/category/software-development/"]')
    UI_UX_Design = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/ui-ux-design/"])[5]')
    Web_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/category/web-development/"])[5]')
    Categories = [App_Development, Artificial_Intelligence, Content_Marketing, CRM_Development, Digital_Marketing, ECommerce_Development, Email_Marketing, Graphic_Design, Software_IT_Company, Software_Development, UI_UX_Design, Web_Development]

    for i in Categories:
        Blog.click()
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

#Contact_US
    page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]').click()
    page.wait_for_load_state("load")
    page.locator('(//input[@placeholder="Your Name"])[2]').fill("Iqbal")
    page.locator('(//input[@placeholder="Your Mail"])[2]').fill("i.mohammed.sofi@gmail.com")
    page.once("dialog", lambda dialog: dialog.accept())
    page.locator('(//button[@type="button"])[2]').click()
    page.locator('(//input[@placeholder="Enter OTP"])[2]').fill("1234")
    page.locator('(//input[@placeholder="Your Company"])[2]').fill("STC")
    page.locator('(//select[@name="service"])[2]').select_option("Web Development")
    page.locator('(//input[@placeholder="Your Phone"])[2]').fill("+919398649944")
    page.locator('(//textarea[@placeholder="Message"])[2]').fill("This is a Message Box")
    page.wait_for_timeout(1000)

#Web Development

    Web_Development = page.locator("//a[@href='https://www.tranktechnologies.com/web-development-company']")
    CMS_Website_Development = page.locator('//a[@href="https://www.tranktechnologies.com/cms-website-development-company"]')
    eCommerce_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[7]')
    Arrow_head_One = page.locator('(//i[@aria-hidden="true"])[3]')
    Website_Development = page.locator('//a[@href="https://www.tranktechnologies.com/website-development-company"]') 
    Custom_Web_Portal_Development = page.locator('//a[@href="https://www.tranktechnologies.com/custom-web-portal-development-company"]')
    Web_Development_List = [Web_Development, CMS_Website_Development, Custom_Web_Portal_Development]
    Web_Development_Sub_List = [Website_Development]

#App Development 
    App_Development = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[1]')
    iOS_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/ios-mobile-app-development-company"]')
    Android_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/app-development-company"]')
    Arrow_head_Two = page.locator('(//i[@aria-hidden="true"])[4]')
    Android_App_Development_Sub = page.locator('//a[@href="https://www.tranktechnologies.com/android-app-development-company"]')
    App_Development_Sub = page.locator('(//a[@href="https://www.tranktechnologies.com/app-development-company"])[2]')
    Hybrid_Mobile_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/hybrid-mobile-app-development-company"]')
    Cross_Platform_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/cross-platform-mobile-app-development-company"]')
    Progressive_Web_App_Development = page.locator('//a[@href="https://www.tranktechnologies.com/progressive-web-app-development-company"]')
    App_Development_List = [App_Development, iOS_App_Development, Hybrid_Mobile_App_Development, Cross_Platform_App_Development, Progressive_Web_App_Development]
    App_Development_Sub_list = [Android_App_Development_Sub, App_Development_Sub]

#Graphic Design
    Graphic_Design = page.locator('//a[@href="https://www.tranktechnologies.com/graphic-design-company"]')
    Logo_Design = page.locator('//a[@href="https://www.tranktechnologies.com/logo-design-company"]')
    Banner_Design = page.locator('//a[@href="https://www.tranktechnologies.com/banner-design-company"]')
    Packaging_Design = page.locator('//a[@href="https://www.tranktechnologies.com/packaging-design-company"]')
    Business_Cards_Design = page.locator('//a[@href="https://www.tranktechnologies.com/business-cards-design-company"]')
    Graphic_Design_List = [Graphic_Design, Logo_Design, Banner_Design, Packaging_Design, Business_Cards_Design]

#UI UX Design

    UI_UX_Design = page.locator('//a[@href="https://www.tranktechnologies.com/ui-ux-design-company"]')
    Mobile_App_Design = page.locator('//a[@href="https://www.tranktechnologies.com/mobile-app-design-company"]')
    Responsive_Web_Design = page.locator('//a[@href="https://www.tranktechnologies.com/responsive-web-design-company"]')
    Brand_Idendity_Design = page.locator('//a[@href="https://www.tranktechnologies.com/brand-identity-design-services-company"]')
    UI_UX_Design_List = [UI_UX_Design, Mobile_App_Design, Responsive_Web_Design, Brand_Idendity_Design]


    for i in Graphic_Design_List:
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    for i in UI_UX_Design_List:
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    for i in Web_Development_List:
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    # for i in Web_Development_Sub_List:
    #     Arrow_head_One.click()
    #     i.click()
    #     page.goto("https://www.tranktechnologies.com/contact-us")
    #     page.wait_for_load_state("load")

    for i in Web_Development_Sub_List:
        Arrow_head_One.click()  # Click the dropdown arrow
        with page.expect_popup() as popup_info:  # Capture the new tab
            i.click()
        new_tab = popup_info.value
        new_tab.wait_for_load_state("load") # Wait for the new tab to load
        new_tab.wait_for_timeout(2000) # Stay on the new tab for 2 seconds
        page.bring_to_front() # Return to the main tab
        new_tab.wait_for_timeout(2000)
    
    for i in App_Development_List:
        i.click()
        page.wait_for_load_state("load")
        page.go_back()

    # for i in App_Development_Sub_list:
    #     Arrow_head_Two.click()
    #     i.click()
    #     page.goto("https://www.tranktechnologies.com/contact-us")
    #     page.wait_for_load_state("load")

    for i in App_Development_Sub_list:
        Arrow_head_Two.click()  # Click the dropdown arrow
        with page.expect_popup() as popup_info:  # Capture the new tab
            i.click()
        new_tab = popup_info.value
        new_tab.wait_for_load_state("load") # Wait for the new tab to load
        new_tab.wait_for_timeout(2000) # Stay on the new tab for 2 seconds
        page.bring_to_front() # Return to the main tab
        new_tab.wait_for_timeout(2000)

#Follow Us Pages

    Facebook = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/facebook.png"]')
    LinkedIn = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/linkedin.png"]')
    Instagram = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/Insta.png"]')
    Pinterest = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/pinterest.png"]')
    Twitter = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/twitter.png"]')
    YouTube = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/youtube.png"]')
    Quora = page.locator('//img[@src="https://www.tranktechnologies.com/assets/new-assets/quora.png"]')
    SocialMedia_Pages = [Facebook, LinkedIn, Instagram, Pinterest, Twitter, YouTube, Quora]

    # for i in SocialMedia_Pages:
    #     i.click()
    #     page.wait_for_load_state("load")
    #     page.locator('(//a[@href="https://www.tranktechnologies.com/contact-us"])[1]').click()
    #     page.wait_for_load_state("load")
    #     # page.go_back()

    for i in SocialMedia_Pages:
        with page.expect_popup() as popup_info:  # Capture the new tab
            i.click()
        new_tab = popup_info.value
        new_tab.wait_for_load_state("load") # Wait for the new tab to load
        new_tab.wait_for_timeout(2000) # Stay on the new tab for 2 seconds
        page.bring_to_front() # Return to the main tab
        new_tab.wait_for_timeout(2000)