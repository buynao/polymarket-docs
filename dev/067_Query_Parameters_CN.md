#### 查询参数

名称 | 类型 | 描述
---|---|---
market | number | 用于获取价格历史的 CLOB token id
startTs | number | 开始时间，UTC unix 时间戳
endTs | number | 结束时间，UTC unix 时间戳
interval | string | 表示从当前时间结束的时间段的字符串
fidelity | number | 数据的分辨率，以分钟为单位

查询参数 `startTs/endTs` 与 `interval` 互斥。`interval` 的选项包括：

  * `1m`: 1个月
  * `1w`: 1周
  * `1d`: 1天
  * `6h`: 6小时
  * `1h`: 1小时
  * `max`: 最大范围
