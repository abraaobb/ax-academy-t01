import time
import pyautogui



class AutomacoesTurma01:
    def __init__(self):
        pass 

    def postador_de_posts(self):
        pyautogui.click(1016,1060)
        time.sleep(5)
        pyautogui.click(430,918)
        time.sleep(5)
        url = "https://www.facebook.com/"
        pyautogui.write(url)
        pyautogui.press("ENTER")
        time.sleep(5)
        email = ""
        senha = ""
        pyautogui.write(email)
        pyautogui.press("TAB")
        pyautogui.write(senha)
        pyautogui.press("TAB")
        pyautogui.press("TAB")
        pyautogui.press("ENTER")
        time.sleep(40)
        pyautogui.press("ESC")
        time.sleep(3)
        pyautogui.click(453,551)
        time.sleep(3)
        with open("textofacebook.txt", "r",encoding="utf-8") as file:
            conteudo = file.read()
        pyautogui.write(conteudo)
        time.sleep(4)
        pyautogui.click(524,794)
        print(pyautogui.position())

        


run = AutomacoesTurma01()
run.postador_de_posts()