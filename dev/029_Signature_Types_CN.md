# 签名类型

### 签名类型

Polymarket 的 CLOB 支持 3 种签名类型。订单必须标识它们使用的签名类型。可用的 typescript 和 python 客户端通过允许在初始化时指定资金提供者地址和签名者类型来抽象使用以下签名类型签名和准备订单的复杂性。支持的签名类型包括：

类型 | ID | 描述
---|---|---
EOA | 0 | 由 EOA 签名的 EIP712 签名
POLY_PROXY | 1 | 由与资金提供 Polymarket 代理钱包关联的签名者签名的 EIP712 签名
POLY_GNOSIS_SAFE | 2 | 由与资金提供 Polymarket Gnosis Safe 钱包关联的签名者签名的 EIP712 签名
