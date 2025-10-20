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
