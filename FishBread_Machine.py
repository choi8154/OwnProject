#구상하기
# 1. 단팥, 슈크림, 고구마무스 가 있는 자판기 만들거야

# 2. 입력
#   2-1 단팥, 슈크림, 고구마무스 중에 골라서 입력
#   2-2. 입력은 단팥, 슈크림, 고구마무스 중 고른 것 갯수

# 3. 출력 : 단팥: 갯수, 슈크림: 갯수, 고구마무스: 갯수, 총 #개로 #원 입니다.

fish_price = {'단팥' : 2500, '슈크림': 2800, '고구마': 3000}

fish_choice = list(input('단팥, 슈크림, 고구마 중 고르시오(공백 문자로 구분) :').split())

fish_ea = []

for fish in fish_choice:
    fish_num = int(input(f'{fish} 몇 개 하시겠습니까 :'))
    fish_ea.append((fish, fish_num))


fish_all=[]
all_num = 0

for fish, fish_num in fish_ea:
    fish_pc = fish_price[fish]
    fish_all.append(fish_pc * fish_num)
    all_num += fish_num

all_price = sum(fish_all)

print(f'총 {all_num}개로 {all_price}원 입니다.')