# 预测市场如何结算？- Polymarket Learn

市场

# 市场结算流程#

_市场由 UMA Optimistic Oracle（一个基于智能合约的乐观预言机）结算。_

## 概述#

  * 当市场结果明确时，市场可以被"结算"或永久确定。

  * 市场根据市场的预定义规则进行结算，这些规则可以在市场订单簿下找到。

  * 当市场结算时，获胜份额的持有者每股获得 1 美元，失败份额变得一文不值，份额交易不再可能。

  * 要结算市场，必须首先"提议"一个结果，这涉及在 USDC.e 中提供保证金，如果提议不成功，保证金将被没收。

  * 如果提议被验证为准确，提议者将因您的提议获得奖励。




如果您过早提出市场结算，或您的提议不成功，您将失去全部 750 美元的保证金。除非您了解流程并对您的观点有信心，否则不要提议结算。

### 提议市场结算#

导航到您想要提议的市场，然后点击 Resolution > Propose Resolution。

您将被带到该市场对应的 UMA 预言机页面，该页面显示所需的保证金和成功提议的奖励。

确保您在 Polygon 上的钱包中有足够的 USDC.e 来提供保证金（通常为 750 美元）

从下拉菜单中选择您想要提议的结果。

连接您的钱包并提交交易。它现在将进入 UMA Oracle 的验证队列。

一旦进入验证流程，UMA 将审查交易以确保其被正确提议。如果获得批准，您将在钱包中收到您的保证金金额加上奖励。如果未获批准，它将进入 Uma 的争议解决流程，此处详细描述。

### 争议提议的结算#

一旦市场被提议结算，它会进入 2 小时的挑战期。

如果您不同意提议的结算，您可以[对结果提出异议](/docs/guides/markets/dispute)。

[市场赔率](/docs/guides/trading/how-are-prices-calculated/)

[市场规则](/docs/guides/markets/how-are-markets-clarified/)

[](https://x.com/polymarket)[](https://discord.gg/polymarket)[](https://github.com/polymarket)

[](https://github.com/polymarket/learn/blob/main/pages/docs/guides/markets/how-are-markets-resolved.mdx)
