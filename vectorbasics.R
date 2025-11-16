# Vectors

# What is a vector?
vector is a 1-dimensional sequence of elements of the SAME type.

---------------------------------------------------------------------------------

## Types of Vector
1. numeric
2. integer
3. logical
4. character
5. complex


#Integer vectors:
x <- c(1L, 2L, 3L, 4L)
class(x)

# Numeric Vectors:
y <- c(1.2, 3.5, 4.5, 6.7)
class(y)

# Logical Vectors:
z <- c(TRUE, FALSE, TRUE, TRUE)
class(z)

# Character Vector:
char <- c("Naveen", "Varma", "Nallapu")
class(char)

# complex Vectors:
com <- c(3+4i, 3+3i, 5+7i)
class(com)


-------------------------------------------------------------------------

# Vector length:
  ------ ------
  
x <- c(1L, 2L, 3L, 4L)
length(x)

y <- c(1.2, 3.5, 4.5, 6.7)
length(y)

z <- c(TRUE, FALSE, TRUE, TRUE)
length(z)

char <- c("Naveen", "Varma", "Nallapu")
length(char)

com <- c(3+4i, 3+3i, 5+7i)
length(com)



------------------------------------------------------------------------

# Positive Indexing:
 ---------  ------- 
  
x <- c(1L, 2L, 3L, 4L)
x[2]
x[c(1,3,4)]


y <- c(1.2, 3.5, 4.5, 6.7)
y[2]
y[c(2,4)]


z <- c(TRUE, FALSE, TRUE, TRUE)
z[1]
z[c(1,2)]


char <- c("Naveen", "Varma", "Nallapu")
char[3]
char[c(1,2)]


com <- c(3+4i, 3+3i, 5+7i)
com[3]
com[c(3,2)]

-------------------------------------------------------------------
  
# Negative Indexing: (Remove elements)
  -------- --------
  
  
x <- c(1L, 2L, 3L, 4L)
x[-2]



y <- c(1.2, 3.5, 4.5, 6.7)
y[-2]
y[c(-2,-4)]


z <- c(TRUE, FALSE, TRUE, TRUE)
z[-1]
z[c(-1,-2)]


char <- c("Naveen", "Varma", "Nallapu")
char[-3]
char[c(-1,-2)]


com <- c(3+4i, 3+3i, 5+7i)
com[-3]
com[c(-3,-2)]

-------------------------------------------------------------------------
  
# Range indexing:  
  ----- --------
  
x <- c(2, 3, 4, 5, 6, 7)
x[1:4]
x[2:5]
x[2:3]
  
 -----------------------------------------------------------------------------
  
  # Logical Indexing:
    ------- --------
we select elements from a vector based on TRUE/FALSE values.

1. Wherever the index is TRUE → element is included
2. Wherever the index is FALSE → element is skipped
  

x <- c(1, 2, 3, 4)
x[c(FALSE, TRUE, TRUE, FALSE)]
  
  
x <- c(1,2,3,4,5,6)
x[c(TRUE, FALSE)]

---------------------------------------------------------------------------------------
  
  
  
  
  
  
  
  