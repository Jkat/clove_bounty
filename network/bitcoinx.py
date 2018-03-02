from clove.network.bitcoin import Bitcoin


class BitcoinX(Bitcoin):
    """
    Class with all the necessary BitcoinX (BCX) network information based on
    https://github.com/bitcoinx-project/bitcoinx/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'bitcoinx'
    symbols = ('BCX', )
    seeds = ('seed.bcx.org', 'seed.bcx.info', )
    port = 9003
    message_start = b'\x11\x05\xbc\xF9'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 63,
        'SECRET_KEY': 128
    }


class BitcoinXTestNet(BitcoinX):
    """
    Class with all the necessary BitcoinX (BCX) testing network information based on
    https://github.com/bitcoinx-project/bitcoinx/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'test-bitcoinx'
    seeds = ('testnet-seed.bcx.org', 'testnet-seed.bcx.info', )
    port = 19003
    message_start = b'\x19\x9F\xF3\x18'
    base58_prefixes = {
        'PUBKEY_ADDR': 65,
        'SCRIPT_ADDR': 196,
        'SECRET_KEY': 239
    }
