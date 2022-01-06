#1
def myfunction(intlist,strlist): # represents the parameter inside the function
    list=[]
    newlist=[]
    count=0
    try:
      if(len(int)!=len(str)): # if length of integer is not equal to length of string then the function wont work when it prints
        print("sorry this function will not work")
      else:
        while(count)!= len(intlist): # loop running where count is not equal to length of numbers in list
            anylist=str(intlist[count]+strlist[count]) # this turns an integer to a string variable code
            newlist.append(anylist) # adds a new num into the list
            print(newlist)
    except:
        print("sorry this is wrong, try again")        
    myfunction()              



#2
strlist=["david","john","joseph","draymond"]
intlist=[10,20,30,40]



def secondfunction():
    intlist=[]
    done=False
    while(done==False): # condition statement to run loop until done=True
        print("hey user, pls add a number type done if you want to stop")
        num=input() # lets user add numbers to the list
    if(num=="done"):
        done= True # represents exit strategy
        print("you can stop adding numbers now")
        print("the list before it changed",intlist) # prints list before list is changed and switched to a new position
    else:
        try:
          num=int(input) # this converts num to an integer
          intlist.append= num
        except:
            print("error obtained") #  used to give an option to skip code incase it crashes 
       
            

      


    

   
    smallestoddnum=intlist[0]
    largestevennum=intlist[0]
    smallestposition=0
    largestposition=0
    count=0

    while(count<len(intlist)):   #loop that searches for largest even and smallest odd number
        if(smallestoddnum>intlist[count]): # if smallestoddnum is greater than intlist[count]
            smallestoddnum=intlist[count] # makes smallestoddnum equal to intlist[count]
            smallestposition=count # searches the smallest position in the list by going through every number in the intlist 
            count+=1 # represents the exit strategy to stop loop from running
        if(largestevennum<intlist[count]): #if largestevennum is less than intlist[count]
            largestevennum=intlist[count] # largestevennum will be equals to intlist[count]
            largestposition=count # searches the largest position in the intlist variable
            count+=1

        placeholder= intlist[smallestposition]  #code that swtiches the position from largest to smallest
        intlist[largestposition]=smallestposition #switches the position from largest to smallest in the intlist
        intlist[smallestposition]=largestposition # switches position from smallest to largest in the intlist
        print("list after it changed",intlist)
secondfunction()        

#3
def thirdfunction():
    done= False
    while(not done):
        print("hey input values to add to a list and type done when done")  # user is given an option to inputting values into a list and click on done when he is done inputting the list  
        num=input
        try:
           if(num=="done"):
            done=True # represents the exit strategy to end the loop
            print("stop inputting values")
           else:
              print("hey input values to add to a list and type done when done")
              num=input()

        except:
            print("sorry cannot run!") # helps ignore any wrong code written

        print("would you like to repeat the process?") # asks user if he would like to repeat process
        newnum=input()    # allows user add new numbers to the list

        if(newnum=="yes"): # if the newnum is correct it will repeat the process
            print("repeat")
        elif(newnum=="no"): # if newnum is wrong it will end the process
            print("have a nice day!") 
            done= True  # exit strategy  


                
    list=[1,2,3,4,5,6,7]
    newlist=[]
    count=1
    for items in list: # a for loop is used
        newitems=items**list[count] # these raises each number by its item in the list +1
        newlist.append(newitems) # this adds new items in newlist
        count+=1 # represents exit srtrategy to end loop
thirdfunction()        

#4
done=False
while(not done):
    myfunction()
    secondfunction()
    thirdfunction()
    print("would you like to run all functions again?")
    response=input()

if(response=="yes"):
    print("keep looping!")
elif(response=="no"):
        print("terminate")    
        done=True
    



            


        
               



    
    


