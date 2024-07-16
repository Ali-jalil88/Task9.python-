lis1 = ["Ali" , "Hassan" , "Hallo"]
lis2 = ["Hallo" , "Ali" , "Hi"]

def intersection_list(x,y):
   result = [x for x in lis1 if x in lis2]
   return result
print(intersection_list(lis1,lis2))

def intersection_list(lis1,lis2):
   return list(set(lis1) & set(lis2)) # ( & this is intersection not and -----> & using just with Set )
print(intersection_list(lis1,lis2))

def intersection_list(lis1,lis2):
   return list(set(lis1) and set(lis2)) # ( and this is and not intersection -----> not using  with Set auch with nothink)
print(intersection_list(lis1,lis2))

       
       