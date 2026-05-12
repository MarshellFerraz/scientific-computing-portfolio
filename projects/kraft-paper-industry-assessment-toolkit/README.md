# Kraft Paper Industry Assessment Toolkit

Structured assessment framework and Python-assisted feedback generator for technical reports on integrated Kraft pulp and paper plants.

This project combines Chemical Engineering process knowledge, analytical rubrics, criterion-based scoring, and automated feedback generation to support consistent, transparent, and educationally useful grading.

## Purpose

The toolkit was designed for evaluating student technical reports on a complete integrated pulp and paper plant based on the Kraft process. The evaluation focuses on:

- sequential understanding of the industrial process;
- critical operating points in each unit operation;
- process variables and their effects on pulp, paper, chemical recovery, energy and productivity;
- objective feedback by criterion;
- reproducible document generation for individual student feedback.

## Rubric structure

The mandatory score is 10.0 points, distributed across nine criteria:

| Item | Criterion | Max. score |
|---:|---|---:|
| 1 | Integrated plant overview | 1.0 |
| 2 | Wood preparation | 1.0 |
| 3 | Kraft pulping / cooking | 1.5 |
| 4 | Washing, screening and pulp purification | 1.0 |
| 5 | Bleaching | 1.0 |
| 6 | Stock preparation and paper production | 1.5 |
| 7 | Chemical recovery and energy generation | 1.5 |
| 8 | Interdependence between stages and impact on product/processing | 1.0 |
| 9 | Organization, clarity and technical language | 0.5 |

A positive-only technical bonus of up to +0.5 may be applied for relevant additional industrial insight, such as safety, environmental control, qualitative mass/energy balances, productivity, energy consumption, closed loops or process stability. The absence of additional material does not reduce the score.

## Important assessment rule

Effluent treatment and environmental control must not be penalized if absent when they were not taught or explicitly required. When correctly discussed, they may be considered as additional evidence of systemic industrial understanding or as positive bonus.

## Repository structure

```text
kraft-paper-industry-assessment-toolkit/
├── README.md
├── rubric/
│   ├── rubrica_kraft_papel_celulose.md
│   ├── rubrica_kraft_papel_celulose.pdf
│   └── criterios_avaliacao.json
├── templates/
│   ├── template_devolutiva_aluno.docx
│   └── modelo_saida_devolutiva_exemplo.pdf
├── examples/
│   ├── exemplo_resposta_aluno_anonimizada.md
│   ├── exemplo_avaliacao_preenchida.md
│   └── exemplo_devolutiva_anonimizada.pdf
├── src/
│   ├── kraft_assessment.py
│   ├── rubric_engine.py
│   ├── feedback_generator.py
│   └── docx_report_builder.py
├── data/
│   ├── sample_student_answer.txt
│   └── sample_scores.json
├── tests/
│   └── test_rubric_engine.py
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python src/kraft_assessment.py data/sample_student_answer.txt --json data/sample_scores.json
```

## What the Python engine does

The Python engine is not intended to replace the evaluator. It provides a preliminary, auditable, keyword-and-concept-based assessment that helps standardize feedback. The final score must be validated by the instructor.

The engine:

1. loads the analytical rubric;
2. checks for expected technical concepts in the student's answer;
3. suggests criterion-level scores;
4. identifies missing technical elements;
5. generates structured feedback text;
6. can export the result as JSON for document generation.

## Suggested portfolio description

This project demonstrates the conversion of domain-specific Chemical Engineering knowledge into a structured assessment system. It combines industrial Kraft pulping and papermaking concepts with criterion-based grading, feedback standardization and Python automation for educational reporting.
