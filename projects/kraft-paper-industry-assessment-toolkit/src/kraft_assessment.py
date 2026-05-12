from __future__ import annotations

import argparse
import json
from pathlib import Path

from rubric_engine import KraftRubricEngine, load_criteria
from feedback_generator import markdown_feedback


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate a Kraft pulp and paper student report.")
    parser.add_argument("answer_file", help="Path to a .txt or .md student answer.")
    parser.add_argument("--rubric", default="rubric/criterios_avaliacao.json", help="Rubric JSON file.")
    parser.add_argument("--bonus", type=float, default=0.0, help="Positive-only technical bonus, max +0.5.")
    parser.add_argument("--json", dest="json_output", help="Optional JSON output path.")
    parser.add_argument("--markdown", dest="markdown_output", help="Optional Markdown feedback output path.")
    args = parser.parse_args()

    answer = Path(args.answer_file).read_text(encoding="utf-8")
    criteria = load_criteria(args.rubric)
    engine = KraftRubricEngine(criteria)
    evaluation = engine.evaluate(answer)

    if args.json_output:
        Path(args.json_output).write_text(json.dumps(evaluation, ensure_ascii=False, indent=2), encoding="utf-8")

    md = markdown_feedback(evaluation, bonus=min(args.bonus, 0.5))
    if args.markdown_output:
        Path(args.markdown_output).write_text(md, encoding="utf-8")
    else:
        print(md)


if __name__ == "__main__":
    main()
