
from clove.network.bitcoin import Bitcoin


class SocialSend(Bitcoin):
    """
    Class with all the necessary SEND network information based on
    https://github.com/SocialSend/SocialSend/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'socialsend'
    symbols = ('SEND', )
    seeds = (
        'seeds.send.goldlineit.org',
    )
    port = 50050
    message_start = b'\x81\xc4\xed\xe9'
    base58_prefixes = {
        'PUBKEY_ADDR': 63,
        'SCRIPT_ADDR': 13,
        'SECRET_KEY': 212
    }
