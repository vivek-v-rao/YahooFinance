month_codes = "FGHJKMNQUVXZ"

dict_bloom_yahoo = \
    {"CO":None, # missing from Yahoo
     "LA":None,
     "LL":None,
     "LN":None,
     "LX":None,
     "BO":"ZL", # different symbols on Yahoo
     "C":"ZC",
     "KW":"KE",
     "LC":"LE",
     "LH":"HE",
     "S":"ZS",
     "SM":"ZM",
     "W":"ZW",
     "XB":"RB",
     "CL":"CL", # same symbols on Yahoo and Bloomberg
     "CT":"CT",
     "GC":"GC",
     "HG":"HG",
     "HO":"HO",
     "KC":"KC",
     "NG":"NG",
     "PL":"PL",
     "SB":"SB"}

dict_month_codes = \
    {"ES":"HMUZ",      # S&P 500
     "YM":"HMUZ",      # Dow Jones Industrial Average
     "NQ":"HMUZ",      # Nasdaq 100
     "RTY":"HMUZ",     # Russell 2000
     "ZB":"HMUZ",      # U.S. Treasury Bond
     "ZN":"HMUZ",      # 10-Year Treasury Note
     "ZF":"HMUZ",      # 5-Year Treasury Note
     "ZT":"HMUZ",      # 2-Year Treasury Note
     "CL":month_codes, # Crude Oil
     "GC":"FGJMQVZ",   # Gold
     "SI":"FGHKNUZ",   # Silver
     "PL":"FGJNV",     # Platinum
     "PA":"FGHNUZ",    # Palladium
     "HG":month_codes, # Copper
     "HO":month_codes, # Heating Oil
     "NG":month_codes, # Natural Gas
     "RB":month_codes, # RBOB Gasoline
     "ZS":"FHKNQUVZ",  # Soybeans
     "ZL":"FHKNQUVZ",  # Soybean Oil
     "ZM":"FHKNQUVZ",  # Soybean Meal
     "ZC":"HKNUZ",     # Corn
     "ZW":"HKNUZ",     # Chicago SRW Wheat
     "KE":"HKNUZ",     # KC HRW Wheat
     "LE":"GJMQVZ",    # Live Cattle
     "HE":"GJKMNQVZ",  # Lean Hogs
     "CC":"HKNUZ",     # Cocoa
     "KC":"HKNUZ",     # Coffee
     "CT":"HKNVZ",     # Cotton
     "ZR":"FHKNUX",    # Rough Rice
     "ZO":"HKNUZ",     # Oats
     "SB":"HKNV"}      # Sugar
    
dict_exchange_codes = {"ES":"CME", "YM":"CME", "NQ":"CME", "RTY":"CME",
    "ZB":"CBT", "ZN":"CBT", "ZF":"CBT", "ZT":"CBT", "CL":"NYM", "GC":"CMX",
    "SI":"CMX", "PL":"NYM", "PA":"NYM", "HG":"CMX", "HO":"NYM", "NG":"NYM",
    "RB":"NYM", "ZS":"CBT", "ZL":"CBT", "ZM":"CBT", "ZC":"CBT", "ZW":"CBT",
    "KE":"CBT", "LE":"CME", "HE":"CME", "CC":"NYB", "KC":"NYB", "CT":"NYB",
    "ZR":"CBT", "ZO":"CBT", "SB":"NYB"}

def sym_dict(symbols, len_commodity_code=2, len_month_code=3):
    """ return a dictionary of futures symbols where the keys are commodity codes
    and the values are lists of month codes """
    dd = {}
    for symbol in symbols:
        prefix = symbol[:len_commodity_code]
        month_code = symbol.split(".")[0][-len_month_code:]
        if prefix in dd:
            dd[prefix] = dd[prefix] + [month_code]
        else:
            dd[prefix] = [month_code]
    return dd
    
def bloomberg_code_from_yahoo(symbol):
    """
    Convert a Yahoo finance symbol to its corresponding Bloomberg symbol.

    Args:
        symbol (str): Yahoo finance symbol.

    Returns:
        str: Bloomberg symbol if a mapping exists; otherwise, the original symbol.
    """
    dd = dict(zip(dict_bloom_yahoo.values(), dict_bloom_yahoo.keys()))
    return dd[symbol] if symbol in dd else symbol

def print_symbols_by_commmodity(symbols, yahoo_to_bloom=True, title=None):
    """
    Print futures symbols grouped by commodity, optionally converting Yahoo
    symbols to Bloomberg.

    Args:
        symbols (list): List of futures symbols.
        yahoo_to_bloom (bool): If True, convert Yahoo symbols to Bloomberg
            symbols (default: True).
    """
    if title:
        print(title)
    dd = sym_dict(symbols)
    for key, value in dd.items():
        code = bloomberg_code_from_yahoo(key) if yahoo_to_bloom else key
        print("%2s"%code, "%3d"%len(value), " ".join(x for x in value))