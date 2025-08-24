import random


while True:
    str = random.randint(1,100)
    int = random.randint(1,100)
    dex = random.randint(1,100)
    if str+int+dex != 100:
        continue
    else:
        print(f'힘:{str}, 지능{int}, 민첩{dex}')
        break