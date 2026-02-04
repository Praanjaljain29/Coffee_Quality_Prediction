import pandas as pd
import numpy as np
import os
# absolute path to this file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# raw csv folder
DATA_DIR = os.path.join(BASE_DIR, "raw_data")

# list all coffee csv files
files = [f for f in os.listdir(DATA_DIR) if f.startswith("coffee_") and f.endswith(".csv")]

# extract coffee ids
coffee_ids = sorted(set(int(f.split("_")[1]) for f in files))
print(f"Found {len(coffee_ids)} coffees")

# check table counts
table_map = {}
for f in files:
    cid = int(f.split("_")[1])
    table_map.setdefault(cid, []).append(f)

bad_coffees = [cid for cid, flist in table_map.items() if len(flist) != 5]
print("Coffees with missing tables:", bad_coffees)

df_list = []

for cid in coffee_ids:
    if cid in bad_coffees:
        print(f"Skipping coffee {cid}")
        continue

    try:
        df1 = pd.read_csv(f"{DATA_DIR}/coffee_{cid}_table_1.csv")
        df2 = pd.read_csv(f"{DATA_DIR}/coffee_{cid}_table_2.csv")
        df3 = pd.read_csv(f"{DATA_DIR}/coffee_{cid}_table_3.csv")
        df4 = pd.read_csv(f"{DATA_DIR}/coffee_{cid}_table_4.csv")

        # ---- TABLE 1 ----
        df1.columns = ['z','c1','v1','c2','v2']
        cols1 = df1['c1'].tolist() + df1['c2'].tolist()
        vals1 = df1['v1'].tolist() + df1['v2'].tolist()
        df1_p = pd.DataFrame([vals1], columns=cols1)

        # ---- TABLE 2 (scores) ----
        df2.columns = ['z','c1','v1','c2','v2']
        cols2 = df2['c1'].tolist() + df2['c2'].tolist()
        vals2 = df2['v1'].tolist() + df2['v2'].tolist()
        df2_p = pd.DataFrame([vals2], columns=cols2)

        # ---- TABLE 3 ----
        df3.columns = ['z','c1','v1','c2','v2']
        cols3 = df3['c1'].tolist() + df3['c2'].tolist()
        vals3 = df3['v1'].tolist() + df3['v2'].tolist()
        df3_p = pd.DataFrame([vals3], columns=cols3)

        # ---- TABLE 4 ----
        df4.columns = ['z','c1','v1']
        df4_p = pd.DataFrame([df4['v1'].tolist()], columns=df4['c1'].tolist())

        # merge all
        df = pd.concat([df1_p, df2_p, df3_p, df4_p], axis=1)
        df = df.rename(columns={np.nan: "NA"})

        df_list.append(df)
        print(f"Processed coffee {cid}")

    except Exception as e:
        print(f"Failed coffee {cid}:", e)

# final dataframe
df_final = pd.concat(df_list, axis=0).reset_index(drop=True)

print("Final shape:", df_final.shape)
df_final.to_csv("df_1_arabica.csv", index=False)

print("Saved df_1_arabica.csv")
