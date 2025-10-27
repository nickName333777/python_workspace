"""
# 운전 콘솔 앱 (OOP)

## 객체지향프로그래밍 OOP
- 현실세계의 모든 사건은 객체(object)와 객체사이의 상호작용인 것에 주목한다.
- 객체간의 상호작용을 구현하기 위해 의인화 적용된다.
- 객체는 스스로 책임을 가지고 행동을 수행할 수 있다.
- 객체는 적절한 책임을 가질수 있도록 클래스 단위로 잘 분리해 작성해야 한다.
- 단일책임원칙 SRP Single Responsibility Principle 하나의 객체는 하나의 책임만 진다.
- (SOLID 객체지향 개발원칙을 참고)

## 객체간의 상호작용
- 객체는 아는 것(속성)과 할수 있는 것(메소드)으로 구성된다.
- 객체는 자기 할수 있는 것을 메소드로써 외부에 노출한다.
- 객체와 객체는 메세지를 주고받는다.
- 송신자객체는 수신자객체에 매개인자를 통해 메소드를 호출함으로써 메시지를 전송한다.
- 수신자객체는 일련의 책임을 수행후 리턴값으로 송신자객체에 응답한다.

## Driving Application

### 1. 요구사항 명세 (클라이언트)
- 운전프로그램을 만들어 주세요.
- 운전자는 시동걸기/끄기, 악셀 또는 브레이크를 밟을 수 있습니다.
- 자동차는 엔진시작/끝, 가속/감속을 할 수 있습니다.
- 자동차는 처음에 대기상태 있어야 합니다. (시동이 꺼진 상태)
- 자동차는 운전자에 의해 시동이 걸리고, 이미 시동이 걸려있다면, 또 시동을 걸수는 없습니다. (-> start_car (start_engine))
- 운전자가 악셀을 밟으면, 자동차는 10km/h씩 가속할 수 있습니다.
- 최대속도는 200km/h 입니다.
- 운전자가 브레이크를 밟으면, 자동차는 10km/h씩 감속할 수 있습니다.
- 운전자가 시동을 끄면, 자동차는 더이상 움직일 수 없습니다. (시동이 꺼진 상태) (-> -> accelerate(increase_speed))
- 자동차가 달리는 동안에는 시동을 끌수 없습니다. (-> stop_car(stop_engine))

### 2. 객체 도출
- 운전자
- 자동차
- 프로그램메뉴 (사용자 보게될 메뉴, 입력폼, 결과출력 담당할 UI객체)

### 3. 객체간의 상호작용

**어떤 객체가 무엇을 알고, 무엇을 할수 있는가?**

```
        프로그램메뉴          운전자             자동차
----------------------------------------------------------------
know     운전자              자동차             엔진작동여부
                                               현재속도
do      메뉴 제공            시동걸기            엔진시작
        메뉴 선택            시동끄기            엔진종료
                            악셀 밟기            가속
                           브레이크 밟기          감속

                ---------->           -------->
                시동을 걸어라            엔진을 시작하라
                    True                   True
                엑셀 밟아라              엔진을 가속하라
                    100                    100
                브레이크를 밟아라          엔진을 감속하라
                     90                     90
                 시동을 꺼라             엔진을 종료하라
                    False                  False
                <----------           <---------

```

### 4. 클래스 설계 (요구사항에 준하는 클래스 설계) => 3개 필요
"""

class Car :
    
    # 모든 Car가 동일하게 갖는 속성(-> 클래스 속성) => 대문자는 final이라는 의미(변하지 않는 속성)
    SPEED_STEP = 10 # km/h
    MAX_SPEED = 200 # km/h
    
    def __init__(self): # 최초의 Car()생성시 상태
        self.__engine_started = False
        self.__speed = 0
        
        
    def start_engine(self):
        #pass # 아무 일도 하지 않는다.
        if self.__engine_started == True:
            return -1 # 이미 시동이 걸려 있는 경우
        else: # self.__engine_started == False 인경우:
            self.__engine_started = True # 이제 이러면, 시동을 킨것
            return self.__engine_started == True # 시동켜기 성공여부 반환
    
    def stop_engine(self):
        #pass
        if self.__speed > 0:
            return -1
        else:
            self.__engine_started = False # 이제 이러면, 시동을 끈것
            #self.__speed = 0 # 0일때만 시동 끌수 있다.
            return self.__engine_started == False # 시동켜기 성공여부 반환
    
    def increase_speed(self):
        #pass
        
        if self.__engine_started == False:
            return -1 # 시동이 꺼져있어 accelerate못하는 상태
        else: 
            # 가속조건 적용 (최고 속도 200km/h)
            #if self.__speed <= Car.MAX_SPEED:
            if self.__speed < Car.MAX_SPEED:
                self.__speed += Car.SPEED_STEP
            return self.__speed    
            #else:
            #    return -1 # 200km/h이상 못 올린다는 으미
            
            #return min(self._speed, 200)
    
    def decrease_speed(self):
        #pass
        if self.__speed > 0:
            #self.__speed -= 10
            self.__speed -= Car.SPEED_STEP
        return self.__speed
    
    def check_start_engine(self):
        return self.__engine_started
    
    def check_current_speed(self): # Getter의 역할
        return self.__speed # private 속성, 
    
########################################################

class Driver: # 드리이버 객체가 생성될때 Car객체를 가지고 있을수 있도록 하자
    def __init__(self):
        self.__car = Car()
        
    def start_car(self):
        # if  self.__car.__engine_started == True:
        #     print(f'이미 시동이 걸려있어 또 시동을 걸수 없습니다')
        #     return
        # else:
        #     return self.__car.start_engine()
        return self.__car.start_engine() # -1(이미 시동이 걸린 상태), False(시동 실패), True(시동 성공)
            
        
        #return self.__car.start_engine()
    
    def stop_car(self):
        #pass
        #if self.__car.__speed > 0:
        #    print(f'자동차가 달리는 동안에는 시동을 끌수 없습니다.')
        #    return
        #else:        
        #    return self.__car.stop_engine()
        
        return self.__car.stop_engine()
    
    def accelerate(self):
        #pass
        #if self.__car.__engine_started ==False:
        #    print("운전자가 시동을 끄면, 자동차는 더이상 움직일 수 없습니다")
        #    return0
        #else:
        #    return self.__car.increase_speed()
        return self.__car.increase_speed()
    
    def brake(self):
        #pass
        return self.__car.decrease_speed()
    
    def check_start_car(self):
        return self.__car.check_start_engine()
    
    def check_current_speed(self):
        return self.__car.check_current_speed()
    
########################################################

class Menu: # 메뉴 객처가 생성될때, Driver(-> Car)가 있을 수 있도록
    def __init__(self):
        self.__driver = Driver()
        
    def main_menu(self):
        menu = """
----------------------------------
🚗🚗🚗 Driving Application 🚗🚗🚗
----------------------------------
1. 시동 걸기
2. 시동 끄기
3. 악셀 밟기
4. 브레이크 밟기
0. 프로그램 종료
----------------------------------
입력 : """
    
        while True: # main_menu()실행 시, 사용자로 부터 입력받는다.
            choice = input(menu)    
            match choice:
                case '1': 
                    # 1) 시동이 걸려있는지 확인
                    if self.__driver.check_start_car() == False:  # Car의 private속성에 직접 접근하지 않는다(메소드통해서한다).              
                        result = self.__driver.start_car() # True: 시동이 켜진면
                        if result:
                            print("부릉~ 시동이 정상적으로 걸렸습니다.")
                       
                    else:
                        print(f'이미 시동이 걸려있어 또 시동을 걸수 없습니다')
                        
                case '2':
                    # 이미 시동이 꺼져있는 경우
                    if self.__driver.check_start_car() == False:
                        print("이미 시동이 꺼져있는 상태입니다.")
                        
                    else:
                        # 달리는 중인 경우
                        if self.__driver.check_current_speed() > 0:
                            print("자동차가 달리는 동안은 시동을 끌 수 없습니다.")
                        else:
                            result = self.__driver.stop_car()
                            if result:
                                print("시동을 껏습니다.")
                        
                case '3':
                    current_speed = self.__driver.accelerate()
                    print("3333333333", current_speed)
                    if current_speed == -1:
                        print("운전자가 시동을 끄면, 자동차는 더이상 움직일 수 없습니다")
                    else:                      
                        #current_speed = self.__driver.accelerate()
                        print(f'현재 속도는 {current_speed}km/h 입니다.')                  
                        
                        #result = self.__driver.accelerate()  
                        #if result > 0:
                        
                        #    print(f'현재 속도는 {result}로 가속되었습니다.')                  
                        
                case '4':
                    current_speed = self.__driver.brake()
                    print(f'현재 속도는 {current_speed}km/h 입니다.')
                    
                case "0":
                    #print('이용해 주셔서 감사합니다.')
                    break
                
                case _: # default: "_"
                    print(f'잘못누르셨습니다.')

        print('이용해 주셔서 감사합니다.')
    
    
##########################################################

# 실행
menu = Menu()
menu.main_menu() # 메뉴화면 호출