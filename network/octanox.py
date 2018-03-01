from clove.network.bitcoin import Bitcoin


class Octanox(Bitcoin):
    """
    Class with all the necessary Octanox network information based on
    https://github.com/dfgv12/Octanox-OTX/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'octanox'
    symbols = ('OTX', )
    seeds = ("185.69.54.33")
    port = 36212
    message_start = b'\xa2\xc5\xf2\xc1'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 12,
        'SECRET_KEY': 203
    }

# no testnet
