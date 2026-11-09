# Evaluation protocol

## What I'm testing

Does switching between a "share" view and a "number of people" view in one chart (interactive) work better than seeing both views side by side (static)?

My guess is that people will be about as accurate in both, but a little faster with the interactive one, since it only shows the view the question needs. It could also go the other way, because switching adds a step.

## The two versions

- Static (`static.html`): two charts side by side. One shows the share of each age group, the other shows the number of people. No controls.
- Interactive (`interactive.html`): one chart with a "Show" switch between those same two views.

Both use the same data (`data/processed/survey_clean.csv`, 40 responses), colors, and labels.

## Questions

There are two tasks, and each has two versions (A and B) with different numbers but the same kind of thinking. The questions use the same names as the legend.

Task 1: compare two age groups on a share. The group with more people is the wrong answer, so you have to look at share.

- 1A: Which age group has the larger share of people in "Haven't heard of them": 18-24 or 55+?
  Answer: 18-24 (2 of 5 = 40%, vs 4 of 12 = 33%)
- 1B: Which age group has the larger share of people in "Heard of them, haven't tried": 35-44 or 18-24?
  Answer: 18-24 (2 of 5 = 40%, vs 3 of 9 = 33%)

Task 2: add up people across age groups. One of the three groups has none, so it has no bar.

- 2A: How many people aged 35 or older are in "Haven't heard of them"?
  Answer: 6 (2 + 0 + 4)
- 2B: How many people aged 44 or younger are in "Heard of them, haven't tried"?
  Answer: 5 (2 + 0 + 3)

I calculated these answers from the processed data. The answer to Task 1 is the same age group in both versions, so I'll watch for that in my notes.

## Who gets what

Everyone uses both versions and answers 4 questions, 2 in each version. In each version they get Task 1 first, then Task 2.

I split people into 4 groups and hand them out in order (first person to group 1, second to group 2, and so on):

| Group | Goes first | Static gets | Interactive gets |
|---|---|---|---|
| 1 | Static | A questions | B questions |
| 2 | Static | B questions | A questions |
| 3 | Interactive | B questions | A questions |
| 4 | Interactive | A questions | B questions |

That way half start with each version, and each set of questions is used equally in both.

I want 12 people (3 per group), and at least 10. Pilot people don't count. Anyone can take part except me.

## What I measure

For each person and each question:

- Correct or not (1 or 0). It has to match the expected answer exactly.
- Time in seconds, from when they see the question until they say their final answer. I use a stopwatch.
- Confidence from 1 to 5 (1 = guessing, 5 = sure), asked after each answer.
- Notes on anything I see, like looking at the wrong chart or asking what a bar means.

Rules I set before starting:

- 120 seconds is the limit for each question. If they hit it, it counts as wrong and the time is 120.
- If they say "I don't know", it counts as wrong and I record the time up to that point.
- If they change their answer, the last one counts.
- I don't say if an answer was right until the end.
- I don't change the questions or the pages once the real study starts.

## What I say and do

Same laptop and browser for everyone, full screen.

1. Welcome. "Thanks for helping. I'm testing the charts, not you. I'll time each question. If you get stuck, give your best answer."
2. Explain the chart. "This is a survey of Beggars Pizza visitors about the new menu items. Each bar is an age group. The colors show if they tried at least one new item, heard of them but haven't tried, or haven't heard of them. The number inside is how many people." Point at the legend. Explain that in the share view each bar goes to 100% of that age group, and in the number view the bar length is the number of people.
3. Practice, not scored, once per version: "How many people aged 25-34 tried at least one new item?" (answer: 2). In the interactive version, show them the switch and have them try it. I don't record these.
4. First version, two questions. Turn over the question card, start the stopwatch, stop when they give a final answer, ask for confidence. Then the next card.
5. Second version, same thing.
6. Wrap up. Ask which version was easier and if anything was confusing. Write down what they say.

It takes about 15 minutes.

## Recording

One row per person per question in `study/results.csv`. People are only listed as P01, P02, and so on. I don't save names or contact info.

## Pilot

I'll try it with 1 or 2 people first using the same script. I'm checking if the instructions make sense, if the questions are too easy or too hard, if anything breaks, and if either version makes a question impossible. Anything I change after the pilot goes in the report, then the protocol stays the same.
