from clove.network.bitcoin import Bitcoin


class FootyCash(Bitcoin):
    """
    Class with all the necessary Footy Cash (XFT) network information based on
    https://github.com/FootyCash/FootyCashV2/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'footycash'
    symbols = ('XFT', )
    seeds = ('seedv2.footycash.com', 'xftseed1.dblocks.io', 'xftseed2.dblocks.io',
             'ns2.footycash.com', 'ns1.footycash.com')
    port = 17017
    message_start = b'\x17\x24\x08\x32'
    base58_prefixes = {
        'PUBKEY_ADDR': 35,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
