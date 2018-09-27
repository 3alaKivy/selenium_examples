from selenium import webdriver
import sys
import time
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()

if len(sys.argv) > 1:
    tag = sys.argv[1]
    driver.get("https://3alam.pro/questions?tag=" + tag)
else:
    driver.get("https://3alam.pro/questions")

questions_table = driver.find_element_by_xpath('//*[@id="main-container"]/div[2]/div/div/div[1]/div/div/table/tbody')
trs = questions_table.find_elements_by_tag_name('tr')
data = {}
counter = 0
for tr in trs:
    counter += 1
    tds = tr.find_elements_by_tag_name('td')
    question_title = tds[1].text.split("\n")[0]
    question_link = tds[1].find_element_by_tag_name('a').get_attribute("href")
    question_answers = tds[2].text
    data[counter] = (question_title, question_answers, question_link)

for key, value in data.items():
    print(value)
time.sleep(5)
driver.quit()