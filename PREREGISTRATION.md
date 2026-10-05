# What I decided to measure before running the model

## Main question

If I remove one fact that is necessary to answer a question, will the model admit that it needs more information? I also want to know whether its confidence changes or whether it stays confident and fills in the gap itself.

## What I expect

I expect the model to answer some incomplete questions with a definite yes or no. I think this will happen more often when the prompt contains positive but irrelevant details that make one answer feel natural.

## Dataset

- 20 base policy scenarios
- 3 matched variants per scenario
- 60 prompts in total
- 10 complete cases with expected answer YES
- 10 complete cases with expected answer NO
- 20 underspecified cases with expected answer INSUFFICIENT
- 20 misleading cases with expected answer INSUFFICIENT

## What I will calculate

1. Accuracy for the complete, underspecified, and misleading versions.
2. How often an incomplete case receives a definite `YES` or `NO`.
3. Average confidence for each version.
4. How often the model is wrong with confidence of at least 80.
5. How confidence changes within the same situation after information is removed.

## How I will interpret it

I will treat the result as evidence for the blind spot only if all three of these happen:

- the model performs well on the complete questions
- it often gives `YES` or `NO` on the incomplete questions
- its confidence does not fall much after the required information is removed

If accuracy is low even when all the information is present, I cannot claim that missing information is the main problem. If the model usually answers `INSUFFICIENT` and lowers its confidence, then my original idea is not supported, and that is the result I will report.

## Fixed inference settings

- Model: `Qwen/Qwen3-4B-Instruct-2507`
- 4-bit NF4 loading
- Greedy decoding
- Maximum 80 generated tokens
- One fixed instruction prompt
- Required JSON response containing decision, confidence, and missing information
