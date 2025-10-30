import os

class Diary:
    
    def __init__(self):
        # 파일명(일기)을 모아둘 리스트
        self.__diaries: list[str] = []
        
        # 프로그램 시작 시 기존 일기 파일을 읽어서 목록 초기화
        self.load_existing_diares()
    
    # 일기 작성    
    def add_diary(self, origin_file_name, diary_content):
        file_name = './files/' + origin_file_name
        
        # 중복 방지
        if os.path.exists(file_name):
            raise FileExistsError("이미 같은 날짜의 일기가 있습니다.")
            

        # w : 없으면 생성, 있으면 삭제 후 새로 작성
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(diary_content)
            
        # 리스트에 파일명(일기제목)만 추가
        self.__diaries.append(origin_file_name)
        
    # 일기 목록 조회
    def view_diary_list(self):
        print()
        print("-------------- 일기 목록 --------------")
        for i, diary in enumerate(self.__diaries) :
            print(f'{i}. {diary}')
        print('--------------------------------------')
        print()
        
    # 일기 읽기
    def view_diary(self, index):
        file_name = './files/' + self.__diaries[index]
        print()
        print("--------------------------------------")
        print(f'[파일명 : {self.__diaries[index]}]')
        
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content)
        print('--------------------------------------')
        print()
        
    def load_existing_diares(self):
        # 시작 시 files 폴더가 없으면 생성
        if not os.path.exists('./files'):
            os.makedirs('./files')
        
        # ./files안의 .txt 파일만 이름 기준으로 정렬
        self.__diaries = sorted(
          f  for f in os.listdir('./files') if f.endswith('.txt')
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
                    try :
                        # 파일명 입력 받기
                        file_name = input('작성 날짜(YYYY-MM-DD) : ')
                        file_name += '.txt'
                        
                        # 일기 내용 입력 받기
                        diary_content = input("일기 내용 : ")
                    
                        # 일기 작성
                        self.__diary.add_diary(file_name, diary_content)

                    except FileExistsError as e :
                        print(e)
                        
                    except Exception as e :
                        print(e)
                    
                case '2':
                    # 목록 출력 후 인덱스 받아 해당 일기 읽기
                    self.__diary.view_diary_list()
                    
                    index = int(input("읽을 일기 목록 번호 : "))
                    
                    self.__diary.view_diary(index)
                
                case '3':
                    print('일기앱 종료')
                    break
                
                case _:
                    print("잘못 입력하셨습니다. 다시 입력해주세요.")
                    
menu = Menu()
menu.display()
    