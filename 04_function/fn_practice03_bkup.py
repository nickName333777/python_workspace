import random

def make_answer():
    """ 3자리 서로 다른 숫자로 정답 문자열 생성 """
    answer = random.sample("0123456789", 3)
    #answer = random.sample(range(0, 10), 3)
    # range(0, 10) : int
    
    
    #return answer # 리스트를 문자열로 합치기
    #return "".join([str(s) for s in answer]) # 리스트를 문자열로 합치기
    #return "".join(str(s) for s in answer) # 튜플을 문자열로 합치기
    return "".join(answer) # 문자열에서 뽑아 문자열로 합치기

#print(make_answer())


# 유효성검사 함수
def valid_guess(guess):
    """ 
    유효성 검사 
    - 전부 숫자인가?
    - 길이가 3인가?
    - 중복 숫자가 없는가?
    """
    return guess.isdigit() and len(guess) == 3 and len(set(guess)) == 3
# isdigit() : 숫자면 True, 아니면 False 반환

# print(valid_guess('str')) # False
# print(valid_guess('123')) # True
# print(valid_guess('1234')) # False
# print(valid_guess('122')) # False


def judge(answer, guess):
    """
    입력(guess)를 비밀번호(answer)와 비교하여
    strike 개수, ball 개수를 반환 (strike과 ball을 알면 out은 그걸로 판단가능)
    """
    # 같은 자리의 숫자가 같은지 비교하여 strike계산
    # answer : 123
    # guess :  125
    #          SS   
    
    strikes =  sum( a==g for a, g in  zip(answer, guess) )
    
    # guess의 각 문자가 정답(answer)에 포함되는지 확인
    # -> 전체 포함 개수 - strike의 수 = ball의 수
    # answer : 123
    # guess : 213
    # strike -> 1, ball -> 2
    #balls = len(set(guess).intersection(set(answer))) - strikes
    #return strikes, balls

    balls =  sum(g in answer for g in guess) - strikes
    return strikes, balls

    
    # ball = len(set(guess).intersection(set(answer))) - strike # 전체 포함 갯수 - strike수
    #  
    # strike = [ ]
    # ball = [ ]
    # out = 0;
    # for i, ch in enumerate(guess):
    #     if ch == answer[i]:
    #         strike.append("Strike")
    #        
    
    

# print(judge('123', '125')) # (2, 0)
# print(judge('123', '213')) # (1, 2)


attempts = 0 # 시도 횟수
answer = make_answer()  # 정답 생성
LENGTH = 3              # 자리수 설정
#print(answer) # 정답 확인용

while True :  # 언제끝날지 모르는 사용자 입력(무한반복)
    guess = input("3자리 숫자 입력(중복 불가) : ")
    
    # 유효성 검사
    if not valid_guess(guess):
        print("형식 오류 : 숫자만 중복없이 3자리로 입력하세요.")
        continue # 유효성 검사 실패시 하단 코드 실행않고 다음 반복으로
        
    # 판정
    attempts += 1
    
    strikes, balls = judge(answer, guess)
    
    if strikes == 3:
        print(f'정답! {attempts}번 만에 맞췄습니다')
        break
    elif strikes == 0 and balls == 0 :# 하나도 맞춘게 없는 경우
        print(f"하나도 못맞췄습니다. out입니다. 다시 시도해 보세요.")
        continue
    else:
        print(f'strike: {strikes}, ball: {balls} 입니다. 다시 시도해 보세요.')
        continue
        
    