from clove.network.bitcoin import Bitcoin


class Unitus(Bitcoin):
    """
    Class with all the necessary UIS network information based on
    https://github.com/unitusdev/unitus/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'unitus'
    symbols = ('UIS', )
    seeds = (
        'core.easymine.online',
        'use.easymine.online',
        'us.nutty.one',
        'nz.nutty.one',
    )
    port = 50603
    message_start = b'\xc5\xab\xc6\x9d'
    base58_prefixes = {
        'PUBKEY_ADDR': 68,
        'SCRIPT_ADDR': 10,
        'SECRET_KEY': 132
    }


class UnitusTestNet(Unitus):
    """
    Class with all the necessary UIS testing network information based on
    https://github.com/unitusdev/unitus/blob/master/src/chainparams.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-unitus'
    seeds = (
        'testseed1.unitus.online',
        'testseed2.unitus.online',
    )
    port = 60603
    message_start = b'\xc6\xab\xc7\x9d'
    base58_prefixes = {
        'PUBKEY_ADDR': 130,
        'SCRIPT_ADDR': 192,
        'SECRET_KEY': 239
    }
