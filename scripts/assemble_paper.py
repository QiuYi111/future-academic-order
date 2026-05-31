#!/usr/bin/env python3
"""Assemble the complete paper from chapter files."""
import os, re, sys

base = os.path.expanduser('~/clawd/projects/PER-242')

def extract_text(tex_path):
    content = open(tex_path).read()
    content = re.sub(r'(?<!\\)%.*', '', content)
    content = re.sub(r'\\(?:section|subsection|subsubsection)\{', '## ', content)
    content = re.sub(r'\\textbf\{([^}]*)\}', r'**\1**', content)
    content = re.sub(r'\\textit\{([^}]*)\}', r'*\1*', content)
    content = re.sub(r'\\emph\{([^}]*)\}', r'*\1*', content)
    content = re.sub(r'\\label\{[^}]*\}', '', content)
    content = re.sub(r'\\ref\{[^}]*\}', '', content)
    content = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}(?!\w)', '', content, flags=re.DOTALL)
    content = re.sub(r'\\begin\{table\}.*?\\end\{table\}(?!\w)', '', content, flags=re.DOTALL)
    content = re.sub(r'\\includegraphics[^}]*\}', '', content)
    content = re.sub(r'\\caption[^}]*\}', '', content)
    content = re.sub(r'\\centering', '', content)
    content = re.sub(r'\\noindent\s*', '', content)
    content = content.replace('\\%', '%')
    content = content.replace('\{', '{').replace('\}', '}')
    content = re.sub(r'\\\\ ', '\n\n', content)
    content = re.sub(r'\\\\', '\n', content)
    content = re.sub(r'\n\t\n', '\n\n', content)
    content = re.sub(r'\n{3,}', '\n\n', content)
    return content.strip()

chapters = [
    ('introduction', '引言'),
    ('chapter1', '第一章：论文、奖项与国家综合实力'),
    ('chapter2', '第二章：人才流动与科研合作'),
    ('chapter3', '第三章：科研基金、产业财富与国际秩序'),
    ('chapter4', '第四章：四国比较与机制总结'),
    ('conclusion', '结论'),
]

parts = []
parts.append('# 未来世界学术秩序：论文、人才与财富\n\n')
parts.append('**作者：** 邱璟祎  **日期：** 2025年5月\n\n---\n\n')
parts.append('## 摘要\n\n')
parts.append('全球秩序不仅由军事、贸易和金融权力决定，也越来越受到学术体系和科技创新体系的影响。')
parts.append('本文以"论文、人才与财富"为三个分析切口，系统考察了学术影响力与国家综合实力之间的关系。')
parts.append('通过对美国、日本、苏联/俄罗斯、中国四个国家的比较分析，')
parts.append('本文发现：(1)学术影响力具有双重属性——在国家崛起早期更像综合国力提升后的后验指标，')
parts.append('在高水平竞争阶段则可能成为驱动因素；(2)论文发表量主要反映科研系统规模，')
parts.append('被引数和国际奖项更能体现原创能力和学术中心地位；(3)人才流动能够促进知识扩散，')
parts.append('但人才流动本身不能直接决定科研实力——关键在于国家是否具备吸收、组织和转化知识的能力；')
parts.append('(4)国际冲突下的科研合作并非全面萎缩，而是按领域分层重组；')
parts.append('(5)科研基金、产业财富和国际秩序之间存在循环强化关系。\n\n')
parts.append('**关键词：** 学术秩序；科研人才；论文影响力；国际科研合作；科技竞争\n\n---\n\n')

for fname, title in chapters:
    tex = os.path.join(base, 'latex', 'chapters', fname + '.tex')
    if not os.path.exists(tex):
        continue
    text = extract_text(tex)
    parts.append('## ' + title + '\n\n')
    parts.append(text + '\n\n')
    parts.append('---\n\n')

parts.append('## 参考文献\n\n')
refs = [
    'National Science Board. Science and Engineering Indicators 2024. NSF, 2024.',
    'OECD. Education at a Glance 2024. OECD Publishing, 2024.',
    'SCImago. SCImago Journal & Country Rank, 2023.',
    'Institute of International Education. Open Doors Report, 2024.',
    'Fortunato, S. et al. Science of science. Science 359 (2018): eaao0185.',
    'Xie, Y., Zhang, C. & Lai, Q. China\'s rise as a major contributor to science and technology. PNAS 118.49 (2021): e2107771118.',
    'King, D.A. The scientific impact of nations. Nature 430 (2004): 311-316.',
    'Van Noorden, R. Nature Index annual tables 2023. Nature 623 (2023).',
    'WIPO. Global Innovation Index 2024.',
    'World Bank. World Development Indicators: R&D expenditure, 2024.',
    'Leydesdorff, L., Wagner, C. & Bornmann, L. The changing geography of research collaboration. JASIST 70.6 (2019): 605-620.',
    '中国教育部. 中国留学回国就业蓝皮书. 2024.',
    'Marginson, S. The New Geopolitics of Higher Education. CGHE, 2018.',
]
for i, ref in enumerate(refs, 1):
    parts.append('[' + str(i) + '] ' + ref + '\n\n')

md = ''.join(parts)
out = os.path.join(base, 'paper.md')
with open(out, 'w') as f:
    f.write(md)

wc = len(md.split())
print('Paper assembled: ' + out)
print('Word count (approx): ' + str(wc))
