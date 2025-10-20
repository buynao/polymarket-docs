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
    
    client = ClobClient(host, key=key, chain_id=chain_id, signature_type=2, funder=POLYMARKET_PROXY_ADDRESS)
    

其中：

  * host：Polymarket CLOB 端点 https://clob.polymarket.com

  * key：从浏览器钱包导出的与账户关联的私钥

  * chain_id：区块链的链 ID。大多数情况下为 137

  * funder：与浏览器钱包登录关联的 Polymarket 地址




更多信息请参见 [CLOB 文档](https://docs.polymarket.com/#clients)和[这些](https://gist.github.com/poly-rodr/f6530175c27e91a1b079c001262218d0)[链接](https://gist.github.com/poly-rodr/f6530175c27e91a1b079c001262218d0)
