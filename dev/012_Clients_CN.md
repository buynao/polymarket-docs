# 客户端

> 安装

```bash
npm i -s @polymarket/clob-client

yarn add @polymarket/clob-client
```

```bash
pip install py-clob-client
```

Polymarket 已实现了以下参考客户端，允许通过编程方式使用 API：

* [clob-client](https://github.com/Polymarket/clob-client) (Typescript)
* [py-clob-client](https://github.com/Polymarket/py-clob-client) (Python)

> 初始化

```python
from py_clob_client.client import ClobClient

host: str = ""
key: str = ""
chain_id: int = 137

### 初始化直接从 EOA 交易的客户端
client = ClobClient(host, key=key, chain_id=chain_id)

### 初始化使用与 Email/Magic 账户关联的 Polymarket 代理的客户端
# funder = "<代理地址>"
# client = ClobClient(host, key=key, chain_id=chain_id, funder=funder, signature_type=SignatureType.POLYMARKET_PROXY)
```

```typescript
import { ClobClient } from "@polymarket/clob-client";

const host = "";
const key = "";
const chainId = 137;

// 初始化直接从 EOA 交易的客户端
const client = new ClobClient(host, key, chainId);

// 初始化使用与 Email/Magic 账户关联的 Polymarket 代理的客户端
// const funder = "<代理地址>";
// const client = new ClobClient(host, key, chainId, undefined, undefined, funder, 1);
```