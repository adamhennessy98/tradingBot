from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce


API_KEY = "PKO0GWQF0D3P7YHGH9OV"
API_SECRET_KEY = "alfWYzOL3MlOncXhaG37AEHepm7rUr151KaTHrIA"

trading_client = TradingClient(API_KEY, API_SECRET_KEY, paper=True)

account = trading_client.get_account()
