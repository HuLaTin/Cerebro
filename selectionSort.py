rand = open(r'Data\rand') # open file
text = rand.read() # read in text

nums = text.split('\n') # split on 'new line' character
nums = [num for num in nums if num.strip()] # remove empty characters
nums =[int(num) for num in nums] # strings to ints

#len(nums)
numCopy = nums.copy() # make a copy just in case
sortedNums = [] # create an empty list
pos = 0 # int(0)
lengthNums = len(nums) # set variable to length of list

while True: # infinite while loop
    lowestNum = nums[0] # placeholder variable
    lowestPos = 0 # placeholder variable

    for i,j in enumerate(nums): # for loop, enumerate
        currentNum = j
        currentPos = i

        if currentNum < lowestNum: # getting smallest number
            lowestNum = currentNum # set lowest number
            lowestPos = i # set position for list
    
    sortedNums.append(lowestNum) # append to list
    pos += 1 # iterate by 1

    del nums[lowestPos] # delete from list by position

    if len(sortedNums) == lengthNums: # if equal then break
        break

print(sortedNums) # print sorted list to console
# save?