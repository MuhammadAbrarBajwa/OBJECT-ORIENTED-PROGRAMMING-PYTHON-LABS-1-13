

#Exercise 1
class TV:
    def __init__(self):
        self.channel = 0
        self.volumeLevel = 0
        self.on = False

    def turnOn(self):
        self.on = True
    
    def turnOff(self):
        self.on = False
    
    def getChannel(self):
        return self.channel
    
    def setChannel(self, channel):
        if self.on and 0 <= channel <= 120:
            self.channel = channel
        
    def getVolumeLevel(self):
        return self.volumeLevel
    
    def setVolume(self, volumeLevel):
        if self.on and 0 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel  
        
    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel += 1
    
    def channelDown(self):
        if self.on and self.channel > 0:
            self.channel -= 1
        
    def volumeUp(self):
        if self.on and self.volumeLevel < 7:
            self.volumeLevel += 1

    def volumeDown(self):
        if self.on and self.volumeLevel > 0:
            self.volumeLevel -= 1


#Exercise 2
print("============= Tv1 ===========\n")
tv1 = TV()
tv1.turnOn()
tv1.setChannel(30)
tv1.setVolume(3)
print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolumeLevel())

print("============= Tv2 ===========\n")
tv2 = TV()
tv2.turnOn()
tv2.channelUp()
tv2.channelUp()
tv2.volumeUp()
print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolumeLevel())
