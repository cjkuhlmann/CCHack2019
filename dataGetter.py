
lat = "50.94"
lon = "-1.40"

import urllib
import urllib.request
import json
import time
import operator
import FireSimulator
import random

"""request = urllib.request.urlopen("https://api.breezometer.com/weather/v1/current-conditions?lat="+lat+"&lon="+lon+"&key=5f3f478873a44987b2918d356348ed6c")
response = request.read()
json = json.loads(response)
data = json["data"]

print(json["data"]["precipitation"]["total_precipitation"]["value"],json["data"]["precipitation"]["total_precipitation"]["units"])

print(str(json["data"]["wind"]["speed"]["value"]),json["data"]["wind"]["speed"]["units"])
print(json["data"]["wind"]["direction"])
"""     
        
class TileMap():
    def __init__(self, anchor, step, length, width):
        self.tilemap = []
        self.anchor = anchor
        self.step = step
        self.length = length
        self.width = width
        self.fireSimulator = FireSimulator.FireSimulator()

    def setSimulatorTiles(self):
        self.fireSimulator.set_values(self.tilemap)

    def simulate(self):
        output = self.fireSimulator.process_fires()
        for item in output:
            for i in range(len(self.tilemap)):
                for j in range(len(self.tilemap[0])):
                    if self.tilemap[i][j].ID[0] == item[0][0] and self.tilemap[i][j].ID[1] == item[0][1]:
                        #print("Item",i,j,item[1])
                        self.tilemap[i][j].fireSpreadRisk = item[1]
                        if random.randint(0,10) == 0 and self.tilemap[i][j].ID != [0,0]:
                            self.tilemap[i][j].fireRisk = item[1]*100

                        
                        """if item[1] >= 0.4:
                            self.tilemap[i][j].hasFire = True
                            self.tilemap[i][j].fireIntensity = 3"""
        
        
        
    def generateTiles(self):        
        for i in range(self.width):
            thisRow = []
            for j in range(self.length):
                thisRow.append(Tile())
                time.sleep(0.05)
                
            self.tilemap.append(thisRow)

    def setFakeData(self, fakeTiles):
        for i in range(self.length):
            nullArray = []
            for j in range(self.width):
                nullArray.append(None)
            self.tilemap.append(nullArray)
            
        for tile in fakeTiles:
            tile.LON = "%.4f" % (-1.4 + tile.ID[1] * 0.001) #yyyyyy
            tile.LAT = "%.4f" % (50.940 + tile.ID[0] * 0.001)####xxxxxxxx
            self.tilemap[tile.ID[0]][tile.ID[1]] = tile
            
                
    def updateTiles(self):
        for i in range(self.width):
            for j in range(self.length):
                self.tilemap[i][j].updateSensorData()
                self.tilemap[i][j].updateAPIData()
                time.sleep(0.2)

    def getFireAlertRanking(self):
        onFireRanking = []
        notOnFireRanking = []
        for i in range(self.length):
            for j in range(self.width):
                if self.tilemap[i][j].getHasFire():
                    onFireRanking.append(self.tilemap[i][j])
                else:
                    notOnFireRanking.append(self.tilemap[i][j])
        onFireRanking.sort(key=operator.attrgetter('fireIntensity'), reverse=True)
        notOnFireRanking.sort(key=operator.attrgetter('fireRisk'), reverse=True)
        fireAlertRanking = []
        for tile in onFireRanking:
            fireAlertRanking.append(tile)
        for tile in notOnFireRanking:
            fireAlertRanking.append(tile)
        return fireAlertRanking
        
            
        

class Tile():
    def __init__(self, ID=[0,0],LON=0,LAT=0,HEIGHT=0,windSpeed=0,\
                 windDirection=0,humidity=0,temperature=0,smoke=0,\
                 precipitation=0,\
                 fireRisk=0,hasFire=False,fireIntensity=0):
        self.ID = ID
        self.LON = LON
        self.LAT = LAT
        self.HEIGHT = HEIGHT
        self.windSpeed = windSpeed
        self.windDirection = windDirection
        self.precipitation = precipitation

        self.humidityTrend = 0
        self.humidity = humidity
        self.temperatureTrend = 0
        self.temperature = temperature
        self.smokeTrend = 0
        self.smoke = smoke
        self.pressure = 0
        self.firePrediction = 0
        self.dryness = 0
        self.fireSpreadRisk = 0

        self.smokeSet =[]
        self.tempSet = []
        self.humidSet = []
        

        
        
        #self.setConst()
        #self.setSensorData()
        #self.setAPIData(self.LON, self.LAT)
        
        

        self.fireRisk = fireRisk
        self.hasFire = hasFire
        self.fireIntensity = fireIntensity
        self.status = self.setStatus()

    def lin_reg(self,data_set):
        if len(data_set) > 10:
            x = 0
            Sxy = 0
            Sx = 0
            Sx2 = 0
            Sy = 0
            Sy2 = 0
            sample_size = len(data_set)
            for y in data_set:
                x += 1
                Sxy += x * y
                Sx += x
                Sx2 += x**2
                Sy += y
                Sy2 += y**2

            lin_reg = ((sample_size*Sxy)-(Sx*Sy))/((sample_size*Sx2)-(Sx)**2)
            return lin_reg
        else:
            return 0

    def detect_fire(self):
        self.setHumidityTrend()
        self.setTemperatureTrend()
        self.setSmokeTrend()
        overall_trend = 0.02*(self.smokeTrend)+self.temperatureTrend*50-self.humidityTrend
        print("Overall trend:",overall_trend)
        print("Humidity trend:", self.humidityTrend)
        print("Temperature trend:", self.temperatureTrend)
        print("Smoke trend:", self.smokeTrend)
        if overall_trend >= 1 or self.temperature >= 60:
            self.hasFire = True
            self.fireIntensity = 3
            #print("on fire!")

    def getFireRisk(self):
        return self.fireRisk

    def getFireSpreadRisk(self):
        return self.fireSpreadRisk

    def getFireIntensity(self):
        return self.fireIntensity

    def getHasFire(self):
        return self.hasFire

    def setPredictedFire(self,fire):
        self.firePrediction = fire
        

    def setHumidityTrend(self):
        self.humidityTrend = self.lin_reg(self.humidSet)
        
    def setHumidity(self,humidity):
        self.humidSet.append(humidity)
        self.humidity = humidity

    def setTemperatureTrend(self):
        self.temperatureTrend = self.lin_reg(self.tempSet)

    def setTemperature(self,temp):
        self.tempSet.append(temp)
        self.temperature = temp

    def setSmokeTrend(self):
        self.smokeTrend = self.lin_reg(self.smokeSet)

    def setSmoke(self,smoke):
        self.smokeSet.append(smoke)
        if len(self.smokeSet) >= 12:
            self.smokeSet.remove(self.smokeSet[0])
        self.smoke = smoke

    def setPressure(self,pres):
        self.pressure = pres

    def setStatus(self):
        if self.hasFire:
            status = "Intensity: " + str(self.fireIntensity)
        else:
            status = "Risk: " + str(self.fireRisk) + "%"
        return status

    #set id, lot, lat, HEIGHT
    def setConst():
        pass

    def updateSensorData(self):
        pass

    def updateAPIData(self):
        import urllib
        import urllib.request
        import json
        request = urllib.request.urlopen("https://api.breezometer.com/weather/v1/current-conditions?lat="+str(self.LAT)+"&lon="+str(self.LON)+"&key=e47dac88341d47d6a7e43239baab61df")
        response = request.read()
        json = json.loads(response)
        data = json["data"]
        #windspeed
        self.windspeed = json["data"]["wind"]["speed"]["value"]
        #winddirection
        self.windDirection = json["data"]["wind"]["direction"]
        #precipitation
        self.precipitation = json["data"]["precipitation"]["total_precipitation"]["value"]
        
    def calculateFirstRisk(self):
        pass

    def checkForFire(self):
        pass








