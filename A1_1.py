import os
import copy

# ── 상수 ──────────────────────────────────────────
CATEGORIES = ["글쓰기", "코딩", "번역", "요약", "기타"]

DEFAULT_PROMPTS = [
    {
        "id": 1,
        "title": "블로그 글쓰기",
        "content": "당신은 전문 블로그 작가입니다. 주어진 주제로 SEO에 최적화된 블로그 글을 작성해주세요.",
        "category": "글쓰기",
        "favorite": False
    },
    {
        "id": 2,
        "title": "파이썬 코드 리뷰",
        "content": "당신은 시니어 파이썬 개발자입니다. 아래 코드를 리뷰하고 개선점을 알려주세요.",
        "category": "코딩",
        "favorite": False
    },
    {
        "id": 3,
        "title": "영어 번역",
        "content": "당신은 전문 번역가입니다. 아래 한국어 텍스트를 자연스러운 영어로 번역해주세요.",
        "category": "번역",
        "favorite": True
    },
]

# ── 전역변수 ───────────────────────────────────────
prompts = copy.deepcopy(DEFAULT_PROMPTS)
next_id = 4

# ── 초기화면 ───────────────────────────────────────
def show_menu():
    print("\n" + "=" * 40)
    print("       🧠 프롬프트 관리 프로그램")
    print("=" * 40)
    print("  1. 프롬프트 추가")
    print("  2. 프롬프트 목록")
    print("  3. 카테고리별 조회")
    print("  4. 프롬프트 검색")
    print("  5. 프롬프트 상세 보기")
    print("  6. 즐겨찾기 관리")
    print("  7. 즐겨찾기 목록")
    print("  0. 종료")
    print("=" * 40)

# ── 1. 프롬프트 추가 ───────────────────────────────
def add_prompt():
    global prompts, next_id
    print("\n[ 프롬프트 추가 ]")

    title = input("제목: ").strip()
    if not title:
        print("❌ 제목을 입력해주세요.")
        return

    content = input("내용: ").strip()
    if not content:
        print("❌ 내용을 입력해주세요.")
        return

    print("카테고리 목록:", ", ".join(CATEGORIES))
    print("직접 입력하려면 '직접입력' 을 선택하세요.")
    category = input("카테고리: ").strip()

    if category == "직접입력":
        category = input("카테고리 직접 입력: ").strip()

    if not category:
        category = "기타"

    new_prompt = {
        "id": next_id,
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)
    next_id += 1
    print(f"✅ '{title}' 프롬프트가 추가되었습니다! (ID: {new_prompt['id']})")

# ── 2. 프롬프트 목록 ───────────────────────────────
def list_prompts():
    print("\n[ 프롬프트 목록 ]")
    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    print(f"{'ID':<5} {'제목':<20} {'카테고리':<10} {'즐겨찾기'}")
    print("-" * 50)
    for p in prompts:
        fav = "⭐" if p.get("favorite", False) else ""
        print(f"{p['id']:<5} {p['title']:<20} {p['category']:<10} {fav}")

# ── 3. 카테고리별 조회 ─────────────────────────────
def list_by_category():
    print("\n[ 카테고리별 조회 ]")
    category = input("조회할 카테고리: ").strip()

    result = [p for p in prompts if p["category"] == category]

    if not result:
        print(f"'{category}' 카테고리에 해당하는 프롬프트가 없습니다.")
        return

    print(f"\n── {category} ──")
    for p in result:
        fav = "⭐" if p.get("favorite", False) else ""
        print(f"  [{p['id']}] {p['title']} {fav}")

# ── 4. 프롬프트 검색 ───────────────────────────────
def search_prompts():
    print("\n[ 프롬프트 검색 ]")
    keyword = input("검색어: ").strip()

    if not keyword:
        print("❌ 검색어를 입력해주세요.")
        return

    result = [
        p for p in prompts
        if keyword in p["title"] or keyword in p["content"]
    ]

    if not result:
        print(f"'{keyword}' 검색 결과가 없습니다.")
        return

    print(f"\n── 검색 결과: {len(result)}건 ──")
    for p in result:
        print(f"  [{p['id']}] {p['title']} ({p['category']})")

# ── 5. 프롬프트 상세 보기 ─────────────────────────
def view_prompt():
    print("\n[ 프롬프트 상세 보기 ]")
    try:
        pid = int(input("ID 입력: "))
    except ValueError:
        print("❌ 숫자를 입력해주세요.")
        return

    target = next((p for p in prompts if p["id"] == pid), None)

    if not target:
        print(f"❌ ID {pid} 프롬프트를 찾을 수 없습니다.")
        return

    fav = "⭐" if target.get("favorite", False) else "없음"
    print(f"\n── 상세 보기 ──")
    print(f"  ID       : {target['id']}")
    print(f"  제목     : {target['title']}")
    print(f"  카테고리 : {target['category']}")
    print(f"  즐겨찾기 : {fav}")
    print(f"  내용     :\n{target['content']}")

# ── 6. 즐겨찾기 관리 ──────────────────────────────
def toggle_favorite():
    print("\n[ 즐겨찾기 관리 ]")
    try:
        pid = int(input("ID 입력: "))
    except ValueError:
        print("❌ 숫자를 입력해주세요.")
        return

    target = next((p for p in prompts if p["id"] == pid), None)

    if not target:
        print(f"❌ ID {pid} 프롬프트를 찾을 수 없습니다.")
        return

    target["favorite"] = not target.get("favorite", False)
    status = "⭐ 추가" if target["favorite"] else "❌ 해제"
    print(f"'{target['title']}' 즐겨찾기 {status}!")

# ── 7. 즐겨찾기 목록 ──────────────────────────────
def list_favorites():
    print("\n[ 즐겨찾기 목록 ]")
    result = [p for p in prompts if p.get("favorite", False)]

    if not result:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for p in result:
        print(f"  ⭐ [{p['id']}] {p['title']} ({p['category']})")

# ── 메인 루프 ──────────────────────────────────────
def main():
    while True:
        show_menu()
        choice = input("메뉴 선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            list_prompts()
        elif choice == "3":
            list_by_category()
        elif choice == "4":
            search_prompts()
        elif choice == "5":
            view_prompt()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            list_favorites()
        elif choice == "0":
            print("👋 프로그램을 종료합니다.")
            break
        else:
            print("❌ 올바른 메뉴를 선택해주세요.")

if __name__ == "__main__":
    main()