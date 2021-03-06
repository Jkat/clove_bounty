from clove.network.bitcoin import Bitcoin


class FCKBanksCoin(Bitcoin):
    """
    Class with all the necessary FCKBanksCoin network information based on
    https://github.com/fckfoundation/fckbankscoin/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'fckbankscoin'
    symbols = ('FCV', )
    seeds = ("seed.fckbanks.org", )
    port = 21779
    message_start = b'\xfc\xd9\xb7\xdd'
    base58_prefixes = {
        'PUBKEY_ADDR': 36,
        'SCRIPT_ADDR': 5,
        'SECRET_KEY': 164
    }

# no testnet
