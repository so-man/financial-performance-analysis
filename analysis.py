"""
Financial Performance Analysis
================================
Comparative study of 10 major tech companies (2019-2023)
Metrics: Revenue, Net Income, Free Cash Flow, Margins, YoY Growth

Author : Soman Yadav
Contact: soman@pillrz.com
LinkedIn: linkedin.com/in/soman-yadav
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ── CONFIG ────────────────────────────────────────────────────────────────────
OUTPUT_DIR = "charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid", font_scale=0.95)
plt.rcParams.update({"font.family": "DejaVu Sans", "axes.spines.top": False, "axes.spines.right": False})

BLUE_PAL   = ["#1E3A5F","#2563EB","#3B82F6","#60A5FA","#93C5FD","#BFDBFE","#DBEAFE","#EFF6FF","#1E40AF","#1D4ED8"]
GREEN_PAL  = ["#064E3B","#059669","#10B981","#34D399","#6EE7B7","#A7F3D0","#D1FAE5","#ECFDF5","#047857","#065F46"]
MULTI_PAL  = ["#2563EB","#10B981","#F59E0B","#EF4444","#8B5CF6","#EC4899","#14B8A6","#F97316","#6366F1","#84CC16"]

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv("financial_data.csv")
df_2023 = df[df["Year"] == 2023].sort_values("Revenue", ascending=False).reset_index(drop=True)

print(f"Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Companies: {df['Company'].nunique()} | Years: {df['Year'].min()}–{df['Year'].max()}")
print("\nColumn list:", list(df.columns))

# ── BASIC EXPLORATION ─────────────────────────────────────────────────────────
print("\n--- Basic Stats ---")
print(df.describe().round(2))

print("\n--- Null Check ---")
print(df.isnull().sum())

# ── CHART 1: REVENUE BY COMPANY 2023 ─────────────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5))
bars = ax.bar(df_2023["Company"], df_2023["Revenue"], color=BLUE_PAL, edgecolor="white", linewidth=0.5, width=0.65)
for b in bars:
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 3,
            f"${b.get_height():.0f}B", ha="center", va="bottom", fontsize=8, color="#374151")
ax.set_title("Total Revenue by Company – FY 2023", fontsize=14, fontweight="bold", pad=14)
ax.set_ylabel("Revenue (USD Billions)", fontsize=10)
ax.tick_params(axis="x", rotation=35, labelsize=9)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_revenue_by_company.png", dpi=180, bbox_inches="tight")
plt.show()

# ── CHART 2: REVENUE TREND TOP 5 ─────────────────────────────────────────────
top5 = df_2023.head(5)["Company"].tolist()
df_t5 = df[df["Company"].isin(top5)]

fig, ax = plt.subplots(figsize=(11, 5))
for i, co in enumerate(top5):
    d = df_t5[df_t5["Company"] == co]
    ax.plot(d["Year"], d["Revenue"], marker="o", linewidth=2.3, color=MULTI_PAL[i], label=co, markersize=6)
    ax.annotate(f"${d[d['Year']==2023]['Revenue'].values[0]:.0f}B",
                (2023, d[d["Year"]==2023]["Revenue"].values[0]),
                textcoords="offset points", xytext=(6, 0), fontsize=8, color=MULTI_PAL[i])
ax.set_title("Revenue Growth Trend – Top 5 Companies (2019–2023)", fontsize=14, fontweight="bold", pad=14)
ax.set_ylabel("Revenue (USD Billions)", fontsize=10)
ax.legend(fontsize=9, framealpha=0.4)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_revenue_trend.png", dpi=180, bbox_inches="tight")
plt.show()

# ── CHART 3: NET MARGIN ───────────────────────────────────────────────────────
df_margin = df_2023.sort_values("Net_Margin_Pct", ascending=False)
avg_margin = df_margin["Net_Margin_Pct"].mean()

fig, ax = plt.subplots(figsize=(11, 5))
bar_colors = [GREEN_PAL[2] if v >= avg_margin else "#CBD5E1" for v in df_margin["Net_Margin_Pct"]]
ax.bar(df_margin["Company"], df_margin["Net_Margin_Pct"], color=bar_colors, edgecolor="white", width=0.65)
ax.axhline(avg_margin, color="#EF4444", linestyle="--", linewidth=1.5, label=f"Sector Avg: {avg_margin:.1f}%")
ax.set_title("Net Profit Margin by Company – FY 2023", fontsize=14, fontweight="bold", pad=14)
ax.set_ylabel("Net Margin %", fontsize=10)
ax.tick_params(axis="x", rotation=35, labelsize=9)
ax.legend(fontsize=9)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_net_margin.png", dpi=180, bbox_inches="tight")
plt.show()

# ── CHART 4: FREE CASH FLOW ───────────────────────────────────────────────────
df_fcf = df_2023.sort_values("Free_Cashflow", ascending=False)
purple_pal = ["#4C1D95","#5B21B6","#6D28D9","#7C3AED","#8B5CF6","#A78BFA","#C4B5FD","#DDD6FE","#EDE9FE","#F5F3FF"]

fig, ax = plt.subplots(figsize=(11, 5))
bars = ax.bar(df_fcf["Company"], df_fcf["Free_Cashflow"], color=purple_pal, edgecolor="white", width=0.65)
for b in bars:
    ax.text(b.get_x() + b.get_width()/2, b.get_height() + 1,
            f"${b.get_height():.0f}B", ha="center", va="bottom", fontsize=8, color="#374151")
ax.set_title("Free Cash Flow by Company – FY 2023", fontsize=14, fontweight="bold", pad=14)
ax.set_ylabel("Free Cash Flow (USD Billions)", fontsize=10)
ax.tick_params(axis="x", rotation=35, labelsize=9)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_free_cashflow.png", dpi=180, bbox_inches="tight")
plt.show()

# ── CHART 5: REVENUE VS NET INCOME SCATTER ───────────────────────────────────
fig, ax = plt.subplots(figsize=(10, 6))
for i, (_, row) in enumerate(df_2023.iterrows()):
    ax.scatter(row["Revenue"], row["Net_Income"], s=row["Net_Margin_Pct"]*25,
               color=MULTI_PAL[i], alpha=0.85, edgecolors="white", linewidth=1, zorder=3)
    ax.annotate(row["Company"], (row["Revenue"], row["Net_Income"]),
                textcoords="offset points", xytext=(7, 4), fontsize=8, color="#374151")
ax.set_title("Revenue vs Net Income – FY 2023\n(Bubble size = Net Margin %)", fontsize=13, fontweight="bold", pad=14)
ax.set_xlabel("Revenue (USD Billions)", fontsize=10)
ax.set_ylabel("Net Income (USD Billions)", fontsize=10)
ax.yaxis.grid(True, linestyle="--", alpha=0.4)
ax.xaxis.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/05_revenue_vs_income.png", dpi=180, bbox_inches="tight")
plt.show()

# ── CHART 6: MULTI-METRIC MARGIN COMPARISON ──────────────────────────────────
fig, ax = plt.subplots(figsize=(12, 5))
x = np.arange(len(df_2023["Company"]))
w = 0.25
ax.bar(x - w,   df_2023["Gross_Margin_Pct"],     w, label="Gross Margin",     color="#2563EB", alpha=0.85)
ax.bar(x,       df_2023["Operating_Margin_Pct"],  w, label="Operating Margin", color="#10B981", alpha=0.85)
ax.bar(x + w,   df_2023["Net_Margin_Pct"],        w, label="Net Margin",       color="#F59E0B", alpha=0.85)
ax.set_xticks(x)
ax.set_xticklabels(df_2023["Company"], rotation=35, fontsize=9)
ax.set_title("Gross vs Operating vs Net Margin – FY 2023", fontsize=14, fontweight="bold", pad=14)
ax.set_ylabel("Margin %", fontsize=10)
ax.legend(fontsize=9)
ax.yaxis.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/06_margin_comparison.png", dpi=180, bbox_inches="tight")
plt.show()

# ── CHART 7: CORRELATION HEATMAP ─────────────────────────────────────────────
numeric_cols = ["Revenue","Gross_Profit","Net_Income","Free_Cashflow","Gross_Margin_Pct","Net_Margin_Pct","FCF_Margin_Pct"]
corr = df[numeric_cols].corr()

fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdYlGn", linewidths=0.5,
            annot_kws={"size": 9}, ax=ax, vmin=-1, vmax=1,
            cbar_kws={"shrink": 0.8})
ax.set_title("Correlation Matrix – Financial Metrics (2019–2023)", fontsize=13, fontweight="bold", pad=14)
ax.tick_params(labelsize=9)
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/07_correlation_heatmap.png", dpi=180, bbox_inches="tight")
plt.show()

# ── SUMMARY STATS ─────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("FINANCIAL SUMMARY – FY 2023")
print("="*60)

top_rev    = df_2023.iloc[0]
top_margin = df_2023.loc[df_2023["Net_Margin_Pct"].idxmax()]
top_fcf    = df_2023.loc[df_2023["Free_Cashflow"].idxmax()]
top_growth = df[df["Year"]==2023].dropna(subset=["Revenue_Growth_Pct"])
top_growth = top_growth.loc[top_growth["Revenue_Growth_Pct"].idxmax()]

print(f"\nHighest Revenue    : {top_rev['Company']} at ${top_rev['Revenue']:.1f}B")
print(f"Highest Net Margin : {top_margin['Company']} at {top_margin['Net_Margin_Pct']:.1f}%")
print(f"Highest FCF        : {top_fcf['Company']} at ${top_fcf['Free_Cashflow']:.1f}B")
print(f"Fastest Growing    : {top_growth['Company']} at {top_growth['Revenue_Growth_Pct']:.1f}% YoY")
print(f"Sector Avg Margin  : {df_2023['Net_Margin_Pct'].mean():.1f}%")
print(f"Total Revenue (all): ${df_2023['Revenue'].sum():.1f}B")
print("="*60)

print(f"\nAll charts saved to /{OUTPUT_DIR}/")
