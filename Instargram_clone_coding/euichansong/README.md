## Instagram_Clone_Coding
### 인스타그램 클론코딩 1 - django 2 / 23.10.23 ~ 23.10.24

##### posts앱 생성/ 기본 url 경로 지정/ 기초 index 생성/ Bootstarp의 nav바 주어짐
<details>
<summary>느낀점</summary>


<!-- summary 아래 한칸 공백 두어야함 -->
- 9월달의 나는 어렵게 한거 같지만 지금 와서 보니 쉬운 문제인거 같다.
- bootstarp만 더 이해하면 좋을거 같다.
</details>

### 인스타그램 클론코딩 2 - django 6 / 23.10.25 ~ 23.10.26
##### 1을 바탕으로 models, forms 정의/ Create 만들어 게시글 생성/ Read 역할 하는 index 생성/ Delete 만들어 게시글 삭제
<details>
<summary>느낀점</summary>


<!-- summary 아래 한칸 공백 두어야함 -->
- CRD 제작하면서 교안을 안보고 치기에는 아직 힘든 단계이다. 
- 복습하는 느낌이라 좋다. 
- bootstrap을 사용하는게 아직도 힘들다 디자인적 측면에선 감각이 없는듯 하다.
- 비슷하게만 만들면 되는거 아닐까...?

</details>

### 인스타그램 클론코딩 3 - django 8 / 23.10.28 ~ 23.10.29 + 23.10.30
##### 이미지파일 업로드/ pillow 라이브러리 추가/ Update 만듬/ Create와 Update를 합치는 작업

<details>
<summary>느낀점</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
- 게시글 위에 사진 올리는게 어려워서 구글링 했다. (class="card-img-top")
- CRUD의 U를 만드는건 어렵긴 했지만 다른 실습과 형식은 비슷하기 때문에 나름 어렵지 않게 만들었다.
- 그런데 update와 create를 form으로 합쳐서 만들려고 하니 많은 오류가 있었다.
- 두번째 게시글부터 edit을 누르니 첫번째 게시글이 삭제되는 오류가 있었고 '</.form>'을 안닫아 줘서 생긴 문제였다.
- 아직 못고친 오류에는 edit을 누르면 기존의 사진은 그대로 있는데 게시글 내용은 안보인다. DB에는 있는거 보면 잘못 불러온거 같다.
- 여전히 bootstrap을 사용하는건 어렵다. edit 옆에 delete가 있어야 하는데 밑으로 갔다. 다른 실습에서는 form을 안쓰고 버튼을 써서 해결했는데 form을 쓰는 방법으로 해결할 수 있지 않을까 싶다.
- 2에서 넘어갔던 post.html 만들었고 include를 사용했다
- edit가 안되는 문제가 있었다. 원인은 form.html로 create와 update를 합치면서 경로를 create로 해줬기 때문에 수정할때마다 수정이 안되고 생성이 됬었다. 이를 해결하기 위해 url 지정 부분에 post가 존재하면 update로 연결 그렇지 않으면 create로 지정해서 문제를 해결했다. thanks to 예진
  
</details>

### 인스타그램 클론코딩 4 - django 9  / 23.10.30
##### account앱 생성/ 유저 로그인, 로그아웃, 회원 가입 기본 url 경로 지정/settings.py 한글화/ load Bootstarp을 통해 디자인 강화/ 로그인해야지만 할 수 있는것 추가
<details>
<summary>느낀점</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
- 거의 1달전에 배웠던 문법들이다
- 익숙한 코드가 거의 없고 사실상 처음 보는 느낌이 강했다.
- 특히 form.get_user()이런걸 언제 했는지 기억이 아예 없다.
- 그래도 유효성검사, html의 form 틀이 비슷한면이 있기 때문에 괜찮았다.
- 교안을 안보고 치려고 했지만 불가능
- 따라 치면서 아 이런 흐름이구나, 이 코딩이 이런 뜻이 구나 인지하고 넘어가야될것 같다
- admin.py에 등록하는게 명세가 좀 이상하다 그냥 내가 한게 맞다고 생각하자
  
</details>

### 인스타그램 클론코딩 5 - django 10 / 23.11.08 ~ 23.11.09

##### 유저 회원탈퇴(delete)/ 회원탈퇴시 한번더 물어보는 html제작/ 유저 회원정보 수정(update)/ 회원정보 원하는 것만 수정할 CustomForm 제작/ 비밀번호 변경(change_password)/ index에 로그인시 만든 버튼 각각 생성
<details>
<summary>느낀점</summary>

<!-- summary 아래 한칸 공백 두어야함 -->
- 4까지 해보니 예전에 배웠던 기억들이 돌아오는것 같다.
- 그럼에도 CustomForm을 포함한 import는 외울 필요가 없다고 해서 그냥 복사 붙여넣기 했다.
- 큰 틀은 이제 안보고 잘 짤수 있지만 세세한 디테일들은 그냥 불가능 하다. 
- instance 넣는건 생각이 아예 나지 않았다.
- 생각없이 url 복붙하다가 회원수정에 회원탈퇴로 걸어서 시간이 좀 걸렸다.

  
</details>

### 인스타그램 클론코딩 6 - db 2  
### 인스타그램 클론코딩 7 - db 3  
### 인스타그램 클론코딩 8 - db 5  
### 인스타그램 클론코딩 9 - db 6