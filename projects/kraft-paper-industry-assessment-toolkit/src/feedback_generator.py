from __future__ import annotations

from typing import Any, Dict, List


def qualitative_concept(final_score: float) -> str:
    if final_score >= 9.0:
        return "Excelente"
    if final_score >= 7.0:
        return "Boa"
    if final_score >= 5.0:
        return "Regular"
    if final_score >= 3.0:
        return "Fraca"
    return "Insuficiente"


def build_summary(evaluation: Dict[str, Any], bonus: float = 0.0) -> Dict[str, Any]:
    base_score = float(evaluation["base_score"])
    final_score = min(10.0, round(base_score + bonus, 2))
    return {
        "base_score": base_score,
        "bonus": bonus,
        "final_score": final_score,
        "concept": qualitative_concept(final_score),
    }


def markdown_feedback(evaluation: Dict[str, Any], bonus: float = 0.0) -> str:
    summary = build_summary(evaluation, bonus)
    lines: List[str] = []
    lines.append(f"# Devolutiva técnica preliminar")
    lines.append("")
    lines.append(f"Nota base sugerida: **{summary['base_score']:.2f} / 10,0**")
    lines.append(f"Bonificação sugerida: **+{summary['bonus']:.2f} / 0,5**")
    lines.append(f"Nota final sugerida: **{summary['final_score']:.2f} / 10,0**")
    lines.append(f"Conceito qualitativo: **{summary['concept']}**")
    lines.append("")
    lines.append("> Esta saída é preliminar e deve ser validada pelo avaliador.")
    lines.append("")

    for item in evaluation["results"]:
        lines.append(f"## {item['item']}. {item['name']} - {item['suggested_score']} / {item['max_score']}")
        lines.append(item["feedback"])
        lines.append("")

    return "\n".join(lines)
