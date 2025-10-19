#!/usr/bin/env python3
"""
批量翻译 Polymarket 开发文档
策略：由于所有134个文件共享相同的内容（只有第一行标题不同），
我们只需要：
1. 翻译一次通用内容（第2行开始）
2. 为每个文件翻译第一行标题
3. 组合成新的中文文档
"""
import os
import glob

def get_all_titles():
    """获取所有文件的标题"""
    dev_dir = '/Users/liufulong/polymarket-docs/dev'
    files = sorted(glob.glob(os.path.join(dev_dir, '[0-9][0-9][0-9]_*.md')))

    titles = []
    for filepath in files:
        filename = os.path.basename(filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            first_line = f.readline().strip()
            titles.append((filename, first_line))

    return titles

# 获取所有标题
titles = get_all_titles()

print(f"总共找到 {len(titles)} 个文件\n")
print("前20个文件的标题：")
print("=" * 80)

for i, (filename, title) in enumerate(titles[:20], 1):
    print(f"{i:3d}. {filename:50s} | {title}")

print("\n" + "=" * 80)
print(f"\n文件21-40的标题：")
print("=" * 80)

for i, (filename, title) in enumerate(titles[20:40], 21):
    print(f"{i:3d}. {filename:50s} | {title}")
