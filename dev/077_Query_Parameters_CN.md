#### 查询参数

名称 | 类型 | 描述
---|---|---
market | number | 要获取价格历史的 CLOB 代币 ID
startTs | number | 开始时间，UTC Unix 时间戳
endTs | number | 结束时间，UTC Unix 时间戳
interval | string | 表示截止到当前时间的持续时间的字符串
fidelity | number | 数据的分辨率，以分钟为单位

查询参数 `startTs/endTs` 与 `interval` 互斥。`interval` 的选项包括：

  * `1m`：1 个月
  * `1w`：1 周
  * `1d`：1 天
  * `6h`：6 小时
  * `1h`：1 小时
  * `max`：最大范围
