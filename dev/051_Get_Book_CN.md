### 获取订单簿

获取市场的订单簿摘要。

#### HTTP 请求

`GET {clob-endpoint}/book`


    Copy to Clipboard

    async function main() {
      const resp = await clobClient.getOrderBook(
        "71321045679252212594626385532706912750332728571942532289631379312455583992563"
      );
      console.log(resp);
    }
    main();



    Copy to Clipboard

    print(
        client.get_order_book(
            "71321045679252212594626385532706912750332728571942532289631379312455583992563"
        )
    )


#### 请求参数

Name | Required | Type | Description
---|---|---|---
token_id | yes | string | 要获取订单簿的市场的 token ID

#### 响应格式

Name | Type | Description
---|---|---
market | string | condition id
asset_id | string | 资产/代币的 ID
hash | string | 订单簿内容的哈希摘要
timestamp | string | 当前订单簿生成的 Unix 时间戳（毫秒，1/1000 秒）
bids | OrderSummary[] | 买单级别列表
asks | OrderSummary[] | 卖单级别列表

`OrderSummary` 对象的格式如下：

Name | Type | Description
---|---|---
price | string | 价格
size | string | 数量
