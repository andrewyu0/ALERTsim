from typing import Literal
from pydantic import BaseModel, Field


class Mandate(BaseModel):
    user_goal: str
    max_spend_usd: float | None = None
    allowed_merchants: list[str] = Field(default_factory=list)
    require_refundable: bool = False
    forbidden_actions: list[str] = Field(default_factory=list)


class Scenario(BaseModel):
    id: str
    name: str
    mandate: Mandate
    merchant_name: str
    advertised_price_usd: float
    final_price_usd: float
    refund_terms: str
    page_text: str
    expected_block: bool


class Violation(BaseModel):
    category: Literal[
        "budget_exceeded",
        "merchant_not_allowed",
        "refund_requirement_failed",
        "forbidden_action",
        "consent_ambiguity",
        "identity_mismatch",
        "deception_missed",
    ]
    severity: Literal["low", "medium", "high", "critical"]
    evidence: list[str]
    rationale: str


class EvalResult(BaseModel):
    allow: bool
    risk_score: float
    violations: list[Violation]
    summary: str
