## Websocket API

### 概述

Polymarket CLOB API 提供 websocket (wss) 通道，客户端可以通过这些通道获取推送更新。这些端点允许客户端维护其订单、交易和一般市场的近实时视图。有两个可用的通道：`user` 和 `market`。

### 订阅

要订阅，请在打开连接时发送包含以下身份验证和意图信息的消息。

字段 | 类型 | 描述
---|---|---
auth | Auth | 参见 WSS Authentication
markets | string[] | 要接收事件的市场数组（条件 ID）（用于 `user` 通道）
assets_ids | string[] | 要接收事件的资产 ID 数组（代币 ID）（用于 `market` 通道）
type | string | 要订阅的通道 ID（**User** 或 **Market**）

其中 `auth` 字段的类型为 `Auth`，其格式在下面的 WSS Authentication 部分中描述。

### WSS Authentication

只有连接到 `user` 通道需要身份验证。字段 | 可选 | 描述
---|---|---
apiKey | 是 | Polygon 账户的 CLOB api key
secret | 是 | Polygon 账户的 CLOB api secret
passphrase | 是 | Polygon 账户的 CLOB api passphrase

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

### Market Channel

与市场更新（二级价格数据）相关的公共通道。

`SUBSCRIBE {wss-channel} market`

#### `book` 消息


    Copy to Clipboard

    {
      "event_type": "book",
      "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",
      "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      "buys": [
        { "price": ".48", "size": "30" },
        { "price": ".49", "size": "20" },
        { "price": ".50", "size": "15" }
      ],
      "sells": [
        { "price": ".52", "size": "25" },
        { "price": ".53", "size": "60" },
        { "price": ".54", "size": "10" }
      ],
      "timestamp": "123456789000",
      "hash": "0x0...."
    }


**触发时机：**

  * 首次订阅 `market/` 时
  * 当有影响订单簿的交易时



**结构：**

名称 | 类型 | 描述
---|---|---
event_type | string | "book"
asset_id | string | 资产 ID（代币 ID）
market | string | 市场的条件 ID
timestamp | string | 当前订单簿生成的 unix 时间戳（毫秒，1/1,000 秒）
hash | string | 订单簿内容的哈希摘要
buys | OrderSummary[] | 买单的 {size, price} 类型的聚合订单簿级别列表
sells | OrderSummary[] | 卖单的 {size, price} 类型的聚合订单簿级别列表

其中 `OrderSummary` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
price | string | 该价格级别的可用数量
size | string | 订单簿级别的价格

#### `price_change` 消息


    Copy to Clipboard

    {
      "asset_id": "71321045679252212594626385532706912750332728571942532289631379312455583992563",
      "changes": [
        {
          "price": "0.4",
          "side": "SELL",
          "size": "3300"
        },
        {
          "price": "0.5",
          "side": "SELL",
          "size": "3400"
        },
        {
          "price": "0.3",
          "side": "SELL",
          "size": "3400"
        }
      ],
      "event_type": "price_change",
      "market": "0x5f65177b394277fd294cd75650044e32ba009a95022d88a0c1d565897d72f8f1",
      "timestamp": "1729084877448",
      "hash": "3cd4d61e042c81560c9037ece0c61f3b1a8fbbdd"
    }


**触发时机：**

  * 下达新订单时
  * 取消订单时



**结构：**

名称 | 类型 | 描述
---|---|---
event_type | string | "price_change"
asset_id | string | 资产 ID（代币 ID）
market | string | 市场的条件 ID
price | string | 受影响的价格级别
size | string | 价格级别的新聚合大小
side | string | buy/sell
timestamp | string | 事件时间

#### `tick_size_change` 消息


    Copy to Clipboard

    {
    "event_type": "tick_size_change",
    "asset_id": "65818619657568813474341868652308942079804919287380422192892211131408793125422",\
    "market": "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
    "old_tick_size": "0.01",
    "new_tick_size": "0.001",
    "timestamp": "100000000"
    }


**触发时机：**

  * 市场的最小 tick size 发生变化时。这发生在订单簿价格达到限制时：`price > 0.96 or price < 0.04`



**结构：**

名称 | 类型 | 描述
---|---|---
event_type | string | "price_change"
asset_id | string | 资产 ID（代币 ID）
market | string | 市场的条件 ID
old_tick_size | 之前的最小 tick size |
new_tick_size | string | 当前的最小 tick size
side | string | buy/sell
timestamp | string | 事件时间
