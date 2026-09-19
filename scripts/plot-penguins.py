import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/raw/penguins.csv")

fig, ax = plt.subplots(figsize=(5, 3.5))
ax.plot(df["bill_length_mm"], df["bill_depth_mm"], "o", color="g")
ax.set_xlabel("bill_length_mm")
ax.set_ylabel("bill_depth_mm")
fig.tight_layout()
fig.savefig("figures/penguins.png", dpi=150)
