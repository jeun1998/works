# 입력 함수 :  [사번, 이름, 기본급, 입사년도]
# from datetime import datetime >> 현재 연도 자동으로 가져올 수 있음
def inputfunc():
    datas = [
        [1, "강나루", 1500000, 2010],
        [2, "이바다", 2200000, 2018],
        [3, "박하늘", 3200000, 2005],
    ]
    return datas
datas = inputfunc()
print(datas)

def processfunc(datas):
    print("사번", "이름", "기본급", "근무년수", "근속수당", "공제액", "수령액")
    print("---------------------------------------------------------------")
    print(datas)
datas = inputfunc()
for data in datas:
    work_year = 2026 - data[3]
    if work_year <= 3:
        bonus = 150000
    elif work_year >= 9:
        bonus = 1000000
    else:
        bonus = 450000
    
    if data[2] + bonus >= 3000000:
        tax = 0.5
    elif data[2] + bonus >= 2000000:
        tax = 0.3
    else:
        tax = 0.15
    salary = (data[2] + bonus) *(1 - tax)
    minussal = data[2] + bonus - salary

    print(data[0], data[1], data[2], work_year, bonus, minussal, salary)
    
# 여기까지가 1번 문항 답

def inputfunc():
    datas = [
        "새우깡,15",
        "감자깡,20",
        "양파깡,10",
        "새우깡,30",
        "감자깡,25",
        "양파깡,40",
        "새우깡,40",
        "감자깡,10",
        "양파깡,35",
        "새우깡,50",
        "감자깡,60",
        "양파깡,20",
    ]
    return datas
datas = inputfunc()
for data in datas:
    result = data.split(",")
    print(result)
    name = result[0]
    amount = int(result[1])
    if name == "새우깡":
        price = 450
    if name == "감자깡":
        price = 300
    if name == "양파깡":
        price = 350
    total_price = amount * price
    print(name, amount, price, total_price)

    if name == "새우깡":
        s_amount = s_amount + amount
        s_money = s_money + total_price
    if name == "감자깡":
        g_amount = g_amount + amount
        g_money = g_money + total_price
    if name == "양파깡":
        y_amount = y_amount + amount
        y_money = y_money + total_price


