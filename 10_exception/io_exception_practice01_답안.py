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
# read_diary()
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

# class DiaryDay:
#     def __init__(self,  diary_time: str , diary_content=""):
#         self.__diary_time = diary_time
#         self.__diary_content = diary_content # 초기에는 빈칸만
        
#         f_daystamp = self.__diary_time.strftime('%Y-%m-%d')
#         self.__diary_path = f'./files/{f_daystamp}.txt'
        
#     def get_diary_time(self):
#         return self.__diary_time
    
#     def get_diary_content(self):
#         return self.__diary_content
    
#     def update_diary_content(self, add_content:str):
#         return  self.__diary_content + '\n' + add_content
    
#     def __str__(self):
#         return f'[기록 시간: {self.__diary_time}] 내용: {self.__diary_content}'
        
# class DiaryUser:
#     def __init__(self):
#         self.__diaries: list[DiaryDay] = [] 
        
#     def sel_diary(self, timestamp: str):
#         return [ diary for diary in self.__diaries if diary.__diary_time == timestamp ] # 이미 일기 쓴 날짜에 있는 diary 선택
        
#     def write_diary(self, diary_content: str, mode: str): #일기 내용 기록 작성(mode='w'), 추가(mode='a')
#         check_timestamp = datetime.now().strftime('%Y-%m-%d')
#         check_fname = f'files/{check_timestamp}.txt'
#         if not os.path.exists(check_fname): # 오늘 일기 아직 안썼을때
#             input_content = input("일기내용 입력: ")
#             with open(check_fname, 'w', encoding='utf-8') as f:
#                 # 1) DiaryDay 생성 (옵션1: 이때 파일로 기록도 같이 해줄 수 있다)
#                 diary = DiaryDay(check_timestamp, input_content)
#                 # 2) File로 기록 (옵션2: 여기서 파일로 기록)
#                 f.write(diary.get_diary_content())
                
#         else:  # 오늘 일기 이미 썼을때
#             add_content = input("추가할 일기내용 입력: ")
#             #check_fname_add = f'files/{check_timestamp}_add.txt'
#             diary_selected = self.sel_diary(check_timestamp)
#             with open(check_fname, 'a', encoding='utf-8') as f:
#                 # 1) DiaryDay 생성 (옵션1: 이때 파일로 기록도 같이 해줄 수 있다)
#                 #diary = DiaryDay(check_timestamp, input_content)
#                 diary_selected.
#                 # 2) File로 기록 (옵션2: 여기서 파일로 기록)
#                 f.write(diary.get_diary_content())            
    
#     def read_diary(self, diary_time: datetime, diary_index: int):
#         pass
    
#     def display_diaries(self): #전체 일기를 시간순으로 출력
#         print('------------------- 전체 일기 조회 ---------------------')
#         for idx, diary in enumerate(self.__diaries):
#             print(f'{idx+1}. {diary}') # (O) __str__()호출 :

import os

class Diary:
    
    def __init__(self):
        # 파일명(일기)을 모아둘 리스트
        self.__diaries: list[str] = [] # 나중에 목록 출력도 염두
        
        # 프로그램 시작 시 기존 일기 파일을 읽어서 목록 초기화
        self.load_existing_diaries()
        
    # 일기 작성
    def add_diary(self, origin_file_name, diary_content):
        file_name = './files/' + origin_file_name
        
        # 중복 방지
        #if os.path.exists(origin_file_name): 
        if os.path.exists(file_name): 
            raise FileExistsError("이미 같은 날짜의 일기가 있습니다.")
        
        # w 모드: 없으면 생성, 있으면 삭제 후 새로 작성
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(diary_content)
    
        # 리스트에 파일명(일기제목)만 추가
        self.__diaries.append(origin_file_name)

    # 일기 목록 조회
    def view_diary_list(self):
        print()
        print("---------------- 일기 목록 ------------------")
        for idx, diary in enumerate(self.__diaries):
            print(f'{idx}. {diary}') # diary제목명만
            
        print("-------------------------------------------")
        print()

    # 특정 일기 읽기
    def view_diary(self, index):
        file_name = './files/' + self.__diaries[index]
        print("-------------------------------------------")
        print(f'[파일명 : {self.__diaries[index]}]')
        
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        print("-------------------------------------------")
        print()
        
    def load_existing_diaries(self):
        # 시작 시 files 폴더가 없으면 생성
        if not os.path.exists('./files'):
            os.makedirs('./files')
            #os.makedir('./files')
        
        
        # ./files안의 .txt 파일만 이름 기준으로 정렬
        self.__diaries = sorted(
                f for f in os.listdir(path='./files') if f.endswith('.txt') 
            )

class Menu:
    def __init__(self):
        self.__diary = Diary()
        
        
    def display(self):
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
                    try:
                        #print("일기 작성")
                        # 파일명 입력 받기
                        file_name = input('작성 날짜(YYYY-MM-DD) : ')
                        file_name += '.txt'
                        
                        # 일기 내용 입력 받기
                        diary_content = input("일기 내용")
                    
                        # 일기 작성
                        self.__diary.add_diary(file_name, diary_content)
                        
                    except FileExistsError as e:
                        print(e)         

                    except Exception as e: # 위의 구체적 예외/에러부터 넓은 범위의 예외/에러를 잡아준다.
                        print(e)
                    
                case '2':
                    #print("일기 읽기")
                    # 목록 출력 후, 인덱스 받아 해당 일기 읽기
                    self.__diary.view_diary_list()
                    
                    index = int(input("읽을 일기 목록 번호 : "))
                    
                    self.__diary.view_diary(index)
                    
                case '3':
                    print("일기앱 종료")
                    break
                case _: 
                    print("잘못 입력하셨습니다. 다시 입력해 주세요")
                
menu = Menu()
menu.display()
print(os.getcwd())