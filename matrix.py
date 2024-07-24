#MATRIX --> to make 2D lists. 
# It is commonly used for machine learning 
#It includes a main array and sun array inside the main array (list).

matrix = [   #main array
    [1,2,3], #these are sub-arrays --> each sub array is list.
    [4,5,6], #sub array
    [7,8,9], #sub array
]


# to make a simple photograph of giant X. computer understand the image based on pixels, so we may have O (for dark) or 1 (for green).
# The axample below --> will produce X when we determine the 0 as dark, 1 is another green, white, green, etc. 

matrix = [   #main array
    [1,0,1], #these are sub-arrays
    [0,1,0], #sub array
    [1,0,1], #sub array
]

#The SIMILARITY BW/ LIST & Matrix --> we can write the specific part inside the matrix using [x(start:y(stop)].
# DIFFRENCE BW LIST & Matrix -->  Matrix: there are subarray, so the first [] refers to which sub array. The second [] refers to which data inside selected subarray.

matrix = [   #main array
    [1,5,1], #these are sub-arrays
    [0,1,0], #sub array
    [1,0,1], #sub array
]

print(matrix[0][1])

