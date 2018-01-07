from selenium import webdriver
from selenium.common.exceptions import WebDriverException


chro = input('输入你下载的chromedriver的绝对路径，或者，把chromedriver.exe放到这个文件夹中，输入相对路径')
urllogin = 'http://www.mooc.whu.edu.cn/portal'


def choose(which, choice):
    the_xpath = '//*[@id="ZyBottom"]/div' \
                + (int(which) - 1) * "/div[4]" \
                                + "/div[2]/ul/li[" \
                                + str(choice) + "]/a"
    return the_xpath


driver = webdriver.Chrome(executable_path=chro)

driver.get(urllogin)

cookies = driver.get_cookies()
for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except WebDriverException:
        print('cookies的添加出现异常,不过这没什么问题')

driver.find_element_by_class_name("loginSub").click()

driver.save_screenshot('screenshot.png')
codeid = input('input your id: ')
codepw = input('input your password: ')

driver.find_element_by_id("username").send_keys(codeid)
driver.find_element_by_name("password").send_keys(codepw)
driver.find_element_by_class_name("btn-login").click()


def frame_switch(name):
    driver.switch_to.frame(driver.find_element_by_name(name))


def frame_switch_id(idd):
    driver.switch_to.frame(driver.find_element_by_id(idd))


frame_switch_id("frame_content")
driver.find_element_by_class_name("clearfix").click()

# Switch tap to the second tab:
driver.switch_to.window(driver.window_handles[1])


while True:
    input('Click on your own need.')
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
    for i in range(1, 21):
        answer = input("The " + str(i) + "th question's answer's?\nPlease choose among 1~4\n")
        for j in answer:
            answer_button = driver.find_element_by_xpath((choose(i, j)))
            answer_button.click()

