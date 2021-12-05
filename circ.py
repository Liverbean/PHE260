import math
refalt= [82, 51]
obsalt= [46,21,7]
reflat = 82.512333
obslat = 45.4095127

def DMStoDD(x): #this function turns an angle formated in DMS in an array into an integer decimal representation of that angle. 
    if len(x) <= 2: #the calculation will not worth without something in the 2nd position. 
        x.append(0) #add a zero to the end
    return x[0]+x[1]/60+x[2]/3600 #Convert DMS to DD. 
print(DMStoDD(refalt),DMStoDD(obsalt))

def northsouth(x,y):
    if x>y:
        return math.radians(x-y)*6357 #convert difference to radians and multiply by the raidus of the earth (S=r*Θ)
    else: 
        return math.radians(y-x)*6357 #Repeat with variables flipped. Otherwise we would have to apply an absolute to the difference. 
print(northsouth(reflat,obslat))

def circumference(obsalt, refalt, obslat, reflat):
    altdifference = (DMStoDD(refalt)-DMStoDD(obsalt)) #Find the difference between the altitudes with the oberseved altitute being the minuend and the reference alt being the subtrahend. 
    print(altdifference)
    latdifference = northsouth(obslat,reflat)
    circ = (360/(altdifference))*latdifference #distance * circumference = p(difference of altitudes)/360. Reform into C = 360/(p)*distance. 
    return circ 

print(circumference(obsalt,refalt,obslat,reflat))
