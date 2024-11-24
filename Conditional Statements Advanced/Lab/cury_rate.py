from yahoo_fin import stock_info as si

exchange_rate = si.get_live_price('EURBGN=X')

amount = float(input('please input a amount in EUR'))

d = exchange_rate * amount

print(d)