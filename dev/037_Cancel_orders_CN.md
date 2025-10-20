# 取消多个订单

此端点需要 L2 Header。

取消多个订单。

## HTTP 请求

`DELETE {clob-endpoint}/orders`


    Copy to Clipboard

    async function main() {
      // 发送到服务器
      const resp = await clobClient.cancelOrders([
        "0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88",
        "0xaaaa...",
      ]);
      console.log(resp);
      console.log(`Done!`);
    }
    main();



    Copy to Clipboard

    resp = client.cancel_orders(["0x38a73eed1e6d177545e9ab027abddfb7e08dbe975fa777123b1752d203d6ac88", "0xaaaa..."])
    print(resp)


## 请求负载参数

名称 | 是否必需 | 类型 | 描述
---|---|---|---
null | 是 | string[] | 要取消的订单ID列表

## 响应格式

名称 | 类型 | 描述
---|---|---
canceled | string[] | 已取消的订单列表
not_canceled | { } | 订单ID与原因的映射，说明为什么该订单无法被取消
