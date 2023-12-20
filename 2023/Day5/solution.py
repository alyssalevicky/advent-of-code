import sys
import math

def apply_rule(toApply, nextNumber):
    for rule in toApply:
            source = int(rule[sourceIndex])
            range = int(rule[rangeIndex])
            destination = int(rule[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                return destination + diff
    return nextNumber

seeds = []
toSoil = []
toFertilizer = []
toWater = []
toLight = []
toTemperature = []
toHumidity = []
toLocation = []

value = 0

destinationIndex = 0
sourceIndex = 1
rangeIndex = 2

with open("2023\Day5\input.txt") as f:
  mapCount = 1
  for gameIndex, fullLine in enumerate(f):
        line = fullLine.strip()
        
        if not line:
            mapCount += 1
            continue
        

        values = [i.strip() for i in line.split(' ')]
        if len(values) == 2:
            continue
        
        match mapCount:
            case 1:
                #Delete line prefix
                values.pop(0)
                seeds = values
               
            case 2:
                toSoil.append(values)
            case 3:
                toFertilizer.append(values)
            case 4:
                toWater.append(values)
            case 5:
                toLight.append(values)
            case 6:
                toTemperature.append(values)
            case 7:
                toHumidity.append(values)
            case 8:
                toLocation.append(values)
                
#Now Lets Do something Crazy with this
while len(seeds) > 0:
    first = int(seeds.pop(0))
    second = int(seeds.pop(0))
    
    rangePossible = sys.maxsize
    
    index = 0
    while(index <= second):
        print("Seed:", index+first)
        
        nextNumber = int(index+first)

        for soil in toSoil:
            source = int(soil[sourceIndex])
            range = int(soil[rangeIndex])
            destination = int(soil[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                remainingRange = source + range - nextNumber
                if remainingRange < rangePossible:
                    rangePossible = remainingRange
                nextNumber = destination + diff
                break

        for fert in toFertilizer:
            source = int(fert[sourceIndex])
            range = int(fert[rangeIndex])
            destination = int(fert[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                remainingRange = source + range - nextNumber
                if remainingRange < rangePossible:
                    rangePossible = remainingRange
                nextNumber = destination + diff
                break
       
        for water in toWater:
            source = int(water[sourceIndex])
            range = int(water[rangeIndex])
            destination = int(water[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                remainingRange = source + range - nextNumber
                if remainingRange < rangePossible:
                    rangePossible = remainingRange
                nextNumber = destination + diff
                break
        
        for light in toLight:
            source = int(light[sourceIndex])
            range = int(light[rangeIndex])
            destination = int(light[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                remainingRange = source + range - nextNumber
                if remainingRange < rangePossible:
                    rangePossible = remainingRange
                nextNumber = destination + diff   
                break     
        
        for temp in toTemperature:
            source = int(temp[sourceIndex])
            range = int(temp[rangeIndex])
            destination = int(temp[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                remainingRange = source + range - nextNumber
                if remainingRange < rangePossible:
                    rangePossible = remainingRange
                nextNumber = destination + diff   
                break 
        
        for hum in toHumidity:
            source = int(hum[sourceIndex])
            range = int(hum[rangeIndex])
            destination = int(hum[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                remainingRange = source + range - nextNumber
                if remainingRange < rangePossible:
                    rangePossible = remainingRange
                nextNumber = destination + diff
                break
        
        for loc in toLocation:
            source = int(loc[sourceIndex])
            range = int(loc[rangeIndex])
            destination = int(loc[destinationIndex])
            if source <= nextNumber <= (source + range):
                diff = nextNumber - source
                remainingRange = source + range - nextNumber
                if remainingRange < rangePossible:
                    rangePossible = remainingRange
                nextNumber = destination + diff
                break
        
        

        print("Location: ", nextNumber)
        if nextNumber < value or value == 0:
            value = nextNumber

        if rangePossible <= 1:
            index += 1
            rangePossible = sys.maxsize
        else:
            index += rangePossible
    

# ONE OFF ERROR FOR PART 2.  The value was one less than what this program outputs
print("Value: ", value)