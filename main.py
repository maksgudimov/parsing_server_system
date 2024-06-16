from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import requests

driver = webdriver.Firefox()
url1 = "https://magnit.ru/promo/?order=desc&sortBy=discountPercentage"

# alcohol__button alcohol__success  class button
# cookies__button class button

driver.get(url1)
time.sleep(5)
button_success = driver.find_element(By.CLASS_NAME, "alcohol__success")
try:
    # # Ожидание элемента и клик
    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[text()='Click me']"))  # Замените на ваш XPATH
    # )
    button_success.click()  # Клик по элементу
    print("Клик выполнен успешно.")
except Exception as e:
    print("Ошибка при клике:", e)
time.sleep(5)
button_cookies = driver.find_element(By.CLASS_NAME, "cookies__button")

try:
    button_cookies.click()  # Клик по элементу
    print("Клик выполнен успешно.")
except Exception as e:
    print("Ошибка при клике:", e)

time.sleep(1)

discounts_elements = driver.find_elements(By.CLASS_NAME, "new-card-product__badge")
images_elements = driver.find_elements(By.CSS_SELECTOR, ".new-card-product__image-wrap.new-card-product__image-wrap-catalog")

for image_element in images_elements:
    img = image_element.find_element(By.TAG_NAME, "img")
    src = img.get_attribute("src")
    print(src)

for discount in discounts_elements:
    print(discount.text, "\n")

driver.close()


####


# test_url = "https://5ka.ru/special_offers"
# page = requests.get(test_url)
# print(page.status_code)
# soup = bs(page.text, "html.parser")
# print(soup)
# print("\n", "==================================================", "\n")
# mass = soup.findAll('div', class_='discount-hint hint')
# print(mass)
# for i in mass:
#     print(i.text)