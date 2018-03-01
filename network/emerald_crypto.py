
from clove.network.bitcoin import Bitcoin


class EmeraldCrypto(Bitcoin):
    """
    Class with all the necessary EMD network information based on
    http://www.github.com/crypto-currency/Emerald/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'emerald-crypto'
    symbols = ('EMD', )
    seeds = ('emeraldcrypto.co',)
    port = 12127
    message_start = b'\xfb\xc0\xb6\xdb'
    base58_prefixes = {
        'PUBKEY_ADDR': 34,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 162
    }


class EmeraldCryptoTestNet(EmeraldCrypto):
    """
    Class with all the necessary EMD testing network information based on
    http://www.github.com/crypto-currency/Emerald/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-emerald-crypto'
    seeds = ('testnet.emeraldcrypto.co',)
    port = 22127
