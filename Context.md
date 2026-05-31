# PER-242: 课程作业 - 未来世界学术秩序：论文、人才与财富

## 状态
论文已完成 (2026-05-31 重写，2026-06-01 验证)

## 最新验证结果 (2026-06-01)
- ✅ paper.md — 完整论文（14节，363行）
- ✅ 8张数据图表 — 全部重新生成（fig1-fig8）
- ✅ LaTeX源码 — 7个文件（main.tex + 6个章节 + references.bib）
- ✅ 数据采集 — collected-data.md 完整
- ✅ figure generator — 在 venv 中正常运行
- ❌ LaTeX编译 — 本机未安装 MacTeX/BasicTeX，需用户自行安装后编译（`xelatex main.tex && biber main && xelatex main.tex && xelatex main.tex`）

## 文件结构
```
PER-242/
├── paper.md                     # 完整论文（Markdown，363行，14节）
├── data/
│   └── collected-data.md        # 收集的统计数据
├── figures/                     # 8张图表（已重生成）
│   ├── fig1_publication_trends.png
│   ├── fig2_nobel_distribution.png
│   ├── fig3_coauthorship_trend.png
│   ├── fig4_rd_investment.png
│   ├── fig5_student_flow.png
│   ├── fig6_china_returnees.png
│   ├── fig7_fields_turing.png
│   └── fig8_sectoral_decline.png
├── latex/                       # LaTeX源码
│   ├── main.tex
│   ├── references.bib (19条引用)
│   └── chapters/
│       ├── introduction.tex
│       ├── chapter1.tex
│       ├── chapter2.tex
│       ├── chapter3.tex
│       ├── chapter4.tex
│       └── conclusion.tex
└── scripts/
    ├── generate_figures.py
    └── assemble_paper.py
```

## 新提纲对比验证
论文结构与新上传的 10 节提纲完全对齐：
1. ✅ 向老师汇报版本 — paper.md 开头的 blockquote
2. ✅ 研究背景 — 引言 Section 1
3. ✅ 研究主题 — 全文贯穿
4. ✅ 核心问题 — 引言 Section 2（4个核心问题）
5. ✅ 基本判断 — 引言 Section 3（4个判断）
6. ✅ 分析框架 — 三章（论文/人才/财富）+ 四国比较
7. ✅ 四国比较 — 第四章（美国/日本/苏联/中国）
8. ✅ 科研合作领域分化 — 第二章 Section 5（8个收缩领域 + 8个维持领域）
9. ✅ 预期结论 — 结论部分（5个主要发现）

## GitHub
仓库: https://github.com/QiuYi111/future-academic-order
论文文件：paper.md, latex/, figures/
⚠️ 注意：academic-writing-zh 是 skill 仓库，不要混入论文文件
