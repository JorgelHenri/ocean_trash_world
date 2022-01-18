import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

startText = "<?xml version='1.0' ?>\n\
<?xml-model href='http://sdformat.org/schemas/root.xsd' schematypens='http://www.w3.org/2001/XMLSchema'?>\n\
<sdf version='1.5'>\n\
  <world name='default'>\n\
    <plugin name='mrs_gazebo_static_transform_republisher_plugin' filename='libMRSGazeboStaticTransformRepublisher.so'/>\n\
    <spherical_coordinates>\n\
      <surface_model>EARTH_WGS84</surface_model>\n\
      <latitude_deg>47.397743</latitude_deg>\n\
      <longitude_deg>8.545594</longitude_deg>\n\
      <elevation>0.0</elevation>\n\
      <heading_deg>0</heading_deg>\n\
    </spherical_coordinates>\n\n\
    <physics name='default_physics' default='0' type='ode'>\n\
      <gravity>0 0 -9.8066</gravity>\n\
      <ode>\n\
        <solver>\n\
          <type>quick</type>\n\
          <iters>10</iters>\n\
          <sor>1.3</sor>\n\
          <use_dynamic_moi_rescaling>0</use_dynamic_moi_rescaling>\n\
        </solver>\n\
        <constraints>\n\
          <cfm>0</cfm>\n\
          <erp>0.2</erp>\n\
          <contact_max_correcting_vel>1000</contact_max_correcting_vel>\n\
          <contact_surface_layer>0.001</contact_surface_layer>\n\
        </constraints>\n\
      </ode>\n\
      <max_step_size>0.004</max_step_size>\n\
      <real_time_factor>1</real_time_factor>\n\
      <real_time_update_rate>250</real_time_update_rate>\n\
      <magnetic_field>6.0e-06 2.3e-05 -4.2e-05</magnetic_field>\n\
    </physics>\n\
    <scene>\n\
      <shadows>false</shadows>\n\
      <sky>\n\
        <clouds/>\n\
      </sky>\n\
    </scene>\n\
    <light name='sun' type='directional'>\n\
      <pose frame=''>0 0 1000 0.4 0.2 0</pose>\n\
      <diffuse>1 1 1 1</diffuse>\n\
      <specular>0.6 0.6 0.6 1</specular>\n\
      <direction>0.1 0.1 -0.9</direction>\n\
      <attenuation>\n\
        <range>20</range>\n\
        <constant>0.5</constant>\n\
        <linear>0.01</linear>\n\
        <quadratic>0.001</quadratic>\n\
      </attenuation>\n\
      <cast_shadows>1</cast_shadows>\n\
    </light>\n"

endText = "     <include>\n\
      <uri>model://platform</uri>\n\
      <pose frame=''>0 0 0.5 1.5708 0 0</pose>\n\
    </include>\n\
    <include>\n\
      <uri>model://ocean</uri>\n\
    </include>\n\
  </world>\n\
</sdf>"

tamX, tamY, tamW, tamH = -50, -50, 100, 100
islandX, islandY, islandW, islandH = 0, 0, 2, 1.5

probTrashAlone = 1
amountTrashAlone = 5
amountSetTrash = 20
minSizeTrash, maxSizeTrash = 10, 20
minDensityTrash, maxDensityTrash = 0.2, 0.6
# format = "X", "quad", "u", "random", "triangle", "other"
format = "X", "quad", "other"

f = open("trash1.world", "w")
f.write(startText)

count = 0

def insertTrash1(x, y, yaw, count):
    model = "<model name='beer_bottle" + str(count) + "'>\n\
            <include>\n\
              <pose>" + str(x) + " " + str(y) + " 1 0 0 " +  str(yaw) + "</pose>\n\
              <uri>model://beer_bottle</uri>\n\
            </include>\n\
          </model>\n"

    count += 1
    return x, y, yaw, model, count

def insertTrash2(x, y, yaw, count):
    model = "<model name='dock_block" + str(count) + "'>\n\
            <include>\n\
              <pose>" + str(x) + " " + str(y) + " 1 0 0 " +  str(yaw) + "</pose>\n\
              <uri>model://dock_block</uri>\n\
            </include>\n\
          </model>\n"

    count += 1
    return x, y, yaw, model, count

def insertTrash3(x, y, yaw, count):
    model = "<model name='garbage_bag" + str(count) + "'>\n\
            <include>\n\
              <pose>" + str(x) + " " + str(y) + " 1 0 0 " +  str(yaw) + "</pose>\n\
              <uri>model://garbage_bag</uri>\n\
            </include>\n\
          </model>\n"
    
    count += 1
    return x, y, yaw, model, count

def insertTrash4(x, y, yaw, count):
    model = "<model name='square_bottle" + str(count) + "'>\n\
            <include>\n\
              <pose>" + str(x) + " " + str(y) + " 1 0 0 " +  str(yaw) + "</pose>\n\
              <uri>model://square_bottle</uri>\n\
            </include>\n\
          </model>\n"
    
    count += 1
    return x, y, yaw, model, count

def insertTrash5(x, y, yaw, count):
    model = "<model name='water_bottle" + str(count) + "'>\n\
            <include>\n\
              <pose>" + str(x) + " " + str(y) + " 1 0 0 " +  str(yaw) + "</pose>\n\
              <uri>model://water_bottle</uri>\n\
            </include>\n\
          </model>\n"
    
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
trashs = [insertTrash1, insertTrash2, insertTrash3, insertTrash4, insertTrash5]

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