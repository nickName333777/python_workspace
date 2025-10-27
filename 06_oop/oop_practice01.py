"""
요구사항

===== 위시리스트 관리 프로그램 =====
1. 상품 추가
2. 상품 삭제
3. 위시리스트 확인
4. 프로그램 종료
==========================
메뉴를 선택하세요:


* 사용자는 위 메뉴를 통해 본인의 위시리스트를 관리할 수 있습니다. (메뉴에서 직접 Product 접근못하게 한다)
* 위 메뉴는 메뉴객체에 의해 제공되어야 합니다.
* 사용자 위시리스트 상품은 상품명, 가격 정보를 가질 수 있습니다.
* 위시리스트는 여러개의 상품을 관리할 수 있습니다. (list타입)
* `1번 상품추가`를 선택하면, 사용자에게 상품명과 가격을 각각 입력 받고, 상품 객체를 생성합니다. 이 상품 객체는 위시리스트에서 관리되어야 합니다.
* `2번 상품삭제`를 선택하면, 위시리스트에서 저장된 상품 인덱스를 추가로 입력받아 해당 상품을 삭제할 수 있습니다.
* `3번 위시리스트확인`을 선택하면 현재 위시리스트에 저장된 상품 목록을 출력합니다.
* `4번 프로그램 종료`를 선택하면 프로그램을 종료합니다.


아래 다이어그램을 참조할 수 있습니다.




객체 다이어그램 (Menu → WishList → Product)


+--------------+        +--------------------+        +-------------------+
|     Menu     |        |   WishList         |        |    Product        |
+--------------+        +--------------------+        +-------------------+
| - __wishlist | 1 ---->| - __products       |<> ---->| - __name: str     |
+--------------+        +--------------------+        | - __price: int    |
| + display()  |        | + add_product()    |        +-------------------+
|              |        | + remove_product() |
|              |        | + print_products() |
+--------------+        +--------------------+




"""
class Product:
    def __init__(self, name: str, price: int):
        self.__name = name
        self.__price = price
        
    def get_product_name(self):
        return self.__name
    
    def get_product_price(self):
        return self.__price
    
    def __str__(self): # magic method (파이썬이 알아서 호출해준다) (Java의 ToString() overriding 함수와 유사한것으로 봐라)
        #return "test"
        return f"Product{{name : {self.__name}, price : {self.__price} }}" # Product{name : 마이구미, price : 1000 }
    
##############################################################
class WishList:
    def __init__(self):
        self.__products: list[Product] = [] # 상품을 담는 리스트, WishList객체의 속성
        
    def add_product(self, product: Product):
        self.__products.append(product)
        
    def print_products(self):
        print()
        print('+'*15)
        for idx, product in enumerate(self.__products):
            #print(f'인덱스: {idx}, name: {product.get_product_name()}, price: {product.get_product_price()}') # Product의 private 속성에 getter써서 접근
            print(f'{idx} - {product}')
        print('+'*15)
        
    def drop_product(self, idx2del):
        return self.__products.pop(idx2del).get_product_name()    
        
    def remove_product(self, index:int):
        return self.__products.pop(index) # 특정 인덱스 값 제거


#############################################################
class Menu:
    def __init__(self) :
        self.__wishlist: WishList = WishList()
        
    def display(self):
        menu = """
===== 위시리스트 관리 프로그램 =====
1. 상품 추가
2. 상품 삭제
3. 위시리스트 확인
4. 프로그램 종료
==========================
메뉴를 선택하세요: """

        while True:
            choice = input(menu)
            match choice:
                case '1':
                    name = input("상품명 입력: ")
                    price = int(input("상품가격 입력: "))
                    product = Product(name, price)
                    
                    
                    self.__wishlist.add_product(product)
                    print("상품이 추가되었습니다.")
                    self.__wishlist.print_products()
                    
                case '2':
                    self.__wishlist.print_products() # 인덱스번호 보여주고, 인덱스번호 입력받자
                    idx2del = int(input("삭제할 상품의 인덱스를 입력해주세요 : "))
                    removed = self.__wishlist.remove_product(idx2del)
                    print("removed : ", removed) # product 객체 제거됨
                    if removed : 
                        print("상품이 삭제되었습니다.")

                    #product2del = self.__wishlist.drop_product(idx2del)
                    #print(f"{product2del}이 삭제되었습니다.")
                    #self.__wishlist.print_products()
                    
                case '3': # 제대로 추가되었는지 확인
                    self.__wishlist.print_products()
                    
                case '4':
                    print("이용해 주셔서 감사합니다.")
                    break    
                case _:
                    print("잘못 입력하셨습니다.")
                    

##################################################################

menu = Menu()
menu.display()

#prod = Product("마이구미", 1000)
#print(prod) # <__main__.Product object at 0x00000198E8516E40> (=> __str__() 매직메소드 정의 안해주면면, 기본값으로이렇게 출력됨)