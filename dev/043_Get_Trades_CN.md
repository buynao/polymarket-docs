# 获取交易

此端点需要 L2 Header。

根据提供的过滤器获取已认证用户的交易。

## HTTP 请求

`GET {clob-endpoint}/data/trades`


    Copy to Clipboard

    async function main() {
      const trades = await clobClient.getTrades({
        market:
          "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        maker_address: await wallet.getAddress(),
      });
      console.log(`trades: `);
      console.log(trades);
    }

    main();



    Copy to Clipboard

    from py_clob_client.clob_types import TradeParams

    resp = client.get_trades(
        TradeParams(
            maker_address=client.get_address(),
            market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        ),
    )
    print(resp)
    print("Done!")


## 请求参数

名称 | 是否必需 | 类型 | 描述
---|---|---|---
id | 否 | string | 要获取的交易ID
taker | taker 或 maker | string | 获取作为 taker 的交易的地址
maker | maker 或 taker | string | 获取作为 maker 的交易的地址
market | 否 | string | 要获取交易的市场（条件ID）
before | 否 | string | Unix时间戳，表示可以包含在此之前发生的交易的截止时间
after | 否 | string | Unix时间戳，表示可以包含在此之后发生的交易的截止时间

## 响应格式

名称 | 类型 | 描述
---|---|---
null | Trade[] | 按查询参数过滤的交易列表

`Trade` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
id | string | 交易ID
taker_order_id | string | 触发交易的 taker 订单（市场订单）的哈希
market | string | 市场ID（条件ID）
asset_id | string | taker 订单（市场订单）的资产ID（代币ID）
side | string | 买入或卖出
size | string | 大小
fee_rate_bps | string | taker 订单支付的费用，以基点表示
price | string | taker 订单的限价
status | string | 交易状态（见上文）
match_time | string | 交易匹配的时间
last_update | string | 最后状态更新的时间戳
outcome | string | 交易的人可读结果
maker_address | string | 交易 taker 的资金地址
owner | string | 交易 taker 的 API key
transaction_hash | string | 执行交易的交易哈希
bucket_index | integer | 当交易在多个交易中执行时，交易的桶索引
maker_orders | MakerOrder[] | taker 交易所匹配的 maker 交易列表
type | string | 交易的类型：TAKER 或 MAKER

`MakerOrder` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
order_id | string | maker 订单的ID
maker_address | string | 订单的 maker 地址
owner | string | 订单所有者的 API key
matched_amount | string | 此交易消耗的 maker 订单的大小
fee_rate_bps | string | taker 订单支付的费用，以基点表示
price | string | maker 订单的价格
asset_id | string | 代币/资产ID
outcome | string | maker 订单的人可读结果
