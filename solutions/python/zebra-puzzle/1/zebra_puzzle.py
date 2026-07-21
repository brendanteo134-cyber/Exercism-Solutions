import itertools

def solve():
    houses = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    

    for (red, green, ivory, yellow, blue) in orderings:
  
        if green != ivory + 1:
            continue
            
        for (norwegian, englishman, spaniard, ukrainian, japanese) in orderings:
         
            if norwegian != 1:
                continue
         
            if englishman != red:
                continue
           
            if abs(norwegian - blue) != 1:
                continue
                
            for (coffee, tea, milk, water, orange_juice) in orderings:
                
                if coffee != green:
                    continue
         
                if ukrainian != tea:
                    continue
               
                if milk != 3:
                    continue
                    
                for (kools, chesterfield, old_gold, lucky_strike, parliament) in orderings:
                   
                    if kools != yellow:
                        continue
                    
                    if lucky_strike != orange_juice:
                        continue
                    
                    if japanese != parliament:
                        continue
                        
                    for (dog, snails, fox, horse, zebra) in orderings:
                       
                        if spaniard != dog:
                            continue
                     
                        if old_gold != snails:
                            continue
                       
                        if abs(chesterfield - fox) != 1:
                            continue
                       
                        if abs(kools - horse) != 1:
                            continue
                            
                      
                        nationalities = {
                            norwegian: "Norwegian",
                            englishman: "Englishman",
                            spaniard: "Spaniard",
                            ukrainian: "Ukrainian",
                            japanese: "Japanese"
                        }
                        return nationalities[water], nationalities[zebra]

def drinks_water():
    water_drinker, _ = solve()
    return water_drinker

def owns_zebra():
    _, zebra_owner = solve()
    return zebra_owner