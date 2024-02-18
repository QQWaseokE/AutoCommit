from playwright.sync_api import sync_playwright
import time

# from bs4 import BeautifulSoup

p = sync_playwright().start()

id = input("아이디(ID) : ")
password = input("비밀번호(Password) : ")

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://github.com/login")

time.sleep(3)

page.fill("input#login_field", id)
page.fill("input#password", password)

time.sleep(1)

page.click("input[type=submit]")

time.sleep(3)

page.click("span[class=Button-content]")

smsCode = input("Authentication code : ")

page.fill("input#sms_totp", smsCode)

time.sleep(5)

# page.click("button[name=button]")

# time.sleep(3)

# page.click(f'a[href="/{id}/AutoCommit"]')

page.goto(f"https://github.com/{id}/AutoCommit/new/main")

time.sleep(5)

commit = input("커밋 제목을 입력하세요. : ")

page.get_by_placeholder("Name your file...").fill(commit)

page.fill("div[class=cm-line]", ".")

time.sleep(3)

page.click('button[data-hotkey="Mod+s"]')

time.sleep(3)

page.get_by_placeholder("Add an optional extended description..").fill(".")

time.sleep(3)

page.click('button[data-hotkey="Mod+Enter"]')

time.sleep(10)

p.stop()
