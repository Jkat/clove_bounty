from clove.network.bitcoin import Bitcoin


class MustangCoin(Bitcoin):
    """
    Class with all the necessary MustangCoin network information based on
    https://github.com/mustangcoin/mst-v3/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'mustangcoin'
    symbols = ('MST', )
    nodes = ("185.122.59.164",
             "185.117.22.239",
             "185.122.58.95",
             "51.254.181.195",
             "45.55.89.248")
    port = 19667
    message_start = b'\xa1\xa0\xa2\xa3'
    base58_prefixes = {
        'PUBKEY_ADDR': 48,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 176
    }


# Has no testnet
