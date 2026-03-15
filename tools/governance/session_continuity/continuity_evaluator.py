from __future__ import annotations

from .continuity_chain_builder import build_chain
from .continuity_classifier import classify_chain
from .models import EvaluationResult, ScenarioDefinition


def evaluate_scenarios(scenarios: list[ScenarioDefinition]) -> list[EvaluationResult]:
    return [classify_chain(build_chain(scenario)) for scenario in scenarios]
