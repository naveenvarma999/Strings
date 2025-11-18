# Logical Vectors:
  ------- ------
    
x <- c(TRUE, FALSE, TRUE)
y <- c(1,2,3,4)
y > 1

---------------------------------
  
# Logical AND:
  ------- ---

x <- c(TRUE, FALSE, TRUE, FALSE)
y <- c(FALSE, TRUE, TRUE, FALSE)
x & y

x <- c(TRUE, FALSE, TRUE, FALSE)
y <- c(FALSE, TRUE, TRUE)
x & y

-----------------------------------
  
 # Logical OR:
   ------ ---
  
x <- c(TRUE, FALSE, TRUE, FALSE)
y <- c(FALSE, TRUE, TRUE, FALSE)
x | y

x <- c(TRUE, FALSE, TRUE, FALSE)
y <- c(FALSE, TRUE, TRUE)
x | y
  
------------------------------------
  
 # Logical NOT !:
   ------- ---
  
x <- c(TRUE, FALSE, TRUE, FALSE)
y <- c(FALSE, TRUE, TRUE, FALSE)
!x & !y
  
-------------------------------------
  
  # Logical Arithematic:
   -------  -----------
  TRUE  = 1
  FALSE = 0
  
x <- c(TRUE, FALSE, TRUE, FALSE)
y <- c(FALSE, TRUE, TRUE, FALSE)
sum(x)
sum(y)

sum(c(TRUE, FALSE, TRUE, FALSE))

--------------------------------------
