print ("welcome")
print("----------------------------------------------")

#First Ask
firs_ask = int(input("Select operation ? 1)Area  2)Environment | "))
#>>>--- Area Selection
if firs_ask == 1:
    print("-- Area Operation --")
    print("if you want to comput Area with radius 'SELECT 1'")
    print("if you want to comput Area with diameter 'SELECT 2'")
    area_input = int(input("Your selection : "))
    #by radial
    if area_input == 1 :
        radial = int(input("Please get radial :"))
        result = (radial + radial) * 3 ;
        print(result)
    #by dimeter
    elif area_input == 2 :
        diameter = int(input("Please get diameter :"))
        result = diameter * 3
        print(result)
    #else
    else :
        print("Please Enter number betwen 1 & 2")
#>>>--- Environment Selection
elif firs_ask == 2:
    print("-- Environment Operation --")
    print("if you want to comput Environment with radius 'SELECT 1'")
    print("if you want to comput Environment with diameter 'SELECT 2'")
    enviroment_input = int(input("Your selection : "))
    #by radial
    if enviroment_input == 1 :
        radial = int(input("Please get radial :"))
        result = radial * radial * 3 ;
        print(result)
    #by dimeter
    elif enviroment_input == 2 :
        diameter = int(input("Please get diameter :"))
        result = (diameter / 2) * (diameter / 2) * 3
        print(result)
    #else
    else :
        print("Please Enter number betwen 1 & 2")
else :
    print("Please Enter number betwen 1 & 2")
# Hossein Araghi
