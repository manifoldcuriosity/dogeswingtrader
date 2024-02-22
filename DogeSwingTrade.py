import robin_stocks as rs
import os
import time
import sys
from datetime import datetime


robin_user = os.environ.get("robinhood_username")
robin_pass = os.environ.get("robinhood_password")

rs.login(username=robin_user,
         password=robin_pass,
         expiresIn=86400,
         by_sms=True)


doge_price = float(rs.crypto.get_crypto_quote('DOGE', "ask_price"))
dogecoin_count = 0
bought_doge_price = doge_price
sold_doge_price = doge_price
now = datetime.now()
timestamp = datetime.timestamp(now)
dt_object = datetime.fromtimestamp(timestamp)
futuresell = bought_doge_price * 1.02
futurebuy = sold_doge_price * .985
#average cost calculations
average_cost = 0
print("timestamp =", dt_object)
print("DOGE is", doge_price)
print("DOGE will be bought at", futurebuy)
print("DOGE will be sold at", futuresell)
print("DOGE Coint count is", dogecoin_count)



while True:
    try:
        doge_price = float(rs.crypto.get_crypto_quote('DOGE', "ask_price"))
        print("DOGE is", doge_price)
        if (doge_price <= (futurebuy) and dogecoin_count < 600):
            
            rs.orders.order_buy_crypto_by_quantity('DOGE', 60, timeInForce='gtc')
            
            dogecoin_count = dogecoin_count + 60
            # average_cost = (average_cost + doge_price) / dogecoin_count
            bought_Doge_price = doge_price
            futuresell = doge_price * 1.02
            futurebuy = futurebuy * .985

            # potential limit orders after purchase, but no way to track coins

            # stoploss = bought_doge_price * .95
          
            # rs.orders.order_buy_crypto_limit('DOGE', 20, futuresell, timeInForce='gtc')
            # rs.orders.order_sell_crypto_limit('DOGE', 20, stoploss, timeInForce='gtc')
            
         
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            dt_object = datetime.fromtimestamp(timestamp)
            print("timestamp =", dt_object)
            print("DOGE Buy Order Complete at", doge_price)
            print("DOGE will be sold at", futuresell)
            print("DOGE next buy order will be at ", futurebuy)
            # print("DOGE average cost is ", average_cost)
            # print("DOGE stoploss will be triggered at", stoploss)
            print("DOGE count is", dogecoin_count)
            
            time.sleep(5)

        elif (doge_price >= futuresell and dogecoin_count > -600):

            rs.orders.order_sell_crypto_by_quantity('DOGE', 60, timeInForce='gtc')
            
            dogecoin_count = dogecoin_count - 60
            # average_cost = (average_cost - doge_price) / abs(dogecoin_count))
            sold_doge_price = doge_price
            futurebuy = sold_doge_price * .985
            futuresell = futuresell * 1.02
            
    
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            dt_object = datetime.fromtimestamp(timestamp)
            print("timestamp =", dt_object)
            print("DOGE Sell Order Complete at", sold_doge_price)
            print("DOGE next sell order will be at ", futuresell)
            print("DOGE will be bought at", futurebuy)
            print("DOGE count is", dogecoin_count)
            time.sleep(5)

        elif (doge_price >= futuresell and dogecoin_count < -600):
            futurebuy = sold_doge_price * .985
            futuresell = futuresell * 1.02
            print("no coins to sell!")
            print("DOGE next buy order will be at ", futurebuy)

        elif (doge_price <= (futurebuy) and dogecoin_count > 600):
            futurebuy = sold_doge_price * .985
            futuresell = futuresell * 1.02
            print("too many coins!")
            print("DOGE next sell order will be at ", futuresell)
                  
        else:  
            print("Still Waiting")
            time.sleep(5)
            
    except Exception as e:
        print("Error fetching latest prices:", e)
        time.sleep(15)      

            
            
            

