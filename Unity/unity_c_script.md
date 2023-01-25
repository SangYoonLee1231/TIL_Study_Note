# 유니티 (Unity) - C# 스크립트 정리

<br/>

> 참고 자료 : <a href="https://www.inflearn.com/course/%EC%9C%A0%EB%8B%88%ED%8B%B0-mmorpg-%EA%B0%9C%EB%B0%9C-part1">[C#과 유니티로 만드는 MMORPG 게임 개발 시리즈] Part1: C# 기초 프로그래밍 입문 (Rookiss 님)</a>

<br/>

## Singleton 패턴

<img src="img\unity_singleton.png">

```c#
// player.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        Manager mg = Manager.Instance;
    }

    // Update is called once per frame
    void Update()
    {

    }
}
```

```c#
// Manager.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Manager : MonoBehaviour
{
    static Manager s_instance;
    public static Manager Instance { get { Init(); return s_instance; } }

    // Start is called before the first frame update
    void Start()
    {
        Init();
    }

    // Update is called once per frame
    void Update()
    {

    }

    static void Init()
    {
        if (s_instance == null)
        {
            GameObject go = GameObject.Find("@Managers");

            if (go == null)
            {
                go = new GameObject { name = "@Managers" };
                go.AddComponent<Manager>();
            }

            DontDestroyOnLoad(go);
            s_instance = go.GetComponent<Manager>();
        }
    }
}
```

<br/><br/>

## 키보드 상하좌우 이동

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [SerializeField]
    float _speed = 10.0f;

    void Start()
    {

    }

    // GameObject (Player)
        // Transform
        // PlayerController

    void Update()
    {
        if (Input.GetKey(KeyCode.W))
            transform.position += new Vector3(0.0f, 0.0f, 1.0f) * Time.deltaTime * _speed;
        if (Input.GetKey(KeyCode.A))
            transform.position += new Vector3(-1.0f, 0.0f, 0.0f) * Time.deltaTime * _speed;
        if (Input.GetKey(KeyCode.S))
            transform.position += new Vector3(0.0f, 0.0f, -1.0f) * Time.deltaTime * _speed;
        if (Input.GetKey(KeyCode.D))
            transform.position += new Vector3(1.0f, 0.0f, 0.0f) * Time.deltaTime * _speed;
    }
}
```

<br/>

- Vector3 코드를 다음과 같이 요약해서 쓰면 가독성이 더 좋아진다.

```c#
void Update()
{
    // 월드(World) 좌표계 기준
    if (Input.GetKey(KeyCode.W))
        transform.position += Vector3.forward * Time.deltaTime * _speed;
    if (Input.GetKey(KeyCode.A))
        transform.position += Vector3.back * Time.deltaTime * _speed;
    if (Input.GetKey(KeyCode.S))
        transform.position += Vector3.left * Time.deltaTime * _speed;
    if (Input.GetKey(KeyCode.D))
        transform.position += Vector3.right * Time.deltaTime * _speed;
}
```

<br/>

- 월드 좌표계가 아닌 <strong>로컬 좌표계</strong>를 기준으로 플레이어를 움직이려면 다음과 같이 코드를 작성해주면 된다.

  - <strong>월드(World) 좌표계</strong> : 가상 세계의 변하지 않는 절대적인 좌표계 (현실세계의 동서남북)

  - <strong>로컬(Local) 좌표계</strong> : 대상(오브젝트) 기준으로 한 상대적인 좌표계

```c#
void Update()
{
    // 로컬(Local) 좌표계 기준
    if (Input.GetKey(KeyCode.W))
        transform.position += transform.TransformDirection(Vector3.forward) * Time.deltaTime * _speed;
    if (Input.GetKey(KeyCode.A))
        transform.position += transform.TransformDirection(Vector3.back) * Time.deltaTime * _speed;
    if (Input.GetKey(KeyCode.S))
        transform.position += transform.TransformDirection(Vector3.left) * Time.deltaTime * _speed;
    if (Input.GetKey(KeyCode.D))
        transform.position += transform.TransformDirection(Vector3.right) * Time.deltaTime * _speed;
}
```

```c#
void Update()
{
    // 로컬(Local) 좌표계 기준
    if (Input.GetKey(KeyCode.W))
        transform.Translate(Vector3.forward * Time.deltaTime * _speed);
    if (Input.GetKey(KeyCode.A))
        transform.Translate(Vector3.back * Time.deltaTime * _speed);
    if (Input.GetKey(KeyCode.S))
        transform.Translate(Vector3.left * Time.deltaTime * _speed);
    if (Input.GetKey(KeyCode.D))
        transform.Translate(Vector3.right * Time.deltaTime * _speed);
}
```

<br/>

- <strong>로컬 좌표계(기준)</strong>를 월드 좌표계로 변한하여 계산 : <code>transform.TransformDirection()</code>, <code>transform.Translate()</code>

- <strong>월드 좌표계(기준)</strong>를 로컬 좌표계로 변한하여 계산 : <code>transform.InverseTransformDirection()</code>

<br/><br/>

## 벡터 (Vector) 구현하기

```c#
struct MyVector
{
    // 벡터의 x, y, z값
    public float x;
    public float y;
    public float z;

    // 벡터 크기 계산
    public float magnitude { get { return Mathf.Sqrt(x*x + y*y + z*z); } }
    // 단위 벡터 반환
    public MyVector normalized
    {
        get { return new MyVector(x / magnitude, y / magnitude, z / magnitude); }
    }

    // 벡터 초기 설정 (생성자)
    public MyVector(float x, float y, float z)
    {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // 벡터 연산 정의
    public static MyVector operator+(MyVector a, MyVector b)
    {
        return new MyVector(a.x + b.x, a.y + b.y, a.z + b.z);
    }

    public static MyVector operator -(MyVector a, MyVector b)
    {
        return new MyVector(a.x - b.x, a.y - b.y, a.z - b.z);
    }

    public static MyVector operator *(MyVector a, float d)
    {
        return new MyVector(a.x * d, a.y * d, a.z * d);
    }
}

public class PlayerController : MonoBehaviour
{
    [SerializeField]
    float _speed = 10.0f;

    void Start()
    {
        MyVector from = new MyVector(5.0f, 0.0f, 0.0f);
        MyVector to = new MyVector(10.0f, 0.0f, 0.0f);
        MyVector dir = to - from; // 방향 벡터 = (5.0f, 0.0f, 0.0f)
        dir = dir.normalized;

        MyVector newPos = from + dir * _speed;
    }

    void Update()
    {
        // ..(생략)..
    }
}
```

<br/><br/>

## 오브젝트 (대상) 회전시키기, 특정 방향으로 바라보도록 하기

- 해당 내용 관련 Unity 공식 문서 (유용함!) 👉🏻 <a href="https://docs.unity3d.com/kr/2021.3/Manual/QuaternionAndEulerRotationsInUnity.html">바로가기</a>

```c#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [SerializeField]
    float _speed = 10.0f;

    void Start()
    {

    }

    float _yAngle = 0.0f;

    void Update()
    {
        _yAngle += Time.deltaTime * 30.0f;

        // < 오브젝트 (대상) 회전시키기 >

        // 회전 방법 1. 절대 회전값
        // transform.eulerAngles = new Vector3(0.0f, _yAngle, 0.0f);

        // 회전 방법 2. +- delta
        // transform.Rotate(new Vector3(0.0f, Time.deltaTime * 100.0f, 0.0f));

        // 회전 방법 3. Quaternion값 지정
        // transform.rotation = Quaternion.Euler(new Vector3(0.0f, _yAngle, 0.0f));


        // < 오브젝트 (대상) 특정 방향으로 바라보도록 하기 >
        if (Input.GetKey(KeyCode.W))
        {
            // LookRotation 함수 : 대상을 원하는 방향으로 바라보도록 rotation값을 조정하는 함수
            // LookRotation은 절대 좌표계 기준으로 동작한다.
            transform.rotation = Quaternion.LookRotation(Vector3.forward);
        }

        if (Input.GetKey(KeyCode.S))
        {
            transform.rotation = Quaternion.LookRotation(Vector3.back);
        }
        if (Input.GetKey(KeyCode.A))
        {
            transform.rotation = Quaternion.LookRotation(Vector3.left);
        }
        if (Input.GetKey(KeyCode.D))
        {
            transform.rotation = Quaternion.LookRotation(Vector3.right);
        }
    }
}
```

<br/>

- 만일 대상의 방향 전환을 좀 더 자연스럽게 하려면 <strong><code>Quaternion.Slerp()</code> 함수</strong>를 이용해주면 된다.

  - <code>Quaternion.Slerp()</code> 함수 관련 내용 👉🏻 <a href="https://docs.unity3d.com/kr/2021.3/ScriptReference/Quaternion.Slerp.html">바로가기</a>

```c#
void Update()
{
    _yAngle += Time.deltaTime * 30.0f;

    if (Input.GetKey(KeyCode.W))
    {
        // LookRotation 함수 : 대상을 원하는 방향으로 바라보도록 rotation값을 조정하는 함수
        // LookRotation은 절대 좌표계 기준으로 동작한다.
        transform.rotation = Quaternion.Slerp(transform.rotation, Quaternion.LookRotation(Vector3.forward), 0.1f);
        transform.position += Vector3.forward * Time.deltaTime * _speed;
    }

    if (Input.GetKey(KeyCode.S))
    {
        transform.rotation = Quaternion.Slerp(transform.rotation, Quaternion.LookRotation(Vector3.back), 0.1f);
        transform.position += Vector3.back * Time.deltaTime * _speed;
    }
    if (Input.GetKey(KeyCode.A))
    {
        transform.rotation = Quaternion.Slerp(transform.rotation, Quaternion.LookRotation(Vector3.left), 0.1f);
        transform.position += Vector3.left * Time.deltaTime * _speed;
    }
    if (Input.GetKey(KeyCode.D))
    {
        transform.rotation = Quaternion.Slerp(transform.rotation, Quaternion.LookRotation(Vector3.right), 0.1f);
        transform.position += Vector3.right * Time.deltaTime * _speed;
    }
}
```

<br/>
