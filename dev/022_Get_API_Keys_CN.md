# 获取 API 密钥

此端点需要 L2 请求头。

获取与 Polygon 地址关联的所有 API 密钥。

## HTTP 请求

`GET {clob-endpoint}/auth/api-keys`

```javascript
const apiKeys = await clobClient.getApiKeys();
```

```python
api_keys = client.get_api_keys()
```

> 上述命令返回的 JSON 结构如下：

```json
{
  "apiKeys": [ "xxxxxxxxx-xxxxx-xxxxxx-xxxx-xxxxxxxxxxxx", ... ]
}
```