from clove.network.bitcoin import Bitcoin


class RootCoin(Bitcoin):
    """
    Class with all the necessary RootCoin network information based on
    https://github.com/bitsta/rootcoin/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'rootcoin'
    symbols = ('ROOT', )
    nodes = ("94.156.237.70",
             "195.34.100.2",
             "212.91.189.164",
             "198.23.160.13",
             "192.99.223.96")
    port = 28388
    message_start = b'\xc0\xc0\xc0\xc0'
    base58_prefixes = {
        'PUBKEY_ADDR': 60,
        'SCRIPT_ADDR': 75,
        'SECRET_KEY': 188
    }

# no testnet
