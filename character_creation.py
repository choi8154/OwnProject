import random
import time

# =======================character status=======================
class Character:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.level = 1
        self.str = 0
        self.int = 0
        self.dex = 0
        self.HP = 1000
        self.skill = {}

#-------------------------character act-------------------------

    def attack(self, monster):
        damage = random.randint(self.str-3,self.str)
        monster.HP -= damage
        time.sleep(2)
        print(f'{monster.name}에게 {damage}의 피해를 입혔다!')
        time.sleep(1)
        print(f'{"":=>10}{monster.name}의 HP는{monster.HP}남았다{"":=<10}\n')


    # def skill(self,skill, monster):
    #     if skill == self.skill[]:

    #     damage = random.randint

#-----------------------character skill-------------------------


# =======================monster status=======================
class Monster:
    def __init__(self, name, level):
        self.level = level
        self.name = name
        self.HP = 10*level
        self.str = level * 10

    def attack(self, character):
        damage = random.randint(self.str-10, self.str)
        character.HP -= damage
        time.sleep(2)
        print(f'LV.{self.level} {self.name}에게 {damage*1}의 피해를 받았다.')
        time.sleep(1)
        print(f'{"":=>10}{character.name}의 HP는{character.HP} 남았다{"":=<10}\n')




player = Character('용사', '전사')
a=5
while a > 0 :
    a-=1
    player.str = random.randint(1,8)
    player.int = random.randint(1,9-player.str)
    player.dex = random.randint(1,10-player.int)
    if player.dex > 0:
        print(f'힘:{player.str}, 지능{player.int}, 민첩{player.dex}')
    A = input(f'계속 진행 하시겠습니까?(y/n)(남은 초기화 {a}회):')
    if A == 'y':
        break
    else :
        continue



M = Monster('홉고블린', 5)

player.attack(M)
M.attack(player)



