'''
a) 
i main: 7, 3
i swap: 3, 7
i main: 7, 3
---> i printglobals: 5, 8
i main: 7, 3

b)
1st print are using local x, y values, which is 7, and 3
2nd print are using the swapped values in another function, not actually changing the values in main
3rd since we actually didn't change value, x=7, y=3 are printed
4th since the function printglobals dont have local x,y values, it will use the global xy, which is
    x=5, y=8
5th we still have not changed any value, so x=5, y=8 are printed
'''


