### 订阅

要订阅，请在打开连接时发送包含以下身份验证和意图信息的消息。

字段 | 类型 | 描述
---|---|---
auth | Auth | 参见 WSS Authentication
markets | string[] | 要接收事件的市场数组（条件 ID）（用于 `user` 通道）
assets_ids | string[] | 要接收事件的资产 ID 数组（代币 ID）（用于 `market` 通道）
type | string | 要订阅的通道 ID（**User** 或 **Market**）

其中 `auth` 字段的类型为 `Auth`，其格式在下面的 WSS Authentication 部分中描述。
