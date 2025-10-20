### 获取多个中间价

获取一组市场的中间价格（最优买价和最优卖价的中间值）。

#### HTTP 请求

`POST {clob-endpoint}/midpoints`


    Copy to Clipboard

    async function main() {
      const YES =
        "71321045679252212594626385532706912750332728571942532289631379312455583992563";
      const NO =
        "52114319501245915516055106046884209969926127482827954674443846427813813222426";

      const midpoints = await clobClient.getMidpoints([
        { token_id: YES },
        { token_id: NO },
      ] as BookParams[]);
    }
    main();



    Copy to Clipboard

    resp = client.get_midpoints(
        params=[
            BookParams(
                token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563"
            ),
            BookParams(
                token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426"
            ),
        ]
    )
    print(resp)


#### 请求负载参数

Name | Required | Type | Description
---|---|---|---
params | yes | BookParams | 订单簿的搜索参数

`BookParams` 对象的格式如下：

Name | Required | Type | Description
---|---|---|---
token_id | yes | string | 要获取订单簿的市场的 token ID

#### 响应

`{[asset_id]: mid price`


    Copy to Clipboard

    {
      "52114319501245915516055106046884209969926127482827954674443846427813813222426": "0.495",
      "71321045679252212594626385532706912750332728571942532289631379312455583992563": "0.505"
    }
