import statistics

median_list=[10,80,70,30,50,60,40,20,100,130,120,150,140,20,30,110,160]

def median_of_number(median_):
    sorted_list=sorted(median_)
    mean = sum(median_)/len(median_)
    median=statistics.median(median_)
    mode=statistics.mode(median_)
    return f"{"sorted_list ="} {sorted_list}\n {"mean ="} {mean}\n {"median ="} {median}\n {"mode ="} {mode}"
print(median_of_number(median_list))
print("--------------------------")
def find_median(median_list):
    median_list.sort()
    n=len(median_list)
    if n % 2 == 0 :
          median = (median_list[ n // 2 -1 ] + median_list [n // 2])/2
          return f"{"median ="} {median}"
    else :
          median =  median_list[ n // 2]
          return f"{"median ="} {median}"
print(find_median(median_list))