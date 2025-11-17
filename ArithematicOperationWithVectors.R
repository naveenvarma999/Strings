# ARITHMETIC OPERATIONS WITH VECTORS:
  ---------- ---------- ----  ------
    
      # Addition:
       ---------
  
x <- c(1, 2, 3)
y <- c(2, 4, 6)
z <- x + y
print(z)

---------------------
x <- c(1,2)
y <- c(1,2,3,4,5)
z <- x + y
print(z)

# Warning message:
  In x + y : longer object length is not a multiple of shorter object length
---------------------
    
x <- c(1,2,3,4)
y <- c(1,2)
z <- x + y
print(z)

---------------------
  
   # Subtraction:
     -----------
  
x <- c(1,2,3,4)
y <- c(1,2)
z <- (x - y)
print(z)
  
-------------------------------
   
  # Multiplication:
    --------------
  
x <- c(1,2,3,4)
y <- c(1,2,3,4)
z <- x * y
print(z)

---------------------------------
  
  # Division:
    --------
 # It gives the exact decimal result.
  
x <- c(10, 20, 30, 40)
y <- 2
z <- x / y
print(z)


---------------------------------

   # Exponentiation:
     --------------
  
x <- c(2,4,6)
y <- c(2,4,6)
z <- x ^ y
print(z)

---------------------------------

  # Modulus (remainder):
    -------  ---------
  
x <- c(2,4,6)
y <- c(2,4,6)
z <- x %% y
print(z)

---------------------------------
  
  # Integer Division:
    ------- --------
# It gives only the whole number part (quotient) and removes decimals.
  
x <- c(2,4,6)
y <- c(2,4,6)
z <- x %/% y
print(z)

----------------------------------
  
  
  
