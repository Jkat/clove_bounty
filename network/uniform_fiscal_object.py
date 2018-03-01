from clove.network.bitcoin import Bitcoin


class UniformFiscalObject(Bitcoin):
    """
    Class with all the necessary Uniform Fiscal Object (UFO) network information based on
    https://github.com/UFOCoins/ufo/blob/master-0.12/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'uniformfiscalobject'
    symbols = ('UFO', )
    seeds = ('seed1.ufocoin.net', 'seed1.ufocoin.net', 'seed1.ufocoin.net', 'seed1.ufocoin.net',
             'dnsseed.lowecraft.it', 'dnsseed.ufocoinnode.com')
    port = 9887
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 27,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 155
    }


class UniformFiscalObjectTestNet(UniformFiscalObject):
    """
    Class with all the necessary Uniform Fiscal Object (UFO) testing network information based on
    https://github.com/UFOCoins/ufo/blob/master-0.12/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-uniformfiscalobject'
    seeds = ('testnet-seed.ufocoin.net', )
    port = 19887
    message_start = b'\xfb\xc0\xb8\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 111,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
