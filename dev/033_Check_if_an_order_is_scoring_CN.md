# 检查订单是否计分

### 检查订单是否计分

此端点需要 L2 请求头。

返回一个布尔值，指示订单是否正在计分。

#### HTTP 请求

`GET {clob-endpoint}/order-scoring?order_id={...}`


    Copy to Clipboard

    async function main() {
      const scoring = await clobClient.isOrderScoring({
        orderId: "0x...",
      });
      console.log(scoring);
    }

    main();



    Copy to Clipboard

    scoring = client.is_order_scoring(
        OrderScoringParams(
            orderId="0x..."
        )
    )
    print(scoring)


#### 请求参数

名称 | 必需 | 类型 | 描述
---|---|---|---
orderId | 是 | string | 要获取信息的订单 ID

#### 响应格式

名称 | 类型 | 描述
---|---|---
null | OrderScoring | 订单计分数据

`OrderScoring` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
scoring | boolean | 指示订单是否正在计分
