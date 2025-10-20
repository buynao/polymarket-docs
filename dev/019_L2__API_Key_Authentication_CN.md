# L2: API 密钥身份验证

下一级别的身份验证包括 API 密钥、密钥和密码短语，它们仅用于验证向 Polymarket 的 CLOB 发出的 API 请求。这包括下单/取消订单或检索账户订单和成交等操作。

当用户通过 `POST` `/auth/api-key` 注册时，服务器将使用签名作为种子来确定性地生成凭据。API 凭据包括三个字段：

**key**：标识凭据的 UUID。

**secret**：用于生成 HMAC 的密钥字符串，不随请求发送。

**passphrase**：每个请求都发送的密钥字符串，用于在我们的数据库中加密/解密密钥，从不存储在我们的数据库中。

所有未由私钥签名的请求（`/auth/api-key`）以及向私有端点发出的请求都需要 API 密钥签名。

## L2 请求头

请求头 | 是否必需？ | 描述
---|---|---
POLY_ADDRESS | 是 | Polygon 地址
POLY_SIGNATURE | 是 | 请求的 HMAC 签名
POLY_TIMESTAMP | 是 | 请求的 UNIX 时间戳
POLY_API_KEY | 是 | Polymarket API 密钥
POLY_PASSPHRASE | 是 | Polymarket API 密钥密码短语