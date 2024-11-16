def display(A):
     n= len(A)
     print("{",end=' ')
     for i in range(n):
            print(A[i],end=',')
            
     print("}") 
def search(key,A):
    for i in range(len(A)):
           if (A[i]==key):
                  return 1
    return 0
def intersection(A,B):
    C=[]
    for i in range(len(A)):
           flag=search(A[i],B)
           if flag==1:
           
                C.append(A[i])
    return C    
def union(A,B,C):
    for i in range(len(B)):
         C.append(B[i])
    for i in range(len(A)):
          flag=search(A[i],B)
          if flag==0:
              C.append(A[i])
def diff(A,B,C):
    for i in range(len(A)):
          flag=search(A[i],B)
          if flag==0:
                C.append(A[i])
         
def accept(A):
     i=1
     n=int(input("Number of students: "))
     while i<=n:
           name=str(input("\nEnter name of student %d: "%(i)))
           if (name not in A):
             A.append(name)
             i=i+1
           else:
             print("Duplicated")
    
     print("\nData entered successfully")

def main():                                                        
    Group_C=[]
    Group_B=[]
    Group_F=[]
    output=[]
    uni=[]
    out=[]
    dif=[]
    
    while True:
         print("\t1.Accept data")
         print("\t2.List of students who play both cricket and badminton")
         print("\t3.List of students who play either cricket or badminton but not both")
         print("\t4.Number of students who play neither cricket nor badminton")
         print("\t5.Number of students who play cricket and football but not badminton")
         print("\t6.Exit")
         
         ch=int(input("\n Enter your choice: "))
         
         if(ch==1):
             print("Your choice is 1.Accept data\n***Kindly entern required data***")
             print("\nStedents who play Cricket")
             accept(Group_C)
             print("\nStedents who play Badminton")
             accept(Group_B)
             print("\nStedents who play Football")
             accept(Group_F)
             display(Group_C)
             display(Group_B)
             display(Group_F)
         elif(ch==2):
             print("Your choice is 2.List of students who play both cricket and badminton")
             out=intersection(Group_C,Group_B)
             display(out)
         elif(ch==3):
             print("Your choice is 3.List of student who play either cricket or badminton but not both")
             out=intersection(Group_C,Group_B)
             output=union(Group_C,Group_B,uni)
             output=diff(uni,out,dif)
             display(dif)
         elif(ch==4):
             print("Your choice is 4.Number of students who play neither cricket nor badminton")
             output=union(Group_C,Group_B,uni)
             output=diff(Group_F,uni,dif)
             display(dif)
         elif(ch==5):
             print("Your choice is 5.Number of students who play cricket and football but not badminton")
             output=union(Group_C,Group_F,uni)
             output=diff(uni,Group_B,dif)
             display(dif)
         elif(ch==6):
             print("Your choice is 6.Exit")
             break
         else:
             print("Wrong choice")
main()
