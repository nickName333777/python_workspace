# **요구사항을 상세히 설명해주세요. 글/사진/그림(흐름도) 모두 사용해봅시다.**  

# 1. 파이썬 일기 콘솔앱을 만들어주세요.
# 2. 사용자는 다음 메뉴의 기능을 이용할수 있어야 합니다.
# - 사용자는 일기를 작성할 수 있습니다.
# - 사용자는 일기읽기를 통해 일기목록을 조회하고, 하나의 일기를 선택해 읽을 수 있습니다.

# ```
# === 일기장 메뉴 ===
# 1. 일기 작성
# 2. 일기 읽기
# 3. 종료
# ===============
# 선택:

# ```

# 1. 작성된 일기는 `files/2025-10-29.txt` 와 같이 `날짜.txt`이름으로 저장됩니다.
# 2. 목록보기에서 해당 일기파일을 선택하면, 그 내용을 읽어 출력합니다.
# 3. 필요한 클래스를 적절히 설계하세요.


# pyy 설정 요구사항
# 1. 클래스 구조
# 🔹 DiaryDay 클래스
# 속성
# diary_content: 일기내용 (문자열)
# diary_time: 기록 시간 (datetime 객체)
# 메서드
# __str__() 오버라이딩하여 다음 형식으로 출력
# [기록 시간: 2025-04-16 14:00:00] 내용: blah blah... 

# ​
# 🔹 DiaryUser 클래스
# 속성
# diaries: DiaryDay 객체 리스트
# 메서드
# write_diary(diary_content: str, mode: str): 일기 내용 기록 작성(mode='w'), 추가(mode='a')
# read_diary(diary_time: datetime, diary_index: int)
# display_diaries(): 전체 일기를 시간순으로 출력
#
# 🔹 DiaryMenu 클래스
# 메서드
# run(): 콘솔 메뉴를 반복 출력하며 사용자 입력에 따라 기능 수행
#  콘솔 메뉴 구성
# === 일기장 메뉴 ===
# 1. 일기 작성
# 2. 일기 읽기
# 3. 종료
# ===============
# 선택:

from datetime import datetime
import os

if not os.path.exists('files'):
    os.mkdir('files')

class DiaryDay:
    def __init__(self,  diary_time: str , diary_content=""):
        self.__diary_time = diary_time
        self.__diary_content = diary_content # 초기에는 빈칸만
        
        f_daystamp = self.__diary_time.strftime('%Y-%m-%d')
        self.__diary_path = f'./files/{f_daystamp}.txt'
        
    def get_diary_time(self):
        return self.__diary_time
    
    def get_diary_content(self):
        return self.__diary_content
    
    def update_diary_content(self, add_content:str):
        return  self.__diary_content + '\n' + add_content
    
    def __str__(self):
        return f'[기록 시간: {self.__diary_time}] 내용: {self.__diary_content}'
        
class DiaryUser:
    def __init__(self):
        self.__diaries: list[DiaryDay] = [] 
        
    def sel_diary(self, timestamp: str):
        return [ diary for diary in self.__diaries if diary.__diary_time == timestamp ] # 이미 일기 쓴 날짜에 있는 diary 선택
        
    def write_diary(self, diary_content: str, mode: str): #일기 내용 기록 작성(mode='w'), 추가(mode='a')
        check_timestamp = datetime.now().strftime('%Y-%m-%d')
        check_fname = f'files/{check_timestamp}.txt'
        if not os.path.exists(check_fname): # 오늘 일기 아직 안썼을때
            input_content = input("일기내용 입력: ")
            with open(check_fname, 'w', encoding='utf-8') as f:
                # 1) DiaryDay 생성 (옵션1: 이때 파일로 기록도 같이 해줄 수 있다)
                diary = DiaryDay(check_timestamp, input_content)
                # 2) File로 기록 (옵션2: 여기서 파일로 기록)
                f.write(diary.get_diary_content())
                
        else:  # 오늘 일기 이미 썼을때
            add_content = input("추가할 일기내용 입력: ")
            #check_fname_add = f'files/{check_timestamp}_add.txt'
            diary_selected = self.sel_diary(check_timestamp)
            with open(check_fname, 'a', encoding='utf-8') as f:
                # 1) DiaryDay 생성 (옵션1: 이때 파일로 기록도 같이 해줄 수 있다)
                #diary = DiaryDay(check_timestamp, input_content)
                diary_selected[0].update_diary_content(add_content)
                # 2) File로 기록 (옵션2: 여기서 파일로 기록)
                f.write(diary.get_diary_content())            
    
    def read_diary(self, diary_time: datetime, diary_index: int):
        pass
    
    def display_diaries(self): #전체 일기를 시간순으로 출력
        print('------------------- 전체 일기 조회 ---------------------')
        for idx, diary in enumerate(self.__diaries):
            print(f'{idx+1}. {diary}') # (O) __str__()호출 :

class DiaryMenu:
    def __init__(self):
        self.__diary_user = DiaryUser()
        
    def run(self):
        menu = """
=== 일기장 메뉴 ===
1. 일기 작성
2. 일기 읽기
3. 종료
===============
선택: """
        
        while True:
            choice = input(menu)
            match choice:
                case '1':
                    print("일기 작성")
                case '2':
                    print("일기 읽기")
                case '3':
                    print("이용해 주셔서 감사합니다")
                    break
                
menu = DiaryMenu()
menu.run()