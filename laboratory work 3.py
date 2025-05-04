#Задание 1, вариант 8

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
df = pd.DataFrame({
    "smoking_yes_cancer_no": [10, 15, 8, 12, 18, 20, 5, 9, 13, 11],
    "smoking_no_cancer_yes": [3, 7, 2, 6, 9, 12, 1, 4, 5, 8],
    "Location": list("ABCDESTUVW")
})
df["Color"] = df["Location"].apply(lambda loc: "grey" if loc <= "R" else "pink")
plt.figure(figsize=(8,6))
plt.scatter(df["smoking_yes_cancer_no"], df["smoking_no_cancer_yes"], c=df["Color"])
plt.xlabel("Smoking Yes, Cancer No")
plt.ylabel("Smoking No, Cancer Yes")
plt.title("Диаграмма рассеяния (china_smoking)")
plt.grid(True)
for i, row in df.iterrows():
    plt.text(row["smoking_yes_cancer_no"] + 0.3, row["smoking_no_cancer_yes"] + 0.3, row["Location"])
colors = {"A-R": "grey", "S-Z": "pink"}
plt.legend(handles=[mpatches.Patch(color=c, label=l) for l, c in colors.items()])
plt.show()