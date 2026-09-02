#!/usr/bin/env python3
"""Validate the DesignForge repository without external dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    ".gitignore",
    ".gitattributes",
    ".github/workflows/ci.yml",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/pull_request_template.md",
    "examples/ecommerce.md",
    "examples/landing-page.md",
    "examples/dashboard.md",
    "examples/ai-app.md",
    "templates/page-spec.md",
    "templates/design-review.md",
]

PLACEHOLDER_PATTERNS = [
    re.compile(r"github\.com/yourusername", re.IGNORECASE),
    re.compile(r"\bTODO_REPOSITORY_URL\b", re.IGNORECASE),
    re.compile(r"\bPASTE_TOKEN_HERE\b", re.IGNORECASE),
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |DSA |EC |)PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{32,}\b"),
    re.compile(r"(?i)(api[_-]?key|access[_-]?token|client[_-]?secret|password)\s*[:=]\s*['\"][^'\"\s]{12,}['\"]"),
]

SECRET_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "id_rsa",
    "id_ed25519",
}

MARKDOWN_LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def iter_text_files() -> list[Path]:
    ignored_dirs = {".git", "__pycache__", "node_modules", ".pytest_cache"}
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in ignored_dirs for part in path.relative_to(ROOT).parts):
            continue
        files.append(path)
    return sorted(files)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_required_files(errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")


def check_skill_frontmatter(errors: list[str]) -> None:
    skill = ROOT / "SKILL.md"
    if not skill.is_file():
        return
    text = read_text(skill)
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter.")
        return
    end = text.find("\n---", 4)
    if end == -1:
        errors.append("SKILL.md frontmatter is not closed.")
        return
    frontmatter = text[4:end]
    if "name: designforge" not in frontmatter:
        errors.append("SKILL.md frontmatter must include `name: designforge`.")
    if "description:" not in frontmatter:
        errors.append("SKILL.md frontmatter must include a description.")


def check_placeholders_and_secrets(errors: list[str]) -> None:
    for path in iter_text_files():
        relative = path.relative_to(ROOT).as_posix()
        if path.name in SECRET_FILE_NAMES:
            errors.append(f"Secret-like file should not be committed: {relative}")
        try:
            text = read_text(path)
        except UnicodeDecodeError:
            continue
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(text):
                errors.append(f"Placeholder text found in {relative}: {pattern.pattern}")
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                errors.append(f"Potential secret found in {relative}: {pattern.pattern}")


def normalize_link_target(raw_target: str) -> str | None:
    target = raw_target.strip()
    if not target or target.startswith("#"):
        return None
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        return None
    target = target.split("#", 1)[0]
    if not target:
        return None
    return target.replace("%20", " ")


def check_markdown_links(errors: list[str]) -> None:
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = read_text(path)
        for match in MARKDOWN_LINK_PATTERN.finditer(text):
            target = normalize_link_target(match.group(1))
            if target is None:
                continue
            target_path = (path.parent / target).resolve()
            try:
                target_path.relative_to(ROOT)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)} links outside repository: {match.group(1)}")
                continue
            if not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)} has broken link: {match.group(1)}")


def check_readme_claims(errors: list[str]) -> None:
    readme = ROOT / "README.md"
    if not readme.is_file():
        return
    text = read_text(readme)
    for example in ["ecommerce.md", "landing-page.md", "dashboard.md", "ai-app.md"]:
        if example not in text:
            errors.append(f"README.md should reference examples/{example}.")
    if "python scripts/validate_repository.py" not in text:
        errors.append("README.md should document repository validation.")


def validate() -> list[str]:
    errors: list[str] = []
    check_required_files(errors)
    check_skill_frontmatter(errors)
    check_placeholders_and_secrets(errors)
    check_markdown_links(errors)
    check_readme_claims(errors)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("DesignForge repository validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1
    print("DesignForge repository validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
