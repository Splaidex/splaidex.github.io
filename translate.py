import os
import yaml
import deepl
from pathlib import Path

API_KEY = os.getenv("DEEPL_API_KEY")
translator = deepl.Translator(API_KEY)

DOCS_DIR = Path("docs")


def translate_text(text):
    if not text or not text.strip():
        return text
    result = translator.translate_text(text, target_lang="EN-US")
    return result.text


def translate_md(filepath):
    content = filepath.read_text(encoding="utf-8")
    translated = translate_text(content)
    out_path = DOCS_DIR / (filepath.stem + ".en.md")
    out_path.write_text(translated, encoding="utf-8")
    print(f"Translated: {filepath.name} → {filepath.stem}.en.md")


def translate_yml():
    yml_path = DOCS_DIR / "projects.yml"
    with open(yml_path, encoding="utf-8") as f:
        data = yaml.safe_load(f)

    for project in data["projects"]:
        project["description_en"] = translate_text(project["description"])
        project["features_en"] = [translate_text(f) for f in project["features"]]

    with open(yml_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, default_flow_style=False)

    print("Translated: projects.yml")


if __name__ == "__main__":
    for md_file in DOCS_DIR.glob("*.md"):
        translate_md(md_file)

    translate_yml()

    print("Done!")