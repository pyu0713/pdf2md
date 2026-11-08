@echo off
chcp 65001 > nul
setlocal
if "%~1"=="" (
    echo 이 파일은 직접 실행하지 마세요.
    echo install_basic.bat 또는 install_standard.bat을 실행하세요.
    pause
    exit /b 1
)
set "TIER=%~1"
cd /d "%~dp0.."
set "ROOT=%CD%"

rem 경로 검사: 한글, 공백 등 영어가 아닌 글자가 있으면 중단
powershell -NoProfile -Command "if ((Get-Location).Path -match '[^\x21-\x7E]') { exit 1 }"
if errorlevel 1 (
    echo [중단] 폴더 경로에 한글이나 공백이 있습니다: %ROOT%
    echo C:\pdf2md 처럼 영어로만 된 경로로 폴더를 옮긴 뒤 다시 실행하세요.
    goto :fail
)

rem 모든 설치를 이 폴더 안에만: uv, Python, 캐시, 모델
set "UV=%ROOT%\.uv\bin\uv.exe"
set "UV_UNMANAGED_INSTALL=%ROOT%\.uv\bin"
set "UV_PYTHON_INSTALL_DIR=%ROOT%\.uv\python"
set "UV_CACHE_DIR=%ROOT%\.uv\cache"
set "UV_MANAGED_PYTHON=1"
set "MINERU_HOME=%ROOT%\.mineru"
set "MINERU_MODEL_SOURCE=huggingface"
set "MINERU_TELEMETRY_DISABLED=1"

echo [1/4] uv 준비
if not exist "%UV%" (
    powershell -NoProfile -ExecutionPolicy Bypass -Command "[Net.ServicePointManager]::SecurityProtocol='Tls12'; irm https://astral.sh/uv/0.13.7/install.ps1 | iex"
    if not exist "%UV%" goto :fail
)

echo [2/4] Python 3.12 가상환경
if not exist ".venv\Scripts\python.exe" (
    "%UV%" venv --python 3.12 .venv || goto :fail
)

echo [3/4] MinerU 설치
"%UV%" pip install --python .venv\Scripts\python.exe -r _system\requirements.txt || goto :fail

echo [4/4] 모델 다운로드: %TIER%
.venv\Scripts\mineru-kit.exe models download --tier %TIER% --source huggingface || goto :fail
.venv\Scripts\mineru-kit.exe models verify --tier %TIER% || goto :fail

echo.
echo 설치 완료! papers 폴더에 PDF를 넣고 convert.bat을 실행하세요.
pause
exit /b 0

:fail
echo.
echo [실패] 설치 중 문제가 생겼습니다. 위 메시지를 확인하고 다시 실행해 보세요.
pause
exit /b 1