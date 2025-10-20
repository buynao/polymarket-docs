### 获取多个订单簿

获取一组市场的订单簿摘要。

#### HTTP 请求

`POST {clob-endpoint}/books`


    Copy to Clipboard

    async function main() {
      const YES =
        "71321045679252212594626385532706912750332728571942532289631379312455583992563";
      const NO =
        "52114319501245915516055106046884209969926127482827954674443846427813813222426";

      const orderbooks = await clobClient.getOrderBooks([
        { token_id: YES },
        { token_id: NO },
      ] as BookParams[]);

      console.log(orderbooks);
    }
    main();



    Copy to Clipboard

    print(
        client.get_order_books(
            params=[
                BookParams(
                    token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563"
                ),
                BookParams(
                    token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426"
                ),
            ]
        )
    )


#### 请求参数

Name | Required | Type | Description
---|---|---|---
params | yes | BookParams | 订单簿的搜索参数

`BookParams` 对象的格式如下：

Name | Required | Type | Description
---|---|---|---
token_id | yes | string | 要获取订单簿的市场的 token ID

#### 响应格式

Name | Type | Description
---|---|---
- | Orderbook[] | 订单簿列表

`Orderbook` 对象的格式如下：

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
