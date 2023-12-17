import requests
import numpy as py
 
moji_listm =[['🙂','😄'],
['😢','😥'],
['😡','😠'],
['🙄'],
['😱'],
['😨',],
['😮'],
['😴','😪'],
['😋'],
['😌'],
['😐'],
['😷'],
['😳'],
['😵'],
['💔'],
['😎','😈'],
['🙃','😏','😂','😭'],
['😬','😅','😶'],
['😉'],
['💖','💙','💚','💗','💓','💜','💘','💛'],
['😇']]

texts  = ['happy',"sad"]
url = "https://api.aiforthai.in.th/emoji"
text = 'ไม่อร่อย อาหารรสชาติห่วยแตก'
params = {'text':text}
headers = {
    'Apikey': "6SdwbWBIe03JeTwlhBLKMM4Xyk3KnxHX"}
response = requests.get(url, params=params, headers=headers)
 
pred_emoji=response.json()
print(pred_emoji)
sorted_emoji = sorted(pred_emoji, key=lambda k: float(pred_emoji[k]), reverse=True)
top_emoji_idx = sorted_emoji[0]
print(sorted_emoji)
print(moji_listm[int(top_emoji_idx)][0])


if top_emoji_idx == '1':
    print('อย่าเศร้าไปเลยนะ บางทีอาจจะไม่ได้แย่อย่างที่คิดก็ได้ ลองออกอยู่กับธรรมชาติซักแปปหนึ่งดูก็ได้นะ มันจะทำให้รู้สึกดีขึ้น 🙂')