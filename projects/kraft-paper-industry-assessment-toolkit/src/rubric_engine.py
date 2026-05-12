from __future__ import annotations

from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Dict, List
import json
import re
import unicodedata


@dataclass
class RubricCriterion:
    item: int
    name: str
    max_score: float
    expected_terms: List[str]
    required_concepts: List[str] = field(default_factory=list)


@dataclass
class CriterionResult:
    item: int
    name: str
    max_score: float
    suggested_score: float
    found_terms: List[str]
    missing_terms: List[str]
    feedback: str


class KraftRubricEngine:
    """Rule-based preliminary evaluator for Kraft pulp and paper reports.

    The engine is designed for triage and feedback standardization. It does not
    replace the instructor's technical judgment.
    """

    def __init__(self, criteria: List[RubricCriterion]):
        self.criteria = criteria

    @staticmethod
    def normalize(text: str) -> str:
        text = unicodedata.normalize("NFKD", text)
        text = "".join(ch for ch in text if not unicodedata.combining(ch))
        text = text.lower()
        text = re.sub(r"\s+", " ", text)
        return text

    @classmethod
    def contains_term(cls, normalized_text: str, term: str) -> bool:
        normalized_term = cls.normalize(term)
        return normalized_term in normalized_text

    def evaluate_criterion(self, text: str, criterion: RubricCriterion) -> CriterionResult:
        normalized = self.normalize(text)
        all_terms = criterion.expected_terms + criterion.required_concepts
        found = [term for term in all_terms if self.contains_term(normalized, term)]
        missing = [term for term in all_terms if not self.contains_term(normalized, term)]

        coverage = len(found) / max(len(all_terms), 1)
        raw_score = criterion.max_score * coverage

        # Avoid overclaiming: rule-based scoring is conservative.
        suggested_score = round(min(raw_score, criterion.max_score), 2)
        feedback = self.build_feedback(criterion, found, missing, suggested_score)

        return CriterionResult(
            item=criterion.item,
            name=criterion.name,
            max_score=criterion.max_score,
            suggested_score=suggested_score,
            found_terms=found,
            missing_terms=missing,
            feedback=feedback,
        )

    def evaluate(self, student_answer: str) -> Dict[str, Any]:
        results = [self.evaluate_criterion(student_answer, criterion) for criterion in self.criteria]
        base_score = round(sum(result.suggested_score for result in results), 2)
        return {
            "base_score": base_score,
            "results": [asdict(result) for result in results],
            "note": "Pontuação sugerida automaticamente; validar tecnicamente antes de usar como nota final.",
        }

    @staticmethod
    def build_feedback(
        criterion: RubricCriterion,
        found: List[str],
        missing: List[str],
        score: float,
    ) -> str:
        if score >= 0.8 * criterion.max_score:
            level = "bom domínio"
        elif score >= 0.5 * criterion.max_score:
            level = "domínio parcial"
        else:
            level = "domínio insuficiente"

        found_text = ", ".join(found) if found else "nenhum elemento central identificado"
        missing_text = ", ".join(missing) if missing else "sem lacunas principais detectadas"
        return (
            f"O item '{criterion.name}' apresenta {level}. "
            f"Elementos identificados: {found_text}. "
            f"Elementos a complementar: {missing_text}."
        )


def load_criteria(path: str | Path) -> List[RubricCriterion]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return [RubricCriterion(**item) for item in data["criteria"]]
