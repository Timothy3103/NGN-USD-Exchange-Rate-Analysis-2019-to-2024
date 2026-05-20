"""
NGN/USD Exchange Rate Analysis — 2019 to 2024
Data Source: CBN Official Rates (NAFEX/NFEM window) — monthly averages
             sourced from CBN Statistical Bulletins and published reports
Author: Ojo Timothy
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings("ignore")

# ── STYLE ─────────────────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--",
    "figure.dpi": 150,
})
NAVY   = "#1F4E79"
BLUE   = "#2E75B6"
ORANGE = "#E8700A"
RED    = "#C0392B"
GREEN  = "#1A7A4A"
GRAY   = "#95A5A6"

# ── 1. BUILD DATASET ──────────────────────────────────────────────────────────
# CBN Official Rate (NGN per 1 USD) — monthly averages
# Source: CBN Statistical Bulletin, NFEM/NAFEX window rates
# Pre-June 2023: managed/pegged rate. Post-June 2023: float after unification

data = {
    # 2019
    "2019-01": 306.9, "2019-02": 306.9, "2019-03": 306.9, "2019-04": 306.9,
    "2019-05": 306.9, "2019-06": 306.9, "2019-07": 306.9, "2019-08": 306.9,
    "2019-09": 306.9, "2019-10": 306.9, "2019-11": 306.9, "2019-12": 306.9,
    # 2020
    "2020-01": 306.9, "2020-02": 306.9, "2020-03": 360.0, "2020-04": 380.0,
    "2020-05": 386.0, "2020-06": 388.0, "2020-07": 388.0, "2020-08": 388.0,
    "2020-09": 388.0, "2020-10": 390.0, "2020-11": 390.0, "2020-12": 394.0,
    # 2021
    "2021-01": 394.0, "2021-02": 394.0, "2021-03": 407.0, "2021-04": 407.0,
    "2021-05": 407.0, "2021-06": 410.0, "2021-07": 410.0, "2021-08": 410.0,
    "2021-09": 412.0, "2021-10": 414.0, "2021-11": 415.0, "2021-12": 415.0,
    # 2022
    "2022-01": 415.0, "2022-02": 415.0, "2022-03": 416.0, "2022-04": 416.0,
    "2022-05": 418.0, "2022-06": 420.0, "2022-07": 421.0, "2022-08": 422.0,
    "2022-09": 435.0, "2022-10": 440.0, "2022-11": 445.0, "2022-12": 448.0,
    # 2023
    "2023-01": 450.0, "2023-02": 460.0, "2023-03": 460.0, "2023-04": 461.0,
    "2023-05": 462.0, "2023-06": 770.0, "2023-07": 790.0, "2023-08": 820.0,
    "2023-09": 860.0, "2023-10": 920.0, "2023-11": 980.0, "2023-12": 899.0,
    # 2024
    "2024-01": 1110.0, "2024-02": 1470.0, "2024-03": 1580.0, "2024-04": 1320.0,
    "2024-05": 1380.0, "2024-06": 1470.0, "2024-07": 1540.0, "2024-08": 1590.0,
    "2024-09": 1620.0, "2024-10": 1660.0, "2024-11": 1670.0, "2024-12": 1535.0,
}

df = pd.DataFrame(list(data.items()), columns=["month", "rate_ngn_usd"])
df["date"] = pd.to_datetime(df["month"])
df["year"]  = df["date"].dt.year
df["month_num"] = df["date"].dt.month
df = df.sort_values("date").reset_index(drop=True)

# Derived columns
df["mom_change"]   = df["rate_ngn_usd"].diff()
df["mom_pct"]      = df["rate_ngn_usd"].pct_change() * 100
df["rolling_3m"]   = df["rate_ngn_usd"].rolling(3).mean()
df["rolling_6m"]   = df["rate_ngn_usd"].rolling(6).mean()

# Year-over-year
df["yoy_pct"] = df["rate_ngn_usd"].pct_change(periods=12) * 100

# Save clean CSV
df[["date","rate_ngn_usd","mom_change","mom_pct","rolling_3m","rolling_6m","yoy_pct"]].to_csv(
    "data/ngn_usd_exchange_rate_2019_2024.csv", index=False
)
print("✅ Dataset saved. Shape:", df.shape)
print(df[["date","rate_ngn_usd","mom_pct"]].tail(12).to_string())

# ── 2. CHART 1 — Full Timeline + Key Events ───────────────────────────────────
fig, ax = plt.subplots(figsize=(16, 7))

ax.plot(df["date"], df["rate_ngn_usd"], color=NAVY, linewidth=2.2, zorder=3)
ax.fill_between(df["date"], df["rate_ngn_usd"], alpha=0.08, color=BLUE)
ax.plot(df["date"], df["rolling_3m"], color=ORANGE, linewidth=1.4,
        linestyle="--", label="3-Month Rolling Average", alpha=0.85)
ax.plot(df["date"], df["rolling_6m"], color=GREEN,  linewidth=1.4,
        linestyle=":",  label="6-Month Rolling Average", alpha=0.85)

# Key event annotations
events = [
    ("2020-03", 360, "COVID-19\nFirst devaluation", "top"),
    ("2021-03", 407, "CBN\ndevaluation 2", "top"),
    ("2023-06", 770, "Tinubu FX\nunification", "top"),
    ("2024-02", 1470, "NFEM rate\nunification shock", "bottom"),
]
for m, y, label, pos in events:
    xpos = pd.to_datetime(m)
    ax.axvline(xpos, color=RED, linewidth=1, linestyle="--", alpha=0.5)
    yoffset = 80 if pos == "top" else -120
    ax.annotate(label, xy=(xpos, y), xytext=(xpos, y + yoffset),
                fontsize=7.5, color=RED, ha="center",
                arrowprops=dict(arrowstyle="-", color=RED, alpha=0.5))

ax.set_title("NGN/USD Exchange Rate — January 2019 to December 2024",
             fontsize=14, fontweight="bold", color=NAVY)
ax.set_ylabel("Naira per 1 US Dollar (₦)", fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₦{x:,.0f}"))
ax.legend(fontsize=9)

# Shade the float era
ax.axvspan(pd.to_datetime("2023-06"), df["date"].max(),
           alpha=0.06, color=ORANGE, label="Post-unification float era")
ax.text(pd.to_datetime("2023-09"), 200, "Float Era\n(Post-June 2023)",
        fontsize=8, color=ORANGE, alpha=0.8)

plt.tight_layout()
plt.savefig("charts/01_full_timeline.png", bbox_inches="tight")
plt.close()
print("✅ Chart 1 saved.")

# ── 3. CHART 2 — Month-on-Month % Change ─────────────────────────────────────
fig, ax = plt.subplots(figsize=(16, 5))
colors = [RED if v > 0 else GREEN for v in df["mom_pct"].fillna(0)]
ax.bar(df["date"], df["mom_pct"].fillna(0), color=colors,
       width=20, edgecolor="white", alpha=0.85)
ax.axhline(0, color=GRAY, linewidth=0.8)

# Annotate the biggest spikes
top_changes = df.nlargest(3, "mom_pct")
for _, row in top_changes.iterrows():
    ax.text(row["date"], row["mom_pct"] + 0.5, f"+{row['mom_pct']:.1f}%",
            ha="center", fontsize=7.5, color=RED, fontweight="bold")

ax.set_title("Month-on-Month % Change in NGN/USD Rate (2019–2024)",
             fontsize=13, fontweight="bold", color=NAVY)
ax.set_ylabel("% Change")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}%"))
plt.tight_layout()
plt.savefig("charts/02_mom_change.png", bbox_inches="tight")
plt.close()
print("✅ Chart 2 saved.")

# ── 4. CHART 3 — Year-over-Year Depreciation ─────────────────────────────────
yoy_df = df.dropna(subset=["yoy_pct"])
fig, ax = plt.subplots(figsize=(14, 5))
bar_colors = [RED if v > 0 else GREEN for v in yoy_df["yoy_pct"]]
ax.bar(yoy_df["date"], yoy_df["yoy_pct"], color=bar_colors, width=20, edgecolor="white", alpha=0.85)
ax.axhline(0, color=GRAY, linewidth=0.8)
ax.set_title("Year-on-Year Depreciation of the Naira vs USD (2020–2024)",
             fontsize=13, fontweight="bold", color=NAVY)
ax.set_ylabel("YoY % Change")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}%"))
plt.tight_layout()
plt.savefig("charts/03_yoy_depreciation.png", bbox_inches="tight")
plt.close()
print("✅ Chart 3 saved.")

# ── 5. CHART 4 — Annual Average Rate Comparison ───────────────────────────────
annual = df.groupby("year")["rate_ngn_usd"].agg(["mean", "min", "max"]).reset_index()
annual.columns = ["year", "avg", "low", "high"]

fig, ax = plt.subplots(figsize=(10, 6))
x = range(len(annual))
bars = ax.bar(x, annual["avg"], color=BLUE, edgecolor="white", width=0.5, label="Annual Average")
ax.errorbar(x, annual["avg"],
            yerr=[annual["avg"] - annual["low"], annual["high"] - annual["avg"]],
            fmt="none", color=NAVY, capsize=6, linewidth=1.5, label="Min–Max Range")

ax.set_xticks(list(x))
ax.set_xticklabels(annual["year"], fontsize=11)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₦{x:,.0f}"))
ax.set_title("Annual Average NGN/USD Rate with Min–Max Range (2019–2024)",
             fontsize=12, fontweight="bold", color=NAVY)
ax.set_ylabel("Naira per 1 USD (₦)")
ax.legend(fontsize=9)

for i, row in annual.iterrows():
    ax.text(i, row["avg"] + 20, f"₦{row['avg']:,.0f}", ha="center", fontsize=8.5, color=NAVY)

plt.tight_layout()
plt.savefig("charts/04_annual_avg.png", bbox_inches="tight")
plt.close()
print("✅ Chart 4 saved.")

# ── 6. CHART 5 — Cumulative Depreciation from Baseline ───────────────────────
baseline = df.loc[df["date"] == "2019-01-01", "rate_ngn_usd"].values[0]
df["cumul_depr_pct"] = ((df["rate_ngn_usd"] - baseline) / baseline) * 100

fig, ax = plt.subplots(figsize=(14, 6))
ax.plot(df["date"], df["cumul_depr_pct"], color=RED, linewidth=2.2)
ax.fill_between(df["date"], df["cumul_depr_pct"], alpha=0.1, color=RED)
ax.axhline(0, color=GRAY, linewidth=0.8)
ax.set_title(f"Cumulative Naira Depreciation vs USD from Jan 2019 Baseline (₦{baseline:.0f})",
             fontsize=12, fontweight="bold", color=NAVY)
ax.set_ylabel("Cumulative % Depreciation")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"{x:.0f}%"))

final_depr = df["cumul_depr_pct"].iloc[-1]
ax.text(df["date"].iloc[-1], final_depr + 5,
        f"Total: +{final_depr:.0f}%\n(₦{baseline:.0f} → ₦{df['rate_ngn_usd'].iloc[-1]:,.0f})",
        ha="right", fontsize=9, color=RED, fontweight="bold")

plt.tight_layout()
plt.savefig("charts/05_cumulative_depreciation.png", bbox_inches="tight")
plt.close()
print("✅ Chart 5 saved.")

# ── 7. SUMMARY ────────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("KEY FINDINGS SUMMARY")
print("="*60)
print(f"Jan 2019 rate:    ₦{df['rate_ngn_usd'].iloc[0]:,.1f} / USD")
print(f"Dec 2024 rate:    ₦{df['rate_ngn_usd'].iloc[-1]:,.1f} / USD")
print(f"Total depreciation: {df['cumul_depr_pct'].iloc[-1]:.1f}% over 6 years")
print(f"\nBiggest single-month jump:")
big = df.loc[df["mom_pct"].idxmax()]
print(f"  {big['date'].strftime('%B %Y')}: +{big['mom_pct']:.1f}% (₦{df.loc[df['mom_pct'].idxmax()-1,'rate_ngn_usd']:,.0f} → ₦{big['rate_ngn_usd']:,.0f})")
print(f"\nAnnual averages:")
for _, row in annual.iterrows():
    print(f"  {row['year']}: ₦{row['avg']:,.1f}  (range: ₦{row['low']:,.0f}–₦{row['high']:,.0f})")

print("\n✅ All charts saved to charts/")
