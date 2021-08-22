#Write a program that prints each item and its corresponding type from the following list.
#One of the output line as an example: The type of clarusway is <class 'str'>.

#Note: Write the program with for statement.
sample_list = [{"section":5, "topic":2}, 'clarusway', [1, 4], 2020, 3.14, 1+618j, False, (10, 20)]

for i in sample_list:
    print("The type of {} is {}".format(i,type(i)))


