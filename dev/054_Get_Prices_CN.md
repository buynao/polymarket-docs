### 获取多个价格

获取一组市场的价格（最优买价或最优卖价）。

#### HTTP 请求

`POST {clob-endpoint}/prices`


    Copy to Clipboard

    async function main() {
      const YES =
        "71321045679252212594626385532706912750332728571942532289631379312455583992563";
      const NO =
        "52114319501245915516055106046884209969926127482827954674443846427813813222426";

      const prices = await clobClient.getPrices([
        { token_id: YES, side: Side.BUY },
        { token_id: YES, side: Side.SELL },
        { token_id: NO, side: Side.BUY },
        { token_id: NO, side: Side.SELL },
      ] as BookParams[]);
    }
    main();



    Copy to Clipboard

    resp = client.get_prices(
        params=[
            BookParams(
                token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
                side="BUY",
            ),
            BookParams(
                token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
                side="SELL",
            ),
            BookParams(
                token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426",
                side="BUY",
            ),
            BookParams(
                token_id="52114319501245915516055106046884209969926127482827954674443846427813813222426",
                side="SELL",
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
side | yes | string | BUY 或 SELL

#### 响应

`{[asset_id]: {[side]: price}}`


    Copy to Clipboard

    {
      "52114319501245915516055106046884209969926127482827954674443846427813813222426": {
        "BUY": "0.49",
        "SELL": "0.5"
      },
      "71321045679252212594626385532706912750332728571942532289631379312455583992563": {
        "BUY": "0.5",
        "SELL": "0.51"
      }
    }
