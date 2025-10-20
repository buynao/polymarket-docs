# 取消订单

### 取消订单

此端点需要 L2 请求头。

取消一个订单。

#### HTTP 请求

`DELETE {clob-endpoint}/order`


    Copy to Clipboard

    async function main() {
      // Send it to the server
      const resp = await clobClient.cancelOrder({
        orderID:
          "0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88",
      });
      console.log(resp);
      console.log(`Done!`);
    }
    main();



    Copy to Clipboard

    resp = client.cancel(order_id="0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88")
    print(resp)


#### 请求负载参数

名称 | 必需 | 类型 | 描述
---|---|---|---
orderID | 是 | string | 要取消的订单 ID

#### 响应格式

名称 | 类型 | 描述
---|---|---
canceled | string[] | 已取消订单列表
not_canceled | { } | 订单 ID - 原因映射，解释为什么该订单无法取消
