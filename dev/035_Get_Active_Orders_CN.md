# 获取活跃订单

### 获取活跃订单

此端点需要 L2 请求头。

获取特定市场的活跃订单。

#### HTTP 请求

`GET {clob-endpoint}/data/orders`


    Copy to Clipboard

    async function main() {
      const resp = await clobClient.getOpenOrders({
        market:
          "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
      });
      console.log(resp);
      console.log(`Done!`);
    }

    main();



    Copy to Clipboard

    from py_clob_client.clob_types import OpenOrderParams

    resp = client.get_orders(
        OpenOrderParams(
            market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        )
    )
    print(resp)
    print("Done!")


#### 请求参数

名称 | 必需 | 类型 | 描述
---|---|---|---
id | 否 | string | 要获取信息的订单 ID
market | 否 | string | 市场的条件 ID
asset_id | 否 | string | 资产/代币的 ID

#### 响应格式

名称 | 类型 | 描述
---|---|---
null | OpenOrder[] | 按查询参数过滤的开放订单列表
