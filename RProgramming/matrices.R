 # Matrices:
   --------
     
m <- matrix(1:6,nrow = 3, byrow=TRUE)
print(m)

n <- matrix(1:12, nrow= 2 , byrow=TRUE)
print(n)

------------------------------------------------------------------

# Indexing Marix:
  -------  -----
  
m[2,1]


------------------------------------------------------------------
  
 # Adding row/column names:
  ----- ----------  -----

rownames(m) <- c("A", "B","c")
colnames(m) <- c("col1", "col2")

print(m)

-------------------------------------------------------------------


students <- matrix(1:20, nrow=5, byrow=TRUE)
print(students)

rownames(students) <- c("Naveen", "sheakar", "Rakhi", "srikanth", "Rohit")
colnames(students) <- c("Stno","Age", "MobileNo", "Email")
print(students)

----------------------------------------------------------------------

  
  
 # ARITHMETIC OPERATIONS WITH MATRICES:
  ----------- ---------- ---  ---------
  
g <- matrix(1:4, nrow=2, byrow=TRUE)
k <- matrix(1:4, nrow=2, byrow=TRUE)

g * k

g + k

g - k

-------------------------------------------------------------------
  
 #  MATRIX MULTIPLICATION (real linear algebra) :
    ------ -------------- ----- ------ --------
 #  Multiply rows of M1 with columns of M2. 
  
g <- matrix(1:4, nrow=2, byrow=TRUE)
k <- matrix(1:6, nrow=2, byrow=TRUE)
print(g)
print(k)


# This uses row × column dot products.:
  ---- ---- ---  ------- --- --------

g %*% k


# Determinant
-- ----------
print(g)
det(g)


# Inverse:
  -------
solve(g)

  
  
  
  
  