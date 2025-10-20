## 赎回

一旦条件的支付已被报告（即由 UmaCTFAdapter 在 CTF 合约上调用 `reportPayouts`），拥有获胜结果份额的用户可以将其赎回为底层抵押品。具体来说，用户可以调用 CTF 合约上的 `redeemPositions` 函数，该函数将根据报告的支付向量销毁所有有价值的条件代币以换取抵押品。此函数具有以下参数：

  * `collateralToken`: IERC20 - 仓位支持的抵押品代币地址。
  * `parentCollectionId`: bytes32 - 被赎回仓位共有的结果集合 ID。在 Polymarket 情况下为空。
  * `conditionId`: bytes32 - 要赎回的条件 ID。
  * `indexSets`: uint[] - 表示给定条件的结果槽位的非平凡分区的不相交索引集数组。例如 A|B 和 C，但不是 A|B 和 B|C（不是不相交的）。每个元素都是一个数字，与条件一起表示结果集合。例如 0b110 是 A|B，0b010 是 B 等。在 Polymarket 情况下为 [1,2]（即 0x01, 0x10）。
