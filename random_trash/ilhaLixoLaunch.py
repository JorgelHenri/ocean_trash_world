import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches



startText = "<?xml version='1.0' encoding='UTF-8'?>\n\
            <launch>\n"

endText = " </launch>"

tamX, tamY, tamW, tamH = -25, -25, 50, 50
islandX, islandY, islandW, islandH = -2, -2, 4, 4

probTrashAlone = 0.2
amountTrashAlone = 5
amountSetTrash = 5
minSizeTrash, maxSizeTrash = 2, 7
minDensityTrash, maxDensityTrash = 0.6, 0.9
# format = "X", "quad", "u", "random", "triangle", "other"
format = "X", "quad", "other"

f = open("trash.launch", "w")
f.write(startText)

count = 0

def insertTrash1(x, y, yaw, count):
    model = "<include file='$(find offshore_uav_pack)/launch/spawn_sdf.launch'>\n\
        <arg name='robot_name' value='trashin" + str(count) + "'/>\n\
        <arg name='x' value='" + str(x) + "' />\n\
        <arg name='y' value='" + str(y) + "' />\n\
        <arg name='z' value='2' />\n\
        <arg name='roll' value='0'/>\n\
        <arg name='pitch' value='0'/>\n\
        <arg name='yaw' value='" + str(yaw) + "' />\n\
        <arg name='sdf_robot_file' value='$(find asv_wave_sim_gazebo)/models/beer_bottle/model.sdf' />\n\
    </include>\n"

    count += 1
    return x, y, yaw, model, count

def insertTrash2(x, y, yaw, count):
    model = "<include file='$(find offshore_uav_pack)/launch/spawn_sdf.launch'>\n\
        <arg name='robot_name' value='trashin" + str(count) + "'/>\n\
        <arg name='x' value='" + str(x) + "' />\n\
        <arg name='y' value='" + str(y) + "' />\n\
        <arg name='z' value='2' />\n\
        <arg name='roll' value='0'/>\n\
        <arg name='pitch' value='0'/>\n\
        <arg name='yaw' value='" + str(yaw) + "' />\n\
        <arg name='sdf_robot_file' value='$(find asv_wave_sim_gazebo)/models/garbage_bag/model.sdf' />\n\
    </include>\n"

    count += 1
    return x, y, yaw, model, count

def insertTrash3(x, y, yaw, count):
    model = "<include file='$(find offshore_uav_pack)/launch/spawn_sdf.launch'>\n\
        <arg name='robot_name' value='trashin" + str(count) + "'/>\n\
        <arg name='x' value='" + str(x) + "' />\n\
        <arg name='y' value='" + str(y) + "' />\n\
        <arg name='z' value='2' />\n\
        <arg name='roll' value='0'/>\n\
        <arg name='pitch' value='0'/>\n\
        <arg name='yaw' value='" + str(yaw) + "' />\n\
        <arg name='sdf_robot_file' value='$(find asv_wave_sim_gazebo)/models/square_bottle/model.sdf' />\n\
    </include>\n"
    
    count += 1
    return x, y, yaw, model, count

def insertTrash4(x, y, yaw, count):
    model = "<include file='$(find offshore_uav_pack)/launch/spawn_sdf.launch'>\n\
        <arg name='robot_name' value='trashin" + str(count) + "'/>\n\
        <arg name='x' value='" + str(x) + "' />\n\
        <arg name='y' value='" + str(y) + "' />\n\
        <arg name='z' value='2' />\n\
        <arg name='roll' value='0'/>\n\
        <arg name='pitch' value='0'/>\n\
        <arg name='yaw' value='" + str(yaw) + "' />\n\
        <arg name='sdf_robot_file' value='$(find asv_wave_sim_gazebo)/models/water_bottle/model.sdf' />\n\
    </include>\n"
    
    count += 1
    return x, y, yaw, model, count

def insertTrash5(x, y, yaw, count):
    model = ""
    
    count += 1
    return x, y, yaw, model, count

def insertTrash6(x, y, yaw, count):
    model = ""
    
    count += 1
    return x, y, yaw, model, count

def insertTrash7(x, y, yaw, count):
    model = ""
    
    count += 1
    return x, y, yaw, model, count

def insertTrash8(x, y, yaw, count):
    model = ""
    
    count += 1
    return x, y, yaw, model, count

def insertTrash9(x, y, yaw, count):
    model = ""
    
    count += 1
    return x, y, yaw, model, count

def insertTrash10(x, y, yaw, count):
    model = ""
    
    count += 1
    return x, y, yaw, model, count

def randomValueAllowedArea(limX, limY, limW, limH, decimal=True, safetyArea=maxSizeTrash):
    x, y = islandX + (islandW/2), islandY + (islandH/2)
    while (x >= islandX - safetyArea and x <= islandX + islandW + safetyArea) and (y >= islandY - safetyArea and y <= islandY + islandH + safetyArea): 
        if decimal:
            x = random.uniform(limX, limX+limW) 
            y = random.uniform(limY, limY+limH) 
        else:
            aX, aY = [limX, limX+limW], [limY, limY+limH]
            x = random.randrange(min(aX), max(aX))
            y = random.randrange(min(aY), max(aY)) 

    return x, y

def X(centralX, centralY, r):
    pointX, pointY = 0, 0
    r = random.uniform(0, r)
    p1 = random.random()
    p2 = 1 - p1
    randomSignal = 1 if random.random() <= 0.5 else -1

    pointX = centralX + r * p1 * randomSignal
    pointY = centralY - r * p2 * randomSignal
    
    return pointX, pointY

def quad(centralX, centralY, r):
    pointX, pointY = 0, 0
    auxX, auxY = r = random.uniform(-r, r), random.uniform(-r, r)

    pointX = centralX + auxX
    pointY = centralY + auxY

    return pointX, pointY

# trashs = [insertTrash1, insertTrash2, insertTrash3, insertTrash4, insertTrash5, insertTrash6, insertTrash7, insertTrash8, insertTrash9, insertTrash10]
trashs = [insertTrash1, insertTrash2, insertTrash3, insertTrash4]

x, y = [], []

formatAuxList = np.random.choice(format, amountSetTrash, p=[0.25, 0.25, 0.5])
print(formatAuxList)

for shape in formatAuxList:
    if random.random() >= probTrashAlone:
        randomSize = random.randrange(minSizeTrash, maxSizeTrash)
        randomDensity = random.uniform(minDensityTrash, maxDensityTrash)
        xPos, yPos = randomValueAllowedArea(tamX, tamY, tamW, tamH, decimal=False)
        
        if shape == "X":
            for _ in range(randomSize*5):
                if random.random() <= randomDensity:
                    xShapePos, yShapePos = X(xPos, yPos, randomSize)
                    newTrash = random.choice(trashs)
                    auxX, auxY, _, textTrash, count = newTrash(xShapePos, yShapePos, random.uniform(0, math.pi), count)
                    x.append(xShapePos)
                    y.append(yShapePos)
                    f.write(textTrash)

        elif shape == "quad":
            for _ in range(randomSize*5):
                if random.random() <= randomDensity:
                    xShapePos, yShapePos = quad(xPos, yPos, randomSize)
                    newTrash = random.choice(trashs)
                    auxX, auxY, _, textTrash, count = newTrash(xShapePos, yShapePos, random.uniform(0, math.pi), count)
                    x.append(xShapePos)
                    y.append(yShapePos)
                    f.write(textTrash)

        # elif shape == "u":

        # elif shape == "random":

        # elif shape == "triangle":

        elif shape == "other":
            for _ in range(randomSize*5):
                if random.random() <= randomDensity:
                    xShapePos, yShapePos = randomValueAllowedArea(xPos - randomSize, yPos - randomSize, xPos + randomSize, yPos + randomSize, decimal=False)
                    newTrash = random.choice(trashs)
                    auxX, auxY, _, textTrash, count = newTrash(xShapePos, yShapePos, random.uniform(0, math.pi), count)
                    x.append(xShapePos)
                    y.append(yShapePos)
                    f.write(textTrash)

    else:
        for _ in range(amountTrashAlone):
            xPos, yPos = randomValueAllowedArea(tamX, tamY, tamW, tamH, decimal=False, safetyArea=maxSizeTrash/5)
            newTrash = random.choice(trashs)
            auxX, auxY, _, textTrash, count = newTrash(xPos, yPos, random.uniform(0, math.pi), count)
            x.append(auxX)
            y.append(auxY)
            f.write(textTrash)


f.write(endText)

plt.plot(x, y, ".", color="red")
plt.xlim([tamX, tamX+tamW])
plt.ylim([tamY, tamY+tamH])
rect=mpatches.Rectangle((islandX,islandY),islandW,islandH, fill=True, color="#ecedc2", linewidth=2)
plt.gca().add_patch(rect)
plt.show()