
from clove.network.bitcoin import Bitcoin


class TodayCoin(Bitcoin):
    """
    Class with all the necessary TODAY network information based on
    http://www.github.com/todayimage/todayimage-source/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'todaycoin'
    symbols = ('TODAY', )
    seeds = ('node.104.238.185.61', )
    port = 7869
    message_start = b'\xba\xad\x07\x9c'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 193
    }
