# 检查多个订单是否计分

### 检查多个订单是否计分

此端点需要 L2 请求头。

返回一个字典，其中包含布尔值，指示订单是否正在计分。

#### HTTP 请求

`POST {clob-endpoint}/orders-scoring`


    Copy to Clipboard

    async function main() {
      const scoring = await clobClient.areOrdersScoring({
        orderIds: ["0x..."],
      });
      console.log(scoring);
    }

    main();



    Copy to Clipboard

    scoring = client.are_orders_scoring(
        OrdersScoringParams(
            orderIds=["0x..."]
        )
    )
    print(scoring)


#### 请求参数

名称 | 必需 | 类型 | 描述
---|---|---|---
orderIds | 是 | string[] | 要获取信息的订单 ID 列表

#### 响应格式

名称 | 类型 | 描述
---|---|---
null | OrdersScoring | 订单计分数据

`OrdersScoring` 对象是一个字典，逐个订单指示其是否计分：


    Copy to Clipboard

    {
      "0x0": true,
      "0x1": false
    }
