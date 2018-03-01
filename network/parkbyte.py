from clove.network.bitcoin import Bitcoin


class ParkByte(Bitcoin):
    """
    Class with all the necessary ParkByte (PKB) network information based on
    https://github.com/parkbyte/ParkByte/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'parkbyte'
    symbols = ('PKB', )
    seeds = ('198.50.147.234', '151.80.232.34', '37.187.139.3')
    port = 58060
    message_start = b'\xe4\xc2\xd8\xe6'
    base58_prefixes = {
        'PUBKEY_ADDR': 55,
        'SCRIPT_ADDR': 28,
        'SECRET_KEY': 183
    }

# no testnet
