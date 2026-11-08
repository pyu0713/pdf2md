# pdf2md

영어 논문 PDF를 Markdown(.md)으로 바꿔 주는 도구입니다.
수식은 LaTeX로, 그림은 이미지 파일로 저장됩니다. RAG 전처리용으로 만들었습니다.

변환 엔진은 [MinerU](https://github.com/opendatalab/MinerU) 4.1.7을 사용합니다.

## 준비물
- Windows 10 / 11
- 인터넷 연결 (설치할 때만)
- 디스크 여유 공간: basic 약 2GB, standard 약 3GB
- 메모리(RAM) 16GB 이상 권장

## 1. 내려받기
1. 이 페이지 위쪽의 초록색 **Code → Download ZIP**을 누릅니다.
2. 압축을 **영어로만 된 짧은 경로**에 풉니다. 예: `C:\pdf2md`

> ⚠️ 경로에 **한글이나 공백**이 있으면 안 됩니다. `바탕 화면`, `문서` 폴더도 피해 주세요.
> 설치한 뒤에는 폴더를 **옮기지 마세요.**

## 2. 설치 (처음 한 번)
작업 관리자(Ctrl+Shift+Esc) → **성능** 탭에서 GPU를 확인하세요.

| 내 PC | 실행할 파일 | 다운로드 |
|---|---|---|
| NVIDIA·AMD 그래픽카드 있음 | `install_standard.bat` | 약 2.1GB |
| 그래픽카드 없음 | `install_basic.bat` | 약 0.9GB |

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

## 보안·개인정보
- 변환은 **내 PC 안에서만** 진행됩니다. 논문이 외부 서버로 올라가지 않습니다.
- 모델은 **Hugging Face에서만** 받도록 고정했습니다.
- MinerU의 사용 통계 전송 기능은 **꺼 두었습니다.**
- 설치되는 모든 것(uv, Python, 모델)은 이 폴더 안에만 저장됩니다.
- MinerU는 중국 상하이 AI 연구소(OpenDataLab)가 만든 오픈소스입니다.

## 저작권 주의
- 구독 논문의 PDF와 변환 결과는 **본인만** 사용하세요. 다른 사람과 공유하지 마세요.
- MinerU 웹 버전(mineru.net)에는 구독 논문을 올리지 마세요.

## 삭제
`pdf2md` 폴더를 통째로 지우면 끝입니다.

## 문제 해결
| 증상 | 해결 |
|---|---|
| 경로에 한글이나 공백이 있다고 나옴 | `C:\pdf2md`처럼 영어 경로로 폴더를 옮기고 다시 설치 |
| 설치 중 다운로드 실패 | 인터넷을 확인하고 같은 install 파일을 다시 실행 (끝난 단계는 건너뜀) |
| GPU 없는 PC인데 standard로 설치해서 느림 | `.mineru\models\MinerU2.5-Pro-2605-1.2B-GGUF` 폴더를 지우면 basic으로 변환됨 |
| 폴더를 옮긴 뒤 변환이 안 됨 | `.venv`, `.uv` 폴더를 지우고 다시 설치 |

## 알려진 문제
- 일부 PDF에서 **표 머리글의 그리스 문자**(ρ, τ, λ 등)가 다른 알파벳으로 바뀔 수 있습니다. 본문의 수식은 정상입니다.

## 참고
- MinerU: https://github.com/opendatalab/MinerU (MinerU Open Source License)
- MinerU2.5 논문: *MinerU2.5: A Decoupled Vision-Language Model for Efficient High-Resolution Document Parsing*, ACL 2026 Industry Track
- 이 저장소의 스크립트: MIT License
