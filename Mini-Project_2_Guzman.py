#Brownie Recipe

#1 Serving
#Makes 16 Large Brownies

#3/4 Cup Flour
#3/4 Cup Unsweetened Cocoa
#1/2 tsp Salt
#3/4 lb Butter
#1 tsp Instant Coffee Powder
#1 1/2 Cups Sugar
#3 Eggs
#1 1/2 tsp Pure Vanilla Extract
#1 Cup Chopped Walnuts or Pecans

#Step 1
#Combine flour, cocoa and salt. Set aside.
#Melt butter in large bowl with coffee added in.
#To butter and coffee mixture add sugar; whisk. Thoroughly whisk in eggs one at a time.
#Add vanilla. Add dry ingredients. Whisk to blend completely. Add nuts.
#Step 2
#Scrape evenly into 8 x 8 Pam sprayed pan (glass or metal).
#Step 3
#Bake at 350°F for 30 - 32 minutes. Cool completely. Cut into 16 large brownies. Serve with COLD milk.

#Link
#https://www.kraftrecipes.com/member-recipe/00119521/best-brownies?categoryid=128

print("Desired amount of brownies must be increments of 8")
Num_brownies = (input("Desired number of brownies: ",))

Flour = (.75/16)
Cocoa = (.75/16)
Salt = (.5/16)
Butter = (.75/16)
Coffee = (1/16)
Sugar = (1.5/16)
Eggs = (3/16)
Vanilla = (1.5/16)
Nuts = (1/16)

Tot_Flour = int(Num_brownies) * Flour
Tot_Cocoa = int(Num_brownies) * Cocoa
Tot_Salt = int(Num_brownies) * Salt
Tot_Butter = int(Num_brownies) * Butter
Tot_Coffee = int(Num_brownies) * Coffee
Tot_Sugar = int(Num_brownies) * Sugar
Tot_Eggs = int(Num_brownies) * Eggs
Tot_Vanilla = int(Num_brownies) * Vanilla
Tot_Nuts = int(Num_brownies) * Nuts

Cost_Flour = 5.00/20
Cost_Cocoa = 6.22/2
Cost_Salt =  3.98/156
Cost_Butter = 3.99/3
Cost_Coffee = 4.33/79.75
Cost_Sugar = 5.42 /13.4
Cost_Eggs = 3.99/12
Cost_Vanilla = 5.84/6
Cost_Nuts = 9.48/2

TCost_Flour = Cost_Flour * Tot_Flour
TCost_Cocoa = Cost_Cocoa * Tot_Cocoa
TCost_Salt = Cost_Salt * Tot_Salt
TCost_Butter = Cost_Butter * Tot_Salt
TCost_Coffee = Cost_Coffee * Tot_Coffee
TCost_Sugar = Cost_Sugar * Tot_Sugar
TCost_Eggs = Cost_Eggs * Tot_Eggs
TCost_Vanilla = Cost_Vanilla * Tot_Vanilla
TCost_Nuts = Cost_Nuts * Tot_Nuts
TCost = TCost_Flour + TCost_Cocoa + TCost_Salt + TCost_Butter + TCost_Coffee + TCost_Sugar + TCost_Eggs + TCost_Vanilla + TCost_Nuts

print(" ")

if int(Num_brownies) >= 1 and int(Num_brownies) % 8 == 0:
    print("To make",Num_brownies," brownies you will need: ")
    print(" ")
    print(format(Tot_Flour,".2f"),"Cups Flour, which will approximately cost $",format(TCost_Flour,".2f"))
    print(format(Tot_Cocoa, ".2f"),"Cups Unsweetened Cocoa, which will approximately cost $", format(TCost_Cocoa, ".2f"))
    print(format(Tot_Salt, ".2f"),"tsp Salt, which will approximately cost $", format(TCost_Salt, ".2f"))
    print(format(Tot_Butter, ".2f"),"lb Butter, which will approximately cost $", format(TCost_Butter, ".2f"))
    print(format(Tot_Coffee, ".2f"),"tsp Instant Coffee Powder, which will approximately cost $", format(TCost_Coffee,".2f"))
    print(format(Tot_Sugar, ".2f"),"Cups Sugar, which will approximately cost $", format(TCost_Sugar, ".2f"))
    print(format(Tot_Eggs, ".2f"),"Eggs, which will approximately cost $",format(TCost_Eggs,".2f"))
    print(format(Tot_Vanilla, ".2f"),"tsp Pure Vanilla Extract, which will approximately cost $", format(TCost_Vanilla, ".2f"))
    print(format(Tot_Nuts, ".2f"),"Cup Chopped Walnuts or Pecans, which will approximately cost $", format(TCost_Nuts, ".2f"))
    print(" ")
    print("The total expected cost for all the ingredients is $",format(TCost,".2f"))

    print(" ")
    print("Let's Make it")
    print(" ")
    print("Step 1:")
    print(" ")
    print("Combine flour, cocoa and salt. Set aside.")
    print("Melt butter in large bowl with coffee added in.")
    print("To butter and coffee mixture add sugar; whisk.")
    print("Throughly whisk in eggs one at a time.")
    print("Add vanilla")
    print("Add dry ingredients. Whisk to blend completely. Add nuts.")

    print("Step 2:")
    print(" ")
    print("Scrape evenly into 8 x 8 Pam sprayed pan (glass or metal).")
    print(" ")
    print("Step 3:")
    print(" ")
    print("Bake at 350°F for 30 - 32 minutes.")
    print("Cool completely. Cut into 16 large brownies. Serve with COLD milk.")
    print(" ")
    print("Recipe Link, https://www.kraftrecipes.com/member-recipe/00119521/best-brownies?categoryid=128")
else:
    print("Desired amount is not a multiple of 8, Try Again.")




