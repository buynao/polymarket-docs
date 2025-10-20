# 创建 API 密钥

此端点需要 L1 请求头。

为用户创建新的 API 密钥凭据。

## HTTP 请求

`POST {clob-endpoint}/auth/api-key`

```javascript
const creds = await clobClient.createApiKey(); // nonce 默认为 0
```

```python
creds = client.create_api_key()
```

> 上述请求返回的 JSON 结构如下：

```json
{
  "apiKey": "xxxxxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxx",
  "secret": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx=",
  "passphrase": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
```