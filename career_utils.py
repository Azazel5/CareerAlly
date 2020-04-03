import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome() 
driver.get("https://www.internships.com/")
driver.find_element_by_name("keywords").send_keys("Software")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[1]/form/button").click()

try:
    internship_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "GridItem__jobContent_14uVD")))
    prev_length = len(internship_list)
    scroll_elem = driver.find_element_by_xpath("//*[@id=\"jobs-page\"]/div/div[2]/div/div/div[2]/div")
    # Pass in the number of jobs you want to extract in the if statement test
    while True:
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_elem)
        internship_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "GridItem__jobContent_14uVD")))
        new_length = len(internship_list)
        if new_length - prev_length == 150:
            break 

except TimeoutException:
    print("Loading took too much time!")

if internship_list != None: 
    for i in range(len(internship_list)):
        postion_name = internship_list[i].find_element_by_xpath(".//div[2]/p").text 
        company_name = internship_list[i].find_element_by_class_name("GridItem__companyNameText_24M9G").text 
        location = internship_list[i].find_element_by_xpath(".//p[2]").text 
        days_go_posted = internship_list[i].find_element_by_xpath(".//p[3]").text 
        print("Position: ", postion_name, " Company: ", company_name, " location: ", location, " Post x days ago: ", days_go_posted)

