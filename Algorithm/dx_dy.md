# dx, dy 테크닉

* (x, y)에서 시작해 한 칸 이동하는 문제가 주어졌다고 하자. 주어지는 숫자에 따라 이동 방향이 달라진다.

    * 숫자 0이 주어지면 동쪽

    * 숫자 1이 주어지면 남쪽

    * 숫자 2가 주어지면 서쪽

    * 숫자 3이 주어지면 북쪽

<br/>

* 먼저, 조건문을 써서 가장 단순하게 풀어보자.

```python
dir_num = 0  # 방향 = 동쪽
x, y = 0, 0  # 현재 위치 = (0, 0)

if dir_num == 0:    nx, ny = x + 1, y    # 동쪽
elif dir_num == 1:    nx, ny = x, y - 1    # 남쪽
elif: dir_num == 2:    nx, ny = x - 1, y    # 서쪽
elif: dir_num == 3:    nx, ny = x, y + 1    # 북쪽
else:   pass
```

<br/>

* 하지만 위의 코드는 (조건문에서) 반복되는 부분이 많다.

* 위와 같이 특정 방향(주로 상하좌우)으로 이동하는 문제를 더 잘 구현하기 위해, <code>dx, dy 테크닉</code>을 사용할 수 있다.

<img src="img/dx_dy1.png" width="350px">

```python
dir_num = 0
x, y = 0, 0

dxs = [1, 0, -1, 0]
dys = [0, -1, -0, 1]

nx, ny = x + dxs[dir_num], dys[dir_num]
```