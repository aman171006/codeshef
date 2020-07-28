### Third variable is not needed for output ###
### map()--->             map(function,iterables)  map() applies float() function to all iterables we get from input()
#                               |          |       You can use map() on any iterable variables not only input
#                               |          |
with_draw,total_balance = map(float,input().split())

if ( with_draw % 5 ) ==0 and ( with_draw + 0.50 ) <= total_balance :        # 0.50 is added to the withdrawal money as interest is paid by your account only
    print("{0:0.2f}".format(total_balance-with_draw-0.50))          # print("any_string1 {} any_string2 {}".format(var1,var2)) easier to read the code and {0:0.2f} for accuracy.
else :
    print("{0:0.2f}".format(total_balance))
    
    
