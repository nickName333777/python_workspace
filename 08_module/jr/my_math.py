# 사용자 모듈 작성

pi: float = 3.143

x: int = 55

__v : str = '바밤바'

def get_circle_area(r:float) -> float:
    return r * r * pi

if __name__ == '__main__':
    print("my_math를 실행하였습니다.")