# 조건문 if
# - if : 특정 조건에서만 실행되어야 하는 경우

# - if ... else : 모 아니면 도인 경우(둘 중 하나는 무조건 실행되는 경우)

# - if ... elif ... else : 고려해야 하는 조건이 여러가지인 경우 (그 중 하나만 실행해야 하는 경우)

def test1():
    # 시험 점수가 90점 이상인 경우 커피 쿠폰 지급
    score: int = int(input('시험 점수 입력 : '))    

    if score >= 90 :
        print('커피쿠폰 지급🍱🍣')

    print('수고하셨습니다~')
    
#test1()


def test2():
    # 시험 점수를 입력받아 60점 이상인 경우 합격, 아니라면 불합격
    score: int = int(input('시험 점수 입력 : '))  
    if score >= 60 :
        print('합격')
    else:
        print("불합격")
        
# test2()


def test3():
    
    score: int = int(input('시험 점수 입력 : '))  
    grade = None
    
    # 사용자 입력값 유효성 검사
    # 0 ~ 100 사이 점수가 아닌 경우
    if not(0 <= score <= 100):
        # -> 파이썬은 연쇄 비교 지원 : 0 <= score and score <= 100으로 자동 변환
        #print("test") 
        raise ValueError("0에서 100사이 점수를 입력해 주세요.") # 오류 던짐
           
    # 등급지정
    #if score >= 90 and score <= 100:
    if score >= 90 :
        grade = 'A'
    elif score >= 80:
        gread = 'B'
    elif score >= 70:
        gread = 'C'
    elif score >= 60:
        gread = 'D'
    else:
        gread = 'F'        
        
    print(f'점수는 {score} 이고 grade는 {grade} ')    
    
    # if score <= 60 :
    #     point = "F"
        
    # if score <= 70 :
    #     point = "D"
                
    # if score <= 80 :
    #     point = "C"
        
    # if score <= 90 :
    #     point = "B"        
        
    # else:
    #     point = "A" 
     
    #print(f"시험성적: {point}")
     
        
test3()   
    
