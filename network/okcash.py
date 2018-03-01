
from clove.network.bitcoin import Bitcoin


class OKCash(Bitcoin):
    """
    Class with all the necessary OK network information based on
    http://www.github.com/okcashpro/okcash/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'okcash'
    symbols = ('OK', )
    seeds = ('seed1.okcash.co', 'seed2.okcash.co', 'seed3.okcash.co',
             'seed4.okcash.co', 'seed5.okcash.co', 'seed6.okcash.co')
    port = 6970
    message_start = b'\x69\xf0\x0f\x69'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 183
    }


class OKCashTestNet(OKCash):
    """
    Class with all the necessary OK testing network information based on
    http://www.github.com/okcashpro/okcash/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-okcash'
    seeds = ()
    port = 7980
    message_start = b'\x00\x09\x7a\x0f'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 73,
        'SECRET_KEY': 196
    }
