# 프롬프트 관리 프로그램 만들기  

=============================  
   📝 나만의 프롬프트 관리 프로그램  
=============================  
1. 프롬프트 추가  
2. 프롬프트 수정  
3. 프롬프트 삭제  
4. 프롬프트 목록  
5. 프롬프트 검색  
6. 프롬프트 상세 보기  
7. 카테고리별 조회  
8. 즐겨찾기 관리  
9. 즐겨찾기 목록  
0. 종료   
=============================  
선택하세요:  



          프로그램 시작  
              ↓
          main() 호출
              ↓
          while True 루프 시작
              ↓
          show_menu() → 메뉴 출력
              ↓
          input() → 사용자 입력 대기
              ↓
          0 입력 → break → 종료
          그 외  → 해당 기능 실행 후 다시 메뉴 출력

--- 

        메인 메뉴 화면 코드
        def show_menu():
            """메뉴 화면 출력"""
            print("\n=============================")
            print("   📝 나만의 프롬프트 관리 프로그램")
            print("=============================")
            print("1. 프롬프트 추가")
            print("2. 프롬프트 수정")
            print("3. 프롬프트 삭제")
            print("4. 프롬프트 목록")
            print("5. 프롬프트 검색")
            print("6. 프롬프트 상세 보기")
            print("7. 카테고리별 조회")
            print("8. 즐겨찾기 관리")
            print("9. 즐겨찾기 목록")
            print("0. 종료")
            print("=============================")
        
        코드 구조 설명
        구성 요소	역할
        prompts = []	나중에 추가할 프롬프트 데이터를 저장할 리스트
        show_menu()	메뉴 화면을 출력하는 함수
        main()	while True 루프로 프로그램을 계속 실행
        choice = input(...)	사용자 입력을 받아 메뉴 분기
        if __name__ == "__main__"	파이썬 표준 시작점  
--- 


        def add_prompt():
            """1번 메뉴 - 프롬프트 추가"""
            print("\n--- 📝 프롬프트 추가 ---")
        
            # 제목 입력 (빈값 재입력 요청)
            while True:
                title = input("제목을 입력하세요: ").strip()
                if title:
                    break
                print("⚠️  제목은 필수 입력입니다. 다시 입력하세요.")
        
            # 내용 입력 (빈값 재입력 요청)
            while True:
                content = input("내용을 입력하세요: ").strip()
                if content:
                    break
                print("⚠️  내용은 필수 입력입니다. 다시 입력하세요.")
        
            # 카테고리 선택
            print("\n--- 카테고리 선택 ---")
            for i, category in enumerate(CATEGORIES, 1):
                print(f"{i}. {category}")
            print("0. 직접 입력")
            print("--------------------")
        
            while True:
                cat_choice = input("카테고리를 선택하세요: ").strip()
        
                # 직접 입력 선택
                if cat_choice == "0":
                    while True:
                        category = input("카테고리를 직접 입력하세요: ").strip()
                        if category:
                            break
                        print("⚠️  카테고리는 필수 입력입니다. 다시 입력하세요.")
                    break
        
                # 목록에서 선택
                elif cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
                    category = CATEGORIES[int(cat_choice) - 1]
                    break
        
                else:
                    print(f"⚠️  1 ~ {len(CATEGORIES)} 또는 0을 입력하세요.")
        
            # 프롬프트 데이터 생성
            prompt = {
                "id"        : len(prompts) + 1,  # 고유 번호
                "title"     : title,             # 제목
                "content"   : content,           # 내용
                "category"  : category,          # 카테고리
                "favorite"  : False              # 즐겨찾기 기본값
            }
        
            # 리스트에 저장
            prompts.append(prompt)
        
            print(f"\n✅ 프롬프트가 추가되었습니다!")
            print(f"   제목     : {title}")
            print(f"   카테고리 : {category}")

        # prompts 리스트에 저장되는 형태
        {
            "id"       : 1,          # 자동 부여 고유 번호
            "title"    : "제목",     # 사용자 입력
            "content"  : "내용",     # 사용자 입력
            "category" : "코딩",     # 선택 또는 직접 입력
            "favorite" : False       # 즐겨찾기 기본값
        }

      제목 입력 → 빈값이면 재입력 요청
          ↓
      내용 입력 → 빈값이면 재입력 요청
          ↓
      카테고리 목록 출력
          ↓
      번호 선택 → 목록에서 카테고리 자동 설정
        0 선택 → 직접 입력 → 빈값이면 재입력 요청
          ↓
      딕셔너리 생성 → prompts 리스트에 저장
          ↓
      완료 메시지 출력

---













📋 기능 목록 (같이 정해봐요!)
번호	기능	          설명
1	➕ 추가	            새 프롬프트 저장
2	📋 목록 보기	      저장된 프롬프트 전체 보기
3	🔍 검색	            키워드로 찾기
4	✏️ 수정	            프롬프트 내용 바꾸기
5	🗑️ 삭제	            프롬프트 지우기
6	💾 파일 저장	껐다 켜도 유지 (JSON 파일)


3. 카테고리별 조회
5. 프롬프트 상세 보기
6. 즐겨찾기 관리
7. 즐겨찾기 목록

1단계: 메뉴 화면 코드 작성! 🎯 

