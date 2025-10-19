# 简介

欢迎访问 Polymarket 的文档！在这里开发者可以找到与 Polymarket 交互所需的所有信息。这包括市场发现、解决方案、交易等方面的文档。无论您是学术研究人员、做市商还是独立开发者，本文档都应该能为您提供入门所需的信息。您在这里和我们的 GitHub 上找到的所有代码都是开源的，可以免费使用。如果您有任何问题，请[加入我们的 discord](https://discord.gg/polymarket) 并将您的问题发送到 #devs 频道。

## 访问状态

请定期通过 [ban-status/ endpoint](https://docs.polymarket.com/#access-status-2) 检查您账户的访问状态。如果 endpoint 返回的 `cert_required` 值为 true，则需要提供居住证明，如果在 14 天内未提供，将导致账户进入只能关闭订单的状态。要证明您没有违反 ToS，请发送电子邮件至 ops@polymarket.com，附上您的地址、身份证明形式（护照、驾照或其他）和居住证明（最近的水电费账单、银行账单、电话账单）。在后续沟通中，您还需要签署并返回非美国认证文件。完成后，cert required 状态应在 24 小时内标记为 false。

# CLOB API

## 简介

欢迎使用 Polymarket Order Book API！在本文档中，您将找到概述、解释、示例和注释，旨在让与订单簿的交互变得轻而易举。在本节中，我们将在深入了解后续章节中的 API 和客户端之前，提供 Polymarket Order Book 和 API 用途的总体概述。

### 系统

Polymarket 的 Order Book，也称为 "CLOB"（中央限价订单簿）或 "BLOB"（二元限价订单簿），是混合去中心化的，其中有一个运营商提供链下撮合/排序服务，而结算/执行则根据用户以签名订单消息形式提供的指令在链上非托管地进行。这种去中心化交易所模型为用户提供了强大的非托管交易体验。

交易系统的底层是一个定制的 Exchange 合约，它根据签名的限价订单促进二元结果代币（CTF ERC1155 资产和 ERC20 PToken 资产）与抵押资产（ERC20）之间的原子交换（结算）。Exchange 合约是专门为二元市场构建的（允许将抵押品拆分为仓位的工具，反之亦然，可以将仓位合并为抵押品，两个仓位最终以等于 1 的价格结算）。这允许订单簿的"统一"，使得一个仓位及其补充仓位的订单可以匹配。明确地说，Exchange 允许包含铸造/合并操作的匹配操作，这允许匹配互补结果代币的订单。

订单表示为签名的类型化结构数据（EIP712）。当订单匹配时，一方被视为 maker，另一方被视为 taker。这种关系始终是一对一或多对一（maker 对 taker），任何价格改进都由 taker 获得。Operator 负责撮合、排序并将匹配的交易提交到底层区块链网络以执行。因此，订单下单和取消可以立即在链下进行，而只有结算操作必须在链上进行。

### API

Polymarket Order Book API 是一组 endpoint，允许做市商、交易者和其他 Polymarket 用户通过访问运营商提供的 API 以编程方式创建和管理市场订单。

可以创建和列出任意数量的订单，或者从给定市场的订单簿中获取和读取订单。该 API 还通过 REST 和 WSS endpoint 提供所有可用市场、市场价格和订单历史的数据。

### 安全性

Polymarket 的 Exchange 合约已由 Chainsecurity 审计，您可以在[这里](https://github.com/Polymarket/ctf-exchange/blob/main/audit/ChainSecurity_Polymarket_Exchange_audit.pdf)找到审计报告。

运营商除了排序之外没有特殊权限，这意味着您必须信任他们的唯一操作是执行正确的排序、不进行审查以及删除取消订单（如果不信任运营商，订单也可以在链上取消）。如果运营商没有公平地执行这些活动，用户可以简单地停止与运营商交互。运营商永远无法为用户设定价格，或在用户创建的签名限价订单之外代表用户执行任何交易。

### 费用

#### 费率表

_可能会变更_

交易量级别 | Maker 费用基准费率 (bps) | Taker 费用基准费率 (bps)
---|---|---
>0 USDC | 0 | 0

#### 概述

费用从输出资产（收益）中征收。具有互补关系的二元期权的费用（即 **`A`** \+ **`A'`** = **`C`**）必须对称以保持市场完整性。对称意味着以 $0.99 卖出 100 份 `A` 的人应该支付与以 $0.01 买入 100 份 `A'` 的人相同的费用金额。理解这一点需要了解，可以随时为抵押品铸造/合并互补代币集。因此，费用按以下方式实施。

如果买入（即接收 **`A`** 或 **`A'`**），则从收益代币中征收费用。如果卖出（即接收 **`C`**），则从收益抵押品中征收费用。基础费率（`baseFeeRate`）被签入订单结构中。基础费率对应于当两个代币的价格相等时（即 $0.50 和 $0.50）交易者支付的费率百分比。远离中心价格时，使用以下公式计算费用以确保保持对称性。

**情况 1：** 如果卖出结果代币（base）换取抵押品（quote）：

feeQuote=baseRate∗min(price,1−price)∗size

**情况 2：** 如果用抵押品（quote）买入结果代币（base）：

feeBase=baseRate∗min(price,1−price)∗size/price

### 其他资源

  * [Exchange 合约源代码](https://github.com/Polymarket/ctf-exchange/tree/main/src)
  * [Exchange 合约文档](https://github.com/Polymarket/ctf-exchange/blob/main/docs/Overview.md)



## 部署

Exchange 合约部署在以下地址：

Network | Address
---|---
**Mumbai:** | [`0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E`](https://mumbai.polygonscan.com/address/0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e)
**Polygon:** | [`0x4bFb41d5B3570DeFd03C39a9A4D8dE6Bd8B8982E`](https://polygonscan.com/address/0x4bfb41d5b3570defd03c39a9a4d8de6bd8b8982e)

## 状态

<https://status-clob.polymarket.com/>

## 客户端

> 安装


    Copy to Clipboard

    npm i -s @polymarket/clob-client

    yarn add @polymarket/clob-client



    Copy to Clipboard

    pip install py-clob-client


Polymarket 已实现参考客户端，允许以编程方式使用以下 API：

  * [clob-client](https://github.com/Polymarket/clob-client) (Typescript)
  * [py-clob-client](https://github.com/Polymarket/py-clob-client) (Python)



> 初始化


    Copy to Clipboard

    from py_clob_client.client import ClobClient

    host: str = ""
    key: str = ""
    chain_id: int = 137

    ### 从 EOA 直接交易的客户端初始化
    client = ClobClient(host, key=key, chain_id=chain_id)

    ### 使用与 Email/Magic 账户关联的 Polymarket Proxy 的客户端初始化
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

    ### 使用与浏览器钱包（Metamask、Coinbase Wallet 等）关联的 Polymarket Proxy 的客户端初始化
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)



    Copy to Clipboard

    import { ClobClient } from "polymarket/clob-client";
    import { SignatureType } from "@polymarket/order-utils";

    // 从 EOA 直接交易的客户端初始化
    const clobClient = new ClobClient(
      host as string,
      (await wallet.getChainId()) as number,
      wallet as ethers.Wallet | ethers.providers.JsonRpcSigner
    );

    // 使用与 Email/Magic 账户关联的 Polymarket Proxy 的客户端初始化
    const clobClient = new ClobClient(
      host as string,
      (await wallet.getChainId()) as number,
      wallet as ethers.Wallet | ethers.providers.JsonRpcSigner,
      undefined, // creds
      SignatureType.POLY_PROXY,
      "YOUR_POLYMARKET_PROXY_ADDRESS"
    );

    // 使用与浏览器钱包（Metamask、Coinbase Wallet）关联的 Polymarket Proxy Wallet 的客户端初始化
    const clobClient = new ClobClient(
      host as string,
      (await wallet.getChainId()) as number,
      wallet as ethers.Wallet | ethers.providers.JsonRpcSigner,
      undefined, // creds
      SignatureType.POLY_GNOSIS_SAFE,
      "YOUR_POLYMARKET_PROXY_ADDRESS"
    );


### Order Utils

Polymarket 已实现实用程序库，用于以编程方式签名和生成订单：

  * [clob-order-utils](https://github.com/Polymarket/clob-order-utils) (Typescript)
  * [python-order-utils](https://github.com/Polymarket/python-order-utils) (Python)
  * [go-order-utils](https://github.com/Polymarket/go-order-utils) (Golang)



## Endpoint

### REST

用于所有 CLOB REST endpoint，表示为 `{clob-endpoint}`。

**<https://clob.polymarket.com/>**

### Websocket

用于所有 CLOB WSS endpoint，表示为 `{wss-channel}`。

**<wss://ws-subscriptions-clob.polymarket.com/ws/>**

## 身份验证

使用 Polymarket 的 CLOB 时需要考虑两个级别的身份验证。所有签名都可以由客户端库直接处理。

### L1: Private Key 身份验证

最高级别的身份验证是通过账户的 Polygon private key。private key 仍由用户的资金控制，因此所有交易都是非托管的。运营商_永远_无法控制用户的资金。

以下操作需要 private key 身份验证：

  * 下单（用于签署订单）
  * 创建或撤销 API key



#### L1 Header
