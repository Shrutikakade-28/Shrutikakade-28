def add(A, B, r, c):
    C = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C
def sub(A,B,r,c,C):
    for i in range(r):
        row=[]
        for j in range(c):
            row.append(A[i][j]-B[i][j])
            C.append(row)   
def mult(A,B,r1,c1,c2):
    C = [[0 for _ in range(c2)] for _ in range(r1)]
    for i in range(r1):
        for j in range(c1):
            for k in range(c2):
                C[i][j] += A[i][k] * B[k][j]
    return C
def transpose(A, r, c):
    C = []
    for i in range(c):
        row = []
        for j in range(r):
            row.append(A[j][i])
        C.append(row)
    return C

def display(M):
     n= len(M)
     for i in range(n):
            print(M[i])

def accept(M):
    r=int(input("Enter number of rows: "))
    c=int(input("Enter number of columns: "))
    for i in range(r):
        row=[]
        for j in range(c):
            V=int(input("Enter value of elements M[%d][%d]: "%(i,j)))
            row.append(V)
        M.append(row)
    return r, c    
def main():
    A=[]
    B=[]
    Output=[]
    ADD=[]
    SUB=[]
    
    while True:
         print("\t1.Accept data")
         print("\t2.Addition of two Matrix")
         print("\t3.Substraction of two Matrix")
         print("\t4.Multiplication of two Matrix")
         print("\t5.Transpose of a Matrix")
         print("\t6.Exit")
         
         ch=int(input("\n Enter your choice: "))
         
         if(ch==1):
             print("Your choice is 1.Accept data\n***Kindly entern required data***")
             accept(A)
             accept(B)
             print("\nFirst Matrix is")
             display(A)
             print("\nSecond Matrix is")
             display(B)
            
         elif(ch==2):
             print("Your choice is 2.")
             if r1 == r2 and c1 == c2: # type: ignore
                print("Performing matrix addition")
                ADD = add(A, B, r1, c1) # type: ignore
                print("Result of Addition:")
                display(ADD)
             else:
                print("Matrices must have the same dimensions for addition!")
            
         elif(ch==3):
             print("Your choice is 3.")
             Output=sub(A,B,SUB)
             display(SUB)
            
         elif(ch==4):
             print("Your choice is 4.")
             
         elif(ch==5):
             print("Your choice is 5.")
            
         elif(ch==6):
             print("Your choice is 6.Exit")
             break
         else:
             print("Wrong choice")
main()