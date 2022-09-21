# Write your MySQL query statement below
SELECT
  *
FROM
  Users
WHERE
  mail REGEXP '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$';
  
# Regexp: regulate the expression, return 1 if match
#^[a-zA-Z]: The email must start with an alphanumeric letter (i.e., not digit). [Ref: D2, D5a]
