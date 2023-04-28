#クリップボードから文字列を取り出して、ToDoist の 今日の項目に post する
#複数行コピペした場合、１行目が todo のタイトル、２行目以降が「説明」に入る
 
from todoist_api_python.api import TodoistAPI
import pyperclip
import time

desc = ''
lines = []
clines = pyperclip.paste().splitlines()

for line in clines: # clip の空行を排除
    if line != '':
        lines.append(line)

count = len(lines)
if count == 0 :
	print ('ERR クリップボードが空です')
	input ()
	exit()

api = TodoistAPI("7b1a925495c9af66a52e0a1883037e4dc6ce03a9")

#priority = 1 だと優先度4 、4だと優先度1 なぜか逆
# https://developer.todoist.com/rest/v2/?python#create-a-new-task

if count >= 2 :
    for todo in lines[1:]: #二行目以降があれば、コメントに
        desc = desc + todo

try:
    task = api.add_task(
    content= lines[0],
    description = desc,
    due_string="today",
    due_lang="ja",
    priority=2,
    )
    print('登録:',lines[0]) 
    time.sleep(3)

except Exception as error:
    print(error)
    input()    
