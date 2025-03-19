myMixedTypeList= [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
print("The value", myMixedTypeList[0], "is of data type", type(myMixedTypeList[0]))  # concatenation is simple but limited formatting

item= myMixedTypeList[1]
print("{} is of data type {}".format(item,type(item)))      #string format is flexible but too wordy

item2= myMixedTypeList[2]
#print(f"{item2} is of data type {type(item2)}")  #f here changes the variable inputted into strings, simple and changeable

