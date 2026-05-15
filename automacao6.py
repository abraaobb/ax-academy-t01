import re
import os
from playwright.sync_api import Playwright, sync_playwright, expect
from dotenv import load_dotenv
from time import sleep  

# Carrega as variáveis do arquivo .env
load_dotenv()

def run(playwright: Playwright) -> None:
    # Lê as credenciais do ambiente
    email = os.getenv("GMAIL_USER")
    password = os.getenv("GMAIL_PASSWORD")

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&dsh=S589114346%3A1778808655132569&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWa2PavyjQ3B1o0eGN_d9ns1mwuEuFAQy2A-qjIF2PcZ4XC2O5NAYMYNm4B_cX3scmP7_46beuseuQ")
    page.get_by_role("textbox", name="E-mail ou telefone").fill(email)
    page.get_by_role("button", name="Avançar").click()

    page.get_by_role("textbox", name="Digite sua senha").click()
    page.get_by_role("textbox", name="Digite sua senha").fill(password)
    page.get_by_role("textbox", name="Digite sua senha").press("Enter")


    page.get_by_role("button", name="Escrever").click()
    page.get_by_role("cell", name="MinimizarTela cheia (Shift").click()

    page.get_by_role("textbox", name="Assunto").click()
    page.get_by_role("textbox", name="Assunto").press("CapsLock")
    page.get_by_role("textbox", name="Assunto").fill("NOTA FISCAL")
    page.get_by_role("textbox", name="Corpo da mensagem").click()
    page.get_by_role("textbox", name="Corpo da mensagem").fill("\n")
    page1 = context.new_page()
    page.get_by_role("textbox", name="Corpo da mensagem").click()
    page.get_by_role("textbox", name="Corpo da mensagem").press("ControlOrMeta+V")
    page.get_by_role("textbox", name="Corpo da mensagem").fill("Prezado(a),\n\nSegue em anexo a nota fiscal referente ao serviço/produto fornecido.\n\nCaso haja qualquer dúvida ou necessidade de informação adicional, permaneço à disposiçã")
    page.get_by_text("Atenciosamente,[Seu Nome][").click()
    page.get_by_text("Destinatários").click()
    page.get_by_role("button", name="Enviar ‪(Ctrl-Enter)‬").click()

    # ---------------------

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)