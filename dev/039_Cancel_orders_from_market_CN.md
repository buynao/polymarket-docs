# 取消市场中的订单

此端点需要 L2 Header。

取消市场中的订单。

## HTTP 请求

`DELETE {clob-endpoint}/cancel-market-orders`


    Copy to Clipboard

    async function main() {
      // 发送到服务器
      const resp = await clobClient.cancelMarketOrders({
        market:
          "0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af",
        asset_id:
          "52114319501245915516055106046884209969926127482827954674443846427813813222426",
      });
      console.log(resp);
      console.log(`Done!`);
    }
    main();



    Copy to Clipboard

    resp = client.cancel_market_orders(market="0xbd31dc8a20211944f6b70f31557f1001557b59905b7738480ca09bd4532f84af", asset_id="52114319501245915516055106046884209969926127482827954674443846427813813222426")
    print(resp)


## 请求负载参数

名称 | 是否必需 | 类型 | 描述
---|---|---|---
market | 否 | string | 市场的条件ID
asset_id | 否 | string | 资产/代币的ID

## 响应格式

名称 | 类型 | 描述
---|---|---
canceled | string[] | 已取消的订单列表
not_canceled | { } | 订单ID与原因的映射，说明为什么该订单无法被取消
