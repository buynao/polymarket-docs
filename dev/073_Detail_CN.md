### 详细说明

  1. Market（市场）
    1. 包含与交易市场相关的数据。映射到一对 clob token id、一个做市商地址、一个问题 id 和一个条件 id
  2. Event（事件）
    1. 包含一组 _markets（市场）_
    2. 变体：
      1. 包含1个 _market（市场）_ 的事件（即产生 SMP）
      2. 包含2个或更多 _markets（市场）_ 的事件（即产生 GMP）
