
#공책 RPG
#?플레이어는 게임이 시작 될 때 클래스를 정할 수 있음.
#?클래스 마다 주어지는 무기와 스킬이 다름.
#플레이어는 스테이지가 끝날 때 마다 계속 진행할지 자신의 무기를 강화 할지 선태 할 수 있음. 
#무기 강화는 
#1., 4개의 스테이지 후 마왕과 마주함. 마왕의 이름은 5번째 스테이지 마다 바뀜 스테이지는 1-5, 2-3 이런식으로 매번 바뀜 총 5-5의 스테이지 까지 있고 마지막은 마신을 마주함.
#적은 공격, 회피, 방어 중 렌덤 한 행동을 함. 그에 대응하는 적절한 선택을 할 시 크리티컬이 들어 갈 수 있음.
import time
import random

def game_start():
    print('켄터베리 왕국에 오신 용사님 환영합니다.')
    time.sleep(2)
    player_name = input('용사님의 이름을 알려주세요! :')
    time.sleep(1)
    print(f'반갑습니다. {player_name}용사님. 이세계의 악을 모두 쓰러트리고 엄청난 부와 명예를 얻기를 .')
    print('로딩중...'); time.sleep(3)
    return player_name

def main_content():
    user_choice = input('싸우시겠습니까?\n무기를 꺼내든다(y)\n도망친다(n):')
    if user_choice == 'y':
        fight()
    else:
        print('도망 쳤습니다.')

def fight():
    HP = 50; MP = 100
    M_HP = 15
    user_status = (f'HP:{HP} MP:{MP}')
    print(f'{user_status:=^30}')
    print(f'적 채력:{M_HP}')
    print()
    while M_HP > 0:
        if HP < 0 :
            print('YOU DIE')
            die_choice = input('다시 하시겠습니까?(y/n):')
            if die_choice == 'y':
                fight()
            else:
                print('게임이 종료 되었습니다.')
                return
        user_choice = int(input('1.공격 2.방어 3.스트라이크:'))
        if user_choice == 1:
            user_damage = random.randint(1,10)
            print(f'{user_damage}의 피해를 입혔습니다.')
            M_HP-=user_damage
            if M_HP <= 0:
                continue
            else:
                print(f'적 체력:<<{M_HP}>>')
                time.sleep(2)
                m_damage = random.randint(1, 10)
                HP-=m_damage
                print(f'{m_damage}의 피해를 입었습니다.')
                user_status = (f'HP:{HP} MP:{MP}')
                if HP <= 0:
                    continue
                else:
                    print(f'{user_status:=^30}')
    print('축하합니다. 적을 쓰러트리셧 습니다.')





if __name__ == '__main__':
    game_start()
    main_content()