#!/usr/bin/env python3
"""Generate figures for the paper."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
import os

# Use Noto Sans CJK SC for Chinese text
import os as _os
_font_path = _os.path.expanduser('~/Library/Fonts/NotoSansCJKsc-Regular.otf')
_bold_font_path = _os.path.expanduser('~/Library/Fonts/NotoSansCJKsc-Bold.otf')
if _os.path.exists(_font_path):
    from matplotlib.font_manager import FontProperties
    _fp = FontProperties(fname=_font_path)
    _name = _fp.get_name()
    fm.fontManager.addfont(_font_path)
    if _os.path.exists(_bold_font_path):
        fm.fontManager.addfont(_bold_font_path)
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = [_name]
    plt.rcParams['axes.unicode_minus'] = False
else:
    # Fallback: try STHeiti
    _st = '/System/Library/Fonts/STHeiti Light.ttc'
    if _os.path.exists(_st):
        fm.fontManager.addfont(_st)
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = ['STHeiti Light']
        plt.rcParams['axes.unicode_minus'] = False

output_dir = os.path.expanduser('~/clawd/projects/PER-242/figures')
os.makedirs(output_dir, exist_ok=True)

# ============================================================
# Figure 1: Publication trends (2010-2023)
# ============================================================
years = list(range(2010, 2024))
china_pubs = [32, 38, 42, 47, 51, 55, 60, 64, 67, 72, 80, 85, 88, 92]
us_pubs = [41, 42, 43, 44, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54]
japan_pubs = [14, 14, 13.5, 13.5, 13, 13, 12.5, 12.5, 12, 12, 11.5, 11, 11, 11]
russia_pubs = [5.5, 5.8, 6, 6.2, 6.5, 6.5, 6.8, 7.2, 7.5, 7.8, 8, 8.5, 9, 9]

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(years, china_pubs, 'o-', color='#E63946', linewidth=2, label='中国')
ax.plot(years, us_pubs, 's-', color='#457B9D', linewidth=2, label='美国')
ax.plot(years, japan_pubs, '^-', color='#2A9D8F', linewidth=2, label='日本')
ax.plot(years, russia_pubs, 'D-', color='#E9C46A', linewidth=2, label='俄罗斯')
ax.axvline(x=2016.5, color='gray', linestyle='--', alpha=0.5, label='中国超越美国')
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('论文发表量（万篇）', fontsize=12)
ax.set_title('四国年度论文发表量变化趋势（2010-2023）', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig1_publication_trends.png'), dpi=200)
plt.close(fig)

# ============================================================
# Figure 2: Nobel Prize distribution
# ============================================================
categories = ['物理学', '化学', '生理学/医学']
us_nobel = [98, 73, 105]
japan_nobel = [12, 8, 5]
russia_nobel = [10, 4, 2]
china_nobel = [0, 0, 1]

x = np.arange(len(categories))
width = 0.2

fig, ax = plt.subplots(figsize=(8, 5))
bars1 = ax.bar(x - 1.5*width, us_nobel, width, color='#457B9D', label='美国')
bars2 = ax.bar(x - 0.5*width, japan_nobel, width, color='#2A9D8F', label='日本')
bars3 = ax.bar(x + 0.5*width, russia_nobel, width, color='#E9C46A', label='苏联/俄罗斯')
bars4 = ax.bar(x + 1.5*width, china_nobel, width, color='#E63946', label='中国（大陆）')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylabel('获奖人数', fontsize=12)
ax.set_title('四国诺贝尔科学奖项分布（1901-2024）', fontsize=14)
ax.legend(fontsize=10)
ax.grid(True, axis='y', alpha=0.3)
# Add value labels
for bars in [bars1, bars2, bars3, bars4]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                    f'{int(height)}', ha='center', va='bottom', fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig2_nobel_distribution.png'), dpi=200)
plt.close(fig)

# ============================================================
# Figure 3: US-China co-authorship trend
# ============================================================
coauthor_years = list(range(2016, 2025))
coauthor_abs = [5.5, 6.0, 6.5, 6.8, 7.2, 6.8, 6.2, 5.5, 5.0]
coauthor_rate = [13.8, 13.6, 13.4, 12.8, 12.0, 10.0, 8.3, 6.9, 5.5]

fig, ax1 = plt.subplots(figsize=(8, 5))
color1 = '#E63946'
color2 = '#457B9D'
ax1.plot(coauthor_years, coauthor_abs, 'o-', color=color1, linewidth=2, label='中美合著论文数')
ax1.set_xlabel('年份', fontsize=12)
ax1.set_ylabel('合著论文数（万篇）', fontsize=12, color=color1)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.axvline(x=2020.5, color='gray', linestyle='--', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(coauthor_years, coauthor_rate, 's-', color=color2, linewidth=2, label='中美合著率（占中国论文比）')
ax2.set_ylabel('合著率（%）', fontsize=12, color=color2)
ax2.tick_params(axis='y', labelcolor=color2)

lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=10, loc='upper right')
ax1.set_title('中美合著论文变化趋势（2016-2024）', fontsize=14)
ax1.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig3_coauthorship_trend.png'), dpi=200)
plt.close(fig)

# ============================================================
# Figure 4: R&D investment vs GDP (2024 updated)
# ============================================================
countries = ['美国', '中国', '日本', '俄罗斯']
gdp = [27.4, 18.5, 4.2, 2.0]  # trillion USD (2024 est.)
rd_intensity = [3.5, 2.68, 3.4, 1.0]  # R&D/GDP % (2024, China updated)
rd_spending = [g * r / 100 for g, r in zip(gdp, rd_intensity)]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Left: R&D/GDP ratio
bars1 = ax1.bar(countries, rd_intensity, color=['#457B9D', '#E63946', '#2A9D8F', '#E9C46A'])
ax1.set_ylabel('R&D投入占GDP比例（%）', fontsize=12)
ax1.set_title('各国R&D强度对比（2024）', fontsize=14)
for bar, val in zip(bars1, rd_intensity):
    ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.02,
             f'{val}%', ha='center', va='bottom', fontsize=10)
ax1.grid(True, axis='y', alpha=0.3)

# Right: R&D spending
bars2 = ax2.bar(countries, rd_spending, color=['#457B9D', '#E63946', '#2A9D8F', '#E9C46A'])
ax2.set_ylabel('R&D总投入（万亿美元）', fontsize=12)
ax2.set_title('各国R&D总投入对比（2024）', fontsize=14)
for bar, val in zip(bars2, rd_spending):
    ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.005,
             f'{val:.2f}', ha='center', va='bottom', fontsize=10)
ax2.grid(True, axis='y', alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig4_rd_investment.png'), dpi=200)
plt.close(fig)

# ============================================================
# Figure 5: International student flow
# ============================================================
destinations = ['美国', '英国', '澳大利亚', '德国', '加拿大', '中国', '日本', '俄罗斯']
students = [105.7, 65.0, 55.0, 45.0, 43.0, 36.0, 22.0, 25.0]

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.barh(destinations, students, color='#457B9D')
ax.set_xlabel('国际学生数（万人）', fontsize=12)
ax.set_title('主要留学生接收国（2023年）', fontsize=14)
for bar, val in zip(bars, students):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2.,
            f'{val:.1f}万', ha='left', va='center', fontsize=9)
ax.grid(True, axis='x', alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig5_student_flow.png'), dpi=200)
plt.close(fig)

# ============================================================
# Figure 6: China returnees trend
# ============================================================
returnees_years = list(range(2010, 2024, 1))
returnees = [13.5, 18.6, 21.8, 27.3, 32.5, 40.9, 42.6, 48.1, 51.9, 58.0, 77.7, 104.9, 56.3, 82.0]

fig, ax = plt.subplots(figsize=(8, 5))
ax.fill_between(returnees_years, returnees, alpha=0.3, color='#2A9D8F')
ax.plot(returnees_years, returnees, 'o-', color='#2A9D8F', linewidth=2)
ax.set_xlabel('年份', fontsize=12)
ax.set_ylabel('回国留学生数（万人）', fontsize=12)
ax.set_title('中国海外留学生回流趋势（2010-2023）', fontsize=14)
ax.grid(True, alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig6_china_returnees.png'), dpi=200)
plt.close(fig)

# ============================================================
# Figure 7: Fields medal and Turing award
# ============================================================
prize_cats = ['菲尔兹奖\n（数学）', '图灵奖\n（计算机科学）']
us_prize = [14, 65]
france_prize = [13, 0]
russia_prize = [9, 0]
uk_prize = [8, 8]
japan_prize = [3, 0]
china_prize = [0, 0]

x2 = np.arange(len(prize_cats))
width2 = 0.15

fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(x2 - 2*width2, us_prize, width2, color='#457B9D', label='美国')
ax.bar(x2 - width2, france_prize, width2, color='#A8DADC', label='法国')
ax.bar(x2, russia_prize, width2, color='#E9C46A', label='苏联/俄罗斯')
ax.bar(x2 + width2, uk_prize, width2, color='#F4A261', label='英国')
ax.bar(x2 + 2*width2, japan_prize, width2, color='#2A9D8F', label='日本')
ax.bar(x2 + 3*width2, china_prize, width2, color='#E63946', label='中国（大陆）')
ax.set_xticks(x2 + width2/2)
ax.set_xticklabels(prize_cats, fontsize=12)
ax.set_ylabel('获奖人数', fontsize=12)
ax.set_title('菲尔兹奖与图灵奖国家分布', fontsize=14)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, axis='y', alpha=0.3)

# Value labels
for bars in [ax.bar(x2 - 2*width2, us_prize, width2, color='#457B9D'),
             ax.bar(x2 - width2, france_prize, width2, color='#A8DADC'),
             ax.bar(x2, russia_prize, width2, color='#E9C46A'),
             ax.bar(x2 + width2, uk_prize, width2, color='#F4A261'),
             ax.bar(x2 + 2*width2, japan_prize, width2, color='#2A9D8F'),
             ax.bar(x2 + 3*width2, china_prize, width2, color='#E63946')]:
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.3,
                    f'{int(height)}', ha='center', va='bottom', fontsize=8)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig7_fields_turing.png'), dpi=200)
plt.close(fig)

# ============================================================
# Figure 8: Sectoral collaboration decline
# ============================================================
sectors = ['航空航天', '半导体/电子', 'AI/计算机', '先进材料', 
           '化学', '生物学', '医学', '数学', '物理学', '天文学', '气候科学']
decline_rates = [60, 55, 40, 36, 32, 27, 28, 12, 8, 8, 5]

fig, ax = plt.subplots(figsize=(9, 5))
colors_sectors = ['#E63946']*4 + ['#E76F51']*4 + ['#2A9D8F']*3
bars = ax.barh(sectors, decline_rates, color=colors_sectors)
ax.set_xlabel('国际合作率下降幅度（%）', fontsize=12)
ax.set_title('各学科领域中美国际合作率下降幅度（2016→2023）', fontsize=14)
ax.axvline(x=20, color='gray', linestyle='--', alpha=0.5, label='平均下降线')
for bar, val in zip(bars, decline_rates):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2.,
            f'{val}%', ha='left', va='center', fontsize=9)
ax.legend(fontsize=9)
ax.grid(True, axis='x', alpha=0.3)
fig.tight_layout()
fig.savefig(os.path.join(output_dir, 'fig8_sectoral_decline.png'), dpi=200)
plt.close(fig)

print("All figures generated successfully.")
print(f"Output: {output_dir}")
for f in sorted(os.listdir(output_dir)):
    print(f"  {f}")
