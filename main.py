import os
import time
import random

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

from sites_config import SITES


load_dotenv()


class AutomacoesTurma01:
    def __init__(self):
        # Dados usados pela automação 8, que veio da develop
        self.user = os.getenv("USER")
        self.password = os.getenv("PASSWORD")
        self.account = os.getenv("ACCOUNT")

        # Dados usados pelo atualizador de dashboard
        self.pasta_destino = "screenshots_noticias"
        self.sites = SITES

        self.driver = None

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
            By.XPATH,
            '//div[@role="button" and @aria-label="Entrar"]'
        ).click()

        search_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//*[name()="svg" and @aria-label="Pesquisa"]/parent::div'
            ))
        )

        self.driver.execute_script("arguments[0].click();", search_icon)

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, f'//a[@href="{self.account}"]'))
        ).click()

        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((
                By.XPATH,
                '//*[name()="svg" and @aria-label="Contas semelhantes"]/ancestor::div[@role="button"]'
            ))
        ).click()

        see_all = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((
                By.XPATH,
                '//span[contains(text(), "Ver tudo")]'
            ))
        )

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            see_all
        )

        delay = random.uniform(2.0, 5.0)
        time.sleep(delay)

        see_all.click()

        followed = 0

        while followed < 20:
            buttons = WebDriverWait(self.driver, 20).until(
                EC.presence_of_all_elements_located((
                    By.XPATH,
                    '//button[.//div[text()="Seguir"]]'
                ))
            )

            for button in buttons:
                if followed >= 20:
                    print("Já está seguindo 20 contas")
                    break

                try:
                    self.driver.execute_script(
                        "arguments[0].scrollIntoView({block: 'center'});",
                        button
                    )

                    time.sleep(1)

                    button.click()

                    followed += 1

                    print(f"Seguiu {followed}")

                    time.sleep(2)

                    if followed % 5 == 0:
                        self.driver.execute_script("""
                            window.scrollBy(0, 800);
                        """)

                        time.sleep(3)

                except Exception as e:
                    print(e)
                    continue

    def atualizador_de_dashboard(self):
        if not os.path.exists(self.pasta_destino):
            os.makedirs(self.pasta_destino)
            print(f"Pasta '{self.pasta_destino}' criada.")

        print("Iniciando o navegador...")

        servico = Service(ChromeDriverManager().install())

        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(service=servico, options=opcoes)

        try:
            for index, (nome_site, info) in enumerate(self.sites.items()):
                try:
                    if index > 0:
                        driver.execute_script("window.open('');")
                        driver.switch_to.window(driver.window_handles[-1])

                    print(f"\nAcessando {nome_site} ({info['url']}) na aba {index + 1}...")

                    driver.get(info["url"])

                    wait = WebDriverWait(driver, 10)

                    elemento_manchete = wait.until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, info["seletor"])
                        )
                    )

                    driver.execute_script(
                        "arguments[0].scrollIntoView(true);",
                        elemento_manchete
                    )

                    time.sleep(1)

                    nome_arquivo = f"manchete_{nome_site.lower()}.png"
                    caminho_arquivo = os.path.join(
                        self.pasta_destino,
                        nome_arquivo
                    )

                    elemento_manchete.screenshot(caminho_arquivo)

                    print(f"Sucesso! Print salvo em: {caminho_arquivo}")

                except Exception as e:
                    print(f"Erro ao processar o site {nome_site}.")
                    print(
                        f"Detalhe: Pode ser que o seletor "
                        f"'{info['seletor']}' tenha mudado."
                    )
                    print(f"Erro original: {e}")

            print("\nTodas as abas foram processadas. Fechando o navegador em 5 segundos...")
            time.sleep(5)

        finally:
            driver.quit()
            print("Processo 'Atualizador de Dashboard' finalizado com sucesso.")


if __name__ == "__main__":
    robo = AutomacoesTurma01()
    robo.atualizador_de_dashboard()