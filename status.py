import random
import time

while True :
    str = random.randint(1,100)
    int = random.randint(1,100)
    dex = random.randint(1,100)
    if (str+int+dex) != 100:
        print(f'힘:{str}, 지능{int}, 민첩{dex}')
        break

# loading : 다운로드 되는 느낌

for i in range(30):
    time.sleep(random.random())
    print('=', end='', flush=True) #GPT 제안 : print('\r[' + '='*(i+1) + ' '*(30-i-1) + ']', end='', flush=True)
print('로딩 완료')

#GTP 제안 해석 : 문자 '='가 지정해놓은 공백에 루프마다 쌓이면서 출력.