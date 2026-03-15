from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ScenarioDefinition:
    title: str
    scenario_id: str
    sessions: tuple[str, ...]
    evidence: tuple[str, ...]
    expected_classification: str | None
    expected_failure_classification: str | None
    boundary_conditions: tuple[str, ...]
    invalid_reasoning_patterns: tuple[str, ...]
    source_path: str

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class ContinuityChain:
    scenario: ScenarioDefinition
    evidence_types: tuple[str, ...]
    explicit_evidence_count: int
    has_boundary_violation: bool
    is_ambiguous: bool
    is_incomplete: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)


@dataclass(frozen=True)
class EvaluationResult:
    scenario_id: str
    source_path: str
    sessions: tuple[str, ...]
    evidence: tuple[str, ...]
    evidence_types: tuple[str, ...]
    classification: str | None
    failure_classification: str | None
    verdict: str
    expected_classification: str | None
    expected_failure_classification: str | None
    matched_expectation: bool

    def to_dict(self) -> dict[str, object]:
        return asdict(self)
