import random
import time

while True:
    U_HP = 20
    M_HP = 20
    print(3);time.sleep(1)
    print(2);time.sleep(1)
    print(1);time.sleep(1)
    print('전투 시작')
    print(f'유저체력:{U_HP}, 몹체력:{M_HP}')
    time.sleep(1)

    while M_HP >0 and U_HP >0:
        time.sleep(1)
        print('====유저 공격 턴====')
        U_D = random.randint(1,4)
        M_HP -= U_D
        print(f'{U_D}의 피해를 줌')
        print(f'몹 체력 : {M_HP}')
        if M_HP <= 0:
            break

        time.sleep(1)
        print('====몹 공격 턴====')
        M_D = random.randint(1,4)

        random_event = random.randint(1, 5)
        if random_event == 3:
            print(f'{"랜덤 이벤트 발생!!!":=^30}')
            rand_ev = int(input('빈틈의 실 발견!(상대방의 데미지를 예측하세요.):'))
            if M_D == rand_ev:
                print('.');time.sleep(1)
                print('.');time.sleep(1)
                print('.');time.sleep(1)
                print(f'패링! {M_D}의 데미지를 돌려줬습니다.')
                time.sleep(1)
                M_HP -= M_D
                print(f'몹 체력 : {M_HP}')
                
                if M_HP <= 0:
                    break
                continue

            else:
                print('실패!!')
                time.sleep(1)
                U_HP -= M_D
                print(f'{M_D}의 피해를 받음')
                print(f'유저 체력:{U_HP}')
                if U_HP <= 0:
                    break
                continue
        else:
            U_HP -= M_D
            print(f'{M_D}의 피해를 받음')
            print(f'유저 체력:{U_HP}')
            if U_HP <= 0:
                break

    print('전투 종료')
    if M_HP <= 0:
        print('승리!')
        break
    else:
        print('패배')
        user_choice = input('다시 하시겠 습니까?(n/y)')
        if user_choice=='y':
            continue
        else :
            break