### User Channel

经过身份验证的通道，用于获取与用户活动（订单、交易）相关的更新，通过 apiKey 为经过身份验证的用户过滤。

`SUBSCRIBE {wss-channel} user`

#### `trade` 消息


    Copy to Clipboard

    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "event_type": "trade",
      "id": "28c4d2eb-bbea-40e7-a9f0-b2fdb56b2c2e",
      "last_update": "1672290701",
      "maker_orders": [
        {
          "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
          "matched_amount": "10",
          "order_id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
          "outcome": "YES",
          "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
          "price": "0.57"
        }
      ],
      "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      "matchtime": "1672290701",
      "outcome": "YES",
      "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "price": "0.57",
      "side": "BUY",
      "size": "10",
      "status": "MATCHED",
      "taker_order_id": "0x06bc63e346ed4ceddce9efd6b3af37c8f8f440c92fe7da6b2d0f9e4ccbc50c42",
      "timestamp": "1672290701",
      "trade_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "type": "TRADE"
    }


**触发时机：**

  * 当市价订单被匹配时（"MATCHED"）
  * 当用户的限价订单被包含在交易中时（"MATCHED"）
  * 交易的后续状态变化（"MINED"、"CONFIRMED"、"RETRYING"、"FAILED"）



**结构：**

名称 | 类型 | 描述
---|---|---
asset_id | string | taker 订单（市价订单）的资产 ID（代币 ID）
event_type | string | "trade"
id | string | 交易 ID
last_update | string | 交易最后更新时间
maker_orders | MakerOrder[] | maker 订单匹配详情数组
market | string | 市场标识符（条件 ID）
matchtime | string | 交易匹配时间
outcome | string | 结果
owner | string | 事件所有者的 api key
price | string | 价格
side | string | BUY/SELL
size | string | 数量
status | string | 交易状态
taker_order_id | string | taker 订单的 ID
timestamp | string | 事件时间
trade_owner | string | 交易所有者的 api key
type | string | "TRADE"

其中 `MakerOrder` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
asset_id | string | maker 订单的资产 ID
matched_amount | string | 交易中匹配的 maker 订单数量
order_id | string | maker 订单 ID
outcome | string | 结果
owner | string | maker 订单的所有者
price | string | maker 订单的价格

#### `order` 消息


    Copy to Clipboard

    {
      "asset_id": "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      "associate_trades": null,
      "event_type": "order",
      "id": "0xff354cd7ca7539dfa9c28d90943ab5779a4eac34b9b37a757d7b32bdfb11790b",
      "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      "order_owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "original_size": "10",
      "outcome": "YES",
      "owner": "9180014b-33c8-9240-a14b-bdca11c0a465",
      "price": "0.57",
      "side": "SELL",
      "size_matched": "0",
      "timestamp": "1672290687",
      "type": "PLACEMENT"
    }


**触发时机：**

  * 当订单被下达时（PLACEMENT）
  * 当订单被更新时（部分匹配）（UPDATE）
  * 当订单被取消时（CANCELLATION）



**结构：**

名称 | 类型 | 描述
---|---|---
asset_id | string | 订单的资产 ID（代币 ID）
associate_trades | string[] | 订单已包含在其中的交易 ID 数组
event_type | string | "order"
id | string | 订单 ID
market | string | 市场的条件 ID
order_owner | string | 订单所有者
original_size | string | 原始订单大小
outcome | string | 结果字符串
owner | string | 订单所有者
price | string | 订单价格
side | string | BUY/SELL
size_matched | string | 已匹配的订单大小
timestamp | string | 事件时间
type | string | PLACEMENT/UPDATE/CANCELLATION
