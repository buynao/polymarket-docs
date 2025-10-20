# 获取采样市场

获取启用了奖励的可用 CLOB 市场。

## HTTP 请求

`GET {clob-endpoint}/sampling-markets?next_cursor={next_cursor}`


    Copy to Clipboard

    async function main() {
      const markets = await clobClient.getSamplingMarkets("");
      console.log(`markets: `);
      console.log(markets);
    }

    main();



    Copy to Clipboard

    resp = client.get_sampling_markets(next_cursor = "")
    print(resp)
    print("Done!")


## 响应格式

名称 | 类型 | 描述
---|---|---
limit | number | 单页结果的限制
count | number | 结果数量
next_cursor | string | 用于检索下一页的分页项，base64 编码。'LTE=' 表示结束，空字符串（''）表示开始
data | Market[] | 采样市场列表
