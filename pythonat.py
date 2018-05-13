from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://3alakivyblog.wordpress.com")

contact_me = driver.find_element_by_id("menu-item-262")
contact_me.click()

name = driver.find_element_by_id("g260")
name.clear()
name.send_keys("مكتبة سيلينيوم")

email = driver.find_element_by_id("g260-1")
email.clear()
email.send_keys("3alaKivyBlog@gmail.com")

message = driver.find_element_by_name("g260-3")
message.clear()
message.send_keys("شكرًا لك على هذا المقال. استمر في قيادة متصفحك")

send_msg = driver.find_element_by_class_name("pushbutton-wide")
send_msg.submit()

done_msg = driver.find_element_by_xpath('//*[@id="contact-form-260"]/h3')
if done_msg.text == "تم إرسال الرسالة (الرجوع للخلف)":
    print("Message has been sent successfully")
else:
    print("Error in sending message")


time.sleep(5)
driver.quit()
