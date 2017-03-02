import csv

def angles(theoretical_angle = 20, rangle_in_tangle = 0.97):
    steps_count = 0

    try:
        csvfile = open("manual_tuning.csv", "r")
    except IOError as e:
        csvfile = open("manual_tuning.csv", "w")
        csvfile.close()
        csvfile = open("manual_tuning.csv", "r")

    freader = csv.reader(csvfile, delimiter = ',')        
    csvfile.close()

    rangles_list = []
    tangles_list = []

    #largest theoretical angle 
    largestTAngle = 0

    #check if CSV freader is empty
    if freader == True:
        for content in freader:
            tangle = content[0]
            tangles_list.append(tangle)

        tangles_list.sort()

        largestTAngle = float(tangles_list[-1])

    csvfile = open("manual_tuning.csv", "a")

    fwriter = csv.writer(csvfile, delimiter = ",")

    rangle_in_tangle = 0.97
    print "Real angle in theoretical: ", rangle_in_tangle
        
    #CHILD angles filling procedure. procedure runs until we meet meet largest element in theoretical angles list, 
    #what means that it is 'PARENT' angle.
    for angle in range(int(largestTAngle), int(abs(theoretical_angle)+1)):
        if theoretical_angle < 0:
            angle *= -1
        
        if abs(angle) is int(abs(theoretical_angle)):
            fwriter.writerow([angle, angle*rangle_in_tangle, "PARENT"])
        else:
            fwriter.writerow([angle, angle*rangle_in_tangle, "CHILD"])    

    csvfile.close()

angles(theoretical_angle = -20)

