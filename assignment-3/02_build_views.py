import altair as alt
import pandas as pd

df = pd.read_csv("data/processed/survey_clean.csv")

age_order = ["18-24", "25-34", "35-44", "45-54", "55+"]
status_order = ["Tried at least one", "Heard of them, haven't tried", "Haven't heard of them"]
modes = ["Share of each age group", "Number of people"]

# one row per mode x age group x status
# in "share" mode a bar runs from 0 to 100% of that age group, in "number" mode it runs by head count
rows = []
for age in age_order:
    people = df[df["age_range"] == age]
    label = age + " (n=" + str(len(people)) + ")"
    share_start = 0
    count_start = 0
    for status in status_order:
        count = int((people["new_items_status"] == status).sum())
        share = count / len(people)
        rows.append({"mode": modes[0], "age": age, "age_label": label, "status": status, "count": count,
                     "start": share_start, "end": share_start + share, "middle": share_start + share / 2})
        rows.append({"mode": modes[1], "age": age, "age_label": label, "status": status, "count": count,
                     "start": count_start, "end": count_start + count, "middle": count_start + count / 2})
        share_start = share_start + share
        count_start = count_start + count
bars_df = pd.DataFrame(rows)

colors = alt.Scale(domain=status_order, range=["#08519c", "#6baed6", "#fdae6b"])
text_color = alt.condition(alt.datum.status == "Tried at least one", alt.value("white"), alt.value("black"))


def make_layers(data, x_axis, x_title, width, height):
    y = alt.Y("age_label:N", sort=alt.SortField("age"), title=None)
    bars = data.mark_bar(stroke="white").encode(
        x=alt.X("start:Q", title=x_title, axis=x_axis), x2="end:Q", y=y,
        color=alt.Color("status:N", scale=colors, sort=status_order, title="new items"))
    numbers = data.transform_filter(alt.datum.count > 0).mark_text(fontSize=13).encode(
        x="middle:Q", y=y, text="count:Q", color=text_color)
    return alt.layer(bars, numbers).properties(width=width, height=height)


def style(chart):
    return chart.configure_axis(labelFontSize=14, titleFontSize=14).configure_legend(
        labelFontSize=14, titleFontSize=14, labelLimit=320).configure_title(fontSize=17)


# static version: both views side by side
share_chart = make_layers(alt.Chart(bars_df[bars_df["mode"] == modes[0]]),
                          alt.Axis(format="%", values=[0, 0.5, 1]),
                          "share of people in that age group", 300, 220).properties(title="Share of each age group")
number_chart = make_layers(alt.Chart(bars_df[bars_df["mode"] == modes[1]]),
                           alt.Axis(tickMinStep=1),
                           "number of people", 300, 220).properties(title="Number of people")
static_chart = alt.hconcat(share_chart, number_chart).resolve_scale(color="shared").properties(
    title="Have visitors tried the new items? By age group")

# interactive version: one chart with a switch between the two views
pick = alt.param(name="show", value=modes[0], bind=alt.binding_radio(options=modes, name="Show: "))
base = alt.Chart(bars_df).transform_filter(alt.datum["mode"] == pick)
x_axis = alt.Axis(labelExpr="show == 'Number of people' ? datum.label : format(datum.value, '.0%')", tickMinStep=1)
interactive_chart = make_layers(base, x_axis, "", 560, 240).add_params(pick).properties(
    title="Have visitors tried the new items? By age group")

# nicer layout for the radio buttons
page_css = """<style>
body { font-family: Helvetica, Arial, sans-serif; margin: 24px; }
.vega-embed { display: flex !important; flex-direction: column-reverse; align-items: flex-start; }
.vega-embed .vega-bindings { position: static !important; font-family: Helvetica, Arial, sans-serif !important;
  font-size: 17px !important; margin: 0 0 18px 0 !important; padding: 0 !important; }
.vega-embed .vega-bind { display: inline-block !important; margin-right: 22px !important; }
.vega-embed .vega-bind label { cursor: pointer; }
.vega-embed .vega-bind input { margin-right: 6px; }
</style>"""


def save_page(chart, path):
    chart.save(path, inline=True, embed_options={"actions": False})
    html = open(path).read().replace("<head>", "<head>" + page_css, 1)
    open(path, "w").write(html)


save_page(style(static_chart), "static.html")
save_page(style(interactive_chart), "interactive.html")

# screenshot of the static version for the report
# (the screenshot of the interactive version was taken in a browser)
style(static_chart).save("figures/static.png", scale_factor=2)
print("saved static.html, interactive.html and figures/static.png")
