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
for seed in seeds:
    print("Seed:", seed)
    
    nextNumber = int(seed)

    for soil in toSoil:
        source = int(soil[sourceIndex])
        range = int(soil[rangeIndex])
        destination = int(soil[destinationIndex])
        if source <= nextNumber <= (source + range):
            diff = nextNumber - source
            nextNumber = destination + diff
            #print("Soil: ", nextNumber)
            break

    for fertilizer in toFertilizer:
        source = int(fertilizer[sourceIndex])
        range = int(fertilizer[rangeIndex])
        destination = int(fertilizer[destinationIndex])
        if source <= nextNumber <= (source + range):
            diff = nextNumber - source
            nextNumber = destination + diff
            #print("Fertilizer: ", nextNumber)
            break

    for water in toWater:
        source = int(water[sourceIndex])
        range = int(water[rangeIndex])
        destination = int(water[destinationIndex])
        if source <= nextNumber <= (source + range):
            diff = nextNumber - source
            nextNumber = destination + diff
            #print("Water: ", nextNumber)
            break

    for light in toLight:
        source = int(light[sourceIndex])
        range = int(light[rangeIndex])
        destination = int(light[destinationIndex])
        if source <= nextNumber <= (source + range):
            diff = nextNumber - source
            nextNumber = destination + diff
            #print("Light: ", nextNumber)
            break

    for temp in toTemperature:
        source = int(temp[sourceIndex])
        range = int(temp[rangeIndex])
        destination = int(temp[destinationIndex])
        if source <= nextNumber <= (source + range):
            diff = nextNumber - source
            nextNumber = destination + diff
            #print("Temperature: ", nextNumber)
            break

    for humidity in toHumidity:
        source = int(humidity[sourceIndex])
        range = int(humidity[rangeIndex])
        destination = int(humidity[destinationIndex])
        if source <= nextNumber <= (source + range):
            diff = nextNumber - source
            nextNumber = destination + diff
            #print("Humidity: ", nextNumber)
            break

    for loc in toLocation:
        source = int(loc[sourceIndex])
        range = int(loc[rangeIndex])
        destination = int(loc[destinationIndex])
        if source <= nextNumber <= (source + range):
            diff = nextNumber - source
            nextNumber = destination + diff
            #print("Location: ", nextNumber)
            break

    print("Location: ", nextNumber)
    if nextNumber < value or value == 0:
        value = nextNumber
    


print("Value: ", value)