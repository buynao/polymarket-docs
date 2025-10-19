# 📡 Polymarket API 概览

本文档包含 Polymarket 平台上可用的 API 类型及其数据获取方式的简要描述。

---

## 1. REST API

REST API 提供经典的 HTTP 端点来获取和管理数据。

**功能：**
- 获取**市场**列表 (`GET /markets`)
- **用户**数据 (`GET /users`)
- 获取**交易**历史
- **订单**管理（创建、取消、获取）
- 获取**价格**、**订单簿**、**价差**
- 通过私钥或 API 密钥进行**身份验证**

📄 相关文件：
- `014_Endpoints.md`
- `040_Trades.md`
- `044_Markets.md`
- `031_Create_and_Place_an_Order.md`

---

## 2. WebSocket API

允许通过订阅获取**实时流数据**。

**功能：**
- 订阅**交易** (`trade`)
- **订单簿** (`book`)
- **市场**变化 (`market`)
- **用户**事件 (`user`)
- 支持授权

📄 相关文件：
- `059_Websocket_API.md`
- `061_Subscription.md`
- `062_WSS_Authentication.md`

---

## 3. Subgraph API (GraphQL)

通过 The Graph 工作。适合从区块链进行深度查询。

**功能：**
- **市场解决**历史
- **流动性**信息
- 按**地址**和事件搜索

📄 相关文件：
- `091_Subgraph.md`
- `092_Overview.md`
- `093_Source.md`

---

## 4. Gamma Markets API

访问市场信息的替代方式。

**功能：**
- 通过 Gamma 系统访问市场
- 与主要 REST 结构不同的查询和选择

📄 相关文件：
- `069_Gamma_Markets_API.md`
- `070_Overview.md`
- `075_Markets.md`

---

> 🔄 基于仓库：`polymarket-docs` @drozdovmv54