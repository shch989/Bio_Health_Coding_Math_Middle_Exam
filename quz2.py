# 문제 2 (25점) - 조건문, 반복문 사용
# 사용자로부터 "가위", "바위", "보" 중 하나를 입력 받고
# 컴퓨터는 무작위로 "가위", "바위", "보" 중 하나를 생성하여
# 사용자와 컴퓨터의 승패를 판단하여 화면에 출력하고
# 다시 사용자로부터 "가위", "바위", "보" 중 하나를 입력받고
# 컴퓨터는 무작위로 "가위", "바위", "보" 중 하나를 생성하여 판단하는 것을 반복하기
# 사용자가 "가위", "바위", "보" 대신 0을 입력하면 게임은 종료되고
# 시행 횟수와 사용자 기준의 전적(0승 0패 0무)을 출력하기


import random

count = 0
win = 0
draw = 0
lose = 0

while True:
    user = input("가위, 바위, 보 중 하나를 입력하세요 (종료: 0): ")
    
    if user == '0':
        print("게임 종료!")
        print("게임 시행 횟수:", count)
        print("전적: {}승 {}패 {}무".format(win, lose, draw))
        break
        
    if user not in ['가위', '바위', '보']:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        continue
    
    count += 1
    computer = random.choice(['가위', '바위', '보'])
    
    print("유저: {}, 컴퓨터: {}".format(user, computer))
    
    if user == computer:
        print("비겼습니다!")
        draw += 1
    elif (user == '가위' and computer == '보') \
        or (user == '바위' and computer == '가위') \
        or (user == '보' and computer == '바위'):
        print("유저가 이겼습니다!")
        win += 1
    else:
        print("컴퓨터가 이겼습니다!")
        lose += 1
