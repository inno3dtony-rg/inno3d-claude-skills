---
name: dental-marketing
description: >
  치과 구강 스캐너의 **불특정 다수 대상 홍보 "문구와 메시지"**를 기획하는 스킬. 무엇을 말할지를 정하고, 실제 파일·이미지 제작은 전용 스킬에 넘긴다.
    담당: 브로셔·리플렛 카피, 광고 문구, SNS 게시글 본문, 슬로건 후보, 영상·유튜브 구성안, 전시회 홍보 메시지, 제품 포지셔닝, 홍보물용 한영일 번역, 이미지 생성 프롬프트 문안.
    넘길 곳: 배너·소셜 이미지 제작은 `banner-design`, 로고·CI 제작은 `design`, 브랜드 컬러·타이포 시스템 정의는 `brand`(Anthropic 브랜드용 `brand-guidelines`와 무관), 랜딩페이지 구현은 `web-artifacts-builder`, 특정 고객 1곳 대상 제안서는 `dental-sales-strategy`.
---

# Dental Marketing Skill (이노쓰리디 맞춤)

> **스킬 선택 기준** — 이 스킬이 담당하는 것: 불특정 다수 대상 홍보 콘텐츠.
> 아래에 해당하면 이 스킬 대신 그쪽을 쓴다: `dental-sales-strategy`(특정 고객 제안서) · `brand`(브랜드 시스템 정의)

## 브랜드 정보
- 제품 브랜드: Densflo (Densflo Scan + Densflo Codi)
- 회사: ㈜이노쓰리디 / 담당: 김민선 과장
- 확정(2026-09-16): 주소 서울 금천구 가산디지털1로 225 1420호 / 판매가 단품900만·세트1250만 / FDA 등록(승인 아님) / SW연사용료 없음
- 유튜브: @INNO3Dmarketing
- 웹사이트: inno3d.co.kr / inno3dental.com

---

## 1. 핵심 메시지 체계 (검증 완료)

```
[표지/헤드라인]
메인:   환자가 스스로 치료를 결정합니다
서브:   스캔부터 환자 상담까지, 하나의 플랫폼으로

[Densflo Codi 섹션]
제목:   진단부터 치료 수락까지, 눈으로 보여주세요
기능 1: 말 대신 화면으로 — 환자가 고개를 끄덕입니다
기능 2: 상담이 끝나면 리포트가 완성되어 있습니다
기능 3: 기공소까지 클릭 한 번으로 연결됩니다

[Densflo Scan 섹션]
제목:   첫 스캔부터 자신 있게
기능 1: 놓치는 각도 없이 — 인접면과 측면까지 한 번에
기능 2: 작은 움직임으로도 넓고 선명하게
기능 3: 처음 쓰는 날부터 능숙하게

[CTA]
헤드:   지금 Densflo를 경험해보세요
서브:   현장에서 직접 체험하고 도입 상담을 받으세요
```

---

## 2. 타겟 고객별 메시지

| 타겟 | 핵심 페인포인트 | 메시지 방향 |
|------|--------------|------------|
| 치과 원장 | 환자 치료 거부율 높음 | 상담 성공률 향상 → 매출 증가 |
| 치과위생사·스탭 | 복잡한 조작 불안 | "처음 쓰는 날부터 능숙하게" |
| 치기공사 | 데이터 연동 불편 | 클릭 한 번으로 기공주문 |
| 해외 딜러 | 가격 경쟁력, 인증 | MFDS+CE+ISO+FDA등록 보유, EX-WORKS 가격, SW연사용료 없음 |

---

## 3. 다국어 표기 (검증 완료)

| 항목 | 한국어 | 영어 | 일본어 |
|------|--------|------|--------|
| 제품명 | 덴스플로 스캔 | Densflo Scan | Densflo Scan |
| 스캐너 범주 | 구강 스캐너 | Intraoral Scanner | 口腔内スキャナー |
| 기공주문 | 기공주문 | Lab Order | 技工オーダー |
| 치료 동의율 | 치료 동의율 | Treatment consent rate | 治療同意率 |
| 회사명 일본어 | — | — | イノスリーディ (요확인) |

### 유튜브 영상 제목 표준
```
KOR: Densflo Intraoral Scanner & Codi (KOR)
ENG: Densflo Intraoral Scanner & Codi (ENG)
JPN: Densflo 口腔内スキャナー & Codi (JPN)
```

---

## 4. 채널별 전략

### 국내 온라인
- 유튜브: 제품 소개, 스캔 시연, 임상 케이스 (@INNO3Dmarketing)
- SNS(인스타·틱톡): 스캔 영상, 환자 반응 before/after
- QR 랜딩페이지: inno3dental.com 기반, 데모 신청 폼 연결

### 오프라인 (전시회)
- 완료: SIDEX 2026 (방문628·상담29·계약2), AEEDC 두바이(45건)
- 계획: 두바이, 뉴욕, IDS (독일)
- 필수 자료: 리플렛(한/영/일), 데모 스크립트, QR 코드, 루프 슬라이드

### 해외 디지털
- LinkedIn: 딜러·치과 의사 타겟 케이스 스터디
- 이메일: 딜러 팔로업 (영어 기준, 일본어 별도)

---

## 5. AI 이미지 프롬프트 프레임 (Densflo Scan 시각화)

```
교합면 스캔으로 버컬·링궐 커버 표현:
"A professional dental marketing illustration showing an intraoral 
scanner tip positioned directly above the occlusal surface. A wide, 
fan-shaped blue light beam radiates downward, visibly wrapping around 
both buccal and lingual surfaces simultaneously. Clean clinical 
background. Style: high-end medical product visualization. 
Color palette: white, light blue, soft pink, silver."
--ar 16:9 --style raw --v 6.1
```

---

## 6. 전시회 마케팅 체크리스트 (SIDEX 학습 반영)

- [ ] 루프 슬라이드 6장 (PPT → PDF)
- [ ] 데모 스크립트 (6단계, 5분)
- [ ] 응대 Q&A 시트 (방문자 유형 4가지)
- [ ] QR 랜딩페이지 활성화 확인
- [ ] 리플렛 (한국어+영어+일본어)
- [ ] 영문 견적서 출력본
- [ ] 메모지+펜 (연락처 수집용)

## 관련 스킬 연계
- 영업 전략 → `dental-sales-strategy`
- 교육 자료 → `dental-education-training`
- pptx → pptx 스킬 / docx → docx 스킬
