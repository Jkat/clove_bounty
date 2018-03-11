from clove.network.bitcoin import Bitcoin


class Cabbage(Bitcoin):
    """
    Class with all the necessary Cabbage network information based on
    https://github.com/CabbageUnit/Cabbage/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cabbage'
    symbols = ('CAB', )
    seeds = ("seed1.cryptolife.net",
             "seed2.cryptolife.net",
             "seed3.cryptolife.net",
             "electrum1.cryptolife.net",
             "wallet.cryptolife.net",
             "explore.cryptolife.net")
    port = 40718
    message_start = b'\xb4\xf3\xe4\xd5'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 20,
        'SECRET_KEY': 156
    }

# Has no testnet
