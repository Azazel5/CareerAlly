import time 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from googlesearch import search 


# Returns the scraped data from the website in a dictionary form. Checks if we ran into captchas, and if so,
# we can specify how long to wait for the user to go into the browser and pass it. After that it uses the 
# helper function to do the scraping of data.
def return_scraped_data(length_internships, time_to_solve_captcha, position_search):
    internship_list = []
    driver = webdriver.Chrome() 
    driver.get("https://www.internships.com/")
    try:
        keyword_searcher = driver.find_element_by_name("keywords")
        search_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[1]/form/button")

    except:
        print("Ran into some captchas. You got %d seconds to solve it." %time_to_solve_captcha)
        try:
            keyword_searcher = WebDriverWait(driver, time_to_solve_captcha).until(EC.presence_of_element_located((By.NAME, "keywords")))
        except:
            print("You couldn't solve the captcha in the required time.")
        
        finally:
            return helper(keyword_searcher, driver, internship_list, length_internships, position_search)

    else:
        return helper(keyword_searcher, driver, internship_list, length_internships, position_search)

# A helper function which specifies what to search for and how many internships we want to spit out.
# The number of internships returned will be 25 more than the argument you pass in. 
def helper(key, driver, internship_list, length_internships, position_search):
    search_button = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div[1]/form/button")
    key.send_keys(position_search)
    search_button.click()
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "GridItem__jobContent_14uVD")))
        internship_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "GridItem__jobContent_14uVD")))
        prev_length = len(internship_list)
        scroll_elem = driver.find_element_by_xpath("//*[@id=\"jobs-page\"]/div/div[2]/div/div/div[2]/div")
        # Pass in the number of jobs you want to extract in the if statement test
        while True:
            driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll_elem)
            internship_list = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "GridItem__jobContent_14uVD")))
            new_length = len(internship_list)
            if new_length - prev_length == length_internships:
                break 

    except TimeoutException:
        print("Loading took too much time! Get a better internet connection :(")

    fina_list = {}
    if internship_list != []: 
        for i in range(len(internship_list)):
            position_name = internship_list[i].find_element_by_xpath(".//div[2]/p").text 
            company_name = internship_list[i].find_element_by_class_name("GridItem__companyNameText_24M9G").text 
            location = internship_list[i].find_element_by_xpath(".//p[2]").text 
            days_ago_posted = internship_list[i].find_element_by_xpath(".//p[3]").text
            fina_list[position_name] = [company_name, location, days_ago_posted]
    
    if fina_list == {}:
        fina_list['result'] = 'You couldn\'\t solve the captcha on time'
    return fina_list

def link_returner(position, company):
    search_string = company + " " + position + " careers"
    for url in search(search_string, stop=1):
        return url

