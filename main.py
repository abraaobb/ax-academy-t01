import os
import random
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()


class AutomacoesTurma01:
    def __init__(self):
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.account = os.getenv("ACCOUNT")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/")

    def automacao_8(self):
        self.setUp()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="email"]'))
        ).send_keys(self.user)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//input[@name="pass"]'))
        ).send_keys(self.password)

        self.driver.find_element(
            By.XPATH, '//div[@role="button" and @aria-label="Entrar"]'
        ).click()

        search_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[name()="svg" and @aria-label="Pesquisa"]/parent::div')
            )
        )

        self.driver.execute_script("arguments[0].click();", search_icon)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f'//a[@href="{self.account}"]'))
        ).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    '//*[name()="svg" and @aria-label="Contas semelhantes"]/ancestor::div[@role="button"]',
                )
            )
        ).click()

        see_all = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//span[contains(text(), "Ver tudo")]')
            )
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", see_all
        )

        delay = random.uniform(2.0, 5.0)
        time.sleep(delay)

        see_all.click()

        followed = 0

        while followed < 20:
            buttons = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//button[.//div[text()="Seguir"]]')
                )
            )

            for button in buttons:
                if followed >= 20:
                    print("Já está seguindo 20 contas")
                    break

                try:
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block: 'center'});", button
                    )

                    time.sleep(1)

                    button.click()

                    followed += 1

                    print(f"Seguiu {followed}")

                    time.sleep(2)

                    # scroll a cada 5
                    if followed % 5 == 0:
                        self.driver.execute_script("""
                            window.scrollBy(0, 800);
                        """)

                        time.sleep(3)

                except Exception as e:
                    print(e)
                    continue

    def teste_soma(self):
        assert 1 + 1 == 2


if __name__ == "__main__":
    ax = AutomacoesTurma01()
    ax.automacao_8()
