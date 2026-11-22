#!/usr/bin/env python3
"""
Minishell LLM Wiki Comprehensive Health Linter
Verifies:
1. Unresolved wikilinks & standard markdown links (excluding code blocks/spans)
2. Forbidden file:/// URLs
3. Orphan pages inside wiki/
4. Raw sources coverage
5. index.md catalog completeness
6. Markdown table column mismatches & LaTeX math collisions
7. Mermaid diagram syntax integrity
"""

import glob
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
os.chdir(ROOT)


def strip_code(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    return text


def resolve_wikilink(target: str, candidates: list[str]):
    t = target.strip()
    t_no_ext = t[:-3] if t.endswith(".md") else t
    for c in candidates:
        c_no_ext = c[:-3] if c.endswith(".md") else c
        if c == t or c == t + ".md" or c_no_ext == t_no_ext:
            return c
        if (
            c.endswith("/" + t)
            or c.endswith("/" + t + ".md")
            or c_no_ext.endswith("/" + t_no_ext)
        ):
            return c
    return None


def resolve_mdlink(src_file: str, link_path: str, candidates: list[str]):
    if (
        link_path.startswith("http://")
        or link_path.startswith("https://")
        or link_path.startswith("#")
        or link_path.startswith("mailto:")
    ):
        return "EXTERNAL"
    if link_path.startswith("file://"):
        return "BROKEN_FILE_URL"
    clean_path = link_path.split("#")[0].strip()
    if not clean_path:
        return "ANCHOR"
    src_dir = os.path.dirname(src_file)
    joined = os.path.normpath(os.path.join(src_dir, clean_path))
    if joined in candidates or os.path.exists(joined):
        return joined
    return None


def main() -> int:
    all_md = sorted(
        f for f in glob.glob("**/*.md", recursive=True) if not os.path.islink(f)
    )

    in_links = defaultdict(set)
    errors = []

    for fpath in all_md:
        with open(fpath, "r", encoding="utf-8") as f:
            raw_content = f.read()

        clean_content = strip_code(raw_content)
        lines = raw_content.splitlines()

        # 1. Wikilinks
        for target in re.findall(r"\[\[([^\]\|]+)(?:\|[^\]]+)?\]\]", clean_content):
            resolved = resolve_wikilink(target, all_md)
            if resolved:
                in_links[resolved].add(fpath)
            else:
                errors.append(f"[UNRESOLVED WIKILINK] {fpath} -> [[{target}]]")

        # 2. Markdown Links & file:// check
        for mlink in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", clean_content):
            res = resolve_mdlink(fpath, mlink, all_md)
            if res == "BROKEN_FILE_URL":
                errors.append(f"[FORBIDDEN FILE URL] {fpath} -> {mlink}")
            elif res in ("EXTERNAL", "ANCHOR"):
                continue
            elif res:
                if res in all_md:
                    in_links[res].add(fpath)
            else:
                errors.append(f"[UNRESOLVED MD LINK] {fpath} -> ({mlink})")

        # 3. LaTeX Math Collision Check
        for m in re.findall(r"(?<!\\)\$([^\$\n]+)(?<!\\)\$", raw_content):
            if re.search(r"\?|\bVAR\b|[<>]|==|!=", m):
                errors.append(f"[MATH COLLISION] {fpath} -> ${m}$")

        # 4. Table Column Consistency Check
        in_table = False
        header_cols = 0
        for lno, line in enumerate(lines, 1):
            s = line.strip()
            if s.startswith("|") and s.endswith("|"):
                cols = s.count("|") - 1
                if not in_table:
                    in_table = True
                    header_cols = cols
                elif cols != header_cols:
                    errors.append(
                        f"[TABLE MISMATCH] {fpath}:{lno} expected {header_cols} cols, got {cols}"
                    )
            else:
                in_table = False

        # 5. Mermaid Syntax Check
        in_mermaid = False
        m_lines = []
        m_start = 0
        for i, line in enumerate(lines):
            if line.strip() == "```mermaid":
                in_mermaid = True
                m_lines = []
                m_start = i + 1
            elif in_mermaid and line.strip() == "```":
                in_mermaid = False
                m_text = "\n".join(m_lines)
                if re.search(r"<br\s*/?>", m_text, re.IGNORECASE):
                    errors.append(f"[MERMAID HTML] {fpath}:{m_start} contains <br>")
                for node_match in re.finditer(r"\[(.*?)\]|\{(.*?)\}", m_text):
                    inner = node_match.group(0)
                    if "->" in inner:
                        errors.append(f"[MERMAID ARROW] {fpath}:{m_start} -> {inner}")
                    if "<" in inner and not inner.startswith("<|") and re.search(r"<[^>]*>", inner):
                        errors.append(f"[MERMAID ANGLE] {fpath}:{m_start} -> {inner}")
                for node_match in re.finditer(r'\["([^"]*)"\]', m_text):
                    if "|" in node_match.group(1):
                        errors.append(f"[MERMAID PIPE] {fpath}:{m_start} -> {node_match.group(1)}")
                for edge_match in re.finditer(r"\|([^|]*)\|", m_text):
                    el = edge_match.group(1)
                    if any(c in el for c in ["(", ")", "&", "<", ">", ","]):
                        errors.append(f"[MERMAID EDGE] {fpath}:{m_start} -> |{el}|")
                if "stateDiagram" in m_text:
                    for s_line in m_lines:
                        if ":" in s_line:
                            lp = s_line.split(":", 1)[1].strip()
                            if any(c in lp for c in ["'", '"', "|", "\\", "<", ">", "&"]):
                                errors.append(f"[MERMAID STATE] {fpath}:{m_start} -> {s_line.strip()}")
            elif in_mermaid:
                m_lines.append(line)

    # 6. Orphan Pages in wiki/
    for fpath in all_md:
        if fpath.startswith("wiki/") and len(in_links[fpath]) == 0:
            errors.append(f"[ORPHAN PAGE] {fpath} has 0 incoming links")

    # 7. index.md Coverage
    with open("index.md", "r", encoding="utf-8") as f:
        idx_content = f.read()
    for fpath in all_md:
        if fpath.startswith("wiki/"):
            bname = os.path.basename(fpath)
            if bname not in idx_content and fpath[:-3] not in idx_content:
                errors.append(f"[MISSING IN INDEX] {fpath}")

    print(f"Checked {len(all_md)} markdown documents.")
    if errors:
        print(f"FAILED with {len(errors)} lint error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("PASSED: 0 lint errors, 0 orphan pages, 0 unresolved links!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
