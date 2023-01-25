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

- 로컬 좌표계 -> 월드 좌표계 : <code>transform.TransformDirection()</code>

- 월드 좌표계 -> 로컬 좌표계 : <code>transform.InverseTransformDirection()</code>. <code>transform.Translate()</code>
