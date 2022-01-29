from os import system
from time import sleep
from selenium import webdriver

Token = str(input("Enter the Token You want to use to Login. : "))
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://discord.com/login')
sleep(1)
driver.execute_script('window.t = "' + Token + '";window.localStorage = document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage;window.setInterval(() => window.localStorage.token = `"${window.t}"`); window.location.reload();')
system('cls')
while True:
    print('You are Login With Your Discord Token.')
    print('Using Token : ' + Token)
    sleep(3)
    system('cls')

