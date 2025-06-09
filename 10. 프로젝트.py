#!/usr/bin/env python
# coding: utf-8

# # 사각형 넓이를 구하는 클래스 완성!

# In[1]:


class Square:
    def __init__(self):
        self.square = int(input('넓이를 구하고 싶은 사각형의 숫자를 써주세요.\n 1.직사각형 2.평행사변형 3.사다리꼴 \n >>>'))

        if self.square == 1:
            print('직사각형 함수는 rect()입니다.')

        elif self.square == 2:
            print('평행사변형 함수는 par()입니다.')
        
        elif self.square == 3:
            print('사다리꼴 함수는 trape()입니다.')
        
        else:
            print('1, 2, 3 중에서 다시 입력해주세요')

    def rect(self):
        width, vertical = map(int, input('가로, 세로를 입력하세요. 예시 : 가로,세로\n >>>').split(','))
        area = width * vertical
        result = '직사각형의 넓이는 : ' + str(area)
        return result

    def par(self):
        bottom, height = map(int, input('밑변, 높이를 입력하세요. 예시 : 밑변, 높이\n >>>').split(','))
        area = bottom * height
        result = '평행사변형의 넓이는 :' + str(area)
        return result

    def trape(self):
        bottom, upper, height = map(int, input('밑변, 윗변, 높이를 입력하세요. 예시 : 밑변, 윗변, 높이\n >>>').split(','))
        area = ((bottom + upper) * height)*(1/2)
        result = '사다리꼴의 넓이는 :' + str(area)
        return result

a = Square()  # 객체 생성 & 2, 3을 각각 입력해 봅시다.


# In[2]:


# 평형사변형의 넓이
a.par()  # 3,2를 입력했을 때 넓이가 6이 나와야 합니다.


# In[3]:


# 사다리꼴의 넓이
a.trape()  # 3,2,1 을 입력했을 때 넓이가 2.5이 나와야 합니다.


# # 키오스크(Kiosk) 만들기 1

# In[31]:


class Kiosk: 
    def __init__(self):
        self.menu = ['americano', 'latte', 'mocha', 'yuza_tea', 'green_tea', 'choco_latte']
        self.price = [2000, 3000, 3000, 2500, 2500, 3000]
        self.order_menu = [] # 주문 리스트
        self.order_price = [] # 가격 리스트
        self.price_sum = 0 # 총 합계

    # 메뉴 출력 메서드    
    def menu_print(self):
        for i in range(len(self.menu)):
            print(i + 1, self.menu[i], ' : ', self.price[i], '원')

    # 주문 메서드        
    def menu_select(self):
        n = 0
        while n < 1 or n > len(self.menu):
            n = int(input("음료 번호를 입력하세요 : ")) # 음료 번호 입력
            if 1 <= n <= len(self.menu):
                self.order_price.append(self.price[n-1]) # 가격 리스트에 추가
                self.price_sum = self.price[n-1] # 합계 금액
                
            # 메뉴판에 없는 번호일 때    
            else:
                print("없는 메뉴입니다. 다시 주문해 주세요.")

                
        # 음료 온도 물어보기        
        t = 0 # 기본값을 넣어주고
        while t != 1 and t != 2: # 1이나 2를 입력할 때까지 물어보기
            t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
            if t == 1:
                self.temp = "HOT"
            elif t == 2:
                self.temp = "ICE"
            else:
                print("1과 2 중 하나를 입력하세요.\n")

        self.order_menu.append(self.temp + ' ' + self.menu[n-1]) #주문 리스트에 추가하기
        print(self.temp, self.menu[n - 1], ' : ', self.price_sum, '원') # 온도 속성을 추가한 주문 결과를 출력함

        
        # 추가 주문 또는 지불(while n != 0: 했을 경우 오류가 발생해서 변경함)
        while True: #지불을 선택하기 전까지 반복함
            print() # 줄 바꾸면서
            n = int(input("추가 주문은 음료 번호를, 지불은 0을 누르세요 : ")) # 추가 주문 또는 지불
            if n == 0: # 지불을 입력하면
                print("주문이 완료되었습니다.")
                print(self.order_menu, self.order_price) #확인을 위한 리스트를 출력함
                break
            elif 1 <= n <= len(self.menu):
                # 추가 음료의 온도
                t = 0
                while t != 1 and t != 2:
                    t = int(input("HOT 음료는 1을, ICE 음료는 2를 입력하세요 : "))
                    if t == 1:
                        self.temp = "HOT"
                    elif t == 2:
                        self.temp = "ICE"
                    else:
                        print("1과 2 중 하나를 입력하세요.\n")

                self.order_menu.append(self.temp + ' ' + self.menu[n - 1])
                self.order_price.append(self.price[n - 1])
                self.price_sum += self.price[n - 1]

                print('추가 주문 음료', self.temp, self.menu[n - 1], ':', self.price[n - 1], '원\n합계 :', self.price_sum, '원')
            else: # 없는 번호를 입력할 때
                print("없는 메뉴입니다. 다시 주문해 주세요.")
                
     #지불           
    def pay(self):
        print("\n총 결제 금액은", self.price_sum, "원입니다.")
        method = input("지불 수단을 선택하세요 (1: 현금 / 2: 카드): ").strip().lower()

        # 숫자 또는 문자열 모두 처리 가능하도록 분기
        if method == '1' or method == 'cash':
            print("직원을 호출하겠습니다.")
        elif method == '2' or method == 'card':
            print("IC칩 방향에 맞게 카드를 꽂아주세요.")
        else:
            print("다시 결제를 시도해 주세요.")
            
    # 주문서 출력
    def table(self):
        print('⟝' + '-' * 30 + '⟞')
        for _ in range(2):
            print('|' + ' ' * 31 + '|')

        for i in range(len(self.order_menu)):
            item = f"{self.order_menu[i]} : {self.order_price[i]}원"
            print('| ' + item.ljust(30) + '|')

        print('| ' + f"합계 금액 : {self.price_sum}원".ljust(30) + '|')

        for _ in range(2):
            print('|' + ' ' * 31 + '|')
        print('⟝' + '-' * 30 + '⟞')            


# In[32]:


a = Kiosk()  # 객체 생성 
a.menu_print()  # 메뉴 출력
a.menu_select()  # 주문
a.pay()  # 지불
a.table()  # 주문표 출력


# In[ ]:





# In[ ]:




