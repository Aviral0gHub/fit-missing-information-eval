# Blind spot: confidence under silent missing information

While building CalibCheck, I studied whether a model's stated confidence matched its accuracy. One limitation kept bothering me: every question had been written to have a clean answer. In normal use, a question can be missing one fact that completely changes the decision. The model then has to notice the gap rather than confidently fill it in.

I tested this with `Qwen/Qwen3-4B-Instruct-2507`, a 4B open-weight instruction model. I created 20 short policy situations based on familiar decisions such as exam eligibility, scholarships, refunds, lab access, project submissions, and model deployment. Each had a complete version, an underspecified version with one required fact removed, and a misleading version that was still incomplete but contained positive irrelevant details.

My first run was an important negative result. The incomplete cases explicitly said when information was not provided, and the instruction warned the model not to assume missing facts. It got all 60 decisions right and reduced its confidence sharply on incomplete questions.

I then removed those explicit cues and used a neutral instruction. The complete cases remained unchanged, and the model still got all 20 correct. On the underspecified cases, accuracy fell to 50%. On the misleading cases, it fell to 40%. Across the 40 incomplete cases, the model gave an unsupported yes or no 22 times. Twenty-one of those errors had confidence of at least 80, and the average confidence on wrong incomplete answers was 96.6.

The main gap was not that the model could never identify missing information. It could do so perfectly when prompted like an evaluator. The problem was that this behavior did not survive a more ordinary interaction where the missing condition was simply absent. For a scholarship requiring both a sufficient CGPA and no active backlogs, the model approved a student based only on CGPA with confidence 100 and claimed that nothing was missing.

I would address this with contrast-balanced data built around decision rules. Each rule should have fully specified positive and negative cases, cases where either required condition is silently omitted, and incomplete cases padded with persuasive but irrelevant details. I would use supervised fine-tuning followed by preference training that rewards naming the missing condition over guessing. I would also penalize high confidence when an answer depends on an unstated assumption. Evaluation should report clarification rate, unsupported commitment rate, and confidence on errors, because aggregate accuracy alone would hide this failure.

This is a small synthetic study with one model, and the follow-up changed both the prompt and the wording cues. I see it as a focused demonstration rather than a prevalence estimate. The next step would be to separate those changes, add human-written cases, and compare several models.

