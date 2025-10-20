# 创建并放置订单

### 创建并放置订单

此端点需要 L2 请求头。

使用 Polymarket CLOB API 客户端创建并放置订单。所有订单都表示为"限价"订单，但通过允许可市场化的限价订单来实现"市价"订单，这些订单在输入时以可用的最佳价格执行。因此，要放置市价订单，只需确保您的价格可与当前静止限价订单进行市场化交易即可。

#### HTTP 请求

`POST {clob-endpoint}/order`


    Copy to Clipboard

    // GTC Order example
    //
    import { Side, OrderType } from "@polymarket/clob-client";

    async function main() {
      // Create a buy order for 100 YES for 0.50c
      // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563
      const order = await clobClient.createOrder({
        tokenID:
          "71321045679252212594626385532706912750332728571942532289631379312455583992563",
        price: 0.5,
        side: Side.BUY,
        size: 100,
        feeRateBps: 0,
        nonce: 1,
      });
      console.log("Created Order", order);

      // Send it to the server

      // GTC Order
      const resp = await clobClient.postOrder(order, OrderType.GTC);
      console.log(resp);
    }

    main();



    Copy to Clipboard

    // GTD Order example
    //
    import { Side, OrderType } from "@polymarket/clob-client";

    async function main() {
      // Create a buy order for 100 YES for 0.50c that expires in 1 minute
      // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563

      // There is a 1 minute of security threshold for the expiration field.
      // If we need the order to expire in 30 seconds the correct expiration value is:
      // now + 1 miute + 30 seconds
      const oneMinute = 60 * 1000;
      const seconds = 30 * 1000;
      const expiration = parseInt(
        ((new Date().getTime() + oneMinute + seconds) / 1000).toString()
      );

      const order = await clobClient.createOrder({
        tokenID:
          "71321045679252212594626385532706912750332728571942532289631379312455583992563",
        price: 0.5,
        side: Side.BUY,
        size: 100,
        feeRateBps: 0,
        nonce: 1,
        // There is a 1 minute of security threshold for the expiration field.
        // If we need the order to expire in 30 seconds the correct expiration value is:
        // now + 1 miute + 30 seconds
        expiration: expiration,
      });
      console.log("Created Order", order);

      // Send it to the server

      // GTD Order
      const resp = await clobClient.postOrder(order, OrderType.GTD);
      console.log(resp);
    }

    main();



    Copy to Clipboard

    // FOK BUY Order example
    //
    import { Side, OrderType } from "@polymarket/clob-client";

    async function main() {
      // Create a market buy order for $100
      // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563

      const marketOrder = await clobClient.createMarketOrder({
        side: Side.BUY,
        tokenID:
          "71321045679252212594626385532706912750332728571942532289631379312455583992563",
        amount: 100, // $$$
        feeRateBps: 0,
        nonce: 0,
        price: 0.5,
      });
      console.log("Created Order", order);

      // Send it to the server
      // FOK Order
      const resp = await clobClient.postOrder(order, OrderType.FOK);
      console.log(resp);
    }

    main();



    Copy to Clipboard

    // FOK SELL Order example
    //
    import { Side, OrderType } from "@polymarket/clob-client";

    async function main() {
      // Create a market sell order for 100 shares
      // YES: 71321045679252212594626385532706912750332728571942532289631379312455583992563

      const marketOrder = await clobClient.createMarketOrder({
        side: Side.SELL,
        tokenID:
          "71321045679252212594626385532706912750332728571942532289631379312455583992563",
        amount: 100, // shares
        feeRateBps: 0,
        nonce: 0,
        price: 0.5,
      });
      console.log("Created Order", order);

      // Send it to the server
      // FOK Order
      const resp = await clobClient.postOrder(order, OrderType.FOK);
      console.log(resp);
    }

    main();



    Copy to Clipboard

    ## GTC Order
    #
    from py_clob_client.clob_types import OrderArgs, OrderType
    from py_clob_client.order_builder.constants import BUY

    ## Create and sign a limit order buying 100 YES tokens for 0.50c each
    order_args = OrderArgs(
        price=0.50,
        size=100.0,
        side=BUY,
        token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
    )
    signed_order = client.create_order(order_args)

    ## GTC Order
    resp = client.post_order(signed_order, OrderType.GTC)
    print(resp)



    Copy to Clipboard

    ## GTD Order
    #
    from py_clob_client.clob_types import OrderArgs, OrderType
    from py_clob_client.order_builder.constants import BUY

    ## Create and sign a limit order buying 100 YES tokens for 0.50c each
    order_args = OrderArgs(
        price=0.50,
        size=100.0,
        side=BUY,
        token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
        # There is a 1 minute of security threshold for the expiration field.
        # If we need the order to expire in 30 seconds the correct expiration value is:
        # now + 1 miute + 30 seconds
        expiration="100000000000"
    )
    signed_order = client.create_order(order_args)

    ## GTD Order
    resp = client.post_order(signed_order, OrderType.GTD)
    print(resp)



    Copy to Clipboard

    ## FOK BUY Order
    #
    from py_clob_client.clob_types import MarketOrderArgs, OrderType
    from py_clob_client.order_builder.constants import BUY

    ## Create and sign a market BUY order for $100
    order_args = MarketOrderArgs(
        token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
        amount=100.0, # $$$
        side=BUY,
    )
    signed_order = client.create_market_order(order_args)

    ## FOK Order
    resp = client.post_order(signed_order, OrderType.FOK)
    print(resp)



    Copy to Clipboard

    ## FOK SELL Order
    #
    from py_clob_client.clob_types import MarketOrderArgs, OrderType
    from py_clob_client.order_builder.constants import SELL

    ## Create and sign a market BUY order for 100 shares
    order_args = MarketOrderArgs(
        token_id="71321045679252212594626385532706912750332728571942532289631379312455583992563",
        amount=100.0, # shares
        side=SELL,
    )
    signed_order = client.create_market_order(order_args)

    ## FOK Order
    resp = client.post_order(signed_order, OrderType.FOK)
    print(resp)


#### 请求负载参数

名称 | 必需 | 类型 | 描述
---|---|---|---
order | 是 | Order | 签名订单对象
owner | 是 | string | 订单所有者的 API 密钥
orderType | 是 | string | 订单类型（"FOK"、"GTC"、"GTD"）

`Order` 对象的格式如下：

名称 | 必需 | 类型 | 描述
---|---|---|---
salt | 是 | integer | 用于创建唯一订单的随机盐
maker | 是 | string | maker 地址（资金提供者）
signer | 是 | string | 签名地址
taker | 是 | string | taker 地址（运营商）
tokenId | 是 | string | 正在交易的条件代币的 ERC1155 代币 ID
makerAmount | 是 | string | maker 愿意支出的最大金额
takerAmount | 是 | string | taker 必须支付给 maker 的最小金额
expiration | 是 | string | Unix 过期时间戳
nonce | 是 | string | 订单关联的 maker 的 Exchange nonce
feeRateBps | 是 | string | 运营商要求的基点费率
side | 是 | string | 买入或卖出枚举索引
signatureType | 是 | integer | 签名类型枚举索引
signature | 是 | string | 十六进制编码签名

##### 订单类型：

  * `FOK`：'Fill-Or-Kill' 订单是一个市价订单，用于购买（以美元）或出售（以股份）必须立即全部执行的股份；否则，整个订单将被取消。
  * `GTC`：'Good-Til-Cancelled' 订单是一个限价订单，在其被履行或取消之前一直有效。
  * `GTD`：'Good-Til-Day' 订单是一种订单，在其指定日期（UTC 秒时间戳）之前一直有效，除非已被履行或取消。有一个一分钟的安全阈值：如果订单需要在 30 秒内过期，正确的过期值是：now + 1 分钟 + 30 秒



#### 响应格式

名称 | 类型 | 描述
---|---|---
success | boolean | 指示服务器端错误的布尔值（如果 success == false -> 服务器端错误）
errorMsg | string | 放置失败时的错误消息（如果 `success == true && errorMsg != ''` -> 客户端错误，原因在 `errorMsg` 中）
orderID | string | 订单 ID
transactionsHashes | string[] | 如果订单可市场化并触发匹配操作，则为结算交易的哈希
status | string | 订单状态

#### 插入错误/消息

如果放置响应对象的 `errorMsg` 字段不是空字符串，则订单无法立即放置。这可能是由于延迟或失败。如果 `success` 不是 `true`，则放置订单时出现问题。可能出现以下错误/消息。

错误 | 失败？ | 消息 | 描述
---|---|---|---
INVALID_ORDER_MIN_TICK_SIZE | 是 | order is invalid. Price () breaks minimum tick size rule: | 订单价格不符合正确的价格刻度
INVALID_ORDER_MIN_SIZE | 是 | order is invalid. Size () lower than the minimum: | 订单大小必须满足最小大小阈值要求
INVALID_ORDER_DUPLICATED | 是 | order is invalid. Duplicated. | 相同订单已被放置，不能再次放置
INVALID_ORDER_NOT_ENOUGH_BALANCE | 是 | not enough balance / allowance | 资金提供者地址没有足够的余额或授权额度用于订单
INVALID_ORDER_EXPIRATION | 是 | invalid expiration | 过期字段表示的时间早于现在
INSERT_ORDER_ERROR | 是 | could not insert order | 插入订单时的系统错误
EXECUTION_ERROR | 是 | could not run the execution | 尝试执行交易时的系统错误
ORDER_DELAYED | 否 | order match delayed due to market conditions | 订单放置延迟
DELAYING_ORDER_ERROR | 是 | error delaying the order | 延迟订单时的系统错误
FOK_ORDER_NOT_FILLED_ERROR | 是 | order couldn't be fully filled. FOK orders are fully filled or killed. | FOK 订单未完全成交，因此无法放置
MARKET_NOT_READY | 否 | the market is not yet ready to process new orders | 系统尚未接受市场订单

#### 插入状态

放置订单时，会包含一个状态字段。此状态字段提供有关订单放置结果状态的附加信息。可能的值包括：

状态 | 描述
---|---
live | 订单已放置且有效
matched | 订单已匹配（可市场化）
delayed | 订单可市场化，但受匹配延迟影响
unmatched | 订单可市场化，但延迟失败，放置不成功
