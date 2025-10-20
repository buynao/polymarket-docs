# 访问状态

此端点按签名者地址返回 `cert_required` 的值。请定期检查此状态，如果 `cert_required` 返回 true，请参考[此章节](https://docs.polymarket.com/#access-status)。

## HTTP 请求

```
GET '{clob-endpoint}/auth/ban-status/cert-required?address={signer address}'
```

## 响应

```json
{
  "cert_required": false | true
}
```