# 访问状态

请定期通过 [ban-status/ 端点](https://docs.polymarket.com/#access-status-2) 检查您账户的访问状态。如果端点返回的 `cert_required` 值为 true，则需要提供居住证明，如果在 14 天内未提供，将导致账户变为仅平仓状态。

为证明您未违反服务条款，请发送邮件至 ops@polymarket.com，包含以下信息：
- 您的地址
- 身份证明（护照、驾照或其他）
- 居住证明（近期的水电费账单、银行账单、电话账单）

在后续通信中，您还需要签署并返回非美国居民证明。完成后，24 小时内 cert_required 状态应会标记为 false。