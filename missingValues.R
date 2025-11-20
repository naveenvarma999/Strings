 # MISSING VALUES (NA):
   ------- ------
     
# What is NA?
     
NA means “not available”.
   
----------------------------------------------------------

# Checking missing values:
 --------- ------ -------
     
     
x <- c(1, 3, NA, TRUE)

is.na(x)
any(is.na(x))  # TRUE if ANY NA
all(is.na(x))  # TRUE if ALL NA

----------------------------------------------------------
  
 # Arithmetic with NA:
   ---------  --- ---

x <- c(1, 3, NA, 5) 
sum(x)


----------------------------------------------------------

  # Logical with NA:
    ------  ---  ---
  
NA & TRUE  # NA
NA | TRUE  # TRUE
  
----------------------------------------------------------
  
  # Remove NA:
    ------ ---
  
x <- c(1, 3, NA, 5) 
z <- na.omit(x)
z


# Ignore NA in calculations:
   -----  -- -- ------------

sum(x, na.rm = TRUE)


y <- c(1, 3, 5, NA, 7)
na.omit(y)

sum(y, na.rm=TRUE)
