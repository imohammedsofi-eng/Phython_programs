from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser=p.chromium.launch(headless=False)
    page=browser.new_page()
    page.goto('https://www.uncodemy.com')

    category= page.locator('//span[@id="categoriesBtn"]')
    # page.locator('//a[text()="Full Stack With NodeJs"]')
    # page.locator('//a[text()="Full Stack With NodeJs"]')
    # page.wait_for_timeout(5000)

    #Full-Stack-Development
    fsd = page.locator("//a[text()='Full-Stack-Development']")
    fsw = page.locator("//a[contains(text(),'Full Stack With')]")
    pfs = page.locator("//a[contains(text(),'Python Full Stack')]")
    fsur = page.locator("(//a[@href='/course/java-full-stack-using-react-training-course-in-noida'])[1]")
    wdtc1 = page.locator("(//a[@href='/course/web-designing-training-course-in-noida'])[1]")
    wdtc2 = page.locator("(//a[@href='/course/web-development-training-course-in-noida'])[1]")
    fdtc = page.locator("(//a[@href='/course/frontend-development-training-course-in-noida'])[1]")
    atc = page.locator("(//a[@href='/course/angular-training-course-in-noida'])[1]")
    rjtc = page.locator("(//a[@href='/course/react-js-training-course-in-noida'])[1]")
    dsa = page.locator("(//a[@href='/course/data-structure-and-algorithm-training-course-in-noida'])[1]")
    mean = page.locator("//a[contains(text(),'Mean')]")
    mern = page.locator("//a[contains(text(),'Mern')]")

    course1 = [fsw, pfs, fsur, wdtc1, wdtc2, fdtc, atc, rjtc, dsa, mean, mern]

        #Data Science
    data_science = page.locator("//a[text()='Data Science']")
    python = page.locator("(//a[@href='/course/python-training-course-in-noida'])[1]")
    dap = page.locator("(//a[@href='/course/data-analytics-using-python-training-course-in-noida'])[1]")
    dsmp = page.locator("//a[contains(text(),'Data Science & Machine Learning using Python')]")
    mlp = page.locator("(//a[@href='/course/machine-learning-using-python-training-course-in-noida'])[1]")
    aip = page.locator("//a[contains(text(),'AI Using Python')]")

    course2 = [python, dap, dsmp, mlp, aip]


    #Software Testing
    software_testing = page.locator("(//a[contains(text(),'Software Testing')])[1]")
    st = page.locator("(//a[contains(text(),'Software Testing')])[2]")
    at = page.locator("//a[contains(text(),'Automation Testing')]")
    pa = page.locator("//a[contains(text(),'Playwright Automation')]")
    mt = page.locator("//a[contains(text(),'Manual Testing')]")
    istqb = page.locator("//a[contains(text(),'ISTQB Training')]")
    manual_selenium = page.locator("(//a[@href='/course/manual-testing-course-in-noida'])[2]")

    course3 = [st, at, pa, mt, istqb, manual_selenium]

    #Cloud Tool
    cloud_tool = page.locator("//a[contains(text(),'Cloud Tools')]")
    ma = page.locator("//a[contains(text(),'Microsoft Azure')]")
    devops = page.locator("//a[contains(text(),'DevOps')]")
    aws = page.locator("//a[contains(text(),'Amazon Web Services (AWS)')]")
    cc = page.locator("//a[contains(text(),'Cloud Computing')]")
    sf = page.locator("//a[contains(text(),'Salesforce')]")

    course4 = [ma, devops, aws, cc, sf]


    #Digital Marketing
    digital_marketing = page.locator("(//a[contains(text(),'Digital Marketing')])[1]")
    dm = page.locator("(//a[contains(text(),'Digital Marketing')])[2]")
    adm = page.locator("//a[@href='/course/advanced-digital-marketing-training-course-in-noida']")
    seo = page.locator("//a[contains(text(),'SEO(Search Engine Optimization)')]")

    course5 = [dm, adm, seo]


    #Java Technology+
    java_technology = page.locator("//a[contains(text(),'Java Technology+')]")
    java = page.locator("(//a[@href='/course/java-training-course-in-noida'])[1]")
    jfb = page.locator("//a[@href='/course/java-for-beginners-training-course-in-noida']")
    je = page.locator("//a[@href='/course/java-expert-training-course-in-noida']")

    course6 = [java_technology, java, jfb, je]

    #Network and Security
    network_security = page.locator("//a[contains(text(),'Network & Security')]")
    eh = page.locator("//a[contains(text(),'Ethical Hacking')]")
    cs = page.locator("//a[contains(text(),'Cyber Security')]")
    ccnp = page.locator("//a[contains(text(),'CCNP')]")
    mcsa = page.locator("//a[contains(text(),'MCSA')]")
    vmwar = page.locator("//a[contains(text(),'Vmware')]")

    course7 = [eh, cs, ccnp, mcsa, vmwar]


    #Programming language
    programming_language = page.locator("//a[contains(text(),'Programming Language')]")
    cdsa = page.locator("//a[@href='/course/c-with-data-structure-and-algorithm-training-course-in-noida']")
    oop1 = page.locator("//a[@href='/course/cpptraining-training-course-in-noida']")
    dotnet = page.locator("//a[contains(text(),'.NET 4 Months')]")
    dotnetfullstack = page.locator("//a[contains(text(),' .NET Full Stack')]")
    rprogramming = page.locator("//a[contains(text(),'R Programming')]")

    course8 = [cdsa, oop1, dotnet, dotnetfullstack, rprogramming]


    #CAD Training
    cad_training = page.locator("(//a[contains(text(),'CAD Training')])[1]")
    autocad = page.locator("//a[contains(text(),'AUTOCAD')]")
    cnc_programming = page.locator("//a[contains(text(),'CNC Programming')]")

    course9 = [autocad, cnc_programming]
    #Graphic Designing
    graphic_designing = page.locator("(//a[contains(text(),'Graphic Designing')])[1]")
    gd = page.locator("(//a[contains(text(),'Graphic Designing')])[2]")
    ui_ux = page.locator("//a[contains(text(),'UI/UX Designing')]")

    course10 = [gd, ui_ux]


    all_course = [fsd, data_science, software_testing, cloud_tool, digital_marketing,
                java_technology, network_security, programming_language,
                cad_training, graphic_designing]

    all_sub_course = [course1, course2, course3, course4, course5, course6,
                    course7, course8, course9, course10]

    selected_course = []



    for i in course1:
        category.hover()
        fsd.hover()
        i.click()
        page.wait_for_timeout(1000)
        page.go_back()
