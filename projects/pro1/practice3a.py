class CoinIn():
    def __init__(self):
        self.cupPrice = 200

    def calc(self, coin, cupCount):
        totalPrice = self.cupPrice * cupCount

        if coin < totalPrice:
            return None
        else:
            change = coin - totalPrice
            return cupCount, change

class Machine():
    def __init__(self):
        self.CoinIn = CoinIn()

    def showData(self):
        while True:
            coin = int(input("동전을 입력하세요:"))
            cup = int(input("몇잔을 원하세요"))
            cupCount, change = self.CoinIn.calc(coin, cup)

            if cupCount is None:
                print("요금이 부족합니다.")
            else:
                print(f"커피 {cupCount}잔과 잔동 {change}원")
            # 계속 실행 여부 판단
            answer = input("계속할까요?(y/n) : ")
            if answer.lower() == 'n':
                print("종료합니다.")
                break

if __name__ == "__main__":
    Machine().showData()