import pandas as pd
import altair as alt

d = pd.read_csv("study/results.csv")
d = d[~d["participant_id"].str.startswith("PILOT")].copy()
d["version"] = pd.Categorical(d["version"], ["static", "interactive"], ordered=True)
d["task_name"] = d["task"].map({"T1": "Task 1: compare shares", "T2": "Task 2: add up counts"})

print("participants:", d["participant_id"].nunique())
print(d.groupby("group")["participant_id"].nunique().to_dict())

summary = (d.groupby(["task_name", "version"], observed=True)
    .agg(n=("correct", "size"), correct=("correct", "sum"), accuracy=("correct", "mean"),
         median_time=("time_sec", "median"), mean_time=("time_sec", "mean"))
    .round(2).reset_index())
overall = (d.groupby("version", observed=True)
    .agg(n=("correct", "size"), correct=("correct", "sum"), accuracy=("correct", "mean"),
         median_time=("time_sec", "median"), mean_time=("time_sec", "mean"))
    .round(2).reset_index())
overall.insert(0, "task_name", "both tasks")
summary = pd.concat([summary, overall], ignore_index=True)
summary.to_csv("study/summary.csv", index=False)
print(summary.to_string(index=False))

per = d.groupby(["participant_id", "version"], observed=True)["time_sec"].median().unstack()
faster = (per["interactive"] < per["static"]).sum()
print("participants with a lower median time on interactive:", faster, "of", len(per))

wrong_t1 = d[(d["task"] == "T1") & (d["correct"] == 0)]
print("task 1 wrong answers:", wrong_t1["answer"].value_counts().to_dict())
print(d[(d["task"] == "T2") & (d["correct"] == 0)][["participant_id", "question_id", "version", "answer", "time_sec"]].to_string(index=False))

colors = alt.Scale(domain=["static", "interactive"], range=["#6baed6", "#fdae6b"])
d["task_name"] = d["task"].map({"T1": "Task 1: shares", "T2": "Task 2: counts"})
summary["task_name"] = summary["task_name"].replace({"Task 1: compare shares": "Task 1: shares", "Task 2: add up counts": "Task 2: counts"})
vsort = ["static", "interactive"]

tasks = ["Task 1: shares", "Task 2: counts"]

def acc_panel(t, first):
    a = summary[summary["task_name"] == t].copy()
    a["label"] = a["correct"].astype(int).astype(str) + " of " + a["n"].astype(str)
    base = alt.Chart(a).encode(x=alt.X("version:N", title=None, sort=vsort, axis=alt.Axis(labelAngle=0)))
    ytitle = "Share answered correctly" if first else None
    bars = base.mark_bar().encode(
        y=alt.Y("accuracy:Q", title=ytitle, scale=alt.Scale(domain=[0, 1]), axis=alt.Axis(format="%")),
        color=alt.Color("version:N", scale=colors, legend=None))
    text = base.mark_text(dy=-8).encode(y="accuracy:Q", text="label:N")
    return alt.layer(bars, text).properties(width=190, height=260, title=t)

alt.hconcat(*[acc_panel(t, i == 0) for i, t in enumerate(tasks)]).properties(
    title="Accuracy by version").save("figures/accuracy.png", scale_factor=2)

def time_panel(t, first):
    x = d[d["task_name"] == t]
    ytitle = "Time (seconds)" if first else None
    pts = alt.Chart(x).mark_circle(size=70, opacity=0.65).encode(
        x=alt.X("version:N", title=None, sort=vsort, axis=alt.Axis(labelAngle=0)),
        y=alt.Y("time_sec:Q", title=ytitle, scale=alt.Scale(domain=[0, 65])),
        color=alt.Color("version:N", scale=colors, legend=None),
        xOffset=alt.XOffset("jitter:Q")).transform_calculate(jitter="sin(datum.time_sec * 97)")
    med = alt.Chart(x).mark_tick(color="black", thickness=2.5, size=70).encode(
        x=alt.X("version:N", sort=vsort), y="median(time_sec):Q")
    return alt.layer(pts, med).properties(width=190, height=260, title=t)

alt.hconcat(*[time_panel(t, i == 0) for i, t in enumerate(tasks)]).properties(
    title="Time per question (black line = median)").save("figures/time.png", scale_factor=2)
