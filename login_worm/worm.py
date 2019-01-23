from selenium import webdriver
def worm(acc , pas):

    browser = webdriver.Chrome("./chromedriver.exe")

    browser.get('http://learningportfolio.fcu.edu.tw/tw/index.aspx')

    account = browser.find_element_by_id("ctl00_ucLogin_txtID")

    account.send_keys(acc)#帳號

    password = browser.find_element_by_id("ctl00_ucLogin_txtPW")

    password.send_keys(pas)#密碼

    btn = browser.find_element_by_id("ctl00_ucLogin_btnLogin").click()
    #ctl00_MainContent_GenMustListView_tableHeader
    #ctl00_MainContent_CollegeMustListView_tableHeader
    #ctl00_MainContent_CollegeProListView_tableHeader
    #ctl00_MainContent_NoCollegeProListView_tableHeader
    #ctl00_MainContent_GenSelectListView_tableHeader

    btn = browser.find_element_by_id("li_LearnAssist").click()

    btn = browser.find_element_by_xpath("//*[@id=\"ctl00_Div_LearnAssist\"]/ul/li[11]/a").click()

    answer = ""
    
    GenMustList = browser.find_element_by_id("ctl00_MainContent_GenMustListView_tableHeader").find_elements_by_tag_name('tr')
    answer += "通識基礎" + "<br><br>"
    
    for i in range(len(GenMustList)):
        if (i == 0 or i == 1):
            continue
        GenMustListtmep = GenMustList[i].find_elements_by_tag_name('td')
        answer += GenMustListtmep[1].text + "<br>"

    CollegeMustListView = browser.find_element_by_id("ctl00_MainContent_CollegeMustListView_tableHeader").find_elements_by_tag_name('tr')
    answer += "院系必修" + "<br><br>"
    
    for i in range(len(CollegeMustListView)):
        if (i == 0 or i == 1):
            continue
        CollegeMustListViewtmep = CollegeMustListView[i].find_elements_by_tag_name('td')
        answer += CollegeMustListViewtmep[1].text + "<br>"

    CollegeProListView = browser.find_element_by_id("ctl00_MainContent_CollegeProListView_tableHeader").find_elements_by_tag_name('tr')
    answer += "本系專業選修" + "<br><br>"

    for i in range(len(CollegeProListView)):
        if (i == 0 or i == 1):
            continue
        CollegeProListViewtmep = CollegeProListView[i].find_elements_by_tag_name('td')
        answer += CollegeProListViewtmep[1].text + "<br>"

    NoCollegeProListView = browser.find_element_by_id("ctl00_MainContent_NoCollegeProListView_tableHeader").find_elements_by_tag_name('tr')
    answer += "非本系專業選修" + "<br><br>"
    
    for i in range(len(NoCollegeProListView)):
        if (i == 0 or i == 1):
            continue
        NoCollegeProListViewtmep = NoCollegeProListView[i].find_elements_by_tag_name('td')
        answer += NoCollegeProListViewtmep[1].text + "<br>"

    GenSelectListView = browser.find_element_by_id("ctl00_MainContent_GenSelectListView_tableHeader").find_elements_by_tag_name('tr')
    answer += "通識選修" + "<br><br>"
    
    for i in range(len(GenSelectListView)):
        if (i == 0 or i == 1):
            continue
        GenSelectListViewtmep = GenSelectListView[i].find_elements_by_tag_name('td')
        answer += GenSelectListViewtmep[1].text + "<br>"
    #browser.quit()
    return answer
