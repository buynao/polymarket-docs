### 获取中间价

获取市场的中间价格（最优买价和最优卖价的中间值）。

#### HTTP 请求

`GET {clob-endpoint}/midpoint`


    Copy to Clipboard

    async function main() {
      const resp = client.getMidpoint(
        (tokenID =
          "71321045679252212594626385532706912750332728571942532289631379312455583992563")
      );
      console.log(resp);
    }
    main();



    Copy to Clipboard

    resp = client.get_midpoint(
        "71321045679252212594626385532706912750332728571942532289631379312455583992563"
    )
    print(resp)
    print("Done!")


#### 请求负载参数

Name | Required | Type | Description
---|---|---|---
token_id | yes | string | 要获取价格的市场的 token ID

#### 响应

`{'mid': '0.55'}`
