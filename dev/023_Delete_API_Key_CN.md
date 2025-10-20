# 删除 API 密钥

此端点需要 L2 请求头。

删除用于验证请求的 API 密钥。

## HTTP 请求

`DELETE {clob-endpoint}/auth/api-key`

```javascript
const resp = await clobClient.deleteApiKey();
console.log(resp);
```

```python
resp = clob_client.delete_api_key()
print(resp)
```

> 如果成功，上述命令返回一个 `"OK"` 字符串值：

```
"OK"
```