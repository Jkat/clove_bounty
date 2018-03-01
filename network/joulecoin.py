
from clove.network.bitcoin import Bitcoin


class Joulecoin(Bitcoin):
    """
    Class with all the necessary XJO network information based on
    http://www.github.com/joulecoin/joulecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'joulecoin'
    symbols = ('XJO', )
    seeds = ('seed1.jouleco.in', 'seed2.jouleco.in', 'seed3.jouleco.in',
             'seed4.jouleco.in', 'joulecoin1.chickenkiller.com', 'joulecoin2.crabdance.com')
    port = 26789
    message_start = b'\xa5\xc0\x79\x55'
    base58_prefixes = {
        'PUBKEY_ADDR': 43,
        'SCRIPT_ADDR': 11,
        'SECRET_KEY': 143
    }


class JoulecoinTestNet(Joulecoin):
    """
    Class with all the necessary XJO testing network information based on
    http://www.github.com/joulecoin/joulecoin/blob/master/src/chainparams.cpp
    (date of access: 02/11/2018)
    """
    name = 'test-joulecoin'
    seeds = ('testseed1.jouleco.in',)
    port = 26783
    message_start = b'\x0a\xc0\x73\x12'
    base58_prefixes = {
        'PUBKEY_ADDR': 83,
        'SCRIPT_ADDR': 13,
        'SECRET_KEY': 212
    }
