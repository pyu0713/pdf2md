import os, shutil, subprocess, zipfile
from urllib.parse import quote
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAPERS, OUTPUT = ROOT / "papers", ROOT / "output"
RAW, WORK = OUTPUT / "_raw", OUTPUT / "_work"
MD, IMG = OUTPUT / "md", OUTPUT / "images"

# 환경 설정: 프로젝트 폴더 안 모델만 사용, 사용 통계 전송 끄기
env = dict(os.environ,
           MINERU_HOME=str(ROOT / ".mineru"),
           MINERU_MODEL_SOURCE="local",
           MINERU_TELEMETRY_DISABLED="1")

# 티어: standard 모델이 있으면 standard, 없으면 basic
gguf = ROOT / ".mineru/models/MinerU2.5-Pro-2605-1.2B-GGUF"
tier = "standard" if any(gguf.glob("*.gguf")) else "basic"

def name_of(pdf):  # Windows 경로 길이 제한(260자) 때문에 80자로 자름
    return pdf.stem[:80].rstrip(" .")

# 이미 변환된 논문은 건너뜀
pdfs = sorted(PAPERS.glob("*.pdf"))
todo = [p for p in pdfs if not (MD / f"{name_of(p)}.md").exists()]
print(f"PDF {len(pdfs)}개 중 새로 변환 {len(todo)}개 / tier: {tier}")

if todo:
    # 새 PDF만 임시 폴더에 복사해서 한 번에 변환
    shutil.rmtree(WORK, ignore_errors=True)
    (WORK / "in").mkdir(parents=True)
    for p in todo:
        shutil.copy2(p, WORK / "in")
    subprocess.run([ROOT / ".venv/Scripts/mineru-kit.exe", "parse", WORK / "in",
                    "-o", WORK / "zips", "--tier", tier, "-f", "zip"], env=env)

    # zip → output/<논문이름>/<논문이름>.md + images/, 원본 zip은 _raw에 보관
    RAW.mkdir(parents=True, exist_ok=True)
    for p in todo:
        z, name = WORK / "zips" / f"{p.stem}.zip", name_of(p)
        if not z.exists():
            print(f"[실패] {p.name}")
            continue
        MD.mkdir(parents=True, exist_ok=True)
        (IMG / name).mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(z) as zf:
            for entry in zf.namelist():
                if entry == "markdown.md":
                    # 그림 링크를 images/x.jpg → ../images/논문이름/x.jpg 로 변경
                    md = zf.read(entry).decode("utf-8")
                    md = md.replace("](images/", f"](../images/{quote(name)}/")
                    (MD / f"{name}.md").write_bytes(md.encode("utf-8"))
                elif entry.startswith("images/") and not entry.endswith("/"):
                    (IMG / name / Path(entry).name).write_bytes(zf.read(entry))
        os.replace(z, RAW / f"{name}.zip")
        print(f"[완료] {name}")
    shutil.rmtree(WORK, ignore_errors=True)
