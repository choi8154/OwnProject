#구상하기
# 1. 단팥, 슈크림, 고구마무스 가 있는 자판기 만들거야
# 2. 입력
#   2-1 단팥, 슈크림, 고구마무스 중에 골라서 입력
#   2-2. 입력은 단팥, 슈크림, 고구마무스 중 고른 것 갯수
# 3. 출력 : 단팥: 갯수, 슈크림: 갯수, 고구마무스: 갯수, 총 #개로 #원 입니다.


#종류별 가격 정하기
fish_price = {'단팥' : 2500, '슈크림': 2800, '고구마': 3000}


 #
while True:
    fish_choice = input('단팥, 슈크림, 고구마 중 고르시오(공백 문자로 구분) :').split()
    if fish_choice == []:
        print('리스트를 입력 하시오')
        continue
    else:
        if not all(fish in fish_price for fish in fish_choice) :
            print('리스트에서만 고르시오!')
            continue
        else:
            break

#붕어빵 별 갯수 입력.
fish_ea = []

 #?여기도 숫자 입력을 안하거나 20개가 넘는 수를 입력시 진짜로 살건지 1번 더 확인하도록 기능을 넣어야함.
for fish in fish_choice:
    fish_num = int(input(f'{fish} 몇 개 하시겠습니까 :'))
    fish_ea.append((fish, fish_num)) #붕어빵, 갯수를 ()로 담아 리스트로 모두 넣음.

#붕어빵 가격 연산하기, 붕어빵 총 갯수 연산하기
fish_all=[]
all_num = 0

for fish, fish_num in fish_ea:
    fish_pc = fish_price[fish]
    fish_all.append(fish_pc * fish_num)
    all_num += fish_num #붕어빵 갯수 모두 구하기

#붕어빵 가격 모두 더하기
all_price = sum(fish_all)
 #?붕어빵 종류별로 갯수와 가격이 출력되도록.
#붕어빵 결과 출력
print(f'총 {all_num}개로 {all_price}원 입니다.')

# !부족한 것 붕어빵별 갯수 구해서 출력하기, 붕어빵 종류 외 입력시 다시 입력하라고 하기, 붕어빵 갯수 입력시 숫자가 아니면 다시 입력하라고 하기