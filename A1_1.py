# -*- coding: utf-8 -*-
import json


# 프롬프트 관리 프로그램

# 데이터 저장 리스트
prompts = []
# 미리 정의된 카테고리 목록
CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]



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


def edit_prompt():
    """2번 메뉴 - 프롬프트 수정"""

    while True:  # ✅ 계속 수정 가능하도록 루프 유지
        print("\n=== ✏️  프롬프트 수정 ===")

        # 프롬프트 없을 때
        if not prompts:
            print("⚠️  저장된 프롬프트가 없습니다.")
            return

        # 전체 목록 출력
        print()
        for i, p in enumerate(prompts, 1):
            star = "⭐" if p["favorite"] else "☆"
            print(f"{i}. [{star}] [{p['category']}] {p['title']}")
        print()

        # 번호 입력
        choice = input("수정할 번호 입력 (0: 메인화면): ").strip()

        if choice == "0":
            print("📋 메인화면으로 돌아갑니다.")
            return

        if not choice.isdigit():
            print("⚠️  숫자를 입력하세요.")
            continue

        index = int(choice) - 1

        if not (0 <= index < len(prompts)):
            print(f"⚠️  1 ~ {len(prompts)} 사이의 번호를 입력하세요.")
            continue

        # ✅ 수정할 프롬프트 선택
        p = prompts[index]

        print()
        print("─" * 40)
        print(f"제목     : {p['title']}")
        print(f"카테고리 : {p['category']}")
        print(f"내용     : {p['content']}")
        print("─" * 40)
        print("※ 변경하지 않을 항목은 Enter를 누르세요.")
        print()

        # 제목 수정
        new_title = input(f"새 제목 ({p['title']}): ").strip()
        if new_title:
            p["title"] = new_title

        # 카테고리 수정
        print()
        for i, cat in enumerate(CATEGORIES, 1):
            print(f"{i}. {cat}")
        print()
        new_cat = input(f"새 카테고리 번호 ({p['category']}): ").strip()
        if new_cat.isdigit():
            cat_index = int(new_cat) - 1
            if 0 <= cat_index < len(CATEGORIES):
                p["category"] = CATEGORIES[cat_index]
            else:
                print("⚠️  올바른 번호가 아니어서 카테고리는 변경되지 않았습니다.")

        # 내용 수정
        new_content = input(f"새 내용 ({p['content']}): ").strip()
        if new_content:
            p["content"] = new_content

        print()
        print(f"✅ '{p['title']}' 프롬프트가 수정되었습니다.")

def delete_prompt():
    """3번 메뉴 - 프롬프트 삭제"""

    while True:  # ✅ 계속 삭제 가능하도록 루프 유지
        print("\n=== 🗑️  프롬프트 삭제 ===")

        # 프롬프트 없을 때
        if not prompts:
            print("⚠️  저장된 프롬프트가 없습니다.")
            return

        # 전체 목록 출력
        print()
        for i, p in enumerate(prompts, 1):
            star = "⭐" if p["favorite"] else "☆"
            print(f"{i}. [{star}] [{p['category']}] {p['title']}")
        print()

        # 번호 입력
        choice = input("삭제할 번호 입력 (0: 메인화면): ").strip()

        if choice == "0":
            print("📋 메인화면으로 돌아갑니다.")
            return

        if not choice.isdigit():
            print("⚠️  숫자를 입력하세요.")
            continue

        index = int(choice) - 1

        if not (0 <= index < len(prompts)):
            print(f"⚠️  1 ~ {len(prompts)} 사이의 번호를 입력하세요.")
            continue

        # ✅ 삭제 전 확인
        p = prompts[index]

        print()
        print("─" * 40)
        print(f"제목     : {p['title']}")
        print(f"카테고리 : {p['category']}")
        print(f"내용     : {p['content']}")
        print("─" * 40)
        print()

        confirm = input(f"⚠️  '{p['title']}' 을(를) 삭제하시겠습니까? (y/n): ").strip().lower()

        if confirm == "y":
            deleted_title = p["title"]
            prompts.pop(index)          # ✅ 리스트에서 제거
            print(f"🗑️  '{deleted_title}' 프롬프트가 삭제되었습니다.")
        else:
            print("❌ 삭제가 취소되었습니다.")
            







def search_prompt():
    """5번 메뉴 - 프롬프트 검색"""

    while True:  # ✅ 재검색 시 루프 유지
        print("\n=== 🔍 프롬프트 검색 ===")

        # 키워드 입력
        while True:
            keyword = input("검색어: ").strip()
            if keyword:
                break
            print("⚠️  검색어를 입력하세요.")

        # 제목에 키워드가 포함된 프롬프트 필터링
        filtered = [p for p in prompts if keyword in p["title"]]

        print()

        # ✅ 검색 결과 없을 때 선택지 제공
        if not filtered:
            print(f"⚠️  '{keyword}' 검색 결과가 없습니다.")
            print("\n1. 다시 검색하기")
            print("0. 메인화면으로 돌아가기")

            while True:
                sub_choice = input("선택하세요: ").strip()
                if sub_choice == "1":
                    break        # ✅ 바깥 while True로 돌아가 재검색
                elif sub_choice == "0":
                    print("📋 메인화면으로 돌아갑니다.")
                    return       # ✅ 함수 종료 → 메인화면
                else:
                    print("⚠️  0 또는 1을 입력하세요.")
            continue  # 재검색 루프

        # 검색 결과 출력
        print("검색 결과:")
        for i, p in enumerate(filtered, 1):
            star = "⭐" if p["favorite"] else ""
            print(f"{i}. [{p['category']}] {p['title']} {star}")

        print()
        print(f"총 {len(filtered)}개의 프롬프트를 찾았습니다.")
        return  # ✅ 검색 성공 시 메인화면으로 복귀


def view_prompt_detail():
    """6번 메뉴 - 프롬프트 상세 보기"""

    while True:  # ✅ 잘못된 입력 시 재입력 루프
        print("\n=== 📄 프롬프트 상세 보기 ===")

        # 전체 프롬프트 목록 먼저 출력 (번호 확인용)
        if not prompts:
            print("⚠️  저장된 프롬프트가 없습니다.")
            return

        print()
        for i, p in enumerate(prompts, 1):
            star = "⭐" if p["favorite"] else ""
            print(f"{i}. [{p['category']}] {p['title']} {star}")
        print()

        # 번호 입력
        choice = input("번호 입력 (0: 메인화면): ").strip()

        # 0번 - 메인화면 복귀
        if choice == "0":
            print("📋 메인화면으로 돌아갑니다.")
            return

        # 숫자 유효성 검사
        if not choice.isdigit():
            print("⚠️  숫자를 입력하세요.")
            continue

        index = int(choice) - 1

        # 범위 유효성 검사
        if not (0 <= index < len(prompts)):
            print(f"⚠️  1 ~ {len(prompts)} 사이의 번호를 입력하세요.")
            continue

        # 선택한 프롬프트 출력
        p = prompts[index]
        star = "⭐" if p["favorite"] else "없음"

        print()
        print("─" * 40)
        print(f"제목     : {p['title']}")
        print(f"카테고리 : {p['category']}")
        print(f"즐겨찾기 : {star}")
        print("─" * 40)
        print("내용:")
        print(p["content"])
        print("─" * 40)

        # 상세 보기 후 선택지
        print("\n1. 다른 프롬프트 보기")
        print("0. 메인화면으로 돌아가기")

        while True:
            sub_choice = input("선택하세요: ").strip()
            if sub_choice == "1":
                break       # ✅ 루프 처음으로 → 목록 다시 출력
            elif sub_choice == "0":
                print("📋 메인화면으로 돌아갑니다.")
                return      # ✅ 함수 종료 → 메인화면
            else:
                print("⚠️  0 또는 1을 입력하세요.")




def view_by_category():
    """7번 메뉴 - 카테고리별 조회"""

    while True:  # ✅ 0번 선택 전까지 카테고리 메뉴에 머물기
        print("\n--- 📂 카테고리별 조회 ---")

        # ✅ 각 카테고리별 프롬프트 갯수 표기
        print("\n--- 카테고리 목록 ---")
        for i, category in enumerate(CATEGORIES, 1):
            count = len([p for p in prompts if p["category"] == category])
            print(f"{i}. {category} ({count})")
        print("0. 초기화면으로 돌아가기")
        print("--------------------")

        # 카테고리 선택
        while True:
            cat_choice = input("조회할 카테고리 번호를 선택하세요: ").strip()

            # ✅ 0번 - 초기화면으로 복귀
            if cat_choice == "0":
                print("📋 초기화면으로 돌아갑니다.")
                return

            elif cat_choice.isdigit() and 1 <= int(cat_choice) <= len(CATEGORIES):
                selected = CATEGORIES[int(cat_choice) - 1]
                break

            else:
                print(f"⚠️  0 ~ {len(CATEGORIES)} 사이의 번호를 입력하세요.")

        # 선택한 카테고리의 프롬프트 필터링
        filtered = [p for p in prompts if p["category"] == selected]

        print(f"\n[ {selected} ] 카테고리 :")
        print("--------------------")

        # ✅ 프롬프트가 없으면 안내 메시지 후 카테고리 메뉴로 유지
        if not filtered:
            print(f"⚠️  [{selected}] 카테고리에 저장된 프롬프트가 없습니다.")
            continue  # 카테고리 목록으로 돌아가기

        # 프롬프트 목록 출력
        for i, p in enumerate(filtered, 1):
            star = "⭐" if p["favorite"] else ""
            print(f"{i}. {p['title']} {star}")

        print("--------------------")
        print(f"총 {len(filtered)}개의 프롬프트가 있습니다.")


def manage_favorite():
    """8번 메뉴 - 즐겨찾기 관리"""

    while True:  # ✅ 계속 토글 가능하도록 루프 유지
        print("\n=== ⭐ 즐겨찾기 관리 ===")

        # 프롬프트 없을 때
        if not prompts:
            print("⚠️  저장된 프롬프트가 없습니다.")
            return

        # 전체 목록 출력 (즐겨찾기 여부 포함)
        print()
        for i, p in enumerate(prompts, 1):
            star = "⭐" if p["favorite"] else "☆"
            print(f"{i}. [{star}] [{p['category']}] {p['title']}")
        print()

        # 번호 입력
        choice = input("번호 입력 (0: 메인화면): ").strip()

        # 0번 - 메인화면 복귀
        if choice == "0":
            print("📋 메인화면으로 돌아갑니다.")
            return

        # 숫자 유효성 검사
        if not choice.isdigit():
            print("⚠️  숫자를 입력하세요.")
            continue

        index = int(choice) - 1

        # 범위 유효성 검사
        if not (0 <= index < len(prompts)):
            print(f"⚠️  1 ~ {len(prompts)} 사이의 번호를 입력하세요.")
            continue

        # ✅ 즐겨찾기 토글
        p = prompts[index]
        p["favorite"] = not p["favorite"]

        if p["favorite"]:
            print(f"⭐ '{p['title']}' 즐겨찾기에 추가되었습니다.")
        else:
            print(f"☆  '{p['title']}' 즐겨찾기가 해제되었습니다.")


def view_favorites():
    """9번 메뉴 - 즐겨찾기 목록"""

    while True:  # ✅ 상세보기 후 돌아올 수 있도록 루프 유지
        print("\n=== ⭐ 즐겨찾기 목록 ===")

        # 즐겨찾기된 프롬프트만 필터링
        favorites = [p for p in prompts if p["favorite"]]

        # 즐겨찾기 없을 때
        if not favorites:
            print("⚠️  즐겨찾기된 프롬프트가 없습니다.")
            return

        # 목록 출력
        print()
        for i, p in enumerate(favorites, 1):
            print(f"{i}. [{p['category']}] {p['title']} ⭐")
        print()
        print(f"총 {len(favorites)}개의 즐겨찾기 프롬프트")
        print()
        print("1. 상세 보기")
        print("0. 메인화면으로 돌아가기")

        # 선택지 입력
        while True:
            sub_choice = input("선택하세요: ").strip()
            if sub_choice == "1":
                break       # ✅ 상세 보기로 이동
            elif sub_choice == "0":
                print("📋 메인화면으로 돌아갑니다.")
                return      # ✅ 함수 종료 → 메인화면
            else:
                print("⚠️  0 또는 1을 입력하세요.")

        # 상세 보기 - 번호 입력
        while True:
            choice = input("번호 입력 (0: 목록으로): ").strip()

            if choice == "0":
                break       # ✅ 루프 처음으로 → 목록 다시 출력

            if not choice.isdigit():
                print("⚠️  숫자를 입력하세요.")
                continue

            index = int(choice) - 1

            if not (0 <= index < len(favorites)):
                print(f"⚠️  1 ~ {len(favorites)} 사이의 번호를 입력하세요.")
                continue

            # 상세 내용 출력
            p = favorites[index]

            print()
            print("─" * 40)
            print(f"제목     : {p['title']}")
            print(f"카테고리 : {p['category']}")
            print(f"즐겨찾기 : ⭐")
            print("─" * 40)
            print("내용:")
            print(p["content"])
            print("─" * 40)
            break  # ✅ 상세 출력 후 루프 처음으로 → 목록 다시 출력



def main():
    """메인 실행 함수"""
    while True:
        show_menu()
        choice = input("선택하세요: ").strip()

        if choice == "1":
            add_prompt()            # 프롬프트 추가
        elif choice == "2":
            edit_prompt()           # 프롬프트 수정
        elif choice == "3":
            delete_prompt()   # 프롬프트 삭제
        elif choice == "4":
            print("준비 중입니다.")   # 프롬프트 목록
        elif choice == "5":
            search_prompt()         # 프롬프트 검색
        elif choice == "6":
            view_prompt_detail()   # 프롬프트 상세 보기
        elif choice == "7":
            view_by_category()      # 카테고리별 조회
        elif choice == "8":
            manage_favorite()       # 즐겨찾기 관리
        elif choice == "9":
            view_favorites()        # 즐겨찾기 목록
        elif choice == "0":
            print("👋 프로그램을 종료합니다. 안녕히 가세요!") #종료
            break
        else:
            print("⚠️  잘못된 입력입니다. 다시 선택하세요.")

# 프로그램 시작
if __name__ == "__main__":
    main()