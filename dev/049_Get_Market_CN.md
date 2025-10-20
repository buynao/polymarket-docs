### 获取市场信息

获取单个 CLOB 市场。


    Copy to Clipboard

    async function main() {
      const market = await clobClient.getMarket("condition_id");
      console.log(`market: `);
      console.log(market);
    }

    main();



    Copy to Clipboard

    resp = client.get_market(condition_id = "...")
    print(resp)
    print("Done!")


#### HTTP 请求

`GET {clob-endpoint}/markets/{condition_id}`

#### 响应格式

Name | Type | Description
---|---|---
market | Market | 市场对象
