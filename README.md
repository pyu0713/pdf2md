# pdf2md

영어 논문 PDF를 Markdown(.md)으로 바꿔 주는 도구입니다.
수식은 LaTeX로, 그림은 이미지 파일로 저장됩니다. 
RAG 전처리용으로, MinerU를 간편하게 다운로드 받을 수 있도록 필요한 코드만 구성하였습니다.

설치 과정 (install 파일이 자동으로 처리)
1. uv(설치 도구)와 Python 3.12 다운로드
2. 가상 환경 생성
3. MinerU 4.1.7 설치
4. AI 모델 다운로드 (basic 또는 standard)

위 과정을 `install_basic.bat` / `install_standard.bat` 더블클릭 한 번으로 처리합니다.

[MinerU](https://github.com/opendatalab/MinerU) 4.1.7을 사용합니다.

## 준비물
- Windows 10 / 11
- 인터넷 연결 (설치할 때만)
- 디스크 여유 공간: basic 약 3GB, standard 약 4GB

## 1. 내려받기
1. 이 페이지 위쪽의 초록색 **Code → Download ZIP**을 누릅니다.
2. 압축을 **영어로만 된 경로**에 풉니다. 예: `C:\pdf2md`

> ⚠️ 경로에 **한글이나 공백**이 있으면 안 됩니다. `바탕 화면`, `문서` 폴더도 피해 주세요.
> 설치한 뒤에는 폴더를 **옮기지 마세요.**

## 2. 설치 (처음 한 번)
작업 관리자(Ctrl+Shift+Esc) → **성능** 탭에서 GPU를 확인하세요.

| 내 PC | 실행할 파일 | 다운로드 |
|---|---|---|
| NVIDIA·AMD 그래픽카드 (외장) 있음 | `install_standard.bat` | 약 2.1GB |
| 그래픽카드 없음 | `install_basic.bat` | 약 0.9GB |


그래픽 카드가 없는 경우에도 standard 사용 가능하지만 실행 시간이 오래걸릴 수 있습니다.
더블클릭하면 설치가 자동으로 진행됩니다. 10~30분 걸릴 수 있습니다.

> "Windows의 PC 보호" 창이 뜨면 **추가 정보 → 실행**을 누르세요.

## 3. 변환
1. `papers` 폴더에 PDF를 넣습니다. 파일 이름은 영어를 권장합니다.
2. `convert.bat`을 더블클릭합니다.
3. 결과는 `output` 폴더에 생깁니다.

```
output\
├─ 논문이름\
│   ├─ 논문이름.md
│   └─ images\
└─ _raw\        (원본 결과 보관)
```
- 이미 변환한 논문은 다시 실행해도 건너뜁니다.
- 논문 이름이 80자를 넘으면 잘려서 저장됩니다.
- `papers` 바로 아래의 PDF만 변환됩니다. 하위 폴더 안 PDF는 무시됩니다.

## 보안·개인정보
- 변환은 **내 PC 안에서만** 진행됩니다. 논문이 외부 서버로 올라가지 않습니다.
- 모델은 **Hugging Face에서만** 받도록 고정했습니다.
- MinerU의 사용 통계 전송 기능은 **꺼 두었습니다.**
- 프로그램(uv, Python, MinerU)과 모델은 이 폴더 안에만 설치됩니다.
- MinerU는 중국 상하이 AI 연구소(OpenDataLab)가 만든 오픈소스입니다.

## 저작권 주의
- 구독 논문의 PDF와 변환 결과는 **본인만** 사용하세요. 다른 사람과 공유하지 마세요.
- MinerU 웹 버전(mineru.net)에는 구독 논문을 올리지 마세요.


## 일부 테스트에서 보였던 문제
- 일부 PDF에서 **표 머리글의 그리스 문자**(ρ, τ, λ 등)가 다른 알파벳으로 바뀔 수도 있습니다. 본문 수식은 정상입니다. 표 머리글은 원본 PDF와 대조 권장드립니다.

## 참고
- MinerU: https://github.com/opendatalab/MinerU (MinerU Open Source License)
- MinerU2.5 논문: *MinerU2.5: A Decoupled Vision-Language Model for Efficient High-Resolution Document Parsing*, ACL 2026 Industry Track
- 이 저장소의 스크립트: MIT License
