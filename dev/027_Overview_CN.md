# 概述

# 简介

欢迎来到 Polymarket 的文档！在这里，开发者可以找到与 Polymarket 交互所需的所有信息。这包括关于市场发现、解决、交易等方面的文档。无论您是学术研究人员、做市商还是独立开发者，本文档都应该能为您提供入门所需的信息。您在这里和我们的 GitHub 上找到的所有代码都是开源和免费使用的。如果您有任何问题，请[加入我们的 Discord](https://discord.gg/polymarket) 并在 #devs 频道提出您的问题。

## 访问状态

请定期使用 [ban-status/ 端点](https://docs.polymarket.com/#access-status-2) 检查您账户的访问状态。如果该端点对 `cert_required` 返回 true 值，则需要提供居住证明，未能在 14 天内提供将导致账户进入仅关闭状态。要证明您未违反服务条款，请发送电子邮件至 ops@polymarket.com，并附上您的地址、身份证明形式（护照、驾照或其他）和居住证明（最近的水电费账单、银行账单、电话账单）。您还需要在后续通信中签署并返回非美国认证。完成后，cert required 状态应在 24 小时内标记为 false。

# CLOB API

## 简介

欢迎使用 Polymarket 订单簿 API！在本文档中，您将找到概述、解释、示例和注释，旨在使与订单簿的交互变得轻而易举。在本节中，我们将提供 Polymarket 订单簿和 API 目的的总体概述，然后在后续章节中深入探讨 API 和客户端。

### 系统

Polymarket 的订单簿，也称为"CLOB"（中央限价订单簿）或"BLOB"（二元限价订单簿），是混合去中心化的，其中运营商提供链下匹配/排序服务，而结算/执行发生在链上，根据用户以签名订单消息形式提供的指令进行非托管操作。这种去中心化交易所模式为用户提供了强大的非托管交易体验。

交易系统的底层是一个定制的 Exchange 合约，该合约根据签名限价订单促进二元结果代币（CTF ERC1155 资产和 ERC20 PToken 资产）与抵押资产（ERC20）之间的原子交换（结算）。Exchange 合约专为二元市场设计（允许将抵押品拆分为仓位的工具，相反地将仓位合并为抵押品，两个仓位最终以等于 1 的价格结算）。这允许订单簿的"统一"，使得一个仓位及其补充仓位的订单可以匹配。明确地说，Exchange 允许包含铸造/合并操作的匹配操作，这允许互补结果代币的订单交叉。

订单表示为签名的类型化结构数据（EIP712）。当订单匹配时，一方被视为 maker，另一方被视为 taker。关系始终是一对一或多对一（maker 对 taker），任何价格改善都由 taker 获得。运营商负责匹配、排序和提交匹配的交易到底层区块链网络以执行。因此，订单放置和取消可以立即在链下进行，而只有结算操作必须在链上进行。

### API

Polymarket 订单簿 API 是一组端点，允许做市商、交易者和其他 Polymarket 用户通过访问运营商提供的 API 以编程方式创建和管理市场订单。

可以创建和列出任何金额的订单，或从给定市场的订单簿中获取和读取订单。API 还通过 REST 和 WSS 端点提供所有可用市场、市场价格和订单历史的数据。

### 安全性

Polymarket 的 Exchange 合约已由 Chainsecurity 审计，您可以在[这里](https://github.com/Polymarket/ctf-exchange/blob/main/audit/ChainSecurity_Polymarket_Exchange_audit.pdf)找到审计报告。

运营商在排序之外没有特殊权限，这意味着您必须信任他们执行的唯一操作是强制正确排序、不审查和删除取消（如果不信任运营商，订单也可以在链上取消）。如果运营商没有公平地进行任何这些活动，用户可以简单地停止与运营商互动。运营商永远无法为用户设定价格，或在用户创建的签名限价订单之外代表用户执行任何交易。

### 费用

#### 费率表

_可能会变更_

交易量级别 | Maker 费用基础费率 (bps) | Taker 费用基础费率 (bps)
---|---|---
>0 USDC | 0 | 0

#### 概述

费用从输出资产（收益）中征收。具有互补关系的二元期权（即 **`A`** \+ **`A'`** = **`C`**）的费用必须对称，以保持市场完整性。对称意味着以 $0.99 卖出 100 份 `A` 的人应该支付与以 $0.01 买入 100 份 `A'` 的人相同的费用价值。理解这一点需要了解可以随时为抵押品铸造/合并互补代币集。因此，费用以以下方式实施。

如果购买（即接收 **`A`** 或 **`A'`**），费用从收益代币中征收。如果出售（即接收 **`C`**），费用从收益抵押品中征收。基础费率（`baseFeeRate`）签入订单结构。基础费率对应于当两个代币价格相等时（即 $0.50）交易者支付的费率百分比。当价格偏离中心价格时，使用以下公式计算费用，确保保持对称性。

**情况 1：** 如果出售结果代币（base）换取抵押品（quote）：

feeQuote=baseRate∗min(price,1−price)∗size

**情况 2：** 如果用抵押品（quote）购买结果代币（base）：

feeBase=baseRate∗min(price,1−price)∗sizeprice

### 附加资源

  * [Exchange 合约源代码](https://github.com/Polymarket/ctf-exchange/tree/main/src)
  * [Exchange 合约文档](https://github.com/Polymarket/ctf-exchange/blob/main/docs/Overview.md)



## 部署

Exchange 合约部署在以下地址：

网络 | 地址
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

    ### Initialization of a client that trades directly from an EOA
    client = ClobClient(host, key=key, chain_id=chain_id)

    ### Initialization of a client using a Polymarket Proxy associated with an Email/Magic account
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)

    ### Initialization of a client using a Polymarket Proxy associated with a Browser Wallet(Metamask, Coinbase Wallet, etc)
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)



    Copy to Clipboard

    import { ClobClient } from "polymarket/clob-client";
    import { SignatureType } from "@polymarket/order-utils";

    // Initialization of a client that trades directly from an EOA
    const clobClient = new ClobClient(
      host as string,
      (await wallet.getChainId()) as number,
      wallet as ethers.Wallet | ethers.providers.JsonRpcSigner
    );

    // Initialization of a client using a Polymarket Proxy associated with an Email/Magic account
    const clobClient = new ClobClient(
      host as string,
      (await wallet.getChainId()) as number,
      wallet as ethers.Wallet | ethers.providers.JsonRpcSigner,
      undefined, // creds
      SignatureType.POLY_PROXY,
      "YOUR_POLYMARKET_PROXY_ADDRESS"
    );

    // Initialization of a client using a Polymarket Proxy Wallet associated with a Browser Wallet(Metamask, Coinbase Wallet)
    const clobClient = new ClobClient(
      host as string,
      (await wallet.getChainId()) as number,
      wallet as ethers.Wallet | ethers.providers.JsonRpcSigner,
      undefined, // creds
      SignatureType.POLY_GNOSIS_SAFE,
      "YOUR_POLYMARKET_PROXY_ADDRESS"
    );


### Order Utils

Polymarket 已实现工具库以编程方式签名和生成订单：

  * [clob-order-utils](https://github.com/Polymarket/clob-order-utils) (Typescript)
  * [python-order-utils](https://github.com/Polymarket/python-order-utils) (Python)
  * [go-order-utils](https://github.com/Polymarket/go-order-utils) (Golang)



## 端点

### REST

用于所有 CLOB REST 端点，表示为 `{clob-endpoint}`。

**<https://clob.polymarket.com/>**

### Websocket

用于所有 CLOB WSS 端点，表示为 `{wss-channel}`。

**<wss://ws-subscriptions-clob.polymarket.com/ws/>**

## 认证

在使用 Polymarket 的 CLOB 时需要考虑两个级别的认证。所有签名都可以由客户端库直接处理。

### L1：私钥认证

最高级别的认证是通过账户的 Polygon 私钥进行。私钥保持对用户资金的控制，因此所有交易都是非托管的。运营商_永远不会_控制用户的资金。

以下操作需要私钥认证：

  * 放置订单（用于签名订单）
  * 创建或撤销 API 密钥



#### L1 请求头

请求头 | 必需？ | 描述
---|---|---
POLY_ADDRESS | 是 | Polygon 地址
POLY_SIGNATURE | 是 | CLOB EIP 712 签名
POLY_TIMESTAMP | 是 | 当前 UNIX 时间戳
POLY_NONCE | 是 | Nonce。默认为 0

POLY_SIGNATURE 通过签名以下 EIP712 结构生成：


    Copy to Clipboard

    const domain = {
      name: "ClobAuthDomain",
      version: "1",
      chainId: chainId, // Polygon ChainID 137
    };

    const types = {
      ClobAuth: [
        { name: "address", type: "address" },
        { name: "timestamp", type: "string" },
        { name: "nonce", type: "uint256" },
        { name: "message", type: "string" },
      ],
    };
    const value = {
      address: signingAddress, // the Signing address
      timestamp: ts, // The CLOB API server timestamp
      nonce: nonce, // The nonce used
      message: "This message attests that I control the given wallet", // A static message indicating that the user controls the wallet
    };
    const sig = await signer._signTypedData(domain, types, value);


[Typescript](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts) 和 [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py) 客户端中存在实现

### L2：API 密钥认证

下一级认证包括 API 密钥、密钥和密码短语，这些仅用于验证对 Polymarket 的 CLOB 的 API 请求。这包括发布/取消订单或检索账户的订单和成交等操作。

当用户通过 `POST` `/auth/api-key` 加入时，服务器将使用签名作为种子以确定性方式生成凭据。API 凭据包括三个字段：

**key**：识别凭据的 UUID。

**secret**：用于生成 HMAC 的密钥字符串，不随请求发送。

**passphrase**：随每个请求发送的密钥字符串，用于加密/解密数据库中的密钥，永远不会存储在数据库中。

所有未由私钥签名（`/auth/api-key`）且对私有端点的请求都需要 API 密钥签名。

#### L2 请求头

请求头 | 必需？ | 描述
---|---|---
POLY_ADDRESS | 是 | Polygon 地址
POLY_SIGNATURE | 是 | 请求的 HMAC 签名
POLY_TIMESTAMP | 是 | 请求 UNIX 时间戳
POLY_API_KEY | 是 | Polymarket API 密钥
POLY_PASSPHRASE | 是 | Polymarket API 密钥密码短语

### 创建 API 密钥

此端点需要 L1 请求头。

为用户创建新的 API 密钥凭据。

#### HTTP 请求

`POST {clob-endpoint}/auth/api-key`


    Copy to Clipboard

    const creds = await clobClient.createApiKey(); // nonce defaults to 0



    Copy to Clipboard

    creds = client.create_api_key()


> 上述请求返回如下结构的 JSON：


    Copy to Clipboard

    {
      "apiKey": "xxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx",
      "secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
      "passphrase": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }


### 派生 API 密钥

此端点需要 L1 请求头。

为地址和 nonce 派生_现有的_ API 密钥。

#### HTTP 请求

`GET {clob-endpoint}/auth/derive-api-key`


    Copy to Clipboard

    const creds = await clobClient.deriveApiKey(); // nonce defaults to 0



    Copy to Clipboard

    creds = client.derive_api_key() ## nonce defaults to 0


> 上述请求返回如下结构的 JSON：


    Copy to Clipboard

    {
      "apiKey": "xxxxxxxxx-xxxxx-xxxxxx-xxxx-xxxxxxxxxxxx",
      "secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
      "passphrase": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }


### 获取 API 密钥

此端点需要 L2 请求头。

获取与 Polygon 地址关联的所有 API 密钥。

#### HTTP 请求

`GET {clob-endpoint}/auth/api-keys`


    Copy to Clipboard

    const apiKeys = await clobClient.getApiKeys();



    Copy to Clipboard

    api_keys = client.get_api_keys()


> 上述命令返回如下结构的 JSON：


    Copy to Clipboard

    {
      "apiKeys": [ "xxxxxxxxx-xxxxx-xxxxxx-xxxx-xxxxxxxxxxxx", ... ]
    }


### 删除 API 密钥

此端点需要 L2 请求头。

删除用于验证请求的 API 密钥。

#### HTTP 请求

`DELETE {clob-endpoint}/auth/api-key`


    Copy to Clipboard

    const resp = await clobClient.deleteApiKey();
    console.log(resp);



    Copy to Clipboard

    resp = clob_client.delete_api_key()
    print(resp)


> 如果成功，上述命令返回一个 `"OK"` 字符串值：


    Copy to Clipboard

    "OK"


### 访问状态

此端点通过签名者地址返回 `cert_required` 的值。请定期检查此值，如果 `cert_required` 返回 true，请参考此[部分](https://docs.polymarket.com/#access-status)

#### HTTP 请求


    Copy to Clipboard

    GET '{clob-endpoint}/auth/ban-status/cert-required?address={signer address}'


#### 响应


    Copy to Clipboard

    {
      "cert_required": false | true
    }


### 获取仅关闭模式状态

此端点需要 L2 请求头。

获取仅关闭模式标志的值。

#### HTTP 请求

`GET {clob-endpoint}/auth/ban-status/closed-only`


    Copy to Clipboard

    const closedOnlyMode = await clobClient.getClosedOnlyMode();



    Copy to Clipboard

    closed_only_mode = client.get_closed_only_mode()


> 上述命令返回如下结构的 JSON：


    Copy to Clipboard

    {
      "closed_only": true|false
    }


## 订单

### 概述

所有订单都表示为限价订单（可以是可市场化的）。底层订单原语必须采用链上二元限价订单协议合约期望和可执行的形式。准备这样的订单相当复杂（结构化、哈希、签名），因此 Polymarket 建议使用开源的 typescript、python 和 golang 库。
