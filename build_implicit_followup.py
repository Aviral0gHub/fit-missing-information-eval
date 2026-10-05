import re
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parent
data = pd.read_csv(ROOT / "ambiguity_eval.csv")


def remove_missing_signal(text):
    patterns = [
        r"\s+Her backlog status is not provided\.$",
        r"\s+His attendance is not provided\.$",
        r"\s+Her final-exam score is not provided\.$",
        r"\s+The submission time is not provided\.$",
        r"\s+The certificate submission time is not provided\.$",
        r"\s+Seat availability is not provided\.$",
        r"\s+His CGPA is not provided\.$",
        r"\s+The presenting author is not identified\.$",
        r"\s+The presence of an approved supervisor is not stated\.$",
        r"\s+Faculty approval is not mentioned\.$",
        r"\s+Participant consent is not described\.$",
        r"\s+The monitoring plan decision is not provided\.$",
        r"\s+Whether she accessed course material is not stated\.$",
        r"\s+Whether he has a student ID is not stated\.$",
        r"\s+The file format is not stated\.$",
        r"\s+His arrival time is not stated\.$",
        r"\s+The number of books she currently holds is not provided\.$",
        r"\s+The type of receipt is not stated\.$",
        r"\s+Submission of a reflection note is not stated\.$",
        r"\s+The student status of each member is not stated\.$",
    ]
    cleaned = text
    for pattern in patterns:
        cleaned = re.sub(pattern, "", cleaned)
    return cleaned


mask = data["variant"].isin(["underspecified", "misleading"])
data.loc[mask, "case"] = data.loc[mask, "case"].map(remove_missing_signal)
data["evaluation_round"] = "implicit_omission_neutral_prompt"

out = ROOT / "ambiguity_eval_implicit.csv"
data.to_csv(out, index=False)

remaining = data.loc[mask, "case"].str.contains(
    r"not provided|not stated|not mentioned|not described|not identified",
    case=False,
    regex=True,
)
if remaining.any():
    bad_ids = data.loc[mask].loc[remaining, "id"].tolist()
    raise ValueError(f"Explicit missing-information cues remain: {bad_ids}")

print(f"Wrote {len(data)} examples to {out}")
