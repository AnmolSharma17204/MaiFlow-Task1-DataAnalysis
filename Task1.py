'''
Task 1 of Data Analysis Internship at Main Flow
Date: 18-06-2024
Task Description : Write a program in Python to create a list ,dictionary and a set.
                  Operation to be perfromed are:
                   1) Add a element
                   2) Remove a element
                   3) Update the element
'''
# Creating a list
lst=[2,4,6,8]
#adding a element
lst.append(10)
#removing a element
lst.remove(6)
#updating the element
lst[0]=1

print("The Updated list is : ",lst) 
# output : The Updated list is : [1,4,8,10]


# Creating a Dictionary 
student={
    'Name':'Anmol',
    'Course':'BCA',
    'Age':'20',
    'Contact':'8171******'
}
#adding a key value pair  
student['Gender']='Male'
#removing a key value pair
del student['Age']
#Updating the value of a key
student['Contact']='817129****'

print("The Updated Dictionary is :",student)
#Output : The Updated Dictionary is : {'Name': 'Anmol', 'Course': 'BCA', 'Contact': '817129****', 'Gender': 'Male'}


# Creating a Set
st={1,2,2,3,3,3,4,4,4,4}
#adding a element
st.add(6)
#removing a element
st.remove(3)
#updating the element
st.discard(2)
st.add(5)

print("The Updates set is :",st)
#Output: The Updates set is : {1, 4, 5, 6}
