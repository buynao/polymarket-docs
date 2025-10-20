#!/usr/bin/env python3
"""
提取每个文档的独特内容，去除重复的通用部分
"""

import os
import re

# 通用内容的标记（这些内容在每个文件中都重复）
COMMON_SECTIONS = [
    "# Introduction\n\nWelcome to Polymarket's docs!",
    "## Access status\n\nPlease regularly check",
    "# CLOB API\n\n## Introduction",
    "### System\n\nPolymarket's Order Book",
    "### API\n\nThe Polymarket Order Book API",
    "### Security\n\nPolymarket's Exchange contract",
    "### Fees\n\n#### Schedule",
    "## Deployments\n\nThe Exchange contract",
    "## Status\n\n<https://status-clob.polymarket.com/>",
    "## Clients\n\n> Installation",
]

def extract_unique_content(filepath):
    """提取文件中的独特内容"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 获取文件的主标题
    title_match = re.match(r'^# (.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1)
    else:
        title = os.path.basename(filepath).replace('_CN.md', '').replace('.md', '')

    # 查找独特内容部分
    unique_parts = []
    lines = content.split('\n')

    in_common_section = False
    current_section = []

    for line in lines:
        # 检查是否进入通用部分
        for common_marker in COMMON_SECTIONS:
            if common_marker.split('\n')[0] in line:
                in_common_section = True
                break

        # 检查是否是该文档特有的章节标题
        if line.startswith('## ') and title.lower() in line.lower():
            in_common_section = False
            current_section = [line]
            continue

        if not in_common_section and current_section:
            current_section.append(line)

    if current_section:
        unique_parts.append('\n'.join(current_section))

    return {
        'title': title,
        'unique_content': '\n\n'.join(unique_parts) if unique_parts else None
    }

# 要处理的文件列表
files_to_process = [
    '101_Pyth_CN.md',
    '102_Rewards_CN.md',
    '103_Liquidity_Rewards_Program_CN.md',
    '104_Overview_CN.md',
    '105_Methodology_CN.md',
    '106_Market_Configurations_CN.md',
    '107_Leaderboard_Competitions_CN.md',
    '108_Conditional_Tokens_Framework_CN.md',
    '109_Overview_CN.md',
    '110_Split_CN.md'
]

# 提取每个文件的独特内容
for filename in files_to_process:
    filepath = f'/Users/liufulong/polymarket-docs/dev/{filename}'
    if os.path.exists(filepath):
        result = extract_unique_content(filepath)
        print(f"\n{'='*60}")
        print(f"文件: {filename}")
        print(f"标题: {result['title']}")
        print(f"独特内容: {'有' if result['unique_content'] else '无'}")
        if result['unique_content']:
            # 只显示前500个字符
            preview = result['unique_content'][:500] + '...' if len(result['unique_content']) > 500 else result['unique_content']
            print(f"预览:\n{preview}")