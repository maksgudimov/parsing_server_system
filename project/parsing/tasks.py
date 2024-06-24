from celery import shared_task
import time
import requests


@shared_task
def parsing_magnit():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.service import Service
    from products.models import Product
    from shops.models import Shop
    from parsing.models import ParsingSetting
    shop = Shop.objects.get(name="МАГНИТ СЕМЕЙНЫЙ")
    parsing = ParsingSetting.objects.get(shop=shop)

    Product.objects.filter(shop=shop).delete()

    service = Service("/home/mgudimov/Документы/parsing-system/project/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get(parsing.website)
    driver.implicitly_wait(5)
    try:
        button_success = driver.find_element(By.CSS_SELECTOR, parsing.parsing_args['button_success'])
        button_success.click()
        print("Клик выполнен успешно.")
    except Exception as exp:
        print("Ошибка при клике:", exp)
    driver.implicitly_wait(5)
    try:
        button_cookies = driver.find_element(By.CSS_SELECTOR, parsing.parsing_args['button_cookies'])
        button_cookies.click()
        print("Клик выполнен успешно.")
    except Exception as exp:
        print("Ошибка при клике:", exp)
    driver.implicitly_wait(1)
    discounts_elements = driver.find_elements(By.CLASS_NAME, parsing.parsing_args['discounts_elements'])
    images_elements = driver.find_elements(By.CLASS_NAME,
                                           parsing.parsing_args['images_elements'])
    names_elements = driver.find_elements(By.CSS_SELECTOR, parsing.parsing_args['names_elements'])
    prices_elements = driver.find_elements(By.CSS_SELECTOR, parsing.parsing_args['prices_elements'])
    last_prices_elements = driver.find_elements(By.CSS_SELECTOR, parsing.parsing_args['last_prices_elements'])

    discounts_list = []
    images_list = []
    names_list = []
    prices_list = []
    last_prices_list = []
    for i in prices_elements:
        print("prices_elements")
        x = i.text.replace(",", ".").replace("₽", "").strip()
        # Убираем любые невидимые символы Unicode
        x = ''.join(c for c in x if c.isdigit() or c == '.')
        print(float(x))
    for i in last_prices_elements:
        print("last_prices_elements")
        x = i.text.replace(",", ".").replace("₽", "").strip()
        # Убираем любые невидимые символы Unicode
        x = ''.join(c for c in x if c.isdigit() or c == '.')
        print(float(x))
    try:
        for discount in discounts_elements:
            normal_discount = discount.text.replace("-", "").replace("%", "")
            discounts_list.append(int(normal_discount))
        for image_element in images_elements:
            img = image_element.find_element(By.TAG_NAME, "img")
            src = img.get_attribute("src")
            images_list.append(src)
        for names_element in names_elements:
            names_list.append(names_element.text)
        for prices_element in prices_elements:
            normal_price = prices_element.text.replace(",", ".").replace("₽", "").strip()
            normal_price = ''.join(c for c in normal_price if c.isdigit() or c == '.')
            prices_list.append(normal_price)
        for last_prices_element in last_prices_elements:
            normal_last_price = last_prices_element.text.replace(",", ".").replace("₽", "").strip()
            normal_last_price = ''.join(c for c in normal_last_price if c.isdigit() or c == '.')
            last_prices_list.append(normal_last_price)

    except Exception as exp:
        print(f"Произошла ошибка при переводе в list() | {exp}")

    driver.close()

    print(discounts_list)
    print(images_list)
    print(names_list)
    print(prices_list)
    print(last_prices_list)

    try:
        bulk_list = []
        for discount, image, name, price, last_price in zip(discounts_list, images_list, names_list, prices_list, last_prices_list):
            if discount >= 35:
                bulk_list.append(Product(discount=discount, img_url=image, name=name, price=price, last_price=last_price, shop=shop))
        Product.objects.bulk_create(bulk_list)
    except Exception as exp:
        print(f"Произошла ошибка при for zip() или в bulk_create | {exp}")


@shared_task
def parsing_crossroads():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.service import Service
    from products.models import Product
    from shops.models import Shop
    from parsing.models import ParsingSetting
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.support import expected_conditions as EC

    shop = Shop.objects.get(name="ПЕРЕКРЕСТОК")
    parsing = ParsingSetting.objects.get(shop=shop)
    Product.objects.filter(shop=shop).delete()
    service = Service("/home/mgudimov/Документы/parsing-system/project/geckodriver")
    driver = webdriver.Firefox(service=service)
    driver.get(parsing.website)
    driver.implicitly_wait(5)
    button_success = driver.find_element(By.CLASS_NAME, parsing.parsing_args['button_success'])
    try:
        # Прокрутить элемент в видимую область
        driver.execute_script("arguments[0].scrollIntoView(true);", button_success)

        # Подождать, пока элемент станет кликабельным
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, parsing.parsing_args['button_success']))
        )
        # Использовать ActionChains для клика
        actions = ActionChains(driver)
        actions.move_to_element(button_success).click().perform()
        print("Клик выполнен успешно.")
    except Exception as exp:
        print("Ошибка при клике:", exp)

    driver.implicitly_wait(5)
    discounts_elements = driver.find_elements(By.CLASS_NAME, parsing.parsing_args['discounts_elements'])
    images_elements = driver.find_elements(By.CLASS_NAME,
                                               parsing.parsing_args['images_elements'])
    names_elements = driver.find_elements(By.CLASS_NAME, parsing.parsing_args['names_elements'])
    prices_elements = driver.find_elements(By.CLASS_NAME, parsing.parsing_args['prices_elements'])
    last_prices_elements = driver.find_elements(By.CLASS_NAME, parsing.parsing_args['last_prices_elements'])
    discounts_list = []
    images_list = []
    names_list = []
    prices_list = []
    last_prices_list = []
    try:
        for discount in discounts_elements:
            normal_discount = discount.text.replace("-", "").replace("%", "")
            discounts_list.append(int(normal_discount))
        for image_element in images_elements:
            img = image_element.find_element(By.TAG_NAME, "img")
            src = img.get_attribute("src")
            images_list.append(src)
        for names_element in names_elements:
            names_list.append(names_element.text)
        for prices_element in prices_elements:
            normal_price = prices_element.text.replace("Цена\n", "").replace(",", ".").split(" ")[0]
            prices_list.append(normal_price)
        for last_prices_element in last_prices_elements:
            normal_last_price = last_prices_element.text.replace("Старая цена\n", "").replace(",", ".").split(" ")[0]
            last_prices_list.append(normal_last_price)
    except Exception as exp:
        print(f"Произошла ошибка при переводе в list() | {exp}")
    driver.close()
    try:
        bulk_list = []
        for discount, image, name, price, last_price in zip(discounts_list, images_list, names_list, prices_list,
                                                            last_prices_list):
            if discount >= 50:
                bulk_list.append(
                    Product(discount=discount, img_url=image, name=name, price=price, last_price=last_price, shop=shop))
        Product.objects.bulk_create(bulk_list)
    except Exception as exp:
        print(f"Произошла ошибка при for zip() или в bulk_create | {exp}")
