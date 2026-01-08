# R3call
> __R3call avoids the concept of failure.<br>
> There is no "retry".<br>
> Only recall.<br>__

## What is R3call?
- R3call is a lightweight word recall tool

## Motivation
- Atcoder 문제를 풀면서 다양한 일본어 단어가 등장.
- 뜻을 아예 모르거나, 읽지조차 못하는 단어도 있었고, 뜻을 모호하게 알고있는 단어도 존재.
- 별도의 시간을 내어 암기에 집중하기엔 비효율적이라 생각.
- 즉 수동적 암기나 일반적인 단어장이 아닌, 자주 접하면서 자연스럽게 암기할 수 있는 아이디어를 구상.

## Idea
1. PC 실행 시 프로그램 자동실행.(db내 단어가 2개 이하일 때는 실행하지 않음.)
2. 프로그램이 실행되면 db내 일본어 단어를 3개 랜덤추출해 하나씩 따로 등장시킴.(뜻, 발음 x)
3. 각 어휘를 보고 뜻(의미)를 암기하고 있다면 pass, 의미를 떠올리지 못했을 때 recall 실행.
4. pass가 실행된다면 db내에서 +1 count. 만약 count가 +3이 된다면 완전히 암기한 단어라고 판단, db에서 삭제.
5. recall이 실행된다면 count를 0set.
6. 새롭게 추가하고 싶은 단어는 언제든지 추가 가능.

## Design
- 의미/발음 미표시 $\rightarrow$ 능동 회상 유도
- pass/recall $\rightarrow$ 완전 암기 기준 정의
- count = +3 $\rightarrow$ DB 자동 삭제

## Tech Stack
- Language : Python
- UI : PySide
- Database : SQLite

## Sample word
| Word | Pronunciation | Meaning|
| :--- | :---: | :---: |
|うっかり|うっかり|不注意で（ぼうっとしていて）気づかないさま。|
|試みる|こころみる|（実際に）どうなるかやってみる。ためしにやってみる。ためす|
|狭義|きょうぎ|同じ言葉（表現）が指す意味の範囲に広さの違いがある時、狭い方の意味。|
|矩形|くけい|すべての角が直角の、四辺形。長方形。|
|式典|しきてん|（大がかりな）儀式。|
|牡蠣|かき|Oyster(eng) 굴(kr)|
|間隔|かんかく|空間に並んだり時間的に相継いだりする事柄の間の隔たり（の大きさ）。|
|跨ぐ|またぐ|またをひらいて立つ。またをひらいて越える。|
|鶴橋|つるはし|堅い土地をほりおこすのに使う鉄製の道具。|
|堅い|かたい|たやすくは崩れないほど確かだ。心や体の状態に、ゆとりや遊びがない。|

## Roadmap
- [x] Skeleton UI
- [x] Initial db
- [x] Button function
- [ ] main util
- [ ] side util
- [ ] n차 수정 및 보완

## To do idea
- [ ] db insert 시 "INSERT"를 사용(NOT "INSERT OR IGNORE").IntegrityError 발생(UNIQUE 위반) 시 동일한 word db를 user에게 공개 후, 수정모드로 진입.