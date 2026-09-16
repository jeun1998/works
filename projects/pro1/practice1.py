
# 문1) 1 ~ 100 사이의 정수 중 3의 배수이나 2의 배수가 아닌 수를 출력하고, 합을 출력
print()
for number in range(1, 100):
    if number % 2 == 0 or number % 3 == 0:
        continue
    else:
        print(number)

i=0
total=0

while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        print(i, end = ' ')
        total += i
    i += 1

print(f"합은 {total}")

# 문2) 2 ~ 5 까지의 구구단 출력
print()
for number in range(1, 6):
    if number % 3 == 0:
        print(number)
    elif number % 3 == 1:
        continue
    else:
        continue

dan = 2
while dan <= 5:
    j = 1
    while j <= 9:
        print(f'{dan} * {j} = {dan*j}', end =' ')
        j += 1
    print()
    dan += 1


# 문3) 1 ~ 100 사이의 정수 중 “짝수는 더하고, 홀수는 빼서” 최종 결과 출력
print()
result = 0
for number in range(1, 100):
    if number % 2 == 0:
        result += number
    else:
        result -= number
print(result)

i = 1
sum = 0
while i <= 100:
    if i%2==0:
        sum=sum+i
    else:
        sum=sum-i
    i+=1
print(f'최종결과 = {sum}')




# 문4) -1, 3, -5, 7, -9, 11 ~ 99 까지의 모두에 대한 합을 출력

print()
result = 0
for a in range(0, 50):
    number = 2*a + 1
    if a % 2 == 0:
        result -= number
    else:
        result += number
print(result)

n = 1
sign = -1
total = 0

while n < 100:
    value = sign * n
    total += value
    sign *= -1
    n += 2
print(total)

i = -1
sum = 0
while abs(i) <= 99:
    sum=sum+i
    if i<0:
        i-=2
    else:
        i+=2
    i*=-1

print(sum)




# 문5) 1 ~ 100 사이의 숫자 중 각 자리 수의 합이 10 이상인 수만 출력

# 예) 29 → 2 + 9 = 11 (출력)

print()
for a in range(0, 10):
    for b in range(0, 10):
        number = 10*a + b
        if a + b >= 10:
            print(number)
        else:
            continue

num = 1
while num <= 100:
    temp = num
    digit_sum = 0

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    if digit_sum >= 10:
        print(num, end = ' ')
    
    num += 1

print()


# 문6) 1부터 시작해서 누적합이 처음으로 1000을 넘는 순간의 숫자와 그때의 합을 출력

# 힌트: 언제 멈출지 미리 모름 → while 적합

number = 1
result = 0
while result <= 1000:
    result += number
    number += 1
print(number - 1)
print(result)

s = 0
i = 1
while s < 1000:
    s += i
    i += 1

print("수자:", i-1)
print("합:", s)



# 문7) 구구단을 출력하되 결과가 30을 넘으면 해당 단 중단하고 다음 단으로 이동

dan = 2
while dan <= 9:
    i = 1
    while i <= 9:
        result = dan * i
        if result > 30:
            break
        print(dan, "*", i, "=", result)
        i += 1
    print()
    dan += 1



# 문8) 1 ~ 1000 사이의 소수(1보다 크며 1과 자신의 수 이외에는 나눌 수 없는 수)와 그 갯수를 출력
# 힌트: 이 문제는 반복이 두 단계다. 2부터 1000까지 하나씩 검사한다. 각 숫자마다 소수인지 확인한다.

num = 2
count = 0
while num <= 1000:
    i = 2
    is_prime = True
    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num, end = ' ')
        count += 1
    num += 1