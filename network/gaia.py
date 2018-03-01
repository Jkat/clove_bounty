from clove.network.bitcoin import Bitcoin


class GAIA(Bitcoin):
    """
    Class with all the necessary GAIA (GAIA) network information based on
    https://github.com/gaiaplatform/GaiaPlatform/blob/master/gaiacoind/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'gaia'
    symbols = ('GAIA', )
    seeds = ('37.59.0.211', '37.187.78.114', '192.99.32.187')
    port = 10101
    message_start = b'\x70\x35\x22\x05'
    base58_prefixes = {
        'PUBKEY_ADDR': 38,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 166
    }

# no testnet
