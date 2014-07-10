#Written by A.Trojan

x = 1

#While loop establishes the Devices operating Wattage for calculation
#Volts x Amps = Watts

print "This is an Estimation based on the cost per kWh you provide."
while x == 1:
    print "Do you know the wattage of the Device? (Yes or No)"
    maths = raw_input()
    
    if maths.lower() == 'yes'or maths.lower() == 'y':
        print "Please enter the Device Wattage: "
        watts = raw_input()
        x = x + 1
        
    elif maths.lower() == 'no'or maths.lower() == 'n':
        print "Enter the Voltage of the Device: "
        volts = raw_input(float)
        print "Enter the Amperage of the Device: " 
        amps = raw_input(float)
        print "The total Watts of this device are: "
        watts = (float(volts) * float(amps))
        print watts
        x = x + 1
    
    #Handles any response that is not a variation of Yes or No
    else:  
        print "Incorrect Entry!"
        print "Please enter Yes or No."
    
#Amount per kWh based on users provider.
print "Your Providers cost per Kilowatt-hour:"
cost = raw_input(float)

#Average hours device will be running per day
print "Estimated hours per day: "
hours = raw_input(float)

#Print out amount of energy used Daily,Weekly,Monthly, and Yearly
#(Wattage × Hours Used Per Day) ÷ 1000 = Daily Kilowatt-hour (kWh) consumption
usage = (float(watts) * float(hours)) / 1000
print "Daily Kilowatt-hour: " + str(usage)
dcost = float(usage) * float(cost)
print "$" + str(dcost)
weekly = float(usage) * 7
print "Weekly Kilowatt-hour: " + str(weekly)
wcost = float(weekly) * float(cost)
print "$" + str(wcost)
year = float(weekly) * 52
month = float(year) / 12 
print "Monthly Kilowatt-hour: " + str(month)
mcost = float(month) * float(cost)
print "$" + str(mcost)
print "Yearly Kilowatt-hour: " + str(year)
ycost = float(year) * float(cost)
print "$" + str(ycost)
