# 获取仅平仓模式状态

此端点需要 L2 请求头。

获取仅平仓模式标志的值。

## HTTP 请求

`GET {clob-endpoint}/auth/ban-status/closed-only`

```javascript
const closedOnlyMode = await clobClient.getClosedOnlyMode();
```

```python
closed_only_mode = client.get_closed_only_mode()
```

> 上述命令返回的 JSON 结构如下：

```json
{
  "closed_only": true|false
}
```