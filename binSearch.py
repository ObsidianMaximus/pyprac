flag = 0 			# global variable scope


def binSearch(arr, key):	# function for performing binary searching
    global flag
    start = 0
    end = len(arr)-1
    mid = int(start + (end-start)/2)
    
    while(start<=end):
        
        if(key == arr[mid]):
            flag = 1		# setting flag
            return mid+1	# returning the value if found
        elif(key>arr[mid]):
            start = mid +1
        else:
            end = mid - 1
            
        mid = int(start + (end-start)/2)
        
def main():			# creating a main function for ease of use and readability.
 ind = 0
 i=0
 marks=[]
 totalLength = int(input("Enter the number of elements you wish to insert in the list : "))
 while(i!=totalLength):	# loop for taking user input
    
    ind = int(input("Enter element: "))
    marks.append(ind)
    i+=1
 marks.sort()			# sorting the list, for binary search to work [ monotonic function ]
  
 print("The entered elements in the list [ in sorted order ] are - ")
 
 for i in marks:
 	print(i, end = " ")
    
 toSearch = int(input("\nEnter the element that you want to search : "))

 index = binSearch(marks.copy(), toSearch)	# using copy keyword to copy the list to the binSearch function. Can be directly passed without copy

 if(flag):
    print(f"Element {toSearch} was found in the list at position {index}!")
 else:
    print(f"Element {toSearch} was not found in the list...")
    
        
main()				# calling the main function
