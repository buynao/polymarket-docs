# L1: 私钥身份验证

最高级别的身份验证是通过账户的 Polygon 私钥。私钥保持对用户资金的控制，因此所有交易都是非托管的。运营商永远不会控制用户的资金。

以下操作需要私钥身份验证：

* 下单（用于签名订单）
* 创建或撤销 API 密钥

## L1 请求头

请求头 | 是否必需？ | 描述
---|---|---
POLY_ADDRESS | 是 | Polygon 地址
POLY_SIGNATURE | 是 | CLOB EIP 712 签名
POLY_TIMESTAMP | 是 | 当前 UNIX 时间戳
POLY_NONCE | 是 | Nonce。默认为 0

POLY_SIGNATURE 通过签名以下 EIP712 结构生成：

```javascript
const domain = {
  name: "ClobAuthDomain",
  version: "1",
  chainId: chainId, // Polygon ChainID 137
};

const types = {
  ClobAuth: [
    { name: "address", type: "address" },
    { name: "timestamp", type: "string" },
    { name: "nonce", type: "uint256" },
    { name: "message", type: "string" },
  ],
};
const value = {
  address: signingAddress, // 签名地址
  timestamp: ts, // CLOB API 服务器时间戳
  nonce: nonce, // 使用的 nonce
  message: "This message attests that I control the given wallet", // 表明用户控制钱包的静态消息
};
const sig = await signer._signTypedData(domain, types, value);
```

在 [Typescript](https://github.com/Polymarket/clob-client/blob/main/src/signing/eip712.ts) 和 [Python](https://github.com/Polymarket/py-clob-client/blob/main/py_clob_client/signing/eip712.py) 客户端中有实现。