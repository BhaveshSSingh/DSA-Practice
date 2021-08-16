// 121. Best Time to Buy and Sell Stock

var maxProfit = function (prices) {
  let minTillNow = 100000;
  bestProfit = 0;
  for (price in prices) {
    if (minTillNow > price) {
      minTillNow = price;
    } else if (bestProfit < price - minTillNow) {
      bestProfit = price - minTillNow;
    }
  }

  return bestProfit;
};
