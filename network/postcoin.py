from clove.network.bitcoin import Bitcoin


class PostCoin(Bitcoin):
    """
    Class with all the necessary PostCoin network information based on
    https://github.com/postcoindevelopers/postcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'postcoin'
    symbols = ('POST', )
    seeds = ("5.45.66.18",
             "node.postcoin.pw",
             "node1.postcoin.pw",
             "node2.postcoin.pw",
             "node3.postcoin.pw",
             "node4.postcoin.pw")
    port = 9130
    message_start = b'\x35\xc3\xd6\xa2'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 183
    }


# Has no testnet
