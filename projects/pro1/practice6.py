from abc import ABC, abstractmethod

class Employee(ABC):
    irum = ""
    nai = ""
    def __init__(self, irum, nai):
        self.irum = irum
        self.nai = nai

    @abstractmethod
    def abstract_pay(self):
        pass

    @abstractmethod
    def abstract_dataprint(self):
        pass

    def irumnai(self):
        print("이름 : ", self.irum, "나이 : "  , self.nai)

class Temporary(Employee):
    ilsu = ""
    ildang = ""

    def __init__(self, irumnai, ilsu, ildang):
        irum, nai = irumnai
        super().__init__(irum, nai)
        self.ilsu = ilsu
        self.ildang = ildang
        monthly_pay = ilsu + ildang

    def abstract_pay(self):
        return self.ilsu * self.ildang

    def abstract_dataprint(self):
        print('이름 : ', self.irum,
            '나이 : ', self.nai,
            '월급 : ', self.abstract_pay())


class Regular(Employee):
    salary = ""

    def __init__(self, irumnai, salary):
        irum, nai = irumnai
        super().__init__(irum, nai)
        self.salary = salary

    def abstract_pay(self):
        return self.salary

    def abstract_dataprint(self):
        print('이름 : ', self.irum,
            '나이 : ', self.nai,
            '급여 : ', self.abstract_pay())
        
class Salesman(Regular):
    sales = ""
    commision = ""

    def __init__(self, irumnai, salary, sales, commission):
        super().__init__(irumnai, salary)

        self.sales = sales
        self.commission = commission

    def abstract_pay(self):
        return self.salary + self.sales * self.commission

    def abstract_dataprint(self):
        print('이름 : ', self.irum,
            '나이 : ', self.nai,
            '수령액 : ', self.abstract_pay())



t = Temporary(("홍길동", 25), 20, 15000)
r = Regular(("한국인", 27), 3500000)
s = Salesman(("손오공", 29), 1200000, 5000000, 0.25)

t.abstract_dataprint()
r.abstract_dataprint()
s.abstract_dataprint()