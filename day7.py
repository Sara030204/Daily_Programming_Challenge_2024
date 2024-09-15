#Trapping rain water

heights=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


def measure_trap_water(input):
    n=len(heights)
    water=0
    i=0
    
    while i<n :
        j=i+1
        max_element_index=0
        gap=0

        while j<n:
            if input[j]>=input[i]:
                max_element_index=j
                break
            gap+=1
            j+=1
        
        if max_element_index==0:
            i=i+1
            continue
        
        water_drop=(gap*input[i])-sum(input[i+1:max_element_index])
        water+=water_drop
        i=max_element_index
    return water

print(measure_trap_water(heights))