# 奖励

Polymarket 提供激励措施，旨在催化市场的供需双方。具体来说，有一个公开的流动性奖励计划以及一次性的公开盈亏/交易量竞赛。

## 流动性奖励计划

### 概述

通过发布静止限价单，流动性提供者（做市商）将自动有资格参与 Polymarket 的激励计划。该计划的总体目标是**催化一个健康、流动性充足的市场。我们可以进一步将其定义为创造激励措施：**

  * 催化所有市场的流动性
  * 鼓励市场整个生命周期的流动性
  * 激励被动、平衡的报价紧贴市场中点
  * 鼓励交易活动
  * 阻止明显的剥削行为



该计划深受 dYdX 流动性提供者奖励的启发，您可以在[此处](https://docs.dydx.community/dydx-governance/rewards/liquidity-provider-rewards)了解更多信息。事实上，激励方法本质上是 dYdX 成功方法的复制品，但进行了一些调整，包括针对二元合约市场与独立订单簿的特定适配、无质押机制、稍微修改的订单效用-相对深度函数以及按市场隔离的奖励金额。奖励每天UTC午夜直接分配到做市商的地址。

### 方法论

Polymarket 流动性提供者将根据一个公式获得奖励，该公式奖励市场参与（互补考虑）、提升双边深度（单边订单仍然计分）和价差（相对于中点市场，根据规模截止调整*）。每个市场将配置一个最大价差和最小规模截止，在此范围内的订单才会被考虑。获得的奖励金额由每个参与者在每个市场中的 QepochQepoch 相对份额乘以该市场的可用奖励来确定。

变量 | 描述  
---|---  
SS | 订单位置评分函数  
vv | 距离中点的最大价差（以美分为单位）  
ss | 距离规模截止调整中点的价差  
bb | 游戏内乘数  
mm | 市场  
m′m′ | 市场互补（即如果 mm = YES，则为 NO）  
nn | 交易者索引  
uu | 样本索引  
cc | 缩放因子（目前所有市场为 3.0）  
QoneQone | 一个样本中第一本订单簿的总分  
QtwoQtwo | 一个样本中第二本订单簿的总分  
SpreadmnSpreadmn | 市场 mm 中订单 nn 距离中点的距离（基点或相对值）  
BidSizeBidSize | 以份额计价的买入数量  
AskSizeAskSize | 以份额计价的卖出数量  
  
**公式 1：**

S(v,s)=(v−sv)2⋅bS(v,s)=(v−sv)2⋅b

**公式 2：**

Qone=S(v,Spreadm1)⋅BidSizem1+S(v,Spreadm2)⋅BidSizem2+…Qone=S(v,Spreadm1)⋅BidSizem1+S(v,Spreadm2)⋅BidSizem2+…

+S(v,Spreadm′1)⋅AskSizem′1+S(v,Spreadm′2)⋅AskSizem′2+S(v,Spreadm1′)⋅AskSizem1′+S(v,Spreadm2′)⋅AskSizem2′

**公式 3：**

Qtwo=S(v,Spreadm1)⋅AskSizem1+S(v,Spreadm2)⋅AskSizem2+…Qtwo=S(v,Spreadm1)⋅AskSizem1+S(v,Spreadm2)⋅AskSizem2+…

+S(v,Spreadm′1)⋅BidSizem′1+S(v,Spreadm′2)⋅BidSizem′2+S(v,Spreadm1′)⋅BidSizem1′+S(v,Spreadm2′)⋅BidSizem2′

**公式 4：**

**公式 4a:**

如果中点在 [0.10,0.90] 范围内，允许单边流动性计分：

Qmin=max(min(Qone,Qtwo),max(Qone/c,Qtwo/c))Qmin=max(min(Qone,Qtwo),max(Qone/c,Qtwo/c))

**公式 4b:**

如果中点在 [0,0.10) 或 (.90,1.0] 范围内，则要求流动性为双边才能计分：

Qmin=min(Qone,Qtwo)Qmin=min(Qone,Qtwo)

**公式 5：**

Qnormal=Qmin∑Nn=1(Qmin)nQnormal=Qmin∑n=1N(Qmin)n

**公式 6：**

Qepoch=∑u=110,080(Qnormal)uQepoch=∑u=110,080(Qnormal)u

**公式 7：**

Qfinal=Qepoch∑Nn=1(Qepoch)nQfinal=Qepoch∑n=1N(Qepoch)n

公式 | 描述/解释  
---|---  
1 | 基于调整后的中点和最大合格价差之间位置的订单的二次评分规则  
2 | 计算第一个市场方的得分。假设交易者有以下未结订单：  
  
- 在 m 上以 @0.49 买入 100q（调整后的中点为 0.50，则此订单的价差为 .01 或 1c）  
- 在 m 上以 @0.48 买入 200q  
- 在 m' 上以 @0.51 卖出 100q  
  
并假设调整后的市场中点为 0.50，m 和 m' 的 maxSpread 配置均为 3c。则交易者的得分为：  
QoneQone = ((3-1)/3)^2 * 100 + ((3-2)/3)^2 * 200 + ((3-1)/3)^2 * 100  
  
QoneQone 每分钟使用随机采样计算一次  
3 | 计算第二个市场方的得分。假设交易者有以下未结订单：  
  
- 在 m 上以 @0.485 买入 100q  
- 在 m' 上以 @0.48 买入 100q  
- 在 m' 上以 @0.505 卖出 200q  
  
并假设调整后的市场中点为 0.50，m 和 m' 的 maxSpread 配置均为 3c。则交易者的得分为：  
  
QtwoQtwo = ((3-1.5)/3)^2 * 100 + ((3-2)/3)^2 * 100 + ((3-.5)/3)^2 * 200  
  
QtwoQtwo 每分钟使用随机采样计算一次  
4 | 通过取 QoneQone 和 QtwoQtwo 的最小值来提升双边流动性，并以降低的速率奖励单边流动性（除以 cc）  
每分钟计算一次  
5 | QnormalQnormal 是做市商的 QminQmin 除以给定样本中其他做市商的所有 QminQmin 之和  
6 | QepochQepoch 是交易者在给定周期内所有 QnormalQnormal 的总和  
7 | Qfinal​Qfinal​ 通过将 Qepoch​Qepoch​ 除以给定周期内所有其他做市商的 Qepoch​Qepoch​ 之和来归一化 Qepoch​Qepoch​，该值乘以市场可用的奖励即为交易者的奖励  
  
* 调整后的中点是传统中点（(`best_bid`+`best_ask`)/2）的规模截止调整解释，使用公式 (`best_bid_min_shares_adjusted` + `best_ask_min_shares_adjusted`)/2 计算，其中 `best_bid_min_shares_adjusted` 是在该价格水平或更好价格的未结买单累计规模大于或等于最小份额要求的价格水平，`best_ask_min_shares_adjusted` 是在该价格水平或更好价格的未结卖单累计规模大于或等于最小份额要求的价格水平。

### 市场配置

可以通过 CLOB API 和 Markets API 获取完整市场对象及其 `min_incentive_size` 和 `max_incentive_spread`。可通过 Markets API 获取某个周期的奖励分配。

## 排行榜竞赛

即将推出
