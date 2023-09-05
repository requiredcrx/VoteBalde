from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Safari()
#driver.fullscreen_window()
while True:
    driver.get("https://www.tuttosport.com/sondaggi/calcio/golden-boy/2023/08/31-112422514/golden_boy_web_step_3_vota_il_tuo_calciatore_preferito_")
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, '//*[@id="didomi-notice-agree-button"]/span').click()
    except Exception:
        pass
    else:
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[6]/main/section/div/div[1]/div[1]/div[2]/div/form/label[6]/div').click()
        driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[6]/main/section/div/div[1]/div[1]/div[2]/div/form/div/div/div/button').click()

