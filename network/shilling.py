
from clove.network.bitcoin import Bitcoin


class Shilling(Bitcoin):
    """
    Class with all the necessary SH network information based on
    http://www.github.com/yavwa/Shilling/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'shilling'
    symbols = ('SH', )
    seeds = ('wallet.cryptolife.net', 'explore.cryptolife.net',
             'seed1.cryptolife.net', 'seed2.cryptolife.net')
    port = 34621


class ShillingTestNet(Shilling):
    """
    Class with all the necessary SH testing network information based on
    http://www.github.com/yavwa/Shilling/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-shilling'
    seeds = ()
    port = 33813
