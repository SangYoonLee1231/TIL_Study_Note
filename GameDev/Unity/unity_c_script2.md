# 유니티 (Unity) - C# 스크립트 정리 2

<br/>

> 참고 자료 : <a href="https://www.inflearn.com/course/%EC%9C%A0%EB%8B%88%ED%8B%B0-mmorpg-%EA%B0%9C%EB%B0%9C-part1">[C#과 유니티로 만드는 MMORPG 게임 개발 시리즈] Part1: C# 기초 프로그래밍 입문 (Rookiss님)</a>

<br/>

### 목차

- <a href="">스크립트를 통해 Prefab 생성 + 프로젝트 파일과 연결</a>
<!-- - <a href=""></a> -->

<br/><br/>

## 스크립트를 통해 Prefab 생성 + 프로젝트 파일과 연결

<img src="img\unity_prefab.png">

```c#
// PrefabTest.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PrefabTest : MonoBehaviour
{
    GameObject prefab;
    GameObject tank;

    void Start()
    {
        prefab = Resources.Load<GameObject>("Prefabs/Tank");
        tank = Instantiate(prefab);

        Destroy(tank, 3.0f);
    }
}
```

<br/>

- 관심사의 분리 (<code>ResourceManager</code> 생성)

```c#
// ResourceManager.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ResourceManager
{
    public T Load<T>(string path) where T : Object
    {
        return Resources.Load<T>(path);
    }

    public GameObject Instantiate(string path, Transform parent = null)
    {
        GameObject prefab = Load<GameObject>($"Prefabs/{path}");
        if (prefab == null)
        {
            Debug.Log($"Failed to load prefab : {path}");
            return null;
        }

        return Object.Instantiate(prefab, parent);
    }

    public void Destory(GameObject go)
    {
        if (go = null)
            return;

        Object.Destroy(go);
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
    static Manager Instance { get { Init(); return s_instance; } }

    InputManager _input = new InputManager();
    ResourceManager _resource = new ResourceManager();
    public static InputManager Input { get { return Instance._input; } }
    public static ResourceManager Resource { get { return Instance._resource; } }

    // Start is called before the first frame update
    void Start()
    {
        Init();
    }

    // Update is called once per frame
    void Update()
    {
        _input.OnUpdate();
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

```c#
// PrefabTest.cs
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PrefabTest : MonoBehaviour
{
    GameObject prefab;
    GameObject tank;

    void Start()
    {
        prefab = Manager.Resource.Instantiate("Tank");

        // Manager.Resource.Destory(tank);

        Destroy(tank, 3.0f);
    }
}
```

<br/><br/>

##
