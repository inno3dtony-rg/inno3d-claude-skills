---
name: inno3d-dental-master
description: >
  이노쓰리디(INNO3D) 김민선 과장의 모든 치과 업무를 처리하는 통합 마스터 스킬.
  구강 스캐너(Densflo Scan/Codi) 관련 영업전략·마케팅기획·시장분석·교육훈련·기술지원·비즈니스개발·
  딜러관리·팔로업이메일·수출서류·회의록·번역(한영일)·가격정책·MOQ·임상테스트·CRM·전시회·
  리드관리·제안서·ROI계산·경쟁사분석·일본시장·이란·러시아·터키·품의서·지출결의서·다우오피스 관련
  모든 요청에 자동 호출. 요청이 여러 영역에 걸치거나 어느 하위 스킬을 써야 할지 애매할 때도 이 스킬을 먼저 호출한다.
  키워드: 이노쓰리디, Densflo, 구강 스캐너, intraoral scanner, IOS, 치과, dental, 영업, sales,
  마케팅, marketing, 딜러, dealer, 팔로업, follow-up, 교육, training, 기술지원, technical support,
  임상, clinical, 시장분석, market analysis, 일본, Japan, 이란, Iran, 러시아, Russia, 터키, Turkey,
  수출, export, MOQ, 가격, price, 계약, contract, 전시회, exhibition, SIDEX, 리드, lead, 제안서,
  proposal, 회의록, minutes, 번역, translation, 슬로건, slogan, CE, MFDS, ISO, 품의서, 지출결의서
---

# 이노쓰리디 통합 마스터 스킬

## 핵심 컨텍스트 (2026-09-16 최종 확정)
**회사**: ㈜이노쓰리디(INNO3D), 서울 금천구 가산디지털1로 225, 1420호 | **담당**: 김민선 과장 | **발신**: sales@inno3d.co.kr | 02-6952-0693
**제품**: Densflo Scan(IDT-1000, 듀얼프로젝터, [확인필요] <5μm 정확도는 측정규격 미확보로 대외 사용 금지) + Densflo Codi(환자상담SW) + Hub/Agent/Design/LabView(특허출원중)
**인증**: MFDS 제26-4138호 ✅ / CE Class I(UDI-DI 880034629002625) ✅ / ISO13485(KM 26137) ✅ / **FDA 시설등록+리스팅 완료**(Reg.No. 3044774668, Status Active) — "FDA 승인/인증"은 절대 금지, "FDA 등록(리스팅)"만 허용(510(k) 면제 Class II) | **HS코드**: 9018.49.9000
**가격**: 단품 900만원 / 세트(스캐너+노트북+카트) 1,250만원 | 국내딜러 MOQ할인 20~40%(1~4세트20%/5~9 25%/10~19 30%/20~49 35%/50+ 40%, KPI충족시+3%p) | SW(Codi) 연사용료 없음(무기한 무료)
**슬로건**: "Innovation of Digital Dentistry by 3D Tech" (공식) | Codi 상담 메시지: "환자가 스스로 치료를 결정합니다"

---

## 하위 스킬 9개 — 자동 라우팅 표

요청 내용을 읽고 해당하는 스킬을 호출한다. **하나만 명확하면 그 스킬만, 여러 개 걸치면 아래 "충돌 시 우선순위" 규칙을 따른다.**

| # | 스킬명 | 담당 영역 |
|---|---|---|
| 1 | `dental-sales-strategy` | 영업 전략·제안서·팔로업·리드·가격협상·딜러계약 |
| 2 | `dental-marketing` | 마케팅 콘텐츠·전시회·브로셔·SNS·AI이미지프롬프트 |
| 3 | `global-dental-market-analysis` | 시장규모·경쟁사·CAGR·지역규제 분석 |
| 4 | `dental-education-training` | 교육 커리큘럼·매뉴얼·온보딩 |
| 5 | `dental-technical-support` | 고객 대응용 AS·트러블슈팅·임상평가 스프레드시트 |
| 6 | `dental-business-development` | 신규 딜러 확장·시장진입·CRM 구축 |
| 7 | `inno3d-admin-docs` | 품의서·지출결의서·다우오피스 |
| 8 | `inno3d-meeting-processing` | CLOVA 전사본 → 회의록 docx |
| 9 | `inno3d-clinical-dev-bridge` | 임상 관찰 → 개발팀 전달용 정량 지표 변환 |

## 충돌 시 우선순위 (여러 스킬이 동시에 걸릴 때)

| 상황 | 먼저 적용할 스킬 | 이유 |
|---|---|---|
| 회의 내용에 지출·품의 건이 섞임 | `inno3d-meeting-processing`으로 회의록 먼저 작성 → 그 안의 지출 건만 `inno3d-admin-docs` 형식으로 별도 섹션 처리 | 회의록과 결의서는 문서 성격이 달라 하나로 합치면 결재 상신 시 반려 위험 |
| 임상 이슈가 "고객 응대"와 "개발팀 전달"에 동시 해당 | 고객에게 나가는 답변은 `dental-technical-support`, 내부 개발팀 전달본은 `inno3d-clinical-dev-bridge` — **둘을 같은 문서에 섞지 않는다** | 고객용은 확정된 해결책만, 개발전달용은 미확정 측정값도 포함 — 대상이 다르면 노출 정보 수위가 다름 |
| 영업 제안서에 시장 통계 인용 필요 | `dental-sales-strategy`가 메인, 통계는 `global-dental-market-analysis`의 검증값 표에서만 인용 | 임의로 새 통계를 만들지 않기 위함 |
| 딜러 확장 전략 + 실제 계약 협상이 동시에 필요 | 전략 단계는 `dental-business-development`, 구체적 가격·조건 협상 문구는 `dental-sales-strategy` | 전자는 방향, 후자는 실행 문서 |
| 특강·딜러교육 자료에 제품 스펙 인용 | `dental-education-training`이 메인, 인증·가격 수치는 반드시 위 "핵심 컨텍스트" 확정값만 사용 | 교육자료가 대외 배포되면 컴플라이언스 문서와 동일한 기준 적용 |

## 공통 출력 원칙 (모든 하위 스킬에 적용)
1. **사실 프로토콜**: 불확실한 수치·정보는 "[확인 필요]" 명시. 최신성 필요한 주제는 먼저 웹 검색.
2. **모바일 기준**: 결론 먼저, 6~8줄 이내 시작.
3. **이메일 발신 표준**: 김민선 과장 / 이노쓰리디 / sales@inno3d.co.kr / 02-6952-0693
4. **미확인 항목**: [확인 필요] / [전언] / [추정] / [변동] 태그 사용, 임의 확정 금지.
5. **문서 초안**: "초안 v0.x — 내부 검토 전용" 워터마크.
6. **HTML/문서 출력**: 설명 없이 파일만.
7. **개인정보**: 후보자명·환자명·타사 내부사정은 익명화 또는 제외.
