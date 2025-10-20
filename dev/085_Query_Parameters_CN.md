#### 查询参数

名称 | 类型 | 描述
---|---|---
limit | number | 限制查询结果数量
offset | number | 分页偏移量
order | string | 排序字段
ascending | boolean | 排序方向，默认为 true，需要 `order` 参数
id | number | 要查询的单个事件 ID，可以多次使用以获取多个事件
slug | string | 要查询的单个事件 slug，可以多次使用以获取多个事件
archived | boolean | 按归档状态筛选
active | boolean | 按活跃状态筛选
closed | boolean | 按关闭状态筛选
liquidity_min | decimal | 按最小流动性筛选
liquidity_max | decimal | 按最大流动性筛选
volume_min | decimal | 按最小交易量筛选
volume_max | decimal | 按最大交易量筛选
start_date_min | string | 按最小开始日期筛选
start_date_max | string | 按最大开始日期筛选
end_date_min | string | 按最小结束日期筛选
end_date_max | string | 按最大结束日期筛选
tag | string | 按标签标签筛选
tag_id | number | 按标签 ID 筛选
related_tags | boolean | 包含相关标签的事件，需要 `tag_id` 参数
tag_slug | string | 按标签 slug 筛选
标签筛选器是互斥的，优先级为 `tag` > `tag_id` > `tag_slug`。
