class animal:
    data = '귀여운 동물들'

    def move(self):
        print("이 동물들은 귀엽구나")

class Dog(animal):
    def name(self):
        print("개")

    def move(self):
        print("특히 우리집의 닥스훈트는 늙었지만 여전히 귀여워")

class Cat(animal):
    def name(self):
        print("고양이")

    def move(self):
        print("튀르키예에는 순하고 귀여운 고양이들이 널려 있다지.")

class Wolf(Dog, Cat):
    def move(self):
        print("늑대들도 어릴때는 강아지와 고양이 같은 시절이 있어!")

class Fox(Dog, Cat):
    def move(self):
        print("일본에 여우 섬의 여우들은 강아지와 고양이 같다구")

    def foxMethod(self):
        print("아쉽게도 한국에는 여우들을 보기가 어렵다 ㅜㅜ")

wolf = Wolf()
wolf.move()
fox = Fox()
fox.move()
fox.foxMethod()

if __name__ =="__main__":
    a = animal()
    a.move()

    print()
    d = Dog()
    c = Cat()
    w = Wolf()
    f = Fox()
    d.move()
    c.move()
    w.move()
    f.move()

    print('----다형성-------')
    ani = [d, c, w, f]
    for a in ani:
        print(id(a))
        a.move()
        print()