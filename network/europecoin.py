from clove.network.bitcoin import Bitcoin


class Europecoin(Bitcoin):
    """
    Class with all the necessary Europecoin network information based on
    https://github.com/LIMXTEC/Europecoin-V3/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'europecoin'
    symbols = ('ERC', )
    seeds = ("85.214.68.75",
             "37.120.190.76",
             "46.105.114.185",
             "144.76.238.2",
             "104.172.24.79",
             "58.153.14.115",
             "104.232.37.138",
             "216.170.126.168",
             "79.132.111.195",
             "189.131.233.149",
             "115.187.185.121",
             "167.114.249.196",
             "86.219.30.13",
             "95.104.192.198")
    port = 8881
    message_start = b'\x45\x55\x52\x4f'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 168
    }


class EuropecoinTestNet(Europecoin):
    """
    Class with all the necessary Europecoin testing network information based on
    https://github.com/LIMXTEC/Europecoin-V3/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-europecoin'
    seeds = ("85.214.68.75")
    port = 8989
    message_start = b'\x45\x55\x52\x4f'
    base58_prefixes = {
        'PUBKEY_ADDR': 33,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 168
    }
