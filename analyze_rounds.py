from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent


def load_round(name):
    return pd.read_csv(ROOT / name / "results.csv")


control = load_round("round1_explicit_control")
implicit = load_round("round2_implicit_neutral")

rows = []
for round_name, data in [
    ("explicit_control", control),
    ("implicit_neutral", implicit),
]:
    for variant, group in data.groupby("variant"):
        rows.append(
            {
                "round": round_name,
                "variant": variant,
                "n": len(group),
                "accuracy": group["correct"].mean(),
                "mean_confidence": group["confidence"].mean(),
                "unsupported_commitment_rate": group[
                    "unsupported_commitment"
                ].mean(),
                "high_confidence_error_rate": group[
                    "high_confidence_error"
                ].mean(),
            }
        )

comparison = pd.DataFrame(rows)
print(comparison.to_string(index=False))

incomplete = implicit[implicit["variant"] != "complete"]
print("\nImplicit neutral round, incomplete cases")
print(f"Unsupported commitments: {int(incomplete['unsupported_commitment'].sum())}/{len(incomplete)}")
print(f"High-confidence errors: {int(incomplete['high_confidence_error'].sum())}/{len(incomplete)}")
print("\nConfidence by correctness")
print(incomplete.groupby("correct")["confidence"].agg(["count", "mean", "median", "min", "max"]))

comparison.to_csv(ROOT / "round_comparison.csv", index=False)

