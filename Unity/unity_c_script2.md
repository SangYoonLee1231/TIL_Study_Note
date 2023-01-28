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
