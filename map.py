from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com/maps")
time.sleep(5)
search_box = driver.find_element(By.ID, "searchboxinput")
search_query = "consultancy near putalisadak"
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(7)


divSideBar=driver.find_element(By.XPATH,f"""//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]""")

keepScrolling=True
max_scroll = 10
scrolled = 0

while(keepScrolling):
    divSideBar.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    divSideBar.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)
    html =driver.find_element(By.TAG_NAME, "html").get_attribute('outerHTML')
    if(html.find("You've reached the end of the list.")!=-1):
        keepScrolling=False

    if scrolled >= max_scroll:
        keepScrolling = False

    scrolled += 1

consultancy_links = [links.get_attribute("href") for links in driver.find_elements(By.CLASS_NAME, 'hfpxzc')]


with open('consultancy.txt', 'w', encoding='utf-8') as f:
    for link in consultancy_links:
        driver.get(link)
        time.sleep(3)

        name = driver.find_element(By.CLASS_NAME, 'DUwDvf.lfPIob').text
        f.write(name + '\n')

        parent_elements = driver.find_elements(By.CLASS_NAME, 'AeaXub')
        for element in parent_elements:
            phone = element.find_element(By.CLASS_NAME, 'Io6YTe.fontBodyMedium.kR99db').text
            f.write(phone + '\n')

        f.write('---------------------------------------\n')
        time.sleep(3)

driver.quit()

