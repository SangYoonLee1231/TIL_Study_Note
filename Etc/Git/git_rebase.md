# Git - Rebase를 통해 커밋 하나로 압축하기

1. <code>git rebase -i main</code>

2. 맨 상단 커밋 하나만 남기고 나머지는 INSERT MODE로 들어가 수정하기 : <code>pick</code> -> <code>s</code> (stash)

3. 여러 커밋 메세지 하나로 합치기 (stash)

4. <code>git push origin [브랜치명] -f</code> (-f : force)

   - 원격 저장소에는 커밋들이 하나로 묶여있지 않기 때문에, 로컬 저장소에서 stash로 묶인 커밋을 푸쉬하려고 한다면 이를 어디로 push 해야 할 지 알 수 없다.

   - 따라서 깃허브에서 이러한 push를 자체적으로 막는다.

   - 그렇기에 개발자가 강제로 push를 해주어야 원격 저장소에 커밋이 반영된다. (-f이 붙는 이유)

<code></code>
