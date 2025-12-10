install.packages("tidyverse")
library(readr)

students <- readr::read_csv("C:/Users/NAVEEN VARMA/Downloads/students_large.csv")
View(students)

-------------------------------------------------------------------------------------------------------------------------

# ✅ 2. tidyr → Data Tidying
  ---  ------ - --- --------
  
# Used for reshaping data (wide ↔ long), filling missing values.
library(tidyr)
students_long <- students %>%
  pivot_longer(col=c("math_score","english_score"),
               names_to = "subject",
               values_to = "score")
View(students_long)


stu_wider <- students_long %>% pivot_wider(names_from =subject, 
                              values_from=score)
View(stu_wider)




-----------------------------------------------------------------------------------------------------------------------
 
  # dplyr → Data Manipulation:
  -----  - ----  -----------
# Filter rows
  -----  ----
  
library(tidyverse)

stud <- students %>% filter(department == "Data Science")
View(stud)


# Select columns:
  ------  ------
stud_col <- students %>% select(name,department)
View(stud_col)
  

# Create new column:
 ------- --- ------
  
student_new <- students %>% mutate(total = math_score + english_score)
View(student_new)


# Groupby
  -------
library(dplyr)
students %>% group_by(department) %>% summarise(avg_math = mean(math_score))

students %>% count(department)


------------------------------------------------------------------------------------------------------------------------------------
  
 # ✅ 4. ggplot2 → Data Visualization
  
  # Used for graphs.
  
ggplot(students, aes(math_score)) + geom_histogram()
students %>%
  group_by(department) %>%
  summarise(avg = mean(math_score)) %>%
  ggplot(aes(department, avg)) +
  geom_col()


-------------------------------------------------------------------------------------------------------------------------------------
  

library(purrr)

map(students[ ,c("math_score","english_score")], mean)

map_dbl(students[,c("math_score", "english_score")],mean)

--------------------------------------------------------------------------------------------------------------------------------------
  
# ✅ 7. stringr → String Manipulation

# Used for working with text.
library(stringr)
students %>% filter(str_starts(name, "S"))
str_length(students$name)


student_DataScience <- students %>% filter(department=='Data Science')
View(student_DataScience)



student_DSE <- students %>% filter(department == "Data Science", english_score >90)
View(student_DSE)


stud_g <- filter(students, attendance > 90, english_score > 90, math_score > 90)
View(stud_g)


## 2. arrange() — sort rows
student_ascmarks <- students %>% arrange(attendance)
View(student_ascmarks)



# ⭐ 3B — Operations on COLUMNS


student_markColumn <- students %>% select(name, english_score, math_score, attendance)
View(student_markColumn)


# To select ALL columns from the dataset students EXCEPT the columns math_score and english_score


Stud_Without_scores <- students %>% select(-english_score, -math_score)
View(Stud_Without_scores)


-------------------------------------------------------------------------------------------------------------------

# mutate() — create/modify columns:
  


 students_totalMarks <- students %>% mutate(totalMarks = english_score + math_score)
 View(students_totalMarks)

 
 ------------------------------------------------------------------------------------------------------------------------
   
   ⭐ 3 Grouped Operations:
   
group_by_studnets <- students %>% summarise(mean(english_score))
View(group_by_studnets)


 
group_summarise <- students %>% group_by(department) %>%
  summarise(count=n(),
            avg_math = mean(math_score),
            median_mathscore= median(math_score),
            sd_math = sd(math_score),
            max_math_score = max(math_score),
            min_math_score = min(math_score))
 View(group_summarise)
 
 
 
 