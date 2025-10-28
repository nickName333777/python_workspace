from datetime import datetime
# datetime:년, 월, 일, 시간, 분, 초, 마이크로초등을 포함하는 datetime 객체

from enum import Enum

class Entry(Enum): # Enum상속 (Enum --> 상수모음; 대문자 쓰는것이 관례)
    # 클래스 속성으로 name=value형식으로 지정
    IN = '입장'     # Entry.IN
    OUT = '퇴장'    # Entry.OUT


# ### 🔹 EntryLog 클래스

# - 속성
#     - `member_id`: 회원 고유 ID (문자열)
#     - `log_type`: `"입장"` 또는 `"퇴장"` 중 하나
#     - `timestamp`: 출입 시간 (`datetime` 객체)
# - 메서드
#     - `__str__()` 오버라이딩하여 다음 형식으로 출력
#           [입장] 회원ID: user001 - 시간: 2025-04-16 14:00:00

class EntryLog:
    #def __init__(self, member_id:str, log_type:str, timestamp: datetime):
    def __init__(self, member_id:str, log_type:Entry, timestamp: datetime):
        self.__member_id = member_id
        self.__log_type = log_type # Enum으로 "입장" 또는 "퇴장" 쓸수 있다
        #self.__timestamp = timestamp.strftime('%Y.%m.%d %H-%M-%S') # '2025.10.28 12-28-22'형식 문자열로 저장
        #self.__timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S') # '2025-10-28 12:28:22'형식 문자열로 저장
        self.__timestamp = timestamp

    def __str__(self): # 해당 객체의 시간필요 -> self
        #print(f'EntryLog(member_id = {self.__member_id}, log_type = {self.__log_type}, timestamp = {self.__timestamp})')
        #print(f'[{self.__log_type}] 회원ID: {self.__member_id} - 시간:{self.__timestamp}')
        time = self.__timestamp.strftime('%Y-%m-%d %H:%M:%S')
        # strftime(string format time) : 지정한 포맷에 맞게 문자열 변환
        return f'[{self.__log_type}] 회원ID : {self.__member_id} - 시간:{self.__timestamp}'
        
    def get_member_id(self):
        return self.__member_id
    
    # def set_member_id(self, member_id):
    #     self.__member_id = member_id
        
    def get_log_type(self):
        return self.__log_type
    
    # def set_log_type(self, log_type):
    #     self.__log_type = log_type
    
    def get_timestamp(self):
        return self.__timestamp
    
    # def set_timestamp(self, timestamp: datetime):
    #     #self.__timestamp = timestamp.strftime('%Y.%m.%d %H-%M-%S') # '2025.10.28 12-28-22'형식 문자열로 저장
    #     self.__timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S') # '2025-10-28 12:28:22'형식 문자열로 저장
        
        
        
        
# ### 🔹 EntryManager 클래스

# - 속성
#     - `logs`: `EntryLog` 객체 리스트
# - 메서드
#     - `add_log(member_id: str, log_type: str)`: 새로운 출입 기록 추가
#     - `display_logs()`: 전체 출입 기록을 시간순으로 출력

class EntryManager:
    #def __init__(self, logs: EntryLog):
    def __init__(self):
        #self.__logs = logs
        #self.__logs: list[EntryLog] = [] # EntryLog를 담는 리스트, EntryManager 객체의 속성
        self.__logs: list[EntryLog] = [] # 
        
    #def add_log(self, member_id: str, log_type: str):
    def add_log(self, member_id: str, log_type: Entry): # 둘다 상관없다.
        #elog = EntryLog(member_id, log_type, datetime.now()) # 여기서 EntryLog객체생성하고, timestamp 인자로 추가
        #self.__logs.append(elog) # 입장이든, 퇴장이든 무조건 추가        
        now_time = datetime.now()
        entrylog = EntryLog(member_id, log_type, now_time)
        self.__logs.append(entrylog)
        
    def display_logs(self):
        print('------------------- 전체 기록 조회 ---------------------')
        #for entrylog in self.__logs:
        for idx, entrylog in enumerate(self.__logs):
            #print(entrylog) # (O) __str__()호출: [입장] 회원ID : 1 - 시간:2025-10-28 14:47:33.081426
            #print({entrylog}) # (X) 객체 호출: {<__main__.EntryLog object at 0x000001B734A63110>}
            print(f'{idx+1}. {entrylog}') # (O) __str__()호출 : [입장] 회원ID : 1 - 시간:2025-10-28 14:47:33.081426
            #print(f'[{log.get_log_type()}] 회원ID: {log.get_member_id()} - 시간:{log.get_timestamp()}')


# ### 🔹 Menu 클래스

# - 메서드
#     - `run()`: 콘솔 메뉴를 반복 출력하며 사용자 입력에 따라 기능 수행
    
class Menu:
    def __init__(self):
        self.__entry_manager = EntryManager() # menu를 톻해서 EntryManager에게 일을 시켜야 한다.
    
    def run(self):
        menu = """===== 헬스장 회원 출입관리시스템 =====
1. 회원 입장
2. 회원 퇴장
3. 입퇴장 기록조회
0. 프로그램 종료
=============================
선택: """

        while True:
            choice = input(menu)
            
            match choice:
                case '1':
                    memId = input("회원ID: ") # member_id as String
                    
                    logTypeInput = "IN"
                    logType = Entry[logTypeInput].value # Entry.IN.value
                    #print(type(logType)) # <class 'str'>
                    self.__entry_manager.add_log(memId, logType) # "입장"
                    
                case '2':
                    memId = input("회원ID: ") # member_id as String
                    
                    logTypeInput = "OUT"
                    #logTypeInput = "OT" # KeyError: 'OT' # by Enum
                    
                    logType = Entry[logTypeInput].value  # Entry.OUT.value
                    self.__entry_manager.add_log(memId, logType) # "퇴장"
                case '3':
                    self.__entry_manager.display_logs()
                    
                case '0':
                    print("프로그램을 종료합니다/")
                    break
                case _:
                    print("잘못 입력하셨습니다.")
                    
        
##################################################################

menu = Menu()
menu.run()