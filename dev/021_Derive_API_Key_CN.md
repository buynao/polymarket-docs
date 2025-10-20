# 派生 API 密钥

此端点需要 L1 请求头。

为地址和 nonce 派生一个现有的 API 密钥。

## HTTP 请求

`GET {clob-endpoint}/auth/derive-api-key`

```javascript
const creds = await clobClient.deriveApiKey(); // nonce 默认为 0
```

```python
creds = client.derive_api_key() ## nonce 默认为 0
```

> 上述请求返回的 JSON 结构如下：

```json
{
  "apiKey": "xxxxxxxxx-xxxxx-xxxxxx-xxxx-xxxxxxxxxxxx",
  "secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
  "passphrase": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```