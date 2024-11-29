
# BRUTE FORCE APPROACH

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = float('-inf')
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                           profit = prices[j]-prices[i]

                           if profit > 0:
                                  max_profit = max(profit , max_profit)
                                


            
        return max_profit if max_profit > float('-inf') else 0
                           
                        #    TIME COMPLEXITY = O(N^2)
                        #    SPACE COMPLEXITY = O(1)


# Approach 2
class Solution:
       def maxProfit(self, prices: List[int]) -> int:
              min_price = float('inf')
              max_profit = 0

              for price in prices:
                     if price < min_price:
                            min_price = price


                    
                     profit = price - min_price

                     if profit > max_profit:
                            max_profit = profit


                
              return max_profit
       