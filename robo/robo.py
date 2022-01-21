from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from random import choice
import time, sys, requests, shutil


def run(users_styles):
    number_identifier = 100

    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.get("https://app.wombo.art")

    with open("words.txt", "r") as file:
        words = file.read()
        words = words.split('\n')

    for word in words:

        # Get the input field
        input_field_xpath = "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[1]/div[1]/input"
        input_field_elem = driver.find_element_by_xpath(input_field_xpath)
        input_field_elem.clear()
        input_field_elem.send_keys(word, Keys.DOWN)
        time.sleep(1)

        # Get the style card
        baroque =   "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]"
        mystical =  "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[7]"
        etching =   "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[1]"
        hd =        "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[8]"
        pastel =    ""
        psychic =   "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[10]"
        vibrant =   "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[9]"
        ukiyoe =    "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[12]"
        syntwave =  "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[13]"
        fantasy =   ""
        steampunk = "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[11]"
        no_style =  "/html/body/div/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[14]"

        styles = {
            "baroque": baroque,
            "mystical": mystical,
            "etching": etching,
            "hd": hd,
            "pastel": pastel,
            "psychic": psychic,
            "vibrant": vibrant,
            "ukiyoe": ukiyoe,
            "syntwave": syntwave,
            "fantasy": fantasy,
            "steampunk": steampunk,
            "no_style": no_style
        }

        if users_styles:
            if (len(users_styles.split(',')) == 1):
                style_card_element = driver.find_element_by_xpath(styles[users_styles])
            else:
                style_card_element = driver.find_element_by_xpath(styles[choice(users_styles.split(','))])
        else:
            style_card_element = driver.find_element_by_xpath(choice(list(styles.values())))
        style_card_element.click()
        time.sleep(2)

        # Create button
        create_button_xpath = "/html/body/div/div/div[3]/div/div/div[1]/div[2]"
        create_button_element = driver.find_element_by_xpath(create_button_xpath)
        create_button_element.click()

        # Get Image
        final_image_xpath = "/html/body/div/div/div[3]/div/div/div[2]/div/img"

        # Get back button 
        get_back_button = "/html/body/div/div/div[3]/div/div/div[1]/div[1]/button"

        # Wait for the save button
        save_button_xpath = "/html/body/div/div/div[3]/div/div/div[1]/div[2]/div/div[4]/div[1]/button"

        # Wait for the image
        try:
            save_button_element = WebDriverWait(driver, 45).until(
                ec.presence_of_element_located((By.XPATH, save_button_xpath))
            )
            image_src = driver.find_element_by_xpath(final_image_xpath).get_attribute("src")
            __image = requests.get(image_src, stream=True)

            with open("output/" + "Ai.morpheus #" + str(number_identifier) + ".png", "wb") as picture:
                shutil.copyfileobj(__image.raw, picture)
                time.sleep(4)
                driver.find_element_by_xpath(get_back_button).click()
                number_identifier += 1
        except Exception as e:
            print("Timedout refreshing.")
            time.sleep(3)   
            driver.refresh()
            pass
            

    driver.close()


