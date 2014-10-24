HuoBi_btc_analyse
=================


required: Anaconda Python (The fastest way)
or H5Py + pandas + numpy + sciki_learn ...

basic usage:
1. clone huobi btc trade history

git clone https://github.com/huobi/btc-trade-result-history btc_history

2.python load_data.py btc_history btc_history.h5

3.python back_test.py btc_history.h5
