import pygame
import threading
import time
import dataGetter
import socket
import random



def calculateColour(fireRisk):
    if fireRisk >= 90:
        return (195, 0, 0) #dark red
    elif fireRisk >= 80:
        return (255, 0,0) #red
    elif fireRisk >= 70:
        return (255, 90, 0) #light red
    elif fireRisk >= 60:
        return (255, 154, 0) #orange
    elif fireRisk >= 40:
        return (255, 206, 0) #yellow
    elif fireRisk >= 20:
        return (240, 255, 0) #light yellow
    elif fireRisk >= 0:
        return (200, 200, 200) #white

def calculateFire(fireIntensity):
    if fireIntensity == 1:
        return pygame.image.load("smallFlame1.png")
    elif fireIntensity == 2:
        return pygame.image.load("medFlame1.png")
    elif fireIntensity == 3:
        return pygame.image.load("largeFlame1.png")
######################

anchor = dataGetter.Tile(ID=[0,0],LAT=50.940,LON=-1.4,HEIGHT=1,windSpeed=1,\
                 windDirection=1,humidity=1,temperature=1,smoke=1,\
                 precipitation=1,\
                 fireRisk=10,hasFire=False,fireIntensity=0)
tile2 = dataGetter.Tile(ID=[0,1],LAT=50.939,LON=-1.4,HEIGHT=2,windSpeed=2,\
                 windDirection=2,humidity=2,temperature=2,smoke=2,\
                 precipitation=2,\
                 fireRisk=20,hasFire=False,fireIntensity=0)
tile3 = dataGetter.Tile(ID=[0,2],LAT=50.938,LON=-1.4,HEIGHT=3,windSpeed=3,\
                 windDirection=3,humidity=3,temperature=3,smoke=3,\
                 precipitation=3,\
                 fireRisk=30,hasFire=True,fireIntensity=1)
tile4 = dataGetter.Tile(ID=[1,0],LAT=50.940,LON=-1.399,HEIGHT=4,windSpeed=4,\
                 windDirection=1,humidity=4,temperature=4,smoke=4,\
                 precipitation=4,\
                 fireRisk=40,hasFire=False,fireIntensity=0)
tile5 = dataGetter.Tile(ID=[1,1],LAT=50.939,LON=-1.399,HEIGHT=5,windSpeed=5,\
                 windDirection=5,humidity=5,temperature=5,smoke=5,\
                 precipitation=5,\
                 fireRisk=50,hasFire=False,fireIntensity=0)
tile6 = dataGetter.Tile(ID=[1,2],LAT=50.938,LON=-1.399,HEIGHT=6,windSpeed=6,\
                 windDirection=6,humidity=6,temperature=6,smoke=6,\
                 precipitation=6,\
                 fireRisk=60,hasFire=False,fireIntensity=0)
tile7 = dataGetter.Tile(ID=[2,0],LAT=50.940,LON=-1.398,HEIGHT=7,windSpeed=7,\
                 windDirection=7,humidity=7,temperature=7,smoke=7,\
                 precipitation=7,\
                 fireRisk=70,hasFire=False,fireIntensity=0)
tile8 = dataGetter.Tile(ID=[2,1],LAT=50.939,LON=-1.398,HEIGHT=8, windSpeed=8,\
                 windDirection=8,humidity=8,temperature=8,smoke=8,\
                 precipitation=8,\
                 fireRisk=80,hasFire=True,fireIntensity=3)
tile9 = dataGetter.Tile(ID=[2,2],LAT=50.938,LON=-1.398,HEIGHT=9, windSpeed=9,\
                 windDirection=9,humidity=9,temperature=9,smoke=9,\
                 precipitation=9,\
                 fireRisk=90,hasFire=False,fireIntensity=0)

tile10 = dataGetter.Tile(ID=[3,0],LAT=50.938,LON=-1.399,HEIGHT=6,windSpeed=6,\
                 windDirection=6,humidity=6,temperature=6,smoke=6,\
                 precipitation=6,\
                 fireRisk=60,hasFire=False,fireIntensity=0)
tile11 = dataGetter.Tile(ID=[3,1],LAT=50.940,LON=-1.398,HEIGHT=7,windSpeed=7,\
                 windDirection=7,humidity=7,temperature=7,smoke=7,\
                 precipitation=7,\
                 fireRisk=70,hasFire=False,fireIntensity=0)
tile12 = dataGetter.Tile(ID=[3,2],LAT=50.939,LON=-1.398,HEIGHT=8, windSpeed=8,\
                 windDirection=8,humidity=8,temperature=8,smoke=8,\
                 precipitation=8,\
                 fireRisk=80,hasFire=False,fireIntensity=0)
tile13 = dataGetter.Tile(ID=[4,0],LAT=50.938,LON=-1.398,HEIGHT=9, windSpeed=9,\
                 windDirection=9,humidity=9,temperature=9,smoke=9,\
                 precipitation=9,\
                 fireRisk=90,hasFire=False,fireIntensity=0)
tile14 = dataGetter.Tile(ID=[4,1],LAT=50.938,LON=-1.399,HEIGHT=6,windSpeed=6,\
                 windDirection=6,humidity=6,temperature=6,smoke=6,\
                 precipitation=6,\
                 fireRisk=60,hasFire=False,fireIntensity=0)
tile15 = dataGetter.Tile(ID=[4,2],LAT=50.940,LON=-1.398,HEIGHT=7,windSpeed=7,\
                 windDirection=7,humidity=7,temperature=7,smoke=7,\
                 precipitation=7,\
                 fireRisk=70,hasFire=False,fireIntensity=0)
tile16 = dataGetter.Tile(ID=[5,0],LAT=50.939,LON=-1.398,HEIGHT=8, windSpeed=8,\
                 windDirection=8,humidity=8,temperature=8,smoke=8,\
                 precipitation=8,\
                 fireRisk=80,hasFire=False,fireIntensity=0)
tile17 = dataGetter.Tile(ID=[5,1],LAT=50.938,LON=-1.398,HEIGHT=9, windSpeed=9,\
                 windDirection=9,humidity=9,temperature=9,smoke=9,\
                 precipitation=9,\
                 fireRisk=90,hasFire=False,fireIntensity=0)
tile18 = dataGetter.Tile(ID=[5,2],LAT=50.938,LON=-1.398,HEIGHT=9, windSpeed=9,\
                 windDirection=9,humidity=9,temperature=9,smoke=9,\
                 precipitation=9,\
                 fireRisk=90,hasFire=False,fireIntensity=0)


tilemap = dataGetter.TileMap(anchor=anchor,step=1,length=15,width=15)
#fakeTiles = [anchor, tile2,tile3, tile4, tile5, tile6, tile7, tile8, tile9,\
             #tile10,tile11, tile12, tile13, tile14, tile15, tile16, tile17,\
             #tile18]

fakeTiles = []
for i in range(15):
    for j in range(15):
        if i == 0 and j == 0:
            fakeTiles.append(dataGetter.Tile(ID=[i,j],LAT=50,LON=-1,HEIGHT=random.randint(8,12), windSpeed=9,\
                 windDirection=random.randint(6,12),humidity=random.randint(0,100),temperature=random.randint(5,20),smoke=random.randint(5,12),\
                 precipitation=random.randint(0,6),\
                 fireRisk=100,hasFire=False,fireIntensity=0))
          
        else:
            
            fakeTiles.append(dataGetter.Tile(ID=[i,j],LAT=50.938,LON=-1.398,HEIGHT=random.randint(8,12), windSpeed=9,\
                 windDirection=random.randint(6,12),humidity=random.randint(0,100),temperature=random.randint(5,20),smoke=random.randint(5,12),\
                 precipitation=random.randint(0,6),\
                 fireRisk=random.randint(0,100),hasFire=False,fireIntensity=0))

        """if random.randint(0,7) == 0:
            fakeTiles[-1].hasFire = True
            fakeTiles[-1].fireIntensity = 3"""

#fakeTiles[0].fireRisk = 100
tilemap.setFakeData(fakeTiles)




def getAPIData():
    
    global tilemap
    print("hi")
    while True:
        for i in range(tilemap.length):
            for j in range(tilemap.width):
                tilemap.tilemap[i][j].updateAPIData()
            time.sleep(3)
    

thread1 = threading.Thread(target = getAPIData)
thread1.start()

def seperateData(data):
    data += ","
    newData = []
    currentString = ""
    for i in data:
        if i != ",":
            currentString += i
        else:
            newData.append(currentString)
            currentString = ""
        
    return newData

def getSensorData():
    global tilemap

    host = ""
    port = 7777

    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    my_ip = socket.gethostbyname(socket.gethostname())
    print(my_ip)
    c.bind(('',25565))
    c.listen(1)
    while True:
        client,addr = c.accept()
        print(addr)
        i=0
        while True:
            data = client.recv(1024)
            if not data:
                break
            data = seperateData(data.decode('utf-8'))
            print("data",data)
            x = int(data[4])
            y = int(data[5])
            #tilemap.tilemap[x][y].setHumidityTrend(float(data[0]))
            tilemap.tilemap[x][y].setHumidity(float(data[0]))
            #tilemap.tilemap[x][y].setTemperatureTrend(float(data[2])) 
            tilemap.tilemap[x][y].setTemperature(float(data[1]))
            #tilemap.tilemap[x][y].setSmokeTrend(float(data[4]))
            tilemap.tilemap[x][y].setSmoke(float(data[2]))
            tilemap.tilemap[x][y].setPressure(float(data[3]))
            
            #print("smoke",tilemap.tilemap[x][y].smokeTrend)
            #print("temp",tilemap.tilemap[x][y].temperatureTrend)
            """
            for i in range(tilemap.length):
                for j in range(tilemap.width):
                    
                    tilemap.tilemap[i][j].detect_fire()
            """
            tilemap.tilemap[0][0].detect_fire()

            
            #if i%5 == 0:
            tilemap.setSimulatorTiles()
            tilemap.simulate()
            #i=0
            #i += 1
            
        
thread2 = threading.Thread(target = getSensorData)
thread2.start()
##############################
pygame.init()
pygame.mixer.init() #initialises pygame
pygame.font.init()
fps = 60 #the game's frames per second
all_fonts = pygame.font.get_fonts()
myfont = pygame.font.SysFont(all_fonts[7], 30)
infoObject = pygame.display.Info()
screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
pygame.display.set_caption("FAFF")
clock = pygame.time.Clock()
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)
grey = (128,128,128)
red = (255,0,0)
darkgreen = (34,139,34)
fontNumber = 0
#########################
class button():  #class to quickly make buttons
    def __init__(self,colour, x,y,width,height, text='',active_colour = (0,0,255,0.5),fontSize = 45):
        self.current_colour = colour
        self.colour = colour #button colour
        self.active_colour = active_colour #colour of the button while the mouse hovers over it.
        self.x = x #x coordinate of top left corner of the button
        self.y = y #y coordinate of top left corner of the button
        self.width = width       #button width
        self.height = height     #button height
        self.text = text         #button text
        self.fontSize = fontSize

        #these are the different button options. 
        #these options allow many different buttons to be created from this class
        
    def draw(self,screen,outline=None,show_active = False):  #method to draw the button
        if outline:   #decides if the button has an outline.
            pygame.draw.rect(screen, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0) #draws the button outline.
            #the outline is a black box which is slighly bigger than the button. This appears as an outline
        if show_active:
            self.current_colour = self.active_colour
        pygame.draw.rect(screen,self.current_colour, (self.x,self.y,self.width,self.height),0)
        #draws the button
        
        if self.text != "":   #only adds text if there is text to add
            font = pygame.font.SysFont(all_fonts[fontNumber], self.fontSize)   #defines the font used.
            text = font.render(self.text, 1, (0,0,0))      #renders the text
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2))) 
            #puts the text in the center of the button.

        if show_active:
            self.current_colour = self.colour
        
            
    def clicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False  #A method to check if the mouse is over the button.
                      #This is run when th user presses the mouse button.


    def hover(self): #makes the button change colour when the mouse is hovered over it.
            if self.clicked(pygame.mouse.get_pos()):
                self.current_colour = self.active_colour
                return True
            else:
                self.current_colour = self.colour
                return False

        

    def press(self):#checks if the mouse button is pressed.
        if self.clicked(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return True 
        return False

    def setColour(self,colour):
        self.colour = colour



running = True
############## surfaces
"""
mapSection = pygame.Surface((infoObject.current_w / 2, infoObject.current_h)) ##left side

mapToggleSection = pygame.Surface((mapSection.get_size()[0], mapSection.get_size()[1] / 8))
mapViewSection = pygame.Surface((mapSection.get_size()[0], mapSection.get_size()[1] - mapToggleSection.get_size()[1]))

tableSection = pygame.Surface((infoObject.current_w / 2, infoObject.current_h)) #right side
pageToggleSection = pygame.Surface((infoObject.current_w / 2, infoObject.current_h / 8))
tableContentSection = pygame.Surface((infoObject.current_w / 2, infoObject.current_h / 8))
tableTitleSection = pygame.Surface((infoObject.current_w / 2, infoObject.current_h / 8))

mapSurface = pygame.Surface((infoObject.current_w / 2, infoObject.current_h / 8))
"""

##############import images
"""
smallFlame = pygame.image.load("smallFlame1.png")
smallFlameScaled = pygame.transform.scale(smallFlame, (100, 100))
medFlame = pygame.image.load("medFlame1.png")
medFlameScaled = pygame.transform.scale(medFlame, (100, 100))
largeFlame = pygame.image.load("largeFlame1.png")
largeFlameScaled = pygame.transform.scale(largeFlame, (100, 100))
"""
############## defining buttons
quitButton = button(red,1628,108,100,100,"Quit")

fireButton = button(grey,192,108,384,100,"Fire")
riskButton = button((0,90,235),576,108,384,100,"Risk")

returnButton = button(grey,960,873,768,100,"Back")

#############  text
font = pygame.font.SysFont(all_fonts[fontNumber], 70) 
text = font.render("Alert Rankings", 1, (255,255,255))

fontHeading = pygame.font.SysFont(all_fonts[fontNumber], 25) 
textHeadingLon = fontHeading.render("Longitude", 1, (255,255,255))
textHeadingLat = fontHeading.render("Latitude", 1, (255,255,255))
textHeadingStat = fontHeading.render("Status", 1, (255,255,255))
textHeadingGoTo = fontHeading.render("Show on Map", 1, (255,255,255))
textHeadingInfo = fontHeading.render("More Info", 1, (255,255,255))
#############
mode = "home"
mapType = "risk"
zoom = 12
mapX = 768
mapY = 864
offsetX = 0
offsetY = 0
rankingOffset = 0

showButtons = []
infoButtons = []
heldCoords = [0,0]
flashingTile = None
waitTime = 0
for i in range(15):
    showButtons.append(button(grey,960+(153.6*3),2+208+(i+1)*51.2,154,51.2,"Show On Map",fontSize = 25))
    infoButtons.append(button(grey,960+(153.6*4),2+208+(i+1)*51.2,154,51.2,"More Info",fontSize = 25))

extraRect = False
flashingTimer = 0
while running:
    ######
    
    ######
    clock.tick(fps)
    screen.fill((0,0,0))
    if waitTime > 0:
        waitTime -= 1

    if flashingTimer > 0:
        flashingTimer -= 1
        if (flashingTimer > 10 and flashingTimer < 20) or \
           (flashingTimer > 30 and flashingTimer < 40) or \
           (flashingTimer > 50 and flashingTimer < 60):
            extraRect = True
        else:
            extraRect = False
        
    #mapToggleSection.fill((215,255,255))
    if mode == "home":
        ranking = tilemap.getFireAlertRanking()
        rankingView = []
        if len(ranking) < 15:
            rankingViewLength = len(ranking)
        else:
            rankingViewLength = 15
        for i in range(rankingViewLength):
            rankingView.append(ranking[i+rankingOffset])


    
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mousePos[0] < 864:
                if event.button == 4 and zoom < 21:
                    zoom += 1
                elif event.button == 5 and zoom > 1:
                    zoom -= 1
            elif mousePos[0] >= 864:
                if event.button == 5 and rankingOffset + 15 < len(ranking):
                    rankingOffset +=1
                elif event.button == 4 and rankingOffset > 1:
                    rankingOffset -=1
                    

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                offsetX += 1
            elif event.key == pygame.K_LEFT:
                offsetX -= 1
            elif event.key == pygame.K_UP:
                offsetY -= 1
            elif event.key == pygame.K_DOWN:
                offsetY += 1
            
                

    #riskTableSection
    


    #screen.blit(mapToggleSection,(0,0))
    
    quitButton.draw(screen)
    quitButton.hover()

    fireButton.draw(screen,(255,255,255))
    fireButton.hover()

    riskButton.draw(screen,(255,255,255))
    riskButton.hover()

    if mapType == "risk" and fireButton.press():
        mapType = "fire"
        fireButton.setColour((0,90,235))
        riskButton.setColour(grey)

    elif mapType == "fire" and riskButton.press():
        mapType = "risk"
        fireButton.setColour(grey)
        riskButton.setColour((0,90,235))
        
    
    if mode == "home":
        
        screen.blit(text, (1020,120))
        
        screen.blit(textHeadingLon, (970,220))
        screen.blit(textHeadingLat, (1124,220))
        screen.blit(textHeadingStat, (1278,220))
        screen.blit(textHeadingGoTo, (1432,220))
        screen.blit(textHeadingInfo, (1586,220))

        fontHeading = pygame.font.SysFont(all_fonts[fontNumber], 20)
        for index ,tile in enumerate(rankingView):
            
            textLon = fontHeading.render(str(tile.LON), 1, (255,255,255))
            screen.blit(textLon, (970,280+(index)*51.2))
            textLat = fontHeading.render(str(tile.LAT), 1, (255,255,255))
            screen.blit(textLat, (1124,280+(index)*51.2))
            textStat= fontHeading.render(str(tile.status), 1, (255,255,255))
            screen.blit(textStat, (1278,280+(index)*51.2))

        for i in range(rankingViewLength):
            showButtons[i].hover()
            showButtons[i].draw(screen)
            infoButtons[i].hover()
            infoButtons[i].draw(screen)
            if infoButtons[i].press() and waitTime == 0:
                waitTime = 15
                mode = "info"
                heldCoords = rankingView[i].ID

            if showButtons[i].press() and waitTime == 0:
                offsetX = - int(zoom / 2) + rankingView[i].ID[0]
                offsetY = - int(zoom / 2) + rankingView[i].ID[1]
                flashingTile = rankingView[i]
                flashingTimer = 60
                

        ########## draw table
        for i in range(5 + 1):
            for j in range(15 + 1):

                #hor
                pygame.draw.rect(screen,(255,0 ,0),(960,208 + (j * 768) / 15 + 2,768, 3))
                #ver
                pygame.draw.rect(screen,(255,0,0),(960 + (i * mapX) / 5, 210 ,1 ,864))
                #

        ###########

    elif mode == "info":
        #print(heldCoords[0],heldCoords[1])
        #print(tilemap.tilemap[0][0].smoke)
        returnButton.hover()
        returnButton.draw(screen)

        font = pygame.font.SysFont(all_fonts[fontNumber], 60)
        tileInfoHeading = font.render("LON: "+str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].LON)+" LAT: "+str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].LAT), 1, (255,255,255))
        screen.blit(tileInfoHeading, (970,120))

        fontHeading = pygame.font.SysFont(all_fonts[fontNumber], 40)
        textHeight = fontHeading.render("Height: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].HEIGHT) + " m", 1, (255,255,255))
        screen.blit(textHeight, (970,280))
        
        textWindSpeed = fontHeading.render("Wind Speed: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].windSpeed) + " km/h", 1, (255,255,255))
        screen.blit(textWindSpeed, (970,331))
        
        textWindSpeed = fontHeading.render("Wind Direction: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].windDirection) + " degrees", 1, (255,255,255))
        screen.blit(textWindSpeed, (970,382))
        
        textPrecipitation = fontHeading.render("Precipitation: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].precipitation) + " mm", 1, (255,255,255))
        screen.blit(textPrecipitation, (970,433))
        
        textHumidity = fontHeading.render("Humidity: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].humidity) + " %", 1, (255,255,255))
        screen.blit(textHumidity, (970,484))
        
        textTemperature = fontHeading.render("Temperature: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].temperature) + " degrees centigrade", 1, (255,255,255))
        screen.blit(textTemperature, (970,536))
        
        textSmoke = fontHeading.render("Smoke: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].smoke) + " mg/m³", 1, (255,255,255))
        screen.blit(textSmoke, (970,587))
        
        textPressure = fontHeading.render("Pressure: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].pressure) + " hPa", 1, (255,255,255))
        screen.blit(textPressure, (970,638))
        
        textFireRisk = fontHeading.render("Fire Risk: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].fireRisk) + " %", 1, (255,255,255))
        screen.blit(textFireRisk, (970,689))
        
        textHasFire = fontHeading.render("Fire: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].hasFire), 1, (255,255,255))
        screen.blit(textHasFire, (970,740))
        
        textFireIntensity = fontHeading.render("Fire Intensity: " + str(tilemap.tilemap[heldCoords[0]][heldCoords[1]].fireIntensity), 1, (255,255,255))
        screen.blit(textFireIntensity, (970,792))
        
        
        if returnButton.press() and waitTime == 0:
            mode = "home"
            waitTime = 15
        
        
    

    ########## drawing map
    for i in range(zoom):
        for j in range(zoom):

            #hor
            pygame.draw.rect(screen,(0,255,0),(188,208 + (j * mapY) / zoom + 2,768,3))
            #ver
            pygame.draw.rect(screen,(0,255,0),(188 + (i * mapX) / zoom,210,3,864))
            #
            if i + offsetX < tilemap.length and j +offsetY < tilemap.width and i + offsetX > -1 and j + offsetY > -1:
                if mapType == "risk":
                    pygame.draw.rect(screen,calculateColour(tilemap.tilemap[i + offsetX][j + offsetY].getFireRisk()),(188 + (i * mapX) / zoom, 208+(j*mapY)/(zoom)+3, mapX/zoom, mapY/zoom))
                elif mapType == "fire":
                    """
                    smallFlame = pygame.image.load("smallFlame1.png")
                    smallFlameScaled = pygame.transform.scale(smallFlame, (100, 100))
                    medFlame = pygame.image.load("medFlame1.png")
                    medFlameScaled = pygame.transform.scale(medFlame, (100, 100))
                    largeFlame = pygame.image.load("largeFlame1.png")
                    largeFlameScaled = pygame.transform.scale(largeFlame, (100, 100))
                    """
                    #print(tilemap.tilemap[i + offsetX][j + offsetY].getFireSpreadRisk())
                    #rint(tilemap.tilemap[i + offsetX][j + offsetY].getFireSpreadRisk() * 100)
                    if tilemap.tilemap[i + offsetX][j + offsetY].getFireSpreadRisk() * 100 > 20:
                        pygame.draw.rect(screen,calculateColour(tilemap.tilemap[i + offsetX][j + offsetY].getFireSpreadRisk() * 100),(188 + (i * mapX) / zoom, 208+(j*mapY)/(zoom)+3, mapX/zoom, mapY/zoom))

                    if tilemap.tilemap[i + offsetX][j + offsetY].getHasFire():
                        
                        image = calculateFire(tilemap.tilemap[i + offsetX][j + offsetY].getFireIntensity())
                        image = pygame.transform.scale(image, ( int(mapX/zoom), int(mapY/zoom)))#.set_colorkey((255,255,255))
                        #image.set_colorkey((255,255,255))
                        screen.blit(image, ([int(188 + (i * mapX) / zoom), int( 208+(j*mapY)/(zoom)+3)])) 

 
                    
            if extraRect:
                if flashingTile.ID[0] == i + offsetX and flashingTile.ID[1] == j + offsetY:
                    pygame.draw.rect(screen,(255,255,255),(188 + (i * mapX) / zoom, 208+(j*mapY)/(zoom)+3, mapX/zoom, mapY/zoom))

                
            


    ########### draw borders
    pygame.draw.rect(screen,(255,255,255),(960 - 4, 108, 6, 864)) #middle
    pygame.draw.rect(screen,(255,255,255),(192, 208, 1536, 6)) #middle row
    
    pygame.draw.rect(screen,(255,255,255),(192, 108, 1536, 6)) #top
    pygame.draw.rect(screen,(255,255,255),(192, 108, 6, 864)) #left
    pygame.draw.rect(screen,(255,255,255),(1728 - 6, 108, 6, 864)) #right
    pygame.draw.rect(screen,(255,255,255),(192, 972 - 6, 1536, 6)) #bottom
    

    pygame.display.flip()
    
    if quitButton.press():
        pygame.quit()
        running = False
        thread1.join()
        thread2.join()

    


    







    
    



