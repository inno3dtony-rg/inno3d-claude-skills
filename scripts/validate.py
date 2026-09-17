#!/usr/bin/env python3
"""이노쓰리디 스킬 무결성 검사 — 모든 항목이 PASS여야 배포 가능."""
import re, sys, pathlib, collections
try: import yaml
except ImportError: print("pyyaml 필요"); sys.exit(2)

# 저장소 루트 탐색: 스크립트 위치 또는 그 상위 중 SKILL.md가 있는 곳
def _find_root(start):
    for cand in [start, start.parent]:
        if list(cand.glob("*/SKILL.md")):
            return cand
    return start
ROOT = _find_root(pathlib.Path(__file__).resolve().parent)
SKILLS = sorted(p for p in ROOT.glob("*/SKILL.md"))
fails, checks = [], 0

def chk(cond, label, detail=""):
    global checks; checks += 1
    if not cond: fails.append(f"{label}{(' — '+detail) if detail else ''}")

# 1. 스킬 개수
chk(len(SKILLS) == 10, "스킬 개수 10개", f"실제 {len(SKILLS)}개")

for p in SKILLS:
    name = p.parent.name
    txt = p.read_text(encoding="utf-8")

    # 2. 프론트매터 구조
    chk(txt.startswith("---\n"), f"[{name}] 프론트매터 시작")
    parts = txt.split("---\n")
    if len(parts) < 3:
        fails.append(f"[{name}] 프론트매터 구분자 부족"); continue
    try:
        fm = yaml.safe_load(parts[1])
    except Exception as e:
        fails.append(f"[{name}] YAML 파싱 실패 — {e}"); continue

    # 3. name 일치
    chk(fm.get("name") == name, f"[{name}] name과 폴더명 일치", str(fm.get('name')))

    # 4. description 존재·길이
    desc = fm.get("description") or ""
    chk(len(desc) >= 100, f"[{name}] description 100자 이상", f"{len(desc)}자")

    # 5. 마스터 외에는 경계 명시 필수
    if name != "inno3d-dental-master":
        chk(("넘길 곳" in desc) or ("쓰지 않는 경우" in desc),
            f"[{name}] description에 경계(넘길 곳) 명시")
        chk("스킬 선택 기준" in txt, f"[{name}] 본문에 스킬 선택 기준 블록")

    # 6. 구식 표현 잔존 금지
    chk("반드시 이 스킬을 사용한다" not in txt, f"[{name}] 구식 '반드시' 표현 없음")

    # 7. 본문 존재
    body = "---\n".join(parts[2:])
    chk(len(body.strip()) > 200, f"[{name}] 본문 최소 분량")

    # 8. 참조 링크 유효성
    for m in re.findall(r'references/([A-Za-z0-9._\-]+)', txt):
        chk((p.parent/"references"/m).exists(), f"[{name}] 참조 파일 존재", m)

# 9. 마스터 필수 섹션
mt = (ROOT/"inno3d-dental-master"/"SKILL.md").read_text(encoding="utf-8")
for sec in ["핵심 컨텍스트", "자동 라우팅 표", "충돌 시 우선순위",
            "참조 문서", "스킬 조합 규칙", "대외 문서 정보 노출 기준", "공통 출력 원칙"]:
    chk(sec in mt, f"[master] 필수 섹션 '{sec}'")

# 10. 참조 파일 고아 없음
refs = {f.name for f in (ROOT/"inno3d-dental-master"/"references").glob("*.md")}
linked = set(re.findall(r'references/([A-Za-z0-9._\-]+)', mt))
chk(not (refs - linked), "[master] 고아 참조 파일 없음", str(sorted(refs-linked)))

# 11. 마스터 라우팅 표가 실제 존재하는 스킬만 가리키는가
folders = {p.parent.name for p in SKILLS}
cited = set(re.findall(r'`(dental-[a-z\-]+|inno3d-[a-z\-]+|global-dental-[a-z\-]+)`', mt))
chk(cited <= folders, "[master] 라우팅이 존재하는 스킬만 참조", str(sorted(cited-folders)))

# 12. 타 스킬 위임 대상이 실제 계정 스킬인가
KNOWN = {"docx","xlsx","pptx","pdf","brand","banner-design","design","design-system",
         "web-artifacts-builder","academy-guide","learn","internal-comms","deep-research",
         "brand-guidelines","canvas-design","ui-styling","ui-ux-pro-max","slides"} | folders
for p in SKILLS:
    t = p.read_text(encoding="utf-8")
    for m in re.findall(r'`([a-z][a-z0-9\-]{3,})`', t):
        if m.endswith(".md") or "/" in m: continue
        if m not in KNOWN and ("-" in m):
            fails.append(f"[{p.parent.name}] 알 수 없는 스킬명 참조: {m}")
        checks += 1

print(f"검사 {checks}건 실행")
if fails:
    print(f"\n❌ 실패 {len(fails)}건")
    for f in fails: print("  -", f)
    sys.exit(1)
print("\n✅ 전체 통과")
