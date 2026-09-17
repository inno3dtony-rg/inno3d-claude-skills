# inno3d-claude-skills

㈜이노쓰리디(INNO3D)의 Claude Code / Claude 앱용 스킬 모음.

## 구조

각 스킬은 저장소 루트의 폴더 하나이며, 그 안에 `SKILL.md`가 있습니다.
Claude의 개인 스킬 폴더(`~/.claude/skills/<스킬명>/SKILL.md`)와 동일한 레이아웃입니다.

```
inno3d-claude-skills/
├── README.md
├── install.sh
└── <스킬명>/
    ├── SKILL.md          # 필수: YAML 프론트매터(name, description) + 본문
    └── references/       # 선택: 분량이 큰 참조 문서
```

## 설치

`~/.claude/skills`에는 이미 다른 스킬이 들어 있을 수 있어
**직접 clone하면 실패합니다**. 별도 위치에 clone한 뒤 심볼릭 링크를 거는 방식을 씁니다.

```bash
git clone https://github.com/inno3dtony-rg/inno3d-claude-skills.git ~/inno3d-claude-skills
cd ~/inno3d-claude-skills
./install.sh
```

`install.sh`는 각 스킬 폴더를 `~/.claude/skills/` 아래로 심볼릭 링크합니다.
이후 저장소에서 `git pull`만 하면 스킬이 바로 갱신됩니다.

### 제거

```bash
./install.sh --uninstall
```

## 스킬 작성 규칙

`SKILL.md`는 YAML 프론트매터로 시작합니다.

```markdown
---
name: skill-name
description: 이 스킬이 언제 쓰이는지. 호출을 유도할 키워드를 포함할 것.
---

# 제목

본문...
```

- `name`: 폴더명과 동일하게, 소문자·하이픈만 사용
- `description`: Claude가 이 스킬을 **언제 부를지** 판단하는 유일한 근거. 트리거 키워드를 한국어·영어 모두 넣을 것
- 본문이 길어지면 `references/` 폴더로 분리하고 `SKILL.md`에서 경로로 참조

## 대외비 취급

이 저장소에 **가격·견적·거래처 연락처·내부 결재라인·미공개 사양**을 넣기 전
저장소 공개 범위(public/private)를 반드시 확인하십시오.
public 저장소에 올린 내용은 삭제해도 포크·캐시·검색엔진에 남습니다.

## 수록 스킬

| 스킬 | 용도 |
|---|---|
| `inno3d-dental-master` | 통합 마스터 — 영업·마케팅·시장분석·교육·기술지원·수출·번역을 아우르는 진입점 |
| `inno3d-admin-docs` | 다우오피스 행정문서 (품의서·기안서·지출결의서) |
| `inno3d-meeting-processing` | CLOVA Note 전사본 → 회의록·통화기록 |
| `inno3d-clinical-dev-bridge` | 임상·기공 현장 관찰 → 개발팀용 정량 지표 |
| `dental-sales-strategy` | B2B·B2C 영업 전략, 제안서, 가격 협상, 딜러 |
| `dental-marketing` | 마케팅 전략, 콘텐츠, 캠페인, 전시회 |
| `dental-business-development` | 신사업, 시장 진입, 파트너십, 일본 진출 |
| `dental-education-training` | 교육 프로그램·매뉴얼·트레이닝 자료 |
| `dental-technical-support` | 기술 지원, 트러블슈팅, 기술 문서 |
| `global-dental-market-analysis` | 글로벌 구강 스캐너 시장·경쟁사 분석 |

`inno3d-dental-master`는 `references/` 아래에 영역별 상세 문서 8종을 둡니다.
