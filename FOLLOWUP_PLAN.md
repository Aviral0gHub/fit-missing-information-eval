# Follow-up after the first run

The first run produced a ceiling result. Qwen3-4B-Instruct-2507 answered all 60 examples correctly. It also reduced average confidence from 98 on complete cases to 33 on underspecified cases and 35 on misleading cases.

That does not support my original hypothesis under the tested conditions. It also leaves an important question. Every incomplete case explicitly said that a fact was "not provided" or "not stated," and the system instruction told the model not to assume missing facts. Those cues made the desired behavior unusually clear.

The follow-up keeps the policies, cases, expected answers, model, decoding settings, and metrics fixed. It changes two things:

1. Sentences explicitly announcing the missing information are removed. The required fact is simply absent.
2. The system prompt is neutral. It still allows `INSUFFICIENT`, but it does not warn the model about missing facts or define when to abstain.

The first run will remain in the final report as an explicit-instruction control. The follow-up tests whether the same behavior survives in a more ordinary interaction.

