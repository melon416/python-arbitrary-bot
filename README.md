Prerequisites
Python 3+ inferior to 3.12! (for windows users: if python or pip isn't recognized as a command, make sure you have installed python by checking the box "add to PATH")
Installation
Clone the repository
git clone https://github.com/nelso0/barbotine-arbitrage-bot # you can also download the zip file
Go to the repository you just cloned
cd barbotine-arbitrage-bot
Install all the requirements to run the arbitrage system
pip install -r requirements.txt
Set your configuration details in exchange_config.py
Run with:
python run.py
Usage
You can also run it with one line like this:

python run.py <mode> [renew-time-minutes] <balance-usdt-to-use> <pair> <exchanges list separated by commas (no space!)>
<mode> = the mode you wanna use between fake-money and real. See #full-version for real mode.

fake-money will run the bot with the balance-usdt-to-use you put, with a virtual balance, just to test.
real will run the bot with real money.
[renew-time-minutes] = ONLY IF YOU ENABLED RENEWAL SETTING IN THE CONFIG. If you enabled it, you have to put the number of minutes a session should last. After each session, the bot sells all the assets back to rebalance. Note: you can trigger a manual rebalance while in a session by pressing the Enter key.

<balance-usdt-to-use> = how to be clearer?

<pair> = The pair you wanna arbitrage on.

<exchanges list> = the exchanges you want the bot to scan the orderbooks on, among all the CCXT-compatible exchanges. From a 2 exchanges minimum, up to an unlimited number. Don't forget to configure the exchanges in exchange_config.py.

Note: as the bot needs to buy assets before getting started (it's necessary in order to operate without transfer between exchanges), if the pair you have chosen looses in value, you'll end up losing money when rebalancing. To avoid that, I created a delta-neutral feature that places a short order to "hedge" and counterbalance the purchase of coins by the bot. You can enable this feature in exchange_config.py.

Examples:

with renewal disabled (default):

python run.py fake-money 500 EOS/USDT binance,okx,kucoin    # run the bot with 500 USDT and rebalance every 15 minutes, with binance okx and kucoin
with renewal enabled:

python run.py real 15 1000 SOL/USDT binance,poloniex,kucoin   # run the bot with 1000 USDT on binance phemex and bybit on SOL/USDT, and rebalance every 15 minutes.
