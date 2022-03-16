import Gate_Api as GA
instance = Gate_Api(   host = "https://api.gateio.ws/api/v4",
    key = "998f4e819ce26285e08937a347aa6968",
    secret = "58d77d473538e5090664d481366a144e422b2ad20405b1aceeee6e7ea0957c25" )
# input your account key and secret

# get price information
## create an non-price-trigger order
order = instance.create_order(currency_pair='ADA_USDT',Type= 'Spot', order_type='limit',amount="2.0",side='buy',price='0.1174')
## get order information
get = instance.get_order(order_id = '129238428627', currency_pair= 'ADA_USDT',Type='Spot')
### create spot-trigger order
put = {'price': '0.65', 'limit': 'limit', 'side': 'buy', 'amount': '2.0', 'account': 'normal', 'time_in_force': 'gtc'}
currency_pair = 'ADA_USDT'
trigger = instance.create_trigger_order(type = 'Spot',trigger=trigger, put=put,currency_pair=currency_pair)
### get spot_tigger order
get_spot_trigger = instance.get_trigger_order(type = 'Spot',id='')
### check current account information
instance.account_value('1h',account_info = 'a')
##
instance.list_all_open_orders(type = 'spot',page = 1,limit = 10)
