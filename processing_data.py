import pandas as pd

df0 = pd.read_csv("data/daily_sales_data_0.csv")
df1 = pd.read_csv("data/daily_sales_data_1.csv")
df2 = pd.read_csv("data/daily_sales_data_2.csv")
all_data = pd.concat([df0, df1, df2], ignore_index=True)

pink_data = all_data[all_data["product"] == "pink morsel"].copy()
pink_data["price"] = pink_data["price"].str.replace("$", "", regex=False)
pink_data["price"] = pd.to_numeric(pink_data["price"], errors="coerce")

pink_data.loc[:, "Sales"] = pink_data["quantity"] * pink_data["price"]
final_data = pink_data[["Sales", "date", "region"]]
print(pink_data.dtypes)

final_data.to_csv("sales.csv", index=False)
