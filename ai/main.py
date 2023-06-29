from ai import GptScrap
gpt=GptScrap()
gpt.Login()
gpt.cookies_generator()
gpt.formality()
token=1
while True:
    token+=1
    if token%2==0:
        if gpt.gpt_talk_verify()==True:
            gpt.gpt_says(token)
            continue
        elif gpt.gpt_talk_verify()==False:
            break
        else:
            pass
    else:
        pass