###

def strcounter(s: str):
    for symbol in set(s):
        counter = 0
        for sub_symbol in s:
            if symbol == sub_symbol:
                counter += 1
        print(symbol, counter)

strcounter("облачко")

###

def strcounter(s: str):
    symbols_dict = {}
    for symbol in s:
        if symbol in symbols_dict:
            symbols_dict[symbol] +=1
        else:
            symbols_dict[symbol] =1
    print(symbols_dict)

strcounter("ппппппппппппппппппппппёёёёёёёёёёёёёссссссссссссссссссссссс")