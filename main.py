from playwright.sync_api import sync_playwright
from datetime import datetime
import time

# from bs4 import BeautifulSoup

p = sync_playwright().start()

id = input("아이디(ID) : ")
password = input("비밀번호(Password) : ")
repository = input("커밋 할 Repository를 입력하세요. : ")
commit_number = int(input("커밋 횟수를 입력하세요. : "))
# commit = input("커밋 제목을 입력하세요. : ")

browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://github.com/login")
time.sleep(3)

page.fill("input#login_field", id)
page.fill("input#password", password)
page.click("input[type=submit]")
time.sleep(3)

page.click("span[class=Button-content]")

# success = "https://github.com/"

# if page.url == success:
#     page.goto(f"https://github.com/{id}/{repository}/new/main")
# else:
#     print("Authentication code를 입력하세요.")

smsCode = input("Authentication code : ")

page.fill("input#sms_totp", smsCode)  # 웹페이지에 직접 입력했을 경우도 고려해보자
page.goto(f"https://github.com/{id}/{repository}/new/main")
time.sleep(3)

title_today = datetime.now().strftime("%Y%m%d")
page.get_by_placeholder("Name your file...").fill(title_today)
page.fill("div[class=cm-line]", ".")
page.click('button[data-hotkey="Mod+s"]')
time.sleep(3)

page.get_by_placeholder("Add an optional extended description..").fill(".")
page.click('button[data-hotkey="Mod+Enter"]')
time.sleep(3)

if commit_number == 1:
    time.sleep(2)
    p.stop()
else:
    for i in range(commit_number - 1):
        page.goto(f"https://github.com/{id}/{repository}/edit/main/{title_today}")
        time.sleep(3)

        page.fill("div[class=cm-line]", "." * (i + 2))
        page.click('button[data-hotkey="Mod+s"]')
        time.sleep(3)

        page.get_by_placeholder("Add an optional extended description..").fill(".")
        page.click('button[data-hotkey="Mod+Enter"]')
        time.sleep(3)

time.sleep(2)
p.stop()
