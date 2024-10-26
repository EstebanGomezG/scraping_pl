import time
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.common.by import By
import pandas as pd 
import os

key_word = "Omar%Restrepo"
def main():
    service= Service(ChromeDriverManager().install())
    option = webdriver.ChromeOptions()
    option.add_argument("--window-size=1080,720")
    driver = Chrome(service=service, options=option)
    driver.get("https://leyes.senado.gov.co/proyectos/index.php/proyectos-ley/cuatrenio-2022-2026/2023-2024")
    time.sleep(3)


    driver.find_element(By.NAME, "search").send_keys(key_word)
    driver.find_element(By.CSS_SELECTOR, "input.button.btn.search").click()
    driver.find_element(By.ID, "limit").click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/form/div[2]/select/option[8]").click() 
    

    data_link= driver.find_elements(By.XPATH, "//td/h3")
    data_f_rad= driver.find_elements(By.XPATH, "//td/div")
    data_autor= driver.find_elements(By.XPATH, "//td/p/b")
    data_comision_sta= driver.find_elements(By.XPATH, "//td")
    

    print(len(data_link))
    print(len(data_f_rad))
    print(len(data_autor))
    print(len(data_comision_sta))
    

    max_length = max(len(data_link), len(data_f_rad), len(data_autor), len(data_comision_sta))
    data_link += [None] * (max_length - len(data_link))
    data_f_rad+= [None] * (max_length - len(data_f_rad))
    data_autor+= [None] * (max_length - len(data_autor))
    data_comision_sta += [None] * (max_length - len(data_comision_sta))

  
    def get_text_or_default(obj, default=""):
        return obj.text if obj is not None else default


    data_link_text = [get_text_or_default(obj) for obj in data_link]
    data_f_rad_text = [get_text_or_default(obj) for obj in data_f_rad]
    data_autor_text = [get_text_or_default(obj) for obj in data_autor]
    data_comision_sta_text = [get_text_or_default(obj) for obj in data_comision_sta]


    data = {
        "link" : data_link_text,
         "rad" : data_f_rad_text,
         "autor" : data_autor_text,
         "Comisión y estado ": data_comision_sta_text      
    }
    df = pd.DataFrame(data)
    print(df)

    df.to_csv("PL_Omar.csv", index=False)
     
if __name__ == "__main__":
    main()
   
