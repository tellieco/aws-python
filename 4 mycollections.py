myFruitList= ["apple","banana","cherry"] #changeable list use []
print(myFruitList)
print(type(myFruitList))
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2]= "orange" 
print(myFruitList)
print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])
myFruitList.reverse() #changes the existing list
print(myFruitList)

myFinalAnswerTuple= ("apple","banana","pineapple") #Tuple= permanent list use ()
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#myFinalAnswerTuple[2]= "blueberry" #this cannot be done because the Tuple is permanent

myFavoriteFruitDictionary= {
    "Akua":"apple",
    "Saanvi":"banana",
    "Paulo":"pineapple"
}

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))
print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])

