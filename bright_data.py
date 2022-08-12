import pandas as pd

def price_t(s):
    if s == "NaN":
        return pd.NA
    try:
        return float(s.replace("$", ""))
    except:
        return pd.NA

def strip_id(url):
    s = url[::-1]
    ind = s.find('/')
    if ind == -1: return None
    return s[:ind][::-1]


def load_data(fn):
    df = pd.read_json(fn)
    df['event_url'] = df['input'].map(lambda x: x['url'])
    df['event_id']  = df['event_url'].map(lambda x: strip_id(x))
    df['price_s']   = df['price']
    df['price']     = df['price_s'].map(lambda x: price_t(x))
    return df