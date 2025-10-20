# 获取订单

### 获取订单

此端点需要 L2 请求头。

通过 ID 获取单个订单。

#### HTTP 请求

`GET {clob-endpoint}/data/order/{order hash}`


    Copy to Clipboard

    async function main() {
      const order = await clobClient.getOrder(
        "0xb816482a5187a3d3db49cbaf6fe3ddf24f53e6c712b5a4bf5e01d0ec7b11dabc"
      );
      console.log(order);
    }

    main();



    Copy to Clipboard

    order = clob_client.get_order("0xb816482a5187a3d3db49cbaf6fe3ddf24f53e6c712b5a4bf5e01d0ec7b11dabc")
    print(order)


#### 请求参数

名称 | 必需 | 类型 | 描述
---|---|---|---
id | 否 | string | 要获取信息的订单 ID

#### 响应格式

名称 | 类型 | 描述
---|---|---
null | OpenOrder | 如果存在则返回订单

`OpenOrder` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
associate_trades | string[] | 订单部分包含在其中的任何交易 ID
id | string | 订单 ID
status | string | 订单当前状态
market | string | 市场 ID（条件 ID）
original_size | string | 放置时的原始订单大小
outcome | string | 订单对应的人类可读结果
maker_address | string | maker 地址（资金提供者）
owner | string | API 密钥
price | string | 价格
side | string | 买入或卖出
size_matched | string | 已匹配/成交的订单大小
asset_id | string | 代币 ID
expiration | string | 订单过期的 Unix 时间戳，如果不过期则为 0
type | string | 订单类型（GTC、FOK、GTD）
created_at | string | 订单创建时的 Unix 时间戳
