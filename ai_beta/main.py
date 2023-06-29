# from ai import GptScrap
# gpt=GptScrap()
# gpt.Login()
# # gpt.cookies_generator()
# gpt.formality()
# token=1
# temp_num=0
# while True:
#     temp_num+=1
#     token+=1
#     if token%2==0:
#         if temp_num%5 or temp_num==1:
#             gpt.gpt_talk_first_time_verify()
#             gpt.gpt_says(token)
#         else:
#             if gpt.gpt_talk_verify()==True:
#                 gpt.gpt_says(token)
#                 continue
#             elif gpt.gpt_talk_verify()==False:
#                 break
#             else:
#                 pass
#     else:
#         pass
from voice_ai import VoiceAi
voice=VoiceAi()
voice.listen_voice()