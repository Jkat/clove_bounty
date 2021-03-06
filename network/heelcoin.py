from clove.network.bitcoin import Bitcoin


class HeelCoin(Bitcoin):
    """
    Class with all the necessary HeelCoin network information based on
    https://github.com/HeelCoin/heelcoin/blob/master/src/chainparams.cpp
    (date of access: 02/15/2018)
    """
    name = 'heelcoin'
    symbols = ('HEEL', )
    nodes = ("52.10.89.163", )
    port = 22077
    message_start = b'\x2c\xc7\xbc\xba'
    base58_prefixes = {
        'PUBKEY_ADDR': 40,
        'SCRIPT_ADDR': 72,
        'SECRET_KEY': 142
    }

# no testnet
