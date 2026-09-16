import random

class machine:
    def __init__(self):
        self.cupCount = 1
        machine = machine()
        machine.cupCount = int(input("몇 잔을 원하시나요?"))

class CoinIn:
    def __init__(self):
        self.coin = 0
        self.change = 0

    def culc(self, cupCount):
        need_money = cupCount * 200

        if self.coin < need_money:
            print("요금이 부족합니다.")
        else:
            self.change = self.coin - need_money
            print("커피", cupCount, "잔돈", self.change, "원")

CoinIn = CoinIn()
CoinIn.coin = 400
CoinIn.culc(1)

while True:
    coin = coin - 200
    print("남은 잔액", coin)

    if coin < 200:
        break
