from clove.network.bitcoin import Bitcoin


class Kurrent(Bitcoin):
    """
    Class with all the necessary Kurrent network information based on
    https://github.com/kurrentproject/kurrent/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'kurrent'
    symbols = ('KURT', )
    seeds = ('212.24.107.99')
    port = 18080
    message_start = b'\xdb\xc3\xfa\xfc'
    base58_prefixes = {
        'PUBKEY_ADDR': 45,
        'SCRIPT_ADDR': 17,
        'SECRET_KEY': 173
    }


# Has no testnet
