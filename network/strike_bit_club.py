from clove.network.bitcoin import Bitcoin


class StrikeBitClub(Bitcoin):
    """
    Class with all the necessary  StrikeBitClub (SBC) network information based on
    https://github.com/sbccoin/sbccoin-source/blob/master/src/net.cpp
    (date of access: 02/18/2018)
    """
    name = 'strike_bit_club'
    symbols = ('SBC', )
    seeds = ('sbc01.seednode.online', 'sbc02.seednode.online', )
    port = 21575
    message_start = b'\x55\x6a\x32\x99'
    base58_prefixes = {
        'PUBKEY_ADDR': 13,
        'SCRIPT_ADDR': 85,
        'SECRET_KEY': 141
    }
