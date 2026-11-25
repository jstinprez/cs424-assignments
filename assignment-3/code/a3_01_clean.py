import pandas as pd

df = pd.read_csv("data/original/survey-responses-a3.csv")

# shorter column names
df.columns = ["timestamp", "location", "satisfaction", "food", "service", "atmosphere",
              "order_text", "visit_freq", "new_items_raw", "age_range", "comment"]

# dates
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.hour

# fill blanks
df["location"] = df["location"].fillna("Unknown")
df["order_text"] = df["order_text"].fillna("")
df["comment"] = df["comment"].fillna("")

# put categories in order
df["visit_freq"] = pd.Categorical(df["visit_freq"], ["First Time", "Occasionally", "Regularly"], ordered=True)
df["age_range"] = pd.Categorical(df["age_range"], ["18-24", "25-34", "35-44", "45-54", "55+"], ordered=True)

# new items question: one true/false column per answer
df["tried_calzones"] = df["new_items_raw"].str.contains("Calzones")
df["tried_deep_dish"] = df["new_items_raw"].str.contains("Caramelized Deep Dish")
df["tried_popcorn"] = df["new_items_raw"].str.contains("Gourmet Popcorn")
df["not_tried_any"] = df["new_items_raw"].str.contains("Haven't tried any")
df["not_heard"] = df["new_items_raw"].str.contains("Haven't heard of them")

df["n_items_tried"] = df["tried_calzones"].astype(int) + df["tried_deep_dish"].astype(int) + df["tried_popcorn"].astype(int)

# one column with 3 groups
# if someone checked both "haven't tried" and "haven't heard", they go in "haven't heard"
status = []
for i in range(len(df)):
    if df["n_items_tried"][i] > 0:
        status.append("Tried at least one")
    elif df["not_heard"][i]:
        status.append("Haven't heard of them")
    else:
        status.append("Heard of them, haven't tried")
df["new_items_status"] = status

# add an id and save
df.insert(0, "response_id", range(1, len(df) + 1))
df.to_csv("data/processed/survey_clean.csv", index=False)

print(len(df), "rows saved")
print(df["new_items_status"].value_counts())
