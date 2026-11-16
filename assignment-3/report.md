# Assignment 3
 
## Task 1: Implementing interaction

I picked the Direction 1 chart from Assignment 2, the stacked bars showing whether visitors have tried the new items, and changed what it compares. Now each bar is an age group, split into people who tried at least one new item, people who heard of them but haven't tried, and people who haven't heard of them. This supports the question of whether awareness of the new items differs by age.

The two ways of reading these bars give different answers. If you count people, the biggest group is whichever age group is largest. If you look at share of each group, small groups can stand out. For example, 55+ has the most people who heard of the items but haven't tried them (7), but 45-54 has the biggest share (all 7 of them).

**Interactive version** (`interactive.html`): one chart with a switch between "Share of each age group" (every bar runs to 100%) and "Number of people" (each bar's length is the head count). The interaction is a change of aggregation, meant to help with tasks where you need to switch between comparing groups of different sizes and comparing how many people are in each category.

![Interactive version, Number of people selected](figures/interactive.png)

**Static version** (`static.html`): the same two views side by side, one showing shares and one showing counts, so everything the switch can show is visible at once. It uses the same data, colors, labels, and order. I did not remove or hide anything from it. The tradeoff is that it takes more room, and the reader has to look at the right chart for the question.

![Static version](figures/static.png)

Both versions use the same cleaned dataset (40 responses, `data/processed/survey_clean.csv`), and the three groups are defined the same way as in Assignment 2.


## Task 2: Evaluation design

**Question and hypothesis.** When people compare age groups on how they reacted to the new items, does switching between a "share" view and a "number of people" view in one chart (interactive) work better than seeing both views side by side (static)? My hypothesis is that accuracy will be about the same and that the interactive version will be faster, because it shows only the one view each question needs. Switching could also cost time, so either result is possible.

**Tasks.** There are two analytical tasks, each with two variants that use different parts of the data but need the same skill. In the first, people compare two age groups on a share, where the group with the larger head count is the wrong answer (for example, "which has the larger share who haven't heard of the new items: 18-24 or 55+?"; the answer is 18-24, 40% vs 33%). In the second, they add up head counts across three age groups, one of which has no bar because its value is zero (for example, "how many people aged 35 or older haven't heard of the new items?"; the answer is 6). Both tasks need more than reading one bar, and both are possible in either version. The full wording and expected answers for all four questions are in `study/protocol.md`.

**Design.** Within-subject: every participant uses both versions and answers four questions, two in each. Order is counterbalanced with four groups: static first or interactive first, crossed with which variant set goes with which version. Participants are assigned to groups in rotation, so each version is used first by half of them and each variant set appears equally in each version. The order of the two tasks inside a version is always the same.

**Measurements.** Accuracy (exact match with the expected answer) and completion time in seconds, plus a 1–5 confidence rating and notes on what I observe. Before starting, I fixed these rules: a 120-second limit per question; a timed-out or skipped question counts as wrong, with the time recorded as 120 (or the time they gave up); the last answer before saying "done" counts; nobody is told if an answer was right until the end.

**Procedure.** Same laptop and browser for everyone, with a fixed script: a short explanation of the chart, an unscored practice question in each version (including how the switch works), then the four questions, timed with a stopwatch. I aim for 12 participants who are not me, plus 1 or 2 pilot people who don't count. The protocol is frozen after the pilot, and changes made after it are listed in Task 3.


## Task 3: Conducting the evaluation

I ran 10 people through the study over a few days. Nine were university students I know, and I ran their sessions online over a video call. Most were in the Chicago area, and the rest were in Detroit, New York, Champaign, Seattle, Dubai, and London. The tenth was my brother. Each person used both versions and answered 4 questions, 2 in each version. Each group ended up with 2 or 3 people (group 1: 2, group 2: 3, group 3: 3, group 4: 2). The participant IDs don't follow the group order, because I numbered them after the sessions.

I did two pilot runs first. The first was me testing the setup, and the second was my cousin, who only speaks Spanish. I translated the questions and guided him, so that session wasn't run the way the study is supposed to be. I didn't count either pilot. Their rows are still in `study/results.csv` labeled PILOT01 and PILOT02, and the analysis ignores them. After the pilot I stopped guiding people and ran everyone the same way.

What I saw:
- One person said they first read "larger share" as a quantity, and another said the question was a mouthful to comprehend.
- My first pilot said it was hard to compare share sizes because the boxes aren't aligned together.
- One person preferred the interactive version because seeing one chart at a time was easier to take in.

## Task 4: Quantitative analysis

I counted an answer as correct only if it matched the expected one exactly. All the numbers come from `code/03_analysis.py` and `study/results.csv` (10 people, 20 answers per version). I didn't run any significance tests, because 10 people is too few to say much.

| | Static | Interactive |
|---|---|---|
| Task 1 (compare shares), correct | 3 of 10 | 2 of 10 |
| Task 1, median time | 20.0 s | 14.3 s |
| Task 2 (add up counts), correct | 8 of 10 | 6 of 10 |
| Task 2, median time | 13.7 s | 8.5 s |
| Both tasks, correct | 11 of 20 (55%) | 8 of 20 (40%) |
| Both tasks, median time | 15.5 s | 9.4 s |

![Accuracy](figures/accuracy.png)
![Completion time](figures/time.png)

**By task.** Interactive was faster in both tasks. It was also less accurate, by 1 answer in Task 1 and 2 answers in Task 2. That's too small to be sure about, but it looks like people moved faster in the interactive version and made more mistakes. All four wrong interactive answers in Task 2 came in under 9 seconds. Two of them were 17, which is the number of people aged 35 or older in a different category ("Heard of them, haven't tried"), so they read the wrong color. In the static version the wrong answers were 9 and 12, and 12 is what you get if you include the 45-54 group.

**By participant.** 6 of 10 people had a lower median time on the interactive version. For accuracy, 6 people got the same number right in both versions, 3 got more right on static, and only 1 got more right on interactive. So the speed gain wasn't universal (4 people were slower on interactive), and the small accuracy drop came from a few people, not everyone.

**Task 1 is the biggest result.** Only 5 of 20 answers were right, which is worse than guessing between two choices. All 15 wrong answers were the age group with the larger number of people (55+ nine times, 35-44 six times), so people were reading counts when I asked about share. That happened in both versions, so it says more about the question and the stacked bars than about static vs interactive.

**Hypothesis.** My guess was that accuracy would be about equal and the interactive version might be faster. The speed part held up. The accuracy part didn't clearly hold up, since interactive was lower, but with this many people I can't say it's a real difference.


## Task 5: Reflection and recommendations
