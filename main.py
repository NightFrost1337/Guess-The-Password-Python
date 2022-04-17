import random
import pyautogui
import string
import time

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRFTUVWXYZ0123456789./&é(-è_çà)€ù*$£:;,^#!?[]}{|²<>%`"

chars_list = list(chars)

print ("Guess The Password is created by NightFrost#0001. ")

password = pyautogui.password("Entrer un mot de passe à trouver : ")

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, k=len(password))

    print("<="+ str(guess_password)+ "=>")

    if(guess_password == list(password)):
        print("Votre mot est de passe est : "+ "".join(guess_password))
        break
time.sleep(2.4)
