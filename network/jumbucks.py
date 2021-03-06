from clove.network.bitcoin import Bitcoin


class JumBucks(Bitcoin):
    """
    Class with all the necessary JumBucks network information based on
    https://github.com/jyap808/jumbucks/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'jumbucks'
    symbols = ('JBS', )
    seeds = ("seed1.getjumbucks.com",
             "dnsseed1.getjumbucks.com")
    port = 51717
    message_start = b'\xfc\xf4\xf1\xb6'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 105,
        'SECRET_KEY': 171
    }
