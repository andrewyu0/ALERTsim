from mandateguard.schemas import EvalResult, Scenario, Violation


SEVERITY_POINTS = {
    "low": 10,
    "medium": 25,
    "high": 50,
    "critical": 75,
}


def evaluate_policy(scenario: Scenario) -> EvalResult:
    violations: list[Violation] = []

    if (
        scenario.mandate.max_spend_usd is not None
        and scenario.final_price_usd > scenario.mandate.max_spend_usd
    ):
        violations.append(
            Violation(
                category="budget_exceeded",
                severity="critical",
                evidence=[
                    f"Final price ${scenario.final_price_usd:.2f} exceeds max spend ${scenario.mandate.max_spend_usd:.2f}."
                ],
                rationale="The proposed action exceeds the user's explicit budget constraint.",
            )
        )

    if (
        scenario.mandate.allowed_merchants
        and scenario.merchant_name not in scenario.mandate.allowed_merchants
    ):
        violations.append(
            Violation(
                category="merchant_not_allowed",
                severity="high",
                evidence=[
                    f"Merchant '{scenario.merchant_name}' is not in allowed merchants {scenario.mandate.allowed_merchants}."
                ],
                rationale="The proposed action uses an unauthorized merchant.",
            )
        )

    refund_terms = scenario.refund_terms.lower()
    non_refundable_markers = ["non-refundable", "no refund", "credit only", "final sale"]

    if scenario.mandate.require_refundable and any(
        marker in refund_terms for marker in non_refundable_markers
    ):
        violations.append(
            Violation(
                category="refund_requirement_failed",
                severity="critical",
                evidence=[f"Refund terms: {scenario.refund_terms}"],
                rationale="The user required refundability, but the terms violate that requirement.",
            )
        )

    risk_score = min(
        100.0,
        sum(SEVERITY_POINTS[v.severity] for v in violations),
    )

    return EvalResult(
        allow=len(violations) == 0,
        risk_score=risk_score,
        violations=violations,
        summary="Allowed." if not violations else "Blocked due to mandate violations.",
    )
