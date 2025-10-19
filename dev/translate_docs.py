#!/usr/bin/env python3
"""
批量翻译 Polymarket 开发文档到中文
"""
import os
import re
from pathlib import Path

# 不需要翻译的专业术语
TECHNICAL_TERMS = [
    'REST', 'WebSocket', 'HTTP', 'JSON', 'URL', 'endpoint', 'webhook',
    'nonce', 'signature', 'hash', 'timestamp', 'payload',
    'Polymarket', 'USDC', 'CLOB', 'CTF', 'BLOB',
    'Ethereum', 'Polygon', 'smart contract', 'wallet', 'private key',
    'API', 'EIP712', 'ERC1155', 'ERC20', 'bps', 'ToS'
]

def extract_unique_section(filepath):
    """
    提取每个文件的独特部分
    由于所有文件都包含完整文档，我们需要找到每个文件真正的内容
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 获取文件名对应的标题
    filename = os.path.basename(filepath)

    # 按照 # 标题分割
    sections = re.split(r'\n(?=# )', content)

    # 第一个section通常是该文件的主要内容
    if sections:
        return sections[0].strip()

    return content

def get_file_main_content(filepath):
    """
    获取文件的主要内容（从第一个标题到下一个相同级别的标题或文件结束）
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return ""

    # 找到第一个 # 标题
    first_heading_idx = -1
    first_heading_level = 0

    for i, line in enumerate(lines):
        if line.strip().startswith('#'):
            first_heading_idx = i
            first_heading_level = len(line) - len(line.lstrip('#'))
            break

    if first_heading_idx == -1:
        return ''.join(lines)

    # 从第一个标题开始，找到下一个相同级别的标题
    content_lines = [lines[first_heading_idx]]

    for i in range(first_heading_idx + 1, len(lines)):
        line = lines[i]

        # 检查是否是相同级别的新标题
        if line.strip().startswith('#'):
            current_level = len(line) - len(line.lstrip('#'))
            if current_level == first_heading_level:
                # 检查标题是否与第一个标题重复（说明是新的部分）
                if i > first_heading_idx + 5:  # 至少要有一些内容
                    break

        content_lines.append(line)

    return ''.join(content_lines).strip()

# 测试前几个文件
dev_dir = Path('/Users/liufulong/polymarket-docs/dev')

for i in range(1, 6):
    filepath = dev_dir / f'{i:03d}_*.md'
    files = list(dev_dir.glob(f'{i:03d}_*.md'))
    if files:
        filepath = files[0]
        print(f"\n{'='*60}")
        print(f"文件: {filepath.name}")
        print(f"{'='*60}")
        content = get_file_main_content(filepath)
        print(content[:500])
        print(f"\n总字符数: {len(content)}")
