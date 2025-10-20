# 常见问题

## CLOB 客户端问题

### 如何初始化 CLOB 客户端？

用户有 3 种初始化 CLOB 客户端的方法：

#### 如果直接从 EOA 地址交易：
    
    
    Copy to Clipboard
    
    client = ClobClient(host, key=key, chain_id=chain_id)
    

其中：

  * host：Polymarket CLOB 端点 https://clob.polymarket.com

  * key：持有资金的 EOA 的私钥

  * chain_id：区块链的链 ID。大多数情况下为 137




#### 如果从使用 Email/Magic 登录的账户交易：
    
    
    Copy to Clipboard
    
    client = client = ClobClient(host, key=key, chain_id=chain_id, signature_type=1, funder=POLYMARKET_PROXY_ADDRESS)
    

其中：

  * host：Polymarket CLOB 端点 https://clob.polymarket.com

  * key：从 Magic 导出的与账户关联的私钥

  * chain_id：区块链的链 ID。大多数情况下为 137

  * funder：与电子邮件登录关联的 Polymarket 地址




#### 如果从使用浏览器钱包（Metamask、Coinbase Wallet）的账户交易
    
    
    Copy to Clipboard
    
    client = client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)
    

其中：

  * host：Polymarket CLOB 端点 https://clob.polymarket.com

  * key：浏览器钱包的私钥

  * chain_id：区块链的链 ID。大多数情况下为 137

  * funder：与浏览器钱包关联的 Polymarket 地址




更多信息请参见 [CLOB 文档](https://docs.polymarket.com/#clients)和[这些](https://gist.github.com/poly-rodr/f6530175c27e91a1b079c001262218d0)[链接](https://gist.github.com/poly-rodr/f6530175c27e91a1b079c001262218d0)

## 链上问题

### 如何解释 OrderFilled 链上事件？

给定一个 OrderFilled 事件：
    
    
    Copy to Clipboard
    
    OrderFilled
    (
        orderHash="0x53187b5f9ca5a942ac48bd251a44249af5fc55e500f9c42231fd83f251fcebc9",
    
        maker="0x48CB8296c4F13C13310a09f7Aa998c435651E192",
    
        taker="0xC5d563A36AE78145C45a50134d48A1215220f80a",
    
        makerAssetId=0,
    
        takerAssetId=21742633143463906290569050155826241533067272736897614950488156847949938836455,
    
        makerAmountFilled=12122310,
    
        takerAmountFilled=24790000,
    
        fee=0,
    )
    

  * orderHash：被填充订单的唯一哈希

  * maker：生成订单并为订单提供资金的用户

  * taker：填充订单的用户，如果订单填充多个限价单，则为 Exchange 合约

  * makerAssetId：发出的资产 ID。如果为 0，表示订单是 BUY，用 USDC 交换结果代币。否则，表示订单是 SELL，用结果代币交换 USDC。

  * takerAssetId：接收的资产 ID。如果为 0，表示订单是 SELL，接收 USDC 交换结果代币。否则，表示订单是 BUY，接收结果代币交换 USDC。

  * makerAmountFilled：发出的资产数量。

  * takerAmountFilled：接收的资产数量。

  * fee：订单制造者支付的费用
