# How are prices calculated? - Polymarket Learn

Markets

# How are prices calculated?#

All trades on Polymarket are peer-to-peer, meaning you are trading with / betting against other Polymarket users, not Polymarket itself.

## Initial Price#

  * When a market is created, there are initially zero shares and no pre-defined prices or odds.

  * Market makers (a fancy term for traders placing limit orders) interested in buying YES or NO shares can place [Limit Orders](/docs/guides/trading/limit-orders) at the price they're willing to pay

  * When offers for the YES and NO side equal $1.00, the order is "matched" and that $1.00 is converted into 1 YES and 1 NO share, each going to their respective buyers.




For example, if you place a limit order at $0.60 for YES, that order is matched when someone places a NO order at $0.40. _This becomes the initial market price._

Polymarket is not a "bookie" and does not set prices / odds. Prices are set by what Polymarket users are currently willling to buy/sell shares at. All trades are peer-to-peer.

## Future Price#

The prices displayed on Polymarket are the midpoint of the bid-ask spread in the orderbook — unless that spread is over $0.10, in which case the last traded price is used.

Like the stock market, prices on Polymarket are a function of realtime supply & demand.

### Prices = Probabilities#

In the market below, the probability of 37% is the midpoint between the 34¢ bid and 40¢ ask. If the bid-ask spread is wider than 10¢, the probability is shown as the last traded price.

![](https://polymarket-upload.s3.us-east-2.amazonaws.com/how_are_prices_calculated.png)

You may not be able to buy shares at the displayed probability / price because there is a bid-ask spread. In the above example, a trader wanting to buy shares would pay 40¢ for up to 4,200 shares, after which the price would rise to 43¢.

[Market creation](/docs/guides/markets/how-are-markets-created/)

[Market resolution](/docs/guides/markets/how-are-markets-resolved/)

[](https://x.com/polymarket)[](https://discord.gg/polymarket)[](https://github.com/polymarket)

[](https://github.com/polymarket/learn/blob/main/pages/docs/guides/trading/how-are-prices-calculated.mdx)