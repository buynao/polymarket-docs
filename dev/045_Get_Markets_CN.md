# 获取市场

获取可用的 CLOB 市场（分页）。

## HTTP 请求

`GET {clob-endpoint}/markets?next_cursor={next_cursor}`


    Copy to Clipboard

    async function main() {
      const markets = await clobClient.getMarkets("");
      console.log(`markets: `);
      console.log(markets);
    }

    main();



    Copy to Clipboard

    resp = client.get_markets(next_cursor = "")
    print(resp)
    print("Done!")


## 请求参数

名称 | 是否必需 | 类型 | 描述
---|---|---|---
next_cursor | 否 | string | 开始的游标，用于遍历分页响应

## 响应格式

名称 | 类型 | 描述
---|---|---
limit | number | 单页结果的限制
count | number | 结果数量
next_cursor | string | 用于检索下一页的分页项，base64 编码。'LTE=' 表示结束，空字符串（''）表示开始
data | Market[] | 市场列表

`Market` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
condition_id | string | 市场ID，也是 CTF 条件ID
question_id | string | 市场的问题ID，也是用于派生 `condition_id` 的 CTF 问题ID
tokens | Tokens[2] | 市场的二元代币对
rewards | Rewards | 奖励相关数据
minimum_order_size | string | 最小限价订单大小
minimum_tick_size | string | 以隐含概率单位表示的最小tick大小（最大价格分辨率）
description | string | 市场描述
category | string | 市场类别
end_date_iso | string | 市场结束日期的 ISO 字符串
game_start_time | string | 用于触发延迟的游戏开始时间的 ISO 字符串
question | string | 问题
market_slug | string | 市场的 slug
min_incentive_size | string | 激励资格的最小静态订单大小
max_incentive_spread | string | 符合激励条件的订单的最大价差（以美分为单位）
active | boolean | 布尔值，指示市场是否活跃/有效
closed | boolean | 布尔值，指示市场是否关闭/开放
seconds_delay | integer | 游戏内交易的匹配延迟秒数
icon | string | 市场图标图像的引用
fpmm | string | Polygon 网络上关联的固定产品做市商的地址

`Token` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
token_id | string | ERC1155 代币ID
outcome | string | 人可读的结果

`Rewards` 对象的格式如下：

名称 | 类型 | 描述
---|---|---
min_size | number | 订单评分的最小大小
max_spread | number | 从中点开始订单评分的最大价差
event_start_date | string | 事件开始时的字符串日期
event_end_date | string | 事件结束时的字符串日期
in_game_multiplier | number | 游戏开始后的奖励乘数
reward_epoch | number | 当前奖励时期
