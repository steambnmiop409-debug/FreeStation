#!/usr/bin/env python3
"""data/ai-papers/*.psv 를 읽어 docs/ai-papers/ 의 Markdown 문서와 catalog.csv 를 생성한다.

PSV 형식 (구분자 '|', 7개 필드)::

    id|year|authors|title|status|tags|summary

* id      : arXiv ID (예: 1706.03762) 또는 ``ext:<URL>`` (arXiv 에 없는 자료)
* status  : V = 이번 작업에서 웹 검색으로 ID·제목 일치를 확인, M = 기억 기반(개별 검증 미실시)
* '#@title:' / '#@intro:' / '#@section:' 로 시작하는 줄은 메타데이터, 그 외 '#' 줄은 주석.

사용법: python3 scripts/build_ai_papers.py
"""
import csv
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "ai-papers"
OUT = ROOT / "docs" / "ai-papers"

ARXIV_RE = re.compile(r"^(\d{4}\.\d{4,5}|[a-z\-]+(\.[A-Z]{2})?/\d{7})$")
STATUS_LABEL = {"V": "✅ 검증(V)", "M": "🔶 기억기반(M)"}


def parse_file(path):
    meta = {"title": path.stem, "intro": ""}
    sections = OrderedDict()
    current = "기타"
    errors = []
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#@"):
            key, _, value = line[2:].partition(":")
            key, value = key.strip(), value.strip()
            if key == "section":
                current = value
            elif key in meta:
                meta[key] = value
            else:
                errors.append(f"{path.name}:{lineno}: 알 수 없는 메타 키 '{key}'")
            continue
        if line.startswith("#"):
            continue
        fields = [f.strip() for f in line.split("|")]
        if len(fields) != 7:
            errors.append(f"{path.name}:{lineno}: 필드 수 {len(fields)} (7 필요)")
            continue
        pid, year, authors, title, status, tags, summary = fields
        if not (ARXIV_RE.match(pid) or pid.startswith("ext:")):
            errors.append(f"{path.name}:{lineno}: 잘못된 ID '{pid}'")
        if status not in STATUS_LABEL:
            errors.append(f"{path.name}:{lineno}: 잘못된 status '{status}'")
        if not re.fullmatch(r"\d{4}", year):
            errors.append(f"{path.name}:{lineno}: 잘못된 연도 '{year}'")
        if not summary or not title:
            errors.append(f"{path.name}:{lineno}: 제목/요약 비어 있음")
        sections.setdefault(current, []).append(
            dict(id=pid, year=year, authors=authors, title=title,
                 status=status, tags=tags, summary=summary)
        )
    return meta, sections, errors


def link(pid):
    if pid.startswith("ext:"):
        url = pid[4:]
        return f"[링크]({url})"
    return f"[arXiv:{pid}](https://arxiv.org/abs/{pid})"


def render_category(idx, meta, sections):
    n = sum(len(v) for v in sections.values())
    v = sum(1 for s in sections.values() for e in s if e["status"] == "V")
    lines = [f"# {idx:02d}. {meta['title']}", ""]
    if meta["intro"]:
        lines += [meta["intro"], ""]
    lines += [f"> 수록 {n}편 · 검증(V) {v}편 · 기억기반(M) {n - v}편", ""]
    lines += ["## 목차", ""]
    k = 0
    for name, entries in sections.items():
        lines.append(f"- **{name}** ({len(entries)}편)")
        for e in entries:
            k += 1
            lines.append(f"  - {k}. {e['title']} ({e['year']})")
    lines.append("")
    k = 0
    for name, entries in sections.items():
        lines += [f"## {name}", ""]
        for e in entries:
            k += 1
            lines += [
                f"### {idx:02d}-{k:02d}. {e['title']}",
                "",
                f"- **식별자**: {link(e['id'])}",
                f"- **연도 / 저자·기관**: {e['year']} / {e['authors']}",
                f"- **검증 상태**: {STATUS_LABEL[e['status']]}",
                f"- **태그**: {', '.join('`' + t.strip() + '`' for t in e['tags'].split(',') if t.strip())}",
                f"- **요약**: {e['summary']}",
                "",
            ]
    return "\n".join(lines)


def main():
    files = sorted(DATA.glob("*.psv"))
    if not files:
        sys.exit(f"데이터 파일이 없습니다: {DATA}")
    OUT.mkdir(parents=True, exist_ok=True)

    all_errors, seen, rows, summary_rows = [], {}, [], []
    for path in files:
        idx = int(path.stem.split("-")[0])
        meta, sections, errors = parse_file(path)
        all_errors += errors
        for cat_name, entries in sections.items():
            for e in entries:
                if e["id"] in seen:
                    all_errors.append(f"중복 ID {e['id']}: {seen[e['id']]} 와 {path.name}")
                seen[e["id"]] = path.name
                rows.append((path.stem, cat_name, e))
        out_name = f"{path.stem}.md"
        (OUT / out_name).write_text(render_category(idx, meta, sections), encoding="utf-8")
        n = sum(len(v) for v in sections.values())
        v = sum(1 for s in sections.values() for e in s if e["status"] == "V")
        summary_rows.append((idx, meta["title"], out_name, n, v))

    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        sys.exit(f"검증 실패: {len(all_errors)}건")

    with open(OUT / "catalog.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["category", "section", "id", "url", "year", "authors", "title", "status", "tags", "summary"])
        for cat, sec, e in rows:
            url = e["id"][4:] if e["id"].startswith("ext:") else f"https://arxiv.org/abs/{e['id']}"
            w.writerow([cat, sec, e["id"], url, e["year"], e["authors"], e["title"],
                        e["status"], e["tags"], e["summary"]])

    total = sum(r[3] for r in summary_rows)
    total_v = sum(r[4] for r in summary_rows)
    by_year = Counter(e["year"] for _, _, e in rows)
    readme = ["# 차세대 AI · 실험적 논문 자료 모음", "",
              f"총 **{total}편** (arXiv 외 자료 {sum(1 for _,_,e in rows if e['id'].startswith('ext:'))}편 포함) · "
              f"✅ 검증(V) {total_v}편 · 🔶 기억기반(M) {total - total_v}편", "",
              "## 읽는 법", "",
              "- 각 항목은 *식별자 / 연도·저자 / 검증 상태 / 태그 / 요약*으로 구성됩니다.",
              "- **✅ 검증(V)**: 이번 작업에서 웹 검색으로 식별자(arXiv ID 또는 DOI/URL)와 제목이 일치함을 확인한 항목입니다. "
              "요약은 가능한 한 검색으로 확인된 초록에 맞췄으나, 요약의 모든 문장을 원문과 대조한 것은 아닙니다(‘ID·제목만 확인’이라고 적은 항목은 내용 미검토).",
              "- **🔶 기억기반(M)**: 널리 인용되는 논문을 기억에 의존해 정리했고, 이번 작업에서 개별적으로 대조하지 않았습니다. "
              "인용 전에 링크의 제목·저자를 확인하세요.",
              "- 저자 칸은 제1저자 또는 소속 조직입니다. 수치(성능·규모)는 확인된 초록에 근거한 것만 적었습니다.",
              "- `catalog.csv` 는 전체 항목의 표 형식 사본입니다 (엑셀: UTF-8 BOM 포함).", "",
              "## 카테고리", "",
              "| # | 카테고리 | 편수 | 검증(V) |", "|---|---|---|---|"]
    for idx, title, fname, n, v in summary_rows:
        readme.append(f"| {idx:02d} | [{title}]({fname}) | {n} | {v} |")
    readme += [f"| | **합계** | **{total}** | **{total_v}** |", "",
               "## 연도 분포", "", "| 연도 | 편수 |", "|---|---|"]
    for y in sorted(by_year):
        readme.append(f"| {y} | {by_year[y]} |")
    readme += ["", "## 범위와 한계", "",
               "- 이 목록은 선별본이며 해당 분야 전체를 망라하지 않습니다. 검색에서 확인된 가장 최근 항목은 2026년 7월(ID 2607.*)이며, 그 이후 발표분과 이 목록에 없는 최신 논문은 누락되어 있을 수 있습니다.",
               "- 🔶(M) 항목은 표본 29건을 검색으로 대조했을 때 ID 불일치는 없었으나(제목 표기 1건 보정), 나머지는 개별 검증하지 않았습니다.",
               "- arXiv 직접 접근이 차단된 환경에서 웹 검색 결과로 대조했으므로, V 표기는 *ID–제목 일치*를 뜻하며 "
               "논문 본문 전체를 읽고 검토했다는 뜻이 아닙니다.",
               "- 같은 논문이 여러 버전(v1~vN)으로 개정되는 경우 수치가 달라질 수 있어, 구체 수치는 원문을 확인하세요.",
               "- 데이터 원본은 `data/ai-papers/*.psv` 이며, `python3 scripts/build_ai_papers.py` 로 문서를 다시 생성합니다.", ""]
    (OUT / "README.md").write_text("\n".join(readme), encoding="utf-8")
    print(f"완료: {total}편 (V {total_v}) → {OUT}")


if __name__ == "__main__":
    main()
