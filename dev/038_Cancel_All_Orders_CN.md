# 取消所有订单

此端点需要 L2 Header。

取消用户发布的所有待处理订单。

## HTTP 请求

`DELETE {clob-endpoint}/cancel-all`


    Copy to Clipboard

    async function main() {
      const resp = await clobClient.cancelAll();
      console.log(resp);
      console.log(`Done!`);
    }

    main();



    Copy to Clipboard

    resp = client.cancel_all()
    print(resp)
    print("Done!")


## 响应格式

名称 | 类型 | 描述
---|---|---
canceled | string[] | 已取消的订单列表
not_canceled | { } | 订单ID与原因的映射，说明为什么该订单无法被取消
