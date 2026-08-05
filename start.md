📌 과제가 뭐냐면...
"프롬프트를 저장하고 찾을 수 있는 프로그램을 만들어라" 입니다.

예시) 지금은...
- ChatGPT 프롬프트를 메모장에 저장
- 필요할 때 못 찾아서 다시 씀 😭

만들고 나면...
  - 프로그램 실행
  - 번호 입력으로 추가/검색/즐겨찾기
  - 깔끔하게 관리 😊



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

          # 프로젝트 폴더 생성  
          mkdir prompt-manager  
          cd prompt-manager  
          
          # Git 초기화  
          git init  
          
          # .gitignore 생성  
          echo "__pycache__/" > .gitignore  
          echo "*.pyc" >> .gitignore  
          echo ".DS_Store" >> .gitignore  

### 3단계: 프로그램 코드 작성  
prompt_manager.py 파일을 생성하세요.  

          # prompt_manager.py
          # 나만의 프롬프트 관리 프로그램
          
          # =============================================
          # 기본 데이터 (이전 미션 프롬프트 4개 등록)
          # =============================================
          
          prompts = [
              {
                  "title": "블로그 글 작성 도우미",
                  "content": "당신은 10년 경력의 전문 블로거입니다. 주어진 주제에 대해 SEO에 최적화된 블로그 글을 작성해주세요. 서론, 본론, 결론 구조를 갖추고, 독자의 관심을 끄는 제목을 3개 제안해주세요.",
                  "category": "텍스트 생성",
                  "favorite": True
              },
              {
                  "title": "판타지 풍경 이미지 생성",
                  "content": "A breathtaking fantasy landscape, enchanted forest with glowing mushrooms, mystical fog, ancient ruins, golden hour lighting, ultra detailed, 8k resolution, digital art style",
                  "category": "이미지 생성",
                  "favorite": False
              },
              {
                  "title": "친절한 고객상담 페르소나",
                  "content": "당신은 10년 경력의 고객 상담 전문가입니다. 항상 공감하는 태도로 고객의 말을 먼저 경청하고, 문제 해결 중심으로 답변합니다. 절대 부정적인 표현을 사용하지 않으며, 모든 답변은 정중하고 따뜻하게 마무리합니다.",
                  "category": "페르소나",
                  "favorite": False
              },
              {
                  "title": "유튜브 쇼츠 스크립트 생성",
                  "content": "60초 유튜브 쇼츠용 스크립트를 작성해주세요. 주제: [주제]. 첫 3초 안에 시청자의 관심을 끄는 훅(Hook)으로 시작하고, 핵심 내용을 빠르게 전달한 뒤 구독 유도 멘트로 마무리하세요.",
                  "category": "영상 생성",
                  "favorite": False
              },
          ]
          
          # 카테고리 목록
          CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]
          
          
          # =============================================
          # 유틸리티 함수
          # =============================================
          
          def print_line():
              """구분선 출력"""
              print("─" * 40)
          
          
          def print_prompt_row(number, prompt):
              """프롬프트 한 줄 요약 출력"""
              star = " ⭐" if prompt["favorite"] else ""
              print(f"{number}. [{prompt['category']}] {prompt['title']}{star}")
          
          
          # =============================================
          # 메뉴 출력
          # =============================================
          
          def show_menu():
              """메인 메뉴 출력"""
              print("\n=== 나만의 프롬프트 관리 ===")
              print("1. 프롬프트 추가")
              print("2. 프롬프트 목록")
              print("3. 카테고리별 조회")
              print("4. 프롬프트 검색")
              print("5. 프롬프트 상세 보기")
              print("6. 즐겨찾기 관리")
              print("7. 즐겨찾기 목록")
              print("0. 종료")
          
          
          # =============================================
          # 1. 프롬프트 추가
          # =============================================
          
          def add_prompt():
              """새 프롬프트 추가"""
              print("\n=== 프롬프트 추가 ===")
          
              # 제목 입력 (빈값 방지)
              while True:
                  title = input("제목: ").strip()
                  if title:
                      break
                  print("⚠️  제목을 입력해주세요.")
          
              # 내용 입력 (빈값 방지)
              while True:
                  content = input("내용: ").strip()
                  if content:
                      break
                  print("⚠️  내용을 입력해주세요.")
          
              # 카테고리 선택
              category = select_category()
          
              # 딕셔너리로 저장
              new_prompt = {
                  "title": title,
                  "content": content,
                  "category": category,
                  "favorite": False      # 기본값 False
              }
              prompts.append(new_prompt)
          
              print(f"\n✅ 프롬프트가 추가되었습니다!")
          
          
          def select_category():
              """카테고리 선택"""
              print("\n카테고리 선택:")
              for i, cat in enumerate(CATEGORIES, 1):
                  print(f"{i}) {cat}")
          
              while True:
                  choice = input("선택: ").strip()
                  if choice.isdigit():
                      idx = int(choice) - 1
                      if 0 <= idx < len(CATEGORIES):
                          return CATEGORIES[idx]
                  print(f"⚠️  1~{len(CATEGORIES)} 사이의 번호를 입력해주세요.")
          
          
          # =============================================
          # 2. 프롬프트 목록
          # =============================================
          
          def show_list():
              """전체 프롬프트 목록 출력"""
              print("\n=== 프롬프트 목록 ===")
          
              if not prompts:
                  print("등록된 프롬프트가 없습니다.")
                  return
          
              for i, prompt in enumerate(prompts, 1):
                  print_prompt_row(i, prompt)
          
              print(f"\n총 {len(prompts)}개의 프롬프트")
          
          
          # =============================================
          # 3. 카테고리별 조회
          # =============================================
          
          def show_by_category():
              """카테고리별 프롬프트 조회"""
              print("\n=== 카테고리별 조회 ===")
          
              for i, cat in enumerate(CATEGORIES, 1):
                  print(f"{i}) {cat}")
          
              while True:
                  choice = input("선택: ").strip()
                  if choice.isdigit():
                      idx = int(choice) - 1
                      if 0 <= idx < len(CATEGORIES):
                          selected_cat = CATEGORIES[idx]
                          break
                  print(f"⚠️  1~{len(CATEGORIES)} 사이의 번호를 입력해주세요.")
          
              # 해당 카테고리만 필터링
              filtered = [p for p in prompts if p["category"] == selected_cat]
          
              print(f"\n[{selected_cat}] 카테고리 프롬프트:")
          
              if not filtered:
                  print("해당 카테고리에 프롬프트가 없습니다.")
                  return
          
              for i, prompt in enumerate(filtered, 1):
                  print_prompt_row(i, prompt)
          
              print(f"\n총 {len(filtered)}개의 프롬프트")
          
          
          # =============================================
          # 4. 프롬프트 검색
          # =============================================
          
          def search_prompt():
              """키워드로 제목/내용 검색"""
              print("\n=== 프롬프트 검색 ===")
          
              keyword = input("검색어: ").strip()
          
              if not keyword:
                  print("⚠️  검색어를 입력해주세요.")
                  return
          
              # 대소문자 구분 없이 제목 또는 내용에서 검색
              results = [
                  p for p in prompts
                  if keyword.lower() in p["title"].lower()
                  or keyword.lower() in p["content"].lower()
              ]
          
              print(f"\n검색 결과:")
          
              if not results:
                  print("검색 결과가 없습니다.")
                  return
          
              for i, prompt in enumerate(results, 1):
                  print_prompt_row(i, prompt)
          
              print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")
          
          
          # =============================================
          # 5. 프롬프트 상세 보기
          # =============================================
          
          def show_detail():
              """프롬프트 상세 내용 출력"""
              print("\n=== 프롬프트 상세 보기 ===")
          
              if not prompts:
                  print("등록된 프롬프트가 없습니다.")
                  return
          
              while True:
                  choice = input("번호 입력: ").strip()
                  if choice.isdigit():
                      idx = int(choice) - 1
                      if 0 <= idx < len(prompts):
                          break
                  print(f"⚠️  1~{len(prompts)} 사이의 번호를 입력해주세요.")
          
              prompt = prompts[idx]
              star = "⭐" if prompt["favorite"] else "없음"
          
              print_line()
              print(f"제목: {prompt['title']}")
              print(f"카테고리: {prompt['category']}")
              print(f"즐겨찾기: {star}")
              print_line()
              print("내용:")
              print(prompt["content"])
              print_line()
          
          
          # =============================================
          # 6. 즐겨찾기 관리 (추가/해제)
          # =============================================
          
          def manage_favorites():
              """즐겨찾기 토글 (추가 ↔ 해제)"""
              print("\n=== 즐겨찾기 관리 ===")
          
              if not prompts:
                  print("등록된 프롬프트가 없습니다.")
                  return
          
              # 현재 목록 보여주기
              for i, prompt in enumerate(prompts, 1):
                  print_prompt_row(i, prompt)
          
              while True:
                  choice = input("\n프롬프트 번호 입력: ").strip()
                  if choice.isdigit():
                      idx = int(choice) - 1
                      if 0 <= idx < len(prompts):
                          break
                  print(f"⚠️  1~{len(prompts)} 사이의 번호를 입력해주세요.")
          
              prompt = prompts[idx]
          
              # 즐겨찾기 토글
              if prompt["favorite"]:
                  prompt["favorite"] = False
                  print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")
              else:
                  prompt["favorite"] = True
                  print(f"'{prompt['title']}' 프롬프트를 즐겨찾기에 추가했습니다! ⭐")
          
          
          # =============================================
          # 7. 즐겨찾기 목록
          # =============================================
          
          def show_favorites():
              """즐겨찾기된 프롬프트만 출력"""
              print("\n=== 즐겨찾기 목록 ===")
          
              favorites = [p for p in prompts if p["favorite"]]
          
              if not favorites:
                  print("즐겨찾기된 프롬프트가 없습니다.")
                  return
          
              for i, prompt in enumerate(favorites, 1):
                  print_prompt_row(i, prompt)
          
              print(f"\n총 {len(favorites)}개의 즐겨찾기")
          
          
          # =============================================
          # 메인 실행 루프
          # =============================================
          
          def main():
              """프로그램 메인 루프"""
              print("프롬프트 관리 프로그램을 시작합니다.")
          
              while True:
                  show_menu()
                  choice = input("선택: ").strip()
          
                  if choice == "1":
                      add_prompt()
                  elif choice == "2":
                      show_list()
                  elif choice == "3":
                      show_by_category()
                  elif choice == "4":
                      search_prompt()
                  elif choice == "5":
                      show_detail()
                  elif choice == "6":
                      manage_favorites()
                  elif choice == "7":
                      show_favorites()
                  elif choice == "0":
                      print("\n프로그램을 종료합니다. 👋")
                      break
                  else:
                      print("⚠️  올바른 번호를 입력해주세요.")
          
          
          # 프로그램 시작점
          if __name__ == "__main__":
              main()

### 4단계: 기능별 커밋 & 브랜치 작업  , Git 커밋 전략 (10개 이상 만들기)   

          # 1. 초기 설정
              git add .gitignore README.md
              git commit -m "init: 프로젝트 초기 설정 및 README 추가"
          
          # 2. 기본 데이터 추가
              git add prompt_manager.py
              git commit -m "feat: 기본 프롬프트 데이터 4개 등록"
          
          # 3. 메뉴 시스템
              git commit -m "feat: 메인 메뉴 출력 및 실행 루프 구현"
          
          # 4. 프롬프트 추가 기능
              git commit -m "feat: 프롬프트 추가 기능 구현 (add_prompt)"
          
          # 5. 브랜치 생성 후 목록 기능 작업
              git checkout -b feature/show-list
              git commit -m "feat: 전체 프롬프트 목록 보기 구현 (show_list)"
              git checkout main
              git merge feature/show-list
              git commit -m "merge: feature/show-list → main 병합"
          
          # 6. 카테고리 조회
              git commit -m "feat: 카테고리별 조회 기능 구현 (show_by_category)"
          
          # 7. 검색
              git commit -m "feat: 키워드 검색 기능 구현 (search_prompt)"
          
          # 8. 상세 보기
              git commit -m "feat: 프롬프트 상세 보기 구현 (show_detail)"
          
          # 9. 즐겨찾기 관리
              git commit -m "feat: 즐겨찾기 추가/해제 기능 구현 (manage_favorites)"
          
          # 10. 즐겨찾기 목록
              git commit -m "feat: 즐겨찾기 목록 보기 구현 (show_favorites)"
          
          # 11. 예외처리 보완
              git commit -m "fix: 빈 입력값 및 잘못된 번호 예외처리 보완"
          
          # GitHub 푸시
              git push origin main



4단계: 기능별 커밋 & 브랜치 작업
5단계: README 작성 & 최종 제출
