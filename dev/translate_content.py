#!/usr/bin/env python3
"""
翻译文档内容的工具脚本
由于所有文件共享相同的内容，我们只需要翻译一次，然后应用到所有文件
"""
import re

# 简单的翻译映射（用于演示和基础翻译）
# 实际项目中应该使用专业的翻译API或人工翻译

TRANSLATION_MAP = {
    # 常见短语
    "Welcome to": "欢迎来到",
    "Here developers can find": "开发者可以在这里找到",
    "all the information they need": "所需的所有信息",
    "If you have any questions please": "如果您有任何问题，请",
    "join our discord": "加入我们的 discord",

    # 技术术语保持不变（已在要求中说明）
    # API, REST, WebSocket, HTTP, JSON, URL, endpoint, webhook
    # nonce, signature, hash, timestamp, payload
    # Polymarket, USDC, CLOB, CTF, Ethereum, Polygon, etc.
}

def translate_line(line):
    """
    基础翻译函数
    注意：这只是一个演示，实际翻译需要更复杂的处理
    """
    # 保持代码块不翻译
    if line.strip().startswith('```') or line.strip().startswith('    '):
        return line

    # 保持链接不翻译
    if '[' in line and '](' in line:
        return line

    # 保持表格不翻译
    if '|' in line and line.count('|') >= 2:
        return line

    # 应用简单的替换
    result = line
    for en, cn in TRANSLATION_MAP.items():
        result = result.replace(en, cn)

    return result

# 说明
print("""
================================================================================
Polymarket 开发文档翻译工具
================================================================================

重要说明：
由于所有134个文档文件共享相同的内容（只有第一行标题不同），我们需要：

1. 翻译一个完整的"通用内容"文件（从第2行开始，共3137行）
2. 将翻译后的通用内容应用到所有134个 _CN.md 文件中

当前状态：
✓ 已创建134个中文文件，每个文件的标题已翻译
✗ 文件的主体内容（第2行开始）尚未翻译

建议的下一步：
================================================================================

方案 1: 使用专业翻译服务（推荐）
- 提取通用内容（从 001_Introduction.md 的第2行开始）
- 使用 DeepL、Google Translate API 或人工翻译服务
- 将翻译结果应用到所有134个文件

方案 2: 分段人工翻译
- 文档分为13个主要部分（见下方列表）
- 逐部分翻译
- 这需要相当多的时间，但质量最好

方案 3: 混合方案
- 使用机器翻译进行初步翻译
- 人工审核和优化关键部分
- 特别注意 API 文档和代码示例

文档结构（13个主要部分）：
================================================================================
1. Introduction（简介）
2. CLOB API
3. Gamma Markets API
4. Subgraph
5. Resolution（解决方案）
6. Rewards（奖励）
7. Conditional Tokens Framework
8. FPMMs
9. Proxy Wallets（代理钱包）
10. Negative Risk（负风险）
11. Bug Bounty（漏洞赏金）
12. Frequently Asked Questions（常见问题）

建议采用方案 1 或 3，以确保翻译质量和效率。
================================================================================
""")

# 提取通用内容供翻译
print("\n正在提取通用内容到文件 common_content_to_translate.md ...")

with open('/Users/liufulong/polymarket-docs/dev/001_Introduction.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 跳过第一行（文件特定的标题）
common_content = ''.join(lines[1:])

with open('/Users/liufulong/polymarket-docs/dev/common_content_to_translate.md', 'w', encoding='utf-8') as f:
    f.write(common_content)

print(f"✓ 已创建 common_content_to_translate.md ({len(lines)-1} 行)")
print("\n提示：请翻译 common_content_to_translate.md 文件，")
print("然后使用 apply_translation.py 脚本将翻译应用到所有134个文件。")
