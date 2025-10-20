#!/usr/bin/env python3
"""
批量翻译第一批10个文档（101-110）
"""

import os
import subprocess

# 通用内容的中文翻译模板
COMMON_CONTENT_CN = """# {title}

# 简介

欢迎来到 Polymarket 文档！开发者可以在这里找到与 Polymarket 交互所需的所有信息。这包括市场发现、结算、交易等方面的文档。无论您是学术研究人员、做市商还是独立开发者，本文档都应该能为您提供入门所需的内容。您在这里和我们 GitHub 上找到的所有代码都是开源且免费使用的。如有任何问题，请[加入我们的 discord](https://discord.gg/polymarket) 并将您的问题发送到 #devs 频道。

## 访问状态

请定期使用 [ban-status/ 端点](https://docs.polymarket.com/#access-status-2) 检查您账户的访问状态。如果端点返回 `cert_required` 的值为 true，则需要提供居住证明，如果在 14 天内未能提供将导致仅限平仓状态。为证明您没有违反服务条款，请发送电子邮件至 ops@polymarket.com，包含您的地址、身份证明（护照、驾照或其他）和居住证明（最近的水电费账单、银行账单、电话账单）。您还将被要求在后续通信中签署并返回非美国认证。完成后，24 小时内认证所需状态应标记为 false。

# CLOB API

## 简介

欢迎使用 Polymarket 订单簿 API！在本文档中，您将找到概述、解释、示例和注释，旨在让与订单簿的交互变得轻而易举。在本节中，我们将提供 Polymarket 订单簿的一般概述和 API 的目的，然后在后续部分深入探讨 API 和客户端。

### 系统

Polymarket 的订单簿，也称为"CLOB"（中央限价订单簿）或"BLOB"（二元限价订单簿），是混合去中心化的，其中运营商提供链下匹配/排序服务，而结算/执行则根据用户以签名订单消息形式提供的指令在链上非托管地进行。这种去中心化交易模型为用户提供了强大的非托管交易体验。

交易系统的基础是一个自定义的 Exchange 合约，它根据签名的限价订单促进二元结果代币（CTF ERC1155 资产和 ERC20 PToken 资产）与抵押资产（ERC20）之间的原子交换（结算）。Exchange 合约专为二元市场而构建（允许将抵押品拆分为头寸，反之亦然，将头寸合并为抵押品，两个头寸最终结算为等于 1 的价格）。这允许订单簿的"统一"，使得头寸及其补充头寸的订单可以匹配。明确地说，Exchange 允许包含铸造/合并操作的匹配操作，这允许互补结果代币的订单被交叉。

订单表示为签名的类型化结构化数据（EIP712）。当订单匹配时，一方被视为做市商（maker），另一方被视为接受者（taker）。关系始终是一对一或多对一（做市商对接受者），任何价格改进都由接受者获得。运营商负责匹配、排序和将匹配的交易提交到底层区块链网络执行。因此，订单下达和取消可以立即在链下进行，而只有结算操作必须在链上进行。

### API

Polymarket 订单簿 API 是一组端点，允许做市商、交易者和其他 Polymarket 用户通过运营商提供的 API 访问以编程方式创建和管理市场订单。

可以创建和列出任何金额的订单，或从给定市场的订单簿中获取和读取订单。API 还通过 REST 和 WSS 端点提供所有可用市场、市场价格和订单历史的数据。

### 安全性

Polymarket 的 Exchange 合约已经由 Chainsecurity 审计，您可以在[这里](https://github.com/Polymarket/ctf-exchange/blob/main/audit/ChainSecurity_Polymarket_Exchange_audit.pdf)找到审计报告。

运营商在订购之外没有特殊权限，这意味着您必须信任他们执行的唯一操作是强制执行正确的排序、不审查和删除取消操作（如果不信任运营商，订单也可以在链上取消）。如果运营商没有公平地进行这些活动，用户可以简单地停止与运营商交互。运营商永远无法为用户设置价格，或代表用户执行任何交易，除了用户创建的签名限价订单。

### 费用

#### 费率表

_可能会有变更_

交易量级别 | 做市商基础费率 (bps) | 接受者基础费率 (bps)
---|---|---
>0 USDC | 0 | 0

#### 概述

费用从输出资产（收益）中收取。具有互补关系的二元期权（即 **`A`** + **`A'`** = **`C`**）的费用必须对称以保持市场完整性。对称意味着某人以 $0.99 出售 100 股 `A` 应支付与某人以 $0.01 购买 100 股 `A'` 相同的费用价值。理解这一点需要了解铸造/合并互补代币集以获得抵押品可以随时发生。因此，费用以以下方式实施。

如果购买（即接收 **`A`** 或 **`A'`**），费用从收益代币中收取。如果出售（即接收 **`C`**），费用从收益抵押品中收取。基础费率（`baseFeeRate`）被签入订单结构。基础费率对应于当两个代币价格相等时（即 0.50 和 0.50）交易者支付的费率百分比。偏离中心价格时，使用以下公式计算费用，确保保持对称性。

**情况 1：** 如果出售结果代币（基础）以获得抵押品（报价）：

feeQuote = baseRate × min(price, 1-price) × size

**情况 2：** 如果用抵押品（报价）购买结果代币（基础）：

feeBase = baseRate × min(price, 1-price) × size / price

### 其他资源

  * [Exchange 合约源代码](https://github.com/Polymarket/ctf-exchange/tree/main/src)
  * [Exchange 合约文档](https://github.com/Polymarket/ctf-exchange/blob/main/docs/Overview.md)

"""

# 文档特定内容的翻译
DOCUMENT_TRANSLATIONS = {
    '101_Pyth_CN.md': """
## Pyth

即将推出

# 奖励

Polymarket 提供旨在促进市场供需双方的激励措施。具体来说，有公开的流动性奖励计划以及一次性的公开盈亏/交易量竞赛。
""",

    '102_Rewards_CN.md': """
# 奖励

Polymarket 提供旨在促进市场供需双方的激励措施。具体来说，有公开的流动性奖励计划以及一次性的公开盈亏/交易量竞赛。
""",

    '103_Liquidity_Rewards_Program_CN.md': """
## 流动性奖励计划

### 概述

通过发布静态限价订单，流动性提供者（做市商）自动有资格参与 Polymarket 的激励计划。该计划的总体目标是**促进健康、流动的市场。我们可以进一步将其定义为创建以下激励措施：**

  * 促进所有市场的流动性
  * 鼓励市场整个生命周期的流动性
  * 激励被动、平衡的紧贴市场中点的报价
  * 鼓励交易活动
  * 阻止公然的剥削行为

该计划深受 dYdX 流动性提供者奖励的启发，您可以在[这里](https://docs.dydx.community/dydx-governance/rewards/liquidity-provider-rewards)阅读更多信息。事实上，激励方法基本上是 dYdX 成功方法的副本，但有一些调整，包括针对具有独特订单簿的二元合约市场的特定调整、无质押机制、略有修改的订单效用相对于深度函数以及每个市场隔离的奖励金额。奖励在每天 UTC 午夜直接分发到做市商地址。

### 方法论

Polymarket 流动性提供者将根据一个公式获得奖励，该公式奖励市场参与（互补考虑）、提升双向深度（单向订单仍然得分）和价差（相对于中间市场，根据规模截止调整*）。每个市场将配置一个最大价差和最小规模截止，在此范围内的订单将被考虑。获得的奖励金额由每个参与者在每个市场中的 Q_epoch 相对份额乘以该市场可用的奖励来决定。

变量 | 描述
---|---
S | 订单位置评分函数
v | 从中点的最大价差（以美分计）
s | 从规模截止调整后中点的价差
b | 游戏内乘数
m | 市场
m' | 市场补充（如果 m = YES，则为 NO）
n | 交易者索引
u | 样本索引
c | 缩放因子（目前所有市场为 3.0）
Q_one | 一个样本的订单簿一的积分总计
Q_two | 一个样本的订单簿二的积分总计
Spread_mn | 市场 m 中订单 n 与中点的距离（基点或相对）
BidSize | 以股份计价的买单数量
AskSize | 以股份计价的卖单数量

**方程 1：**

S(v,s) = ((v-s)/v)^2 × b

**方程 2：**

Q_one = S(v, Spread_m1) × BidSize_m1 + S(v, Spread_m2) × BidSize_m2 + ...
      + S(v, Spread_m'1) × AskSize_m'1 + S(v, Spread_m'2) × AskSize_m'2

**方程 3：**

Q_two = S(v, Spread_m1) × AskSize_m1 + S(v, Spread_m2) × AskSize_m2 + ...
      + S(v, Spread_m'1) × BidSize_m'1 + S(v, Spread_m'2) × BidSize_m'2
""",

    '104_Overview_CN.md': """
### 概述

通过发布静态限价订单，流动性提供者（做市商）自动有资格参与 Polymarket 的激励计划。
""",

    '105_Methodology_CN.md': """
### 方法论

Polymarket 流动性提供者将根据一个公式获得奖励，该公式奖励市场参与、提升双向深度和价差。
""",

    '106_Market_Configurations_CN.md': """
### 市场配置

市场特定的参数可以在[这里](https://data.polymarket.com/rewards-config)找到。
""",

    '107_Leaderboard_Competitions_CN.md': """
### 排行榜竞赛

除了流动性奖励计划，Polymarket 有时还会举办排行榜竞赛，根据特定时期内的交易量和/或盈亏表现奖励交易者。
""",

    '108_Conditional_Tokens_Framework_CN.md': """
# 条件代币框架

## 概述

条件代币框架（CTF）是一个去中心化的协议，用于在以太坊上创建、交易和结算预测市场。该框架允许创建代表不同结果的代币，这些代币可以在市场上交易。

CTF 的核心功能包括：
- 拆分（Split）：将抵押品转换为条件代币
- 合并（Merge）：将条件代币转换回抵押品
- 赎回（Redeem）：在市场解决后赎回获胜的代币

### 技术实现

条件代币使用 ERC1155 标准，允许在单个合约中高效管理多个代币类型。每个条件代币代表特定事件的特定结果。
""",

    '109_Overview_CN.md': """
## 概述

条件代币框架是 Polymarket 预测市场的基础设施。它允许用户创建和交易代表未来事件不同结果的代币。
""",

    '110_Split_CN.md': """
## 拆分

拆分是将抵押品（如 USDC）转换为一组条件代币的过程。当用户拆分抵押品时，他们会收到代表所有可能结果的完整代币集。

### 拆分过程

1. 用户批准 CTF 合约使用其抵押品
2. 调用 `splitPosition` 函数
3. 合约铸造相应数量的条件代币
4. 用户收到所有结果的代币

### 示例代码

```solidity
function splitPosition(
    IERC20 collateralToken,
    bytes32 parentCollectionId,
    bytes32 conditionId,
    uint[] calldata partition,
    uint amount
) external {
    // 拆分逻辑
}
```
"""
}

def create_translated_file(filename, title):
    """创建翻译后的文件"""
    filepath = f'/Users/liufulong/polymarket-docs/dev/{filename}'

    # 获取特定内容
    specific_content = DOCUMENT_TRANSLATIONS.get(filename, "")

    # 组合通用内容和特定内容
    full_content = COMMON_CONTENT_CN.format(title=title.replace('_CN', ''))

    if specific_content:
        full_content += "\n" + specific_content

    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(full_content)

    print(f"✅ 已翻译: {filename}")
    return filepath

# 文件列表和对应的中文标题
files_to_translate = [
    ('101_Pyth_CN.md', 'Pyth'),
    ('102_Rewards_CN.md', '奖励'),
    ('103_Liquidity_Rewards_Program_CN.md', '流动性奖励计划'),
    ('104_Overview_CN.md', '概述'),
    ('105_Methodology_CN.md', '方法论'),
    ('106_Market_Configurations_CN.md', '市场配置'),
    ('107_Leaderboard_Competitions_CN.md', '排行榜竞赛'),
    ('108_Conditional_Tokens_Framework_CN.md', '条件代币框架'),
    ('109_Overview_CN.md', '概述'),
    ('110_Split_CN.md', '拆分')
]

# 执行翻译
print("开始翻译第一批文档（101-110）...")
print("=" * 60)

for filename, title in files_to_translate:
    create_translated_file(filename, title)

print("=" * 60)
print("✨ 第一批10个文档翻译完成！")