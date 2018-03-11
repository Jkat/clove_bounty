from clove.network.bitcoin import Bitcoin


class NewZealandCoin(Bitcoin):
    """
    Class with all the necessary NewZealandCoin network information based on
    https://github.com/oliveradnaya/newzealandcoin-source/blob/master/src/net.cpp
    (date of access: 02/17/2018)
    """
    name = 'newzealandcoin'
    symbols = ('NZC', )
    seeds = ("node.walletbuilders.com", )
    port = 7769
    message_start = b'\x69\x2a\xb5\x47'
    base58_prefixes = {
        'PUBKEY_ADDR': 53,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 181
    }

# no testnet
