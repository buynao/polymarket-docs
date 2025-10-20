### 获取价差列表

获取一组市场的价差。

#### HTTP 请求

`GET {clob-endpoint}/spread`


    Copy to Clipboard

    async function main() {
      const YES =
        "71321045679252212594626385532706912750332728571942532289631379312455583992563";
      const NO =
        "52114319501245915516055106046884209969926127482827954674443846427813813222426";

      const spreads = await clobClient.getSpreads([
        { token_id: YES },
        { token_id: NO },
      ] as BookParams[]);
    }
    main();



    Copy to Clipboard

    resp = client.get_spreads(
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


#### 请求参数

名称 | 必需 | 类型 | 描述
---|---|---|---
params | 是 | BookParams | 订单簿的搜索参数

`BookParams` 对象的格式如下：

名称 | 必需 | 类型 | 描述
---|---|---|---
token_id | 是 | string | 要获取订单簿的市场代币 ID

#### 响应

`{[asset_id]: spread`


    Copy to Clipboard

    {
      "52114319501245915516055106046884209969926127482827954674443846427813813222426": "0.01",
      "71321045679252212594626385532706912750332728571942532289631379312455583992563": "0.01"
    }
