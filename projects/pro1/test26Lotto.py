# 로또 번호 출력기
# 45개의 넘버링된 볼 객체 생성 후 혼합 후 6개의 공을 출력

import random

class LottoBall:
    def __init__(self, num):
        self.num = num

class LottoMachine:
    def __init__(self):
        self.ballList = []

        # for i in range(1, 46):
        # self.ballList.append(LottoBall(i))  # 클래스 포함
        random.shuffle(self.ballList)

    def selectBalls (self):
        # for a in range(45):
        #    print(self.ballList[a].num, end = ' ')

        # print('여섯 개 출력 : ', self.ballList[0:6])
        return self.ballList[0:6]
        # 볼 섞기
        
class LottoUI:
    def __init__(self):
        self.machine = LottoMachine()  # 클래스의 포함

    def playLotto(self):
        input("로또를 시작하려면 엔터키를 누르시오.")
        selBalls = self.machine.selectBalls()

if __name__ == '__main__':
    # machine = LottoMachine()
    # machine.selectBalls()

    # lot = LottoUI()
    # lot.playLotto()
    LottoUI().playLotto()