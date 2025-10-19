# Polymarket 开发文档翻译项目

## 项目状态

已完成：
- ✅ 创建了 134 个中文文档文件（*_CN.md）
- ✅ 翻译了所有文件的标题（第一行）
- ✅ 提取了通用内容文件（common_content_to_translate.md）

待完成：
- ⏳ 翻译通用内容（3138 行技术文档）
- ⏳ 将翻译内容应用到所有 134 个文件

## 文件结构说明

### 重要发现
所有 134 个原始英文文档（001-134）共享完全相同的内容（3138行），只有第一行标题不同。

这意味着：
- 我们只需要翻译一次通用内容（`common_content_to_translate.md`）
- 然后将翻译结果应用到所有 134 个中文文件中

### 当前文件
1. **原始文件**：`001_Introduction.md` 到 `134_How_do_I_interpret_the_OrderFilled_onchain_event_.md`
2. **中文文件**：`001_Introduction_CN.md` 到 `134_How_do_I_interpret_the_OrderFilled_onchain_event__CN.md`
3. **通用内容**：`common_content_to_translate.md`（待翻译）

## 文档结构（13个主要部分）

1. **Introduction** - 简介
2. **CLOB API** - CLOB API
3. **Gamma Markets API** - Gamma Markets API
4. **Subgraph** - Subgraph
5. **Resolution** - 解决方案
6. **Rewards** - 奖励
7. **Conditional Tokens Framework** - Conditional Tokens Framework
8. **FPMMs** - FPMMs
9. **Proxy Wallets** - 代理钱包
10. **Negative Risk** - 负风险
11. **Bug Bounty** - 漏洞赏金
12. **Frequently Asked Questions** - 常见问题

## 翻译要求

### 保留的术语（不翻译）
- API 相关：REST, WebSocket, HTTP, JSON, URL, endpoint, webhook
- 技术术语：nonce, signature, hash, timestamp, payload
- Polymarket 特定：Polymarket, USDC, CLOB, CTF, BLOB
- 区块链相关：Ethereum, Polygon, smart contract, wallet, private key, EIP712, ERC1155, ERC20
- 其他：EOA, HMAC, UUID

### 保持原样的内容
- 代码示例和代码块
- 命令行指令
- API 端点 URL
- 函数名、变量名、参数名
- JSON 结构
- 表格数据（可翻译表头）
- 链接

## 建议的翻译方法

### 方法 1: 使用专业翻译服务（推荐）
使用 DeepL API 或 Google Translate API，配合自定义词汇表（保留技术术语）

### 方法 2: 人工分段翻译
由于文档分为13个主要部分，可以分段进行高质量人工翻译

### 方法 3: 混合方法
1. 机器翻译生成初稿
2. 人工审核和优化
3. 重点关注 API 文档的准确性

## 下一步操作

### 选项 A: 使用提供的工具脚本
```bash
# 1. 翻译 common_content_to_translate.md 文件
# （您可以使用任何翻译工具或服务）

# 2. 将翻译结果保存为 common_content_CN.md

# 3. 运行应用脚本（需要创建）
python3 apply_translation_to_all.py
```

### 选项 B: 手动处理
逐个部分翻译 common_content_to_translate.md，注意保留技术术语

## 文件清单

总计：268 个文件
- 原始英文文件：134 个
- 中文文件（已创建标题）：134 个
- 辅助文件：工具脚本和说明文档

## 联系信息

如有问题或需要协助，请参考 Polymarket Discord #devs 频道。
