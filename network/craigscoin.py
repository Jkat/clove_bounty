from clove.network.bitcoin import Bitcoin


class CraigsCoin(Bitcoin):
    """
    Class with all the necessary CraigsCoin network information based on
    https://github.com/CraigsCoin/CraigsCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'craigscoin'
    symbols = ('CRAIG', )
    nodes = ("54.88.218.165", )
    port = 30365
    message_start = b'\x88\xf0\xb1\xe9'
    base58_prefixes = {
        'PUBKEY_ADDR': 28,
        'SCRIPT_ADDR': 29,
        'SECRET_KEY': 156
    }


class CraigsCoinTestNet(CraigsCoin):
    """
    Class with all the necessary CraigsCoin testing network information based on
    https://github.com/CraigsCoin/CraigsCoin/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-craigscoin'
    nodes = ("54.85.156.177", )
    port = 30367
    message_start = b'\x99\x88\x77\xff'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
