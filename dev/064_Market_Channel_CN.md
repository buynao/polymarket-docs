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
