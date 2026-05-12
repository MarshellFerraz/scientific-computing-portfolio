from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from rubric_engine import KraftRubricEngine, RubricCriterion


def test_engine_detects_expected_terms():
    criteria = [RubricCriterion(1, "Teste", 1.0, ["licor branco", "NaOH"])]
    engine = KraftRubricEngine(criteria)
    result = engine.evaluate("O licor branco contém NaOH e Na2S.")
    assert result["base_score"] == 1.0
