from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from undetected_chromedriver import Chrome
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import json
HEADER={
    User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.35,
    Accept-Language:en-GB,en;q=0.9,en-US;q=0.8
}
class GptScrap():
    def __init__(self):
        cookies = []
        with open(./cookies.json, r) as file:
            for line in file:
                cookies.append(eval(line.strip()))
        self.date_today=datetime.now().strftime(%Y-%m-%d %H:%M:%S)
        self.chrome_options = Options()
        for key, value in HEADER.items():
            self.chrome_options.add_argument(f--header={key}:{value})
        self.driver = Chrome(options=self.chrome_options)
    def Login(self):
        Login_credential=True
        while True:
            # my_email = astroknestrok@gmail.com
            # passw = Aquatype1
            # my_email = input(Gmail Id:-)

                self.driver.get(https://chat.openai.com)
                time.sleep(4)
                with open(./cookies.json, r) as file:
                    cookies = json.load(file)
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                self.driver.get(https://chat.openai.com)
                time.sleep(300)
                # login=self.driver.find_element(xpath,/html/body/div[1]/div[1]/div[1]/div[4]/button[1])
                # login.click()
                # time.sleep(5)
                # google=self.driver.find_element(xpath,/html/body/div/main/section/div/div/div/div[4]/form[2]/button)
                # google.click()
                # time.sleep(3)
                # user_input=self.driver.find_element(xpath,//*[@id=identifierId])
                # user_input.send_keys(my_email)
                # user_next=self.driver.find_element(xpath,//*[@id=identifierNext]/div/button)
                # user_next.click()
                # time.sleep(6)
                # password_input=self.driver.find_element(xpath,//*[@id=password]/div[1]/div/div[1]/input)
                # password_input.send_keys(passw)
                # time.sleep(1)
                # password_next=self.driver.find_element(xpath,//*[@id=passwordNext]/div/button)
                # password_next.click()
                # time.sleep(13)
                break
    # def formality(self):
    #     next=self.driver.find_element(xpath,//*[@id=radix-:r8:]/div/div/div[4]/button)
    #     next.click()
    #     time.sleep(1)
    #     for i in range(0,2):
    #         next=self.driver.find_element(xpath,//*[@id=radix-:r8:]/div/div/div[4]/button[2])
    #         next.click()
    #         time.sleep(1)
    def gpt_talk_verify(self):
        user_text=input(ask:- )
        with open(./chat,a) as file:
            file.write(f\nUser Output on {self.date_today}\n)
        if user_text==exit or user_text==Exit or user_text==EXIT:
            print(Okay Good byy See You later Kashif !!!)
            return False
        else:
            gpt_input=self.driver.find_element(By.TAG_NAME,textarea)
            gpt_input.send_keys(user_text)
            gpt_input=gpt_input.find_element(By.XPATH, following-sibling::button)
            gpt_input.click()
            time.sleep(5)
            print(Please Wait For Response\n)
            while True:
                elements=self.driver.find_elements(By.TAG_NAME,fpolyline)
                temp=0
                for element in elements:
                    text = element.get_attribute(outerHTML)
                    if str(text)==<polyline points=1 4 1 10 7 10></polyline> or str(text)==<polyline points=23 20 23 14 17 14></polyline>:
                        return True
                    else:
                         pass
                temp+=1
                if temp==2:
                    print(The two most Powerful Warriors are Patience and Time.\nSo be Patience and say (GptScrap take ur Time)\n\n\n\n)
                time.sleep(5)
    def gpt_says(self,i):
        with open(./chat,a) as file:
            file.write(f\nGptScrap Output on {self.date_today}\n)
        element=self.driver.find_element(By.XPATH,f/html/body/div[1]/div[2]/div/div/main/div[2]/div/div/div/div[{i}]/div/div[2]/div[1]/div/div)
        text = element.get_attribute(outerHTML)
        soup = BeautifulSoup(text, html.parser)
        child_elements = soup.find(div).find_all()
        # Extract the text content of each child element
        for child_element in child_elements:
            if child_element.name == p:
                text_item=child_element.text.strip()
                print(text_item)
                with open(./chat.text,a) as file:
                    file.write(f{text_item}\n)
            elif child_element.name == ul or child_element.name == ol:
                for li_element in child_element.find_all(li):
                    text_item=li_element.text.strip()
                    print(text_item)
                    with open(./chat.text,a) as file:
                        file.write(f{text_item}\n)
            elif child_element.name == pre:
                code = child_element.find_all(code)
                text_item=str(code[0].text.strip())
                print(text_item)
                with open(./data/code,a) as file:
                    file.write(f# Here is ur code on date {self.date_today})
                    file.write(f{text_item}\n)
            else:
                pass