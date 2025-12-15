# range() - used to create sequence of values
#   - ordered
#   - indexed
#   - immutable
#   range(stop) 
#       - it will create sequnce from 0 to stop-1
#   range(start, stop) 
#       - it will create sequence from start to stop - 1
#   range(start, stop, step) 
#       - it will create sequence from start to stop - 1 but step size step

r = range(10)
print(f"type(r) = {type(r)}")
print(r[2])     #   value of 2 index
print(r[:2])    #   range from index 0 to 2

#for value in range(10):
#    print(value)

#for value in range(11, 20):
#    print(value)

#for value in range(11, 20, 3):
#    print(value)
