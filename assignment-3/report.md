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
## Task 3: Conducting the evaluation
## Task 4: Quantitative analysis
## Task 5: Reflection and recommendations
