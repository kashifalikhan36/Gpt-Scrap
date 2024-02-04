from ai import GptScrap
import time
gpt=GptScrap()
gpt.Login()
try:
    gpt.formality()
except:
    pass
token=1
data_no=0
while True:
        token+=1
        if token%2 != 0:
            if gpt.gpt_talk_verify(data_no)==True:
                data_no+=1
                gpt.gpt_says(token,data_no)
                continue
            elif gpt.gpt_talk_verify()==False:
                break
            else:
                pass
        else:
            pass