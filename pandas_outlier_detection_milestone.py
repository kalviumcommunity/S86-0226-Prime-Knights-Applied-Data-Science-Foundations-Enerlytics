"""
Detecting Outliers Using Visual Inspection and Simple Rules
Applied Data Science Foundations – Enerlytics
Milestone 15 – Outlier Detection

This milestone demonstrates:
- Understanding what outliers are and why they matter
- Detecting outliers using visual inspection (boxplots & scatter plots)
- Applying simple statistical rules (IQR method, threshold checks)
- Interpreting outlier findings thoughtfully before any cleaning decision
"""

import os
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')          # Non-interactive backend (safe for scripts)
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# SECTION 0: Constants & Setup
# ----------------------------------------------------------

OUTPUT_DIR = 'outputs/figures'
DATA_PATH  = 'data/processed/energy_usage_cleaned.csv'
os.makedirs(OUTPUT_DIR, exist_ok=True)

SEED = 42
np.random.seed(SEED)

print("=" * 65)
print("MILESTONE 15 – Outlier Detection (Visual + IQR Rules)")
print("=" * 65)

# ==========================================================
# SECTION 1: Load or Generate Dataset
# ==========================================================

print("\n[STEP 1] Loading Dataset")
print("-" * 40)

if os.path.exists(DATA_PATH):
    df = pd.read_csv(DATA_PATH)
    print(f"✓ Loaded from: {DATA_PATH}")
else:
    print(f"⚠  '{DATA_PATH}' not found — generating synthetic energy dataset...")

    n = 200
    hours = np.tile(np.arange(24), n // 24 + 1)[:n]

    df = pd.DataFrame({
        'timestamp':           pd.date_range('2026-01-01', periods=n, freq='h'),
        'hour':                hours,
        'consumption_kwh':     np.random.normal(loc=18, scale=4, size=n).clip(min=2),
        'temperature_celsius': np.random.normal(loc=26, scale=3, size=n),
        'cost_inr':            np.random.normal(loc=180, scale=35, size=n).clip(min=20),
        'humidity_pct':        np.random.normal(loc=60, scale=8, size=n).clip(0, 100),
    })

    # Inject realistic outliers for demonstration
    df.loc[5,   'consumption_kwh']     = 68.0   # Extreme high – e.g. equipment fault
    df.loc[42,  'consumption_kwh']     = 1.2    # Extreme low  – e.g. sensor outage
    df.loc[101, 'temperature_celsius'] = 47.5   # Heat-wave spike
    df.loc[155, 'cost_inr']            = 950.0  # Billing anomaly
    df.loc[180, 'consumption_kwh']     = 72.0   # Second extreme high
    df.loc[190, 'humidity_pct']        = 99.8   # Near-saturation

    print(f"✓ Synthetic dataset created  →  {n} rows, {df.shape[1]} columns")

print(f"\nDataset shape : {df.shape}")
print("\nFirst 5 rows:")
print(df.head())
print("\nSummary statistics (numeric columns):")
print(df.describe().round(2))


# ==========================================================
# SECTION 2: Visual Inspection – Boxplots
# ==========================================================

print("\n" + "=" * 65)
print("[STEP 2] Visual Inspection – Boxplots")
print("=" * 65)

numeric_cols = ['consumption_kwh', 'temperature_celsius', 'cost_inr', 'humidity_pct']
# Keep only columns that actually exist in the dataframe
numeric_cols = [c for c in numeric_cols if c in df.columns]

# --- 2a. Individual boxplot for consumption_kwh ---
col_focus = 'consumption_kwh'
fig, ax = plt.subplots(figsize=(7, 6))

bp = ax.boxplot(
    df[col_focus].dropna(),
    patch_artist=True,
    boxprops=dict(facecolor='#4A90D9', color='#2c5f8a'),
    medianprops=dict(color='#FF5252', linewidth=2.5),
    whiskerprops=dict(color='#2c5f8a', linewidth=1.5),
    capprops=dict(color='#2c5f8a', linewidth=1.5),
    flierprops=dict(marker='o', markerfacecolor='#FF5252',
                    markeredgecolor='#8B0000', markersize=9, alpha=0.85),
)

ax.set_title(f'Boxplot – {col_focus}\n(Red dots = potential outliers beyond 1.5×IQR)',
             fontsize=13, fontweight='bold')
ax.set_ylabel(col_focus, fontsize=11)
ax.set_xticks([])
ax.grid(axis='y', alpha=0.35, linestyle='--')
ax.set_facecolor('#F9FAFB')
fig.tight_layout()
path_box1 = f'{OUTPUT_DIR}/outlier_boxplot_consumption.png'
fig.savefig(path_box1, dpi=150)
plt.close(fig)
print(f"✓ Saved: {path_box1}")
print("  → Interpretation: Points plotted individually beyond the whiskers are flagged.")
print("    A single extreme high point is clearly visible above the upper whisker.")

# --- 2b. Side-by-side boxplots for all numeric columns ---
fig, axes = plt.subplots(1, len(numeric_cols), figsize=(4 * len(numeric_cols), 6),
                         sharey=False)

colors = ['#4A90D9', '#F5A623', '#7ED321', '#9B59B6']
for i, (col, ax) in enumerate(zip(numeric_cols, axes)):
    ax.boxplot(
        df[col].dropna(),
        patch_artist=True,
        boxprops=dict(facecolor=colors[i % len(colors)], alpha=0.75),
        medianprops=dict(color='#FF5252', linewidth=2),
        flierprops=dict(marker='o', markerfacecolor='#FF5252',
                        markeredgecolor='darkred', markersize=7, alpha=0.85),
    )
    ax.set_title(col.replace('_', '\n'), fontsize=10, fontweight='bold')
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    ax.set_facecolor('#F9FAFB')
    ax.set_xticks([])

fig.suptitle('Side-by-Side Boxplots – All Numeric Columns\n(Outliers shown as red dots)',
             fontsize=13, fontweight='bold', y=1.02)
fig.tight_layout()
path_box_all = f'{OUTPUT_DIR}/outlier_boxplots_all_columns.png'
fig.savefig(path_box_all, dpi=150, bbox_inches='tight')
plt.close(fig)
print(f"✓ Saved: {path_box_all}")
print("  → Interpretation: Each panel's whiskers extend to 1.5×IQR.")
print("    Columns with wide boxes have high variability (large IQR).")
print("    Columns with distant dots have extreme outliers worth investigating.")


# ==========================================================
# SECTION 3: Visual Inspection – Scatter Plot
# ==========================================================

print("\n" + "=" * 65)
print("[STEP 3] Visual Inspection – Scatter Plot (Isolation View)")
print("=" * 65)

# Compute IQR bounds for consumption to colour-code outliers
q1_c = df['consumption_kwh'].quantile(0.25)
q3_c = df['consumption_kwh'].quantile(0.75)
iqr_c = q3_c - q1_c
lower_c = q1_c - 1.5 * iqr_c
upper_c = q3_c + 1.5 * iqr_c

mask_outlier = (df['consumption_kwh'] < lower_c) | (df['consumption_kwh'] > upper_c)
normal_pts  = df[~mask_outlier]
outlier_pts = df[mask_outlier]

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(
    normal_pts['temperature_celsius'], normal_pts['consumption_kwh'],
    alpha=0.55, s=45, color='steelblue', edgecolors='white',
    linewidth=0.5, label=f'Normal points ({len(normal_pts)})',
)
ax.scatter(
    outlier_pts['temperature_celsius'], outlier_pts['consumption_kwh'],
    alpha=0.95, s=120, color='#FF5252', edgecolors='#8B0000',
    linewidth=1, marker='X', zorder=5,
    label=f'Outliers – IQR rule ({len(outlier_pts)})',
)

# Annotate outlier points
for _, row in outlier_pts.iterrows():
    ax.annotate(
        f"{row['consumption_kwh']:.1f} kWh",
        xy=(row['temperature_celsius'], row['consumption_kwh']),
        xytext=(8, 4), textcoords='offset points',
        fontsize=8, color='#8B0000',
        arrowprops=dict(arrowstyle='->', color='#8B0000', lw=0.8),
    )

ax.axhline(y=upper_c, color='#FF5252', linestyle='--', linewidth=1.2,
           label=f'IQR upper bound ({upper_c:.1f})')
ax.axhline(y=lower_c, color='orange', linestyle='--', linewidth=1.2,
           label=f'IQR lower bound ({lower_c:.1f})')

ax.set_xlabel('Temperature (°C)', fontsize=12)
ax.set_ylabel('Energy Consumption (kWh)', fontsize=12)
ax.set_title('Scatter Plot – Outlier Highlighting\n(Temperature vs Consumption)',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=9)
ax.grid(alpha=0.25, linestyle='--')
ax.set_facecolor('#F9FAFB')
fig.tight_layout()

path_scatter = f'{OUTPUT_DIR}/outlier_scatter_highlighted.png'
fig.savefig(path_scatter, dpi=150)
plt.close(fig)
print(f"✓ Saved: {path_scatter}")
print("  → Interpretation: Red X markers are isolated from the main cluster,")
print("    visually confirming they are unusual. Dashed lines show IQR boundaries.")


# ==========================================================
# SECTION 4: Simple Statistical Rules – IQR Method
# ==========================================================

print("\n" + "=" * 65)
print("[STEP 4] Outlier Detection Using IQR Rule")
print("=" * 65)
print("""
Rule: A value is a potential outlier if it falls outside:
  Lower Bound = Q1 - 1.5 × IQR
  Upper Bound = Q3 + 1.5 × IQR
where IQR = Q3 - Q1  (the middle 50% of data)
""")

summary_rows = []

for col in numeric_cols:
    series = df[col].dropna()
    q1  = series.quantile(0.25)
    q3  = series.quantile(0.75)
    iqr = q3 - q1
    lb  = q1 - 1.5 * iqr
    ub  = q3 + 1.5 * iqr

    outliers_col = series[(series < lb) | (series > ub)]
    pct = round(len(outliers_col) / len(series) * 100, 1)

    print(f"\n  Column: {col}")
    print(f"    Q1 = {q1:.2f}   Q3 = {q3:.2f}   IQR = {iqr:.2f}")
    print(f"    Lower bound = {lb:.2f}   Upper bound = {ub:.2f}")
    print(f"    Outliers flagged: {len(outliers_col)} ({pct}% of total)")
    if not outliers_col.empty:
        print(f"    Values: {sorted(outliers_col.tolist())}")

    summary_rows.append({
        'Column':         col,
        'Q1':             round(q1, 2),
        'Q3':             round(q3, 2),
        'IQR':            round(iqr, 2),
        'Lower Bound':    round(lb, 2),
        'Upper Bound':    round(ub, 2),
        'Outlier Count':  len(outliers_col),
        'Outlier %':      pct,
    })

summary_df = pd.DataFrame(summary_rows)
print("\n" + "-" * 65)
print("IQR Outlier Summary Table:")
print(summary_df.to_string(index=False))


# ==========================================================
# SECTION 5: Simple Threshold-Based Rule (Domain Knowledge)
# ==========================================================

print("\n" + "=" * 65)
print("[STEP 5] Threshold-Based Rule (Domain Knowledge Check)")
print("=" * 65)
print("""
Energy domain thresholds (reasonable limits):
  • consumption_kwh  : expected range  [1, 50]  kWh per hour
  • temperature_celsius: expected range [0, 45]  °C
  • cost_inr         : expected range  [10, 500] INR per hour
  • humidity_pct     : expected range  [20, 98]  %
""")

domain_rules = {
    'consumption_kwh':     (1.0,  50.0),
    'temperature_celsius': (0.0,  45.0),
    'cost_inr':            (10.0, 500.0),
    'humidity_pct':        (20.0, 98.0),
}

threshold_flags = pd.DataFrame({'timestamp': df['timestamp']})

for col, (lo, hi) in domain_rules.items():
    if col not in df.columns:
        continue
    flag_col = f'{col}_threshold_flag'
    threshold_flags[flag_col] = (df[col] < lo) | (df[col] > hi)
    flagged = threshold_flags[threshold_flags[flag_col]]
    print(f"  {col}: {len(flagged)} rows outside [{lo}, {hi}]")
    if not flagged.empty:
        print(f"    → Values: {df.loc[flagged.index, col].tolist()}")

any_flag = threshold_flags.iloc[:, 1:].any(axis=1)
print(f"\n  Total rows with at least one threshold violation: {any_flag.sum()}")


# ==========================================================
# SECTION 6: Combined Outlier Summary Chart
# ==========================================================

print("\n" + "=" * 65)
print("[STEP 6] Combined Outlier Count Bar Chart")
print("=" * 65)

fig, ax = plt.subplots(figsize=(8, 5))

bar_colors = ['#E74C3C' if v > 0 else '#2ECC71'
              for v in summary_df['Outlier Count']]
bars = ax.bar(summary_df['Column'], summary_df['Outlier Count'],
              color=bar_colors, edgecolor='white', linewidth=0.8)

# Label bars
for bar, cnt in zip(bars, summary_df['Outlier Count']):
    ax.text(bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.1,
            str(cnt), ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_xlabel('Column', fontsize=12)
ax.set_ylabel('Number of Outliers (IQR Rule)', fontsize=12)
ax.set_title('Outlier Count per Column\n(IQR 1.5× Method)',
             fontsize=13, fontweight='bold')
ax.set_facecolor('#F9FAFB')
ax.grid(axis='y', alpha=0.3, linestyle='--')
fig.tight_layout()
path_bar = f'{OUTPUT_DIR}/outlier_count_barchart.png'
fig.savefig(path_bar, dpi=150)
plt.close(fig)
print(f"✓ Saved: {path_bar}")


# ==========================================================
# SECTION 7: Interpretation – Ask "Does This Value Make Sense?"
# ==========================================================

print("\n" + "=" * 65)
print("[STEP 7] Thoughtful Interpretation of Flagged Outliers")
print("=" * 65)
print("""
Potential Outlier                  Possible Explanation
-----------------------------------------------------------------
consumption_kwh = 68.0 kWh        Equipment malfunction / surge
consumption_kwh = 72.0 kWh        Second extreme event – investigate
consumption_kwh = 1.2  kWh        Sensor offline / meter reset
temperature_celsius = 47.5 °C     Genuine heat-wave or probe fault
cost_inr = 950.0 INR              Billing error or punitive tariff
humidity_pct = 99.8 %             Humidity sensor near-saturation

Key takeaways:
  ✓ Outliers identified using BOTH visual tools (boxplot, scatter)
    AND a statistical rule (IQR 1.5×) for consistency.
  ✓ Not all extreme values are errors — some may be real events.
  ✓ Cross-checking with domain knowledge (threshold rules) adds context.
  ✓ No automatic removal was performed; investigation comes first.
  ✓ Next step would be: log findings, consult source data, decide action.
""")


# ==========================================================
# SECTION 8: Final Summary
# ==========================================================

print("=" * 65)
print("MILESTONE 15 COMPLETE – Outlier Detection")
print("=" * 65)
print(f"""
Output files generated:
  • {path_box1}
  • {path_box_all}
  • {path_scatter}
  • {path_bar}

Techniques demonstrated:
  1. Boxplot visual inspection  – single column & multi-column
  2. Scatter plot isolation     – outliers highlighted with X markers
  3. IQR rule (1.5×)           – systematic statistical flagging
  4. Threshold / domain rules  – domain-knowledge-based checks
  5. Contextual interpretation – reasoning before any action
""")
print("=" * 65)
