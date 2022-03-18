# C언어

<br/>

### 목차

- <a href="https://github.com/SangYoonLee1231/TIL/blob/main/ComputerSystem/CS50_2019/c.md#%ED%95%98%EB%93%9C%EC%9B%A8%EC%96%B4%EC%9D%98-%ED%95%9C%EA%B3%84">하드웨어의 한계</a>

<br/>

## 하드웨어의 한계

### RAM (혹은 메모리)

- 모든 프로그램이 실행 중 저장되는 곳

- 모든 파일이 열려있는 동안 저장되는 곳

- 컴퓨터가 여러 일을 한 번에 할 때, 정보를 기억하기 위해 사용한다.

<br/>

- 그러나, RAM은 어디까지나 하드웨어(HW)이므로, 성능에 <strong>한계</strong>가 존재한다.

- 컴퓨터의 메모리는 <strong>유한</strong>하다.

- 즉, <strong>컴퓨터가 할 수 있는 일은 근본적인 한계가 있다.</strong>

  - 저장공간의 한계

  - 연산의 한계

<br/>

- 예시

  ```c
  int main(void)

  {
      float x;
      float y;

      printf("x: ");
      scanf("%f", &x);

      printf("y: ");
      scanf("%f", &y);

      printf("x / y = %.50f\n", x / y);

      return 0;
  }
  ```

  ```
  x : 1
  y : 50
  x / y = 0.10000000149011611938476562500000000000000000000000
  ```

  - 정확한 출력 결과는 0.1이 되어야 하나, float에서 저장 가능한 비트의 수가 유한하므로 이런 부정확한 결과가 나오는 것이다.

<br/>

- <strong>정수 오버플로우(Integer Overflow)</strong>도 컴퓨터의 한계를 잘 보여주는 또 다른 예시이다.

- 이런 문제는 실생활에도 종종 나타나므로, 다루고자 하는 데이터 값의 범위에 유의해서 프로그램을 작성하는 것이 중요하다.
