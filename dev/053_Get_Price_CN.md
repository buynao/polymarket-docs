### 获取价格

获取市场的价格（最优买价或最优卖价）。

#### HTTP 请求

`GET {clob-endpoint}/price`


    Copy to Clipboard

    async function main() {
      const YES_TOKEN_ID =
        "71321045679252212594626385532706912750332728571942532289631379312455583992563";
      const NO_TOKEN_ID =
        "52114319501245915516055106046884209969926127482827954674443846427813813222426";

      clobClient
        .getPrice(YES_TOKEN_ID, "buy")
        .then((price: any) => console.log("YES", "BUY", price));
      clobClient
        .getPrice(YES_TOKEN_ID, "sell")
        .then((price: any) => console.log("YES", "SELL", price));
      clobClient
        .getPrice(NO_TOKEN_ID, "buy")
        .then((price: any) => console.log("NO", "BUY", price));
      clobClient
        .getPrice(NO_TOKEN_ID, "sell")
        .then((price: any) => console.log("NO", "SELL", price));
    }
    main();



    Copy to Clipboard

    print(
        client.get_price(
            token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563", side="buy
        )
    )


#### 请求负载参数

Name | Required | Type | Description
---|---|---|---
token_id | yes | string | 要获取价格的 token ID
side | yes | string | buy 或 sell

#### 响应

`{"price": ".513"}`
