

# 과제 3: 리스트, 딕셔너리, 함수 등 사용하여 대면수업 때 만들던 게임 보완
# A반 20200738 김유지 




#딕셔너리 사용
#딕셔너리로 조준성공할 경우의 경우의 수를 만든다.
hit = {
    1: '오른쪽', 
    2: '가운데', 
    3: '왼쪽' 
    }

#함수 사용
#함수로 조준성공이나 실패값을 리턴한다.
def start(choice, enemys):
    result = '0'
    if hit[choice] == enemys:
        result = '조준 성공! 적 비행기를 맞추었습니다.'
        return result
    else:
        result = '조준 실패! 적 비행기를 맞추지 못하였습니다.'
        return result
        


print("*********** 갤러그 게임 시작***********")

while 1:

    print("====================================================================================================================")
    print("적 비행기가 나타났습니다!")
    print("1. 오른쪽으로 이동해서 미사일 발사   2. 가운데를 향해 미사일 발사   3. 왼쪽으로 이동해서 미사일 발사   4. 게임 종료")

    number = int(input("숫자를 입력하세요: "))

    if number == 4:
        break

    elif (number != 1) and (number != 2) and (number != 3):
        print("잘못입력하셨습니다. 1,2,3,4 중 하나를 골라 입력하십시오.")
        continue

    else: 
        import random
        
        #리스트 사용
        list = ['오른쪽', '가운데', '왼쪽']    
        enemy = random.choice(list)
        print("--------------------------------------------------------------------------------------------------------------------")
        print(start(number,enemy))
        print( " 적비행기는", enemy, "에 있었습니다. ")


print("====================================================================================================================")
print("게임 종료")

