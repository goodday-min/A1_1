📌 과제가 뭐냐면...
"프롬프트를 저장하고 찾을 수 있는 프로그램을 만들어라" 입니다.

예시) 지금은...
- ChatGPT 프롬프트를 메모장에 저장
- 필요할 때 못 찾아서 다시 씀 😭

만들고 나면...
  - 프로그램 실행
  - 번호 입력으로 추가/검색/즐겨찾기
  - 깔끔하게 관리 😊

✅ VSCode 설치  
✅ Python 설치  
✅ Git 설치 & 설정  
✅ GitHub 저장소 생성  
✅ git init (로컬 저장소 생성)  
✅ git add (파일 추가)  
✅ git commit (로컬 저장)  
✅ git pull (GitHub → 내 컴퓨터)  
✅ git push (내 컴퓨터 → GitHub)  


---  
📦 1. 설치 (GUI 작업)

      VSCode    → https://code.visualstudio.com/
      Python    → https://www.python.org/
      Git       → https://git-scm.com/  
*설치 시 Python은 "Add to PATH" 체크 필수!*

⚙️ 2. Git 최초 설정 (딱 한 번만) : 내가 누구인지 Git에게 알려주는 작업

      git config --global user.name "내이름"
      git config --global user.email "내이메일@gmail.com"

🏠 3. 로컬 저장소 생성

      cd 내프로젝트폴더    # 폴더로 이동
      git init             # Git 저장소 시작 (.git 폴더 생성)

🔗 4. GitHub 저장소 연결 : 로컬 ↔ GitHub 연결 다리 만들기

      git remote add origin https://github.com/내아이디/저장소이름.git

📸 5. 파일 저장 (add → commit)

      git add .                        # 변경된 모든 파일 스테이징
      git commit -m "첫 번째 커밋"     # 로컬에 저장 (스냅샷 찍기)
      
      작업흐름:
      내 파일 수정 → git add → git commit → (로컬 저장 완료!)

🔄 6. GitHub와 동기화

      # GitHub → 내 컴퓨터 (받아오기)
      git pull origin main
      
      # 내 컴퓨터 → GitHub (올리기)
      git push origin main

🗺️ 전체 흐름 한눈에 보기

      [내 컴퓨터]                    [GitHub]
         │                              │
         │  git add .                   │
         │  git commit -m "메시지"      │
         │                              │
         │  ──── git push ────────────► │
         │  ◄─── git pull ──────────── │

✅ 자주 쓰는 상태 확인 명령어 (보너스!)

        git status    # 현재 상태 확인
        git log       # 커밋 기록 보기


💡 핵심 루틴 기억하기!
수정 → add → commit → push 이 4단계가 앞으로 매일 하는 작업이에요!

--------------------------------------------------

1단계: 개발환경 설정  
2단계: Git/GitHub 설정 (저장소 설정)  
3단계: 프로그램 코드 작성  
4단계: 기능별 커밋 & 브랜치 작업  
5단계: README 작성 & 최종 제출  



### 1단계: 개발환경 설정  

    Python 버전 확인  
          python --version  
          # 또는  
          python3 --version  
          # Python 3.10 이상이어야 함  
    Git 초기 설정  
          # 버전 확인  
          git --version  
          
          # 사용자 정보 설정  
          git config --global user.name "홍길동"  
          git config --global user.email "your@email.com"  
          
          # 기본 브랜치를 main으로 설정  
          git config --global init.defaultBranch main  

### 2단계: Git/GitHub 설정 (저장소 설정)  
-----
  #### 프로젝트 폴더 생성
  mkdir prompt-manager
  cd prompt-manager

  #### 프로젝트 파일 생성

  
  #### Git 초기화
  git init
  
  #### .gitignore 생성
  echo "__pycache__/" > .gitignore
  echo "*.pyc" >> .gitignore
  echo ".DS_Store" >> .gitignore

------------




- GitHub 저장소 생성  
- 로컬 폴더 Git 초기화 & GitHub 연결  
         로컬 폴더 만들기  
         Git 초기화  
         GitHub 연결  
         
      - 첫 커밋 & 푸시  
          # 프로젝트 폴더 생성  
          mkdir A1_1  
          cd A1_1  
          
          # Git 초기화  
          git init  

  ### 3단계. GitHub 저장소 연결  
        
  git remote add origin https://github.com/본인아이디/A1_1.git
  *origin	GitHub 주소의 별명 (관례적 이름)*
  
        git remote add origin https://github.com/goodday-min/A1_1.git
                 │      │        │
                 │      │        └── 실제 GitHub 주소
                 │      └── 별명 (내가 마음대로 정할 수 있어요!)
                 └── "원격 저장소를 추가해줘"  
                 
        1단계 - GitHub 연결 : git remote add origin https://github.com/goodday-min/A1_1.git
        2단계 - 연결 확인 :   git remote -v
                              -> origin  https://github.com/goodday-min/A1_1.git (fetch)
                              -> origin  https://github.com/goodday-min/A1_1.git (push)

        
        파일 추가
          git add .
                📁 내 폴더 안의 모든 파일들을
                        ↓
                📦 "커밋 준비 상태"로 올려놓은 것

          
        첫 커밋
          >git commit -m "first commit: 프롬프트 관리 프로그램 초기 버전"
          
          >git commit -m "first commit"
              │       │       │
              │       │       └── 메모 내용 (내가 쓰고 싶은 말)
              │       └── message의 약자 (메모를 쓰겠다는 신호)
              └── "지금 상태를 저장해줘"
        
            # -m 있을 때 (한 줄로 바로 작성) : git commit -m "first commit"
            # -m 없을 때 (편집기가 열려버림 😱) : git commit
            그냥 항상 -m 쓰세요 😄

            >git commit -m "first commit
            -> On branch main (지금 main 브랜치에 있어요)
            -> Initial commit (이미 커밋이 되어있어요)
            -> nothing to commit (create/copy files and use "git add" to track) (커밋할 게 없어요 (이미 다 저장됨))

            >ls (지금 파일 상태 확인)  
            -> (아무것도 안 나옴) <----폴더가 비어 있음 (파일이 없음)

            파일 먼저 만들기 
            📁 A1_1
              └── 📄 A1_1.py   ← 이걸 만들어요!

            >echo "" > A1_1.py
              │    │    │
              │    │    └── 만들 파일 이름
              │    └── 빈 내용 (파일 안에 들어갈 내용)
              └── "이 내용을 출력/전달해줘"
            > 는 "오른쪽 파일에 저장해" 
            

            >echo "" > A1_1.py
            >ls
            >A1_1.py             <- 이렇게 나오면 성공
            
            Git에 등록
            >git add A1_1.py
              │   │    │
              │   │    └── 등록할 파일 이름
              │   └── "이 파일을 추적 목록에 올려줘"
              └── "준비해줘"
  
            >git commit -m "first commit"
                │       │       │
                │       │       └── 메모 내용 (내가 쓰고 싶은 말)
                │       └── -m : message의 약자 (메모를 쓰겠다는 신호)
                └── "지금 이 상태를 저장해줘"


               -> [main (root-commit) 7a28fe1] first commit
                   │         │          │         │
                   │         │          │         └── 내가 쓴 메모
                   │         │          └── 커밋 고유번호 (일종의 저장 ID)
                   │         └── 첫 번째 커밋이라는 표시
                   └── main 브랜치에 저장됨
                
               -> 1 file changed, 0 insertions(+), 0 deletions(-)
                   │                  │                  │
                   │                  │                  └── 삭제된 줄 : 0줄
                   │                  └── 추가된 줄 : 0줄 (빈 파일이라서)
                   └── 변경된 파일 : 1개
                
               -> create mode 100644 A1_1.py
                                      │
                                      └── A1_1.py 파일이 새로 등록됨






GitHub에 푸시
  git push -u origin main

          
          # .gitignore 생성  
          echo "__pycache__/" > .gitignore  
          echo "*.pyc" >> .gitignore  
          echo ".DS_Store" >> .gitignore  





git config --global user.name "홍길동"
git config --global user.email "your_email@example.com"


기본 브랜치도 main으로 설정
git config --global init.defaultBranch main

설정 확인하기 ( 이름 이메일 설정이 잘되었는지 확인)
git config --list

⑤ VSCode 확장 설치
VSCode 왼쪽 블록 아이콘(Extensions) 클릭 후 검색:

검색어	설치할 것
Python	Microsoft 만든 것 설치
Korean	Korean Language Pack (선택사항)

-----------------
✅ 1단계 완료 체크리스트
□ python --version  → 3.10 이상 확인
□ git --version     → 버전 확인
□ git config 이름/이메일 설정 완료
□ VSCode Python 확장 설치 완료
-----------------
파이쎈 버전 확인
py --list

---------------------------------------------------------------------

1단계: 프로젝트 폴더 만들기
 C:\Users\user\goodday_min> mkdir A1_1
폴더 이동
 C:\Users\user\goodday_min> cd A1_1

2. Git 초기화 ************************ 이 폴더를 Git이 관리하도록 시작하는 명령어예요  (.git 폴더 생성)
PS C:\Users\user\goodday_min\A1_1> git init


3. GitHub 저장소 연결 

 github에 로컬에 있는 A1_1.git 파일 만들기 위함.
(집에서 github에 A1_1.git 파일을 만들어 뒀기 때문에 새로 만들 필요없음)
git remote add origin https://github.com/본인아이디/A1_1.git

현재 상태만 확인 해봄.
git remote -v
예상 결과 : 
origin  https://github.com/goodday-min/A1_1.git (fetch) <-- fetch	GitHub에서 가져오기 연결
origin  https://github.com/goodday-min/A1_1.git (push) <-- push	GitHub로 올리기 연결



---------------------------------------- 이제 GitHub에서 파일 받아오면 돼요!--------
1.  집에서 작업한거 서버로 Push
2.  서버에 있는거 교육장 로컬로 Pull

1. 집에서 작업한거 서버로 Push
Push 전 필수 순서
# 1단계: 변경된 파일 스테이징
git add A1_1.py prompts.json

⚠️ prompts.json도 같이 올려야 해요!
prompts.json은 프롬프트 데이터가 저장되는 파일이라서
이것도 같이 올리지 않으면 교육장 컴퓨터에서 데이터가 없어요!

# 2단계: 커밋 (저장 기록 남기기)
git commit -m "A1_1.py 작업 내용"

# 3단계: GitHub에 올리기
git push origin main

왜 순서가 필요한가?
작업파일 → git add → git commit → git push → GitHub
(내 파일)   (준비)     (기록저장)    (업로드)    (서버)

2. 서버에서 있는거 교육장 로컬로 Pull







4. 파일 추가 **************************현재 폴더의 모든 파일을 Git에 추가해요
git add .

5. 첫 커밋
git commit -m "first commit: 프롬프트 관리 프로그램 초기 버전"

6. GitHub에 푸시
git push -u origin main
















