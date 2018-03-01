from clove.network.bitcoin import Bitcoin


class YoviCoin(Bitcoin):
    """
    Class with all the necessary YoviCoin network information based on
    https://github.com/dmdcoin/diamond/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'yovicoin'
    symbols = ('YOVI', )
    nodes = ("37.1.193.77",
             "62.162.181.2",
             "192.52.166.80",
             "70.92.184.203",
             "109.87.255.75",
             "155.99.160.206",
             "2.179.149.174")
    port = 26372
    message_start = b'\xe4\xe8\xbd\xfd'
    base58_prefixes = {
        'PUBKEY_ADDR': 90,
        'SCRIPT_ADDR': 8,
        'SECRET_KEY': 218
    }

# no testnet
