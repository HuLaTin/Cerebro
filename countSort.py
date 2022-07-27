rand = open(r'Data\rand') # open file
text = rand.read() # read in text

nums = text.split('\n') # split on 'new line' character
nums = [num for num in nums if num.strip()] # remove empty characters
nums =[int(num) for num in nums] # strings to ints

#len(nums)
numCopy = nums.copy() # make a copy just in case
countNums = [] # create an empty list

highestNum = nums[0] # placeholder

for i in nums: # for loop
    currentNum = i # set current number
    if currentNum > highestNum: # getting largest number
        highestNum = currentNum # set highest number so far

highestNum += 1 # to account for 0

countNums = [0] * highestNum # create an empty list

for i in nums: # for loop
    countNums[i] += 1 # count each number

sortedNums = [] # create an empty list

for index, item in enumerate(countNums): # for loop with enumeration
    if item != 0: # does this count as a comparison?
        sortedNums.extend([int(index)] * item) # using extend to add items multiple times

print(sortedNums) # print list