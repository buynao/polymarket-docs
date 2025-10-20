### 获取价差

获取市场的价差。

#### HTTP 请求

`GET {clob-endpoint}/spread`


    Copy to Clipboard

    async function main() {
      const YES_TOKEN_ID =
        "71321045679252212594626385532706912750332728571942532289631379312455583992563";
      const NO_TOKEN_ID =
        "52114319501245915516055106046884209969926127482827954674443846427813813222426";

      clobClient
        .getSpread(YES_TOKEN_ID)
        .then((spread: any) => console.log("YES", spread));
      clobClient
        .getSpread(NO_TOKEN_ID)
        .then((spread: any) => console.log("NO", spread));
    }
    main();



    Copy to Clipboard

    print(
        client.get_spread(
            "71321045679252212594626385532706912750332728571942532289631379312455583992563"
        )
    )


#### 请求参数

名称 | 必需 | 类型 | 描述
---|---|---|---
token_id | 是 | string | 要获取价差的代币 ID

#### 响应

`{"spread": ".513"}`
