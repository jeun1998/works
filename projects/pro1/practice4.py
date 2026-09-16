class ElecrProduct:
    volume = 0
    def volumeControl(self,volume):
        print("volume")

class ElecTv(ElecrProduct):
    def volumecontrol(self, volume):
        self.volume += volume
        print("텔레비전 음량:", self.volume)

class ElecRadio(ElecrProduct):
    def radiochannel(self, channel):
        print("라디오 채널 번호:", channel)

    def volumecontrol(self, volume):
        self.volume += volume
        print("라디오 음량", self.volume)

tv = ElecTv()
tv.volumecontrol(7)

radio = ElecRadio()
radio.volumecontrol(6)
radio.radiochannel(93.9)

product = tv
product.volumecontrol(5)
product = radio
product.radiochannel(91.9)

if __name__ == "__main__":
    electro_product = ElecrProduct()
    electro_product.volumeControl(1)

    print()
    tv = ElecTv()
    tv.volumecontrol(7)

    radio = ElecRadio()
    radio.volumecontrol(6)
    radio.radiochannel(93.9)

    product = tv
    product.volumecontrol(5)
    product = radio
    product.radiochannel(91.9)

    group = [ElecTv(), ElecRadio()]
    for g in group:
        g.volumeControl(4)
        print()