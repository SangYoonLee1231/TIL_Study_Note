DayoftheWeek = ['일','월','화','수','목','금','토']

yy1, yy2 = input().split()
yy1 = int(yy1)
yy2 = int(yy2)

yy1day = input()
LPcount = 0     #주어진 해 중 윤년 카운트, 있을 경우 마지막 셈에서 카운트 1개당 1씩 추가

for k in range(yy1, yy2+1):      #윤년은 4의 배수이면서 100의 배수가 아니거나 400의 배수일 때 이다
    if (k % 4 == 0) & (k % 100 != 0):
        LPcount += 1
    elif k % 400 == 0:
        LPcount += 1



for i in range(7):     #주어진 요일을 숫자화한다(0~6)
    if yy1day == DayoftheWeek[i]:
        yy1num = i

term = 0

for j in range(yy2 - yy1):     #주어진 두 수의 차를 횟수로 365를 더해준다
    term += 365


remainder = term % 7     #365를 7로 나누어 나머지를 구한다

final = yy1num + remainder + LPcount     #나머지와 처음 요일, 그리고 윤년의 카운트만큼 더하여 요일을 구한다.

if final > 7:     #만약 최종 final값이 윤년 등의 사유로 7이 넘는다면 그 나머지를 구하여 요일을 구한다.
   temp = final
   final = temp % 7

print(DayoftheWeek[final])