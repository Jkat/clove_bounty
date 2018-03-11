from clove.network.bitcoin import Bitcoin


class InfChain(Bitcoin):
    """
    Class with all the necessary InfChain (INF) network information based on
    https://github.com/xunliankeji/infchain/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'infchain'
    symbols = ('INF', )
    nodes = ('119.23.214.249',
             '47.92.128.30',
             '116.62.150.78',
             '47.52.108.183',
             '47.74.1.150',
             '47.88.153.130',
             '47.91.43.180',
             '47.89.242.204',
             '47.91.93.115')
    port = 17725
    message_start = b'\x6d\x3c\x61\x53'
    base58_prefixes = {
        'PUBKEY_ADDR': 75,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 153
    }

# no testnet
