def sum_of_numbers(flock):
    total = 0

    for bird in flock:
        total += bird
    
    print "Sum of given numbers is:", total

def mul_of_numbers(flock):
   total = 1

   for bird in flock:
       total *= bird
    
   print "Product of given numbers is:", total


sum_of_numbers([1, 2, 3, 4, 5])    
mul_of_numbers([1, 2, 3, 4, 5])    
