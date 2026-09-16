# 냉장고 객체에 음식 개체 저장하기

class Fridge:   # 음식 객체 (냉장고에 보관될 클래스)
    isOpened = False
    foods= []

    def open(self):
        self.isOpened = True
        print('냉장고 문이 열림')

    def close(self):
        self.isOpened = False
        print('냉장고 문 닫기')

    def foodList(self):
        for f in self.foods:
            print(f" - {f.name} {f.expiry_date}")  # 냉장고 문이 열린 경우 음식물 확인 메소드

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print(f"냉장고에 {thing.name} 넣음")
            self.foodList()
        else:
            print("냉장고 문이 닫혀있음")


class FoodData:
    def __init__(self, name, expiry_date):
        self.name = name
        self.expiry_date = expiry_date

f0bj = Fridge()

apple = FoodData("사과", "2026-9-6")
f0bj.put(apple)
f0bj.open()
f0bj.put(apple)
f0bj.close()
print()
cola = FoodData('콜라', '2027-05-05')
f0bj.open()
f0bj.put(cola)
f0bj.close()