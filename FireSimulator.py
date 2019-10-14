from math import *


        
                


class Tile(): #Class to hold tile data
    def __init__(self):
        self.x = 0
        self.y = 0
        self.onFire = 0
        self.already_spread = False
        self.wind_strength = 0
        self.wind_direction = 0 
        self.dryness = 0
        self.height = 0

    def set_values(self,x,y,wind_strength,wind_direction,dryness,onFire,height): #Sets values so data is protected
        self.x = x
        self.y = y
        self.onFire = onFire
        self.already_spread = False
        self.wind_strength = wind_strength
        self.wind_direction = wind_direction
        self.dryness = dryness
        self.height = height
        

class FireSimulator(): #Class to store fire predictions
    def __init__(self):
        self.gridDimension = 500.0
        self.grid = []
        self.timeFrame = 10000
        self.defaultFireVel = 0.5

    def set_values(self,tile_data): #Imports Values from map
        for i in range(len(tile_data)):
            self.grid.append([])
            for j in range(len(tile_data[0])):
                self.grid[-1].append(Tile())
                self.grid[-1][-1].set_values(tile_data[i][j].ID[0],tile_data[i][j].ID[1],tile_data[i][j].windSpeed,\
                                         tile_data[i][j].windDirection,tile_data[i][j].dryness,tile_data[i][j].hasFire,tile_data[i][j].HEIGHT)
                if self.grid[-1][-1].onFire == True:
                    self.grid[-1][-1].onFire = 1
                else:
                    self.grid[-1][-1].onFire = 0
                
    def calcSpread(self,Tile,xDiff,yDiff,slopeAngle): #Function to calculate spead of fire
        if xDiff == 0 and yDiff == 0: #If target tile is the spreading tile
            angle = True
        elif xDiff == 0 and yDiff == -1:
            angle = 0.0
        elif xDiff == 1 and yDiff == -1:
            angle = pi/4
        elif xDiff == 1 and yDiff == 0:
            angle = pi/2
        elif xDiff == 1 and yDiff == 1:
            angle = 3*pi/4
        elif xDiff == 0 and yDiff == 1:
            angle = pi
        elif xDiff == -1 and yDiff == 1:
            angle = 5*pi/4
        elif xDiff == -1 and yDiff == 0:
            angle = 3*pi/2
        else:
            angle = 7*pi/4
            
        if angle == True: #If target tile is the spreading tile
            fireVel = 0
        else:
            angleDiff = abs(angle-Tile.wind_direction) #Gets difference in angles
            windInDirection = cos(angleDiff) #Gets component of wind in direction of tile
            velocity = windInDirection * Tile.wind_strength #Gets velocity in direction of time
            minus = False
            
            if velocity < 0: #Avoids complex numbers by flagging negatives
                velocity = -velocity
                minus = True

            fireVel = self.defaultFireVel*(1 + 24*((tan(slopeAngle))**2) + 0.062 * (velocity**1.67))#*self.dryness #Calculate fire velocity using slope and wind modifiers

            if minus: #Resolving negative velocity flag
                fireVel = -fireVel
                
        return fireVel



    def process_fires(self): 
        for i in range(len(self.grid)): #Iterates over each tile in the grid
            for j in range(len(self.grid[0])):
                tile = self.grid[i][j]
                if tile.onFire != 0 and tile.already_spread == False: 
                    self.calc_surrounding_fires(tile,self.timeFrame) #Spread fires if on fire
                    tile.already_spread = True #Flags fire spread

        output = []
        for i in range(len(self.grid)): #Iterates over each tile in the grid
            for j in range(len(self.grid[0])):
                tile = self.grid[i][j]
                if tile.onFire != 0:
                    output.append([[tile.x,tile.y],tile.onFire])

        return output

        #[[[x,y],onFire],   ..., ]
                



    def calc_surrounding_fires(self,tile,remaining_time): #Calculates whether a fire will be spread
        X0 = tile.x
        Y0 = tile.y

        for x in range(-1,2): #Iterates over tiles 1 around spreading tile
            for y in range(-1,2):
                if X0+x >= 0 and Y0+y >= 0 and X0+x < len(self.grid) and Y0+y < len(self.grid[0]) :
                    if self.grid[X0+x][Y0+y].onFire == 0: #Checks tile is not already on fire
                        grid_dim = self.gridDimension
                        if x%2 == 1 and y%2 == 1: #Checks if tile is a diagonal from spreading 
                            grid_dim = grid_dim * sqrt(2)
                            
                            
                        slopeAngle = atan((self.grid[X0+x][Y0+y].height-tile.height)/grid_dim) #Generates slope angle from heights
                        spread_velocity = self.calcSpread(self.grid[X0+x][Y0+y],x,y,slopeAngle) #Calculates velocity of fire
                        #print("SPread velocity",spread_velocity)
                        if spread_velocity == 0:
                            time_taken = 10000000000000000000000000000
                        else:
                            time_taken = grid_dim/abs(spread_velocity) #Calculates time taken to spread
                        if time_taken <= remaining_time: #If fire will spread within timeframe
                            #print("SPREAD!")
                            self.grid[X0+x][Y0+y].onFire = 0.5*(1-(time_taken/remaining_time)) #Calculates probability of spread
                            remaining_time -= time_taken
                            self.calc_surrounding_fires(self.grid[X0+x][Y0+y],remaining_time) #Spread of fire from new tile to surroundings
                            self.grid[X0+x][Y0+y].already_spread = True #Flags as having spread
                            #print("verer",self.grid[X0+x][Y0+y].onFire)


            



        
