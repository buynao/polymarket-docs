### 获取简化市场信息

获取以简化模式表示的可用 CLOB 市场。

#### HTTP 请求

`GET {clob-endpoint}/simplified-markets?next_cursor={next_cursor}`


    Copy to Clipboard

    async function main() {
      const markets = await clobClient.getSimplifiedMarkets("");
      console.log(`markets: `);
      console.log(markets);
    }

    main();



    Copy to Clipboard

    resp = client.get_simplified_markets(next_cursor = "")
    print(resp)
    print("Done!")


#### 响应格式

Name | Type | Description
---|---|---
limit | number | 单页结果的限制数量
count | number | 结果数量
next_cursor | string | 用于检索下一页的分页项，base64 编码。'LTE=' 表示结束，空字符串 ('') 表示开始
data | SimplifiedMarket[] | 市场列表

`SimplifiedMarket` 对象的格式如下：

Name | Type | Description
---|---|---
condition_id | string | 市场的 ID，也是 CTF condition ID
tokens | Tokens[2] | 市场的二元代币对
rewards | Rewards | 奖励相关数据
min_incentive_size | string | 激励资格的最小挂单规模
max_incentive_spread | string | 订单有资格获得激励的最大价差（以美分为单位）
active | boolean | 表示市场是否处于活跃/在线状态的布尔值
closed | boolean | 表示市场是否关闭/开放的布尔值
