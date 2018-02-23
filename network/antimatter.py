from clove.network.bitcoin import Bitcoin


class Antimatter(Bitcoin):
    """
    Class with all the necessary Antimatter network information based on
    https://github.com/staycrypto/antimatter/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'antimatter'
    symbols = ('ANTX', )
    seeds = ("seed.baconmakesyourfeaturessizzle.com")
    port = 9334
	
   
class AntimatterTestNet(Antimatter):
    """
    Class with all the necessary Antimatter testing network information based on
    https://github.com/staycrypto/antimatter/blob/master/src/net.cpp
    (date of access: 02/19/2018)
    """
    name = 'test-antimatter'
    seeds = ("testnet-seed.baconmakesyourfeaturessizzle.com")
    port = 19334               