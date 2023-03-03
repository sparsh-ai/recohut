#! /bin/bash

# This script accepts the user's first name and last name
# and then prints a message greeting the user

# Print the prompt message on screen
echo -n "Enter your first name: "        

# Wait for user to enter his/her first name, and save the entered name into the variable 'first_name'
read first_name  

# Print the prompt message on screen
echo -n "Enter your last name: " 

# Wait for user to enter his/her lat name, and save the entered name into the variable 'last_name'
read last_name                


# Print the welcome message followed by the name    
echo "Hello $first_name $last_name."

# The following message should print on a single line. Hence the usage of '-n'
echo -n "Congratulations! You just created and ran your second shell script "
echo "using Bash on IBM Skills Network"