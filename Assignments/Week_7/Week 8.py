#CS101 Lab  Week 8
#Program Lab Week 8
#Jonathan Garcia  Sanchez
#jggfh@umsystem.edu
#PROBLEM: Read through a file with vehicle descriptions and split that file based on the tab character then read the lines that the user input, then ask for an output file to choose based one mpg that a user will input.

#1. start
#2. set up a function for mpg, inside have min_mpg equal to one then begin a while loop for while min mpg is none have try
#3. In the try have a mpg input that is also equal to none, then ask for the mpg input, if it is not between 1-100 range raise value error, then have an except value  error:
#4. if mpg input  is none print that  they must enter a number for the fuel economy, if it is less than - print it must be greater than 0, else it must  be less than  100, out of the else have min mpg equal to mpg input
#5. outside the function in the main have input file equal to one and while input file is one have a try
#6. in the try have variable for input file to open with input from the user that reads (r)
#7. then have  an except for filenot found error as e that print could not open file name 
#8. another except for input ouput error  as e and print that it oculd not open for reading
#9. reapt the input file steps for an outpule file but have it write (w) instead of read
#10. have a for loop for row in the inputfile that reads starting at 1 [1:]
#11. have words equal the row split by tab
#12. now have a try, inside  have total equal to float of words at [-3]
#13. if the total is greater than min mpg, output file write the words at[0]:<5, words at [1]:<15 , words[2]:<20, and total:>10
#14. except for value error to print that coule convert value for words[-3], [1], [2]
#15. close both files
#16. stop

########

def mpg():
    global min_mpg
    min_mpg = None
    while min_mpg is None:
        try:
            mpg_input = None
            mpg_input = int(input("Enter the minimum mpg ==> "))
            if mpg_input not in range(1,100):raise ValueError
        except ValueError:
            if mpg_input is None:
                print("You must enter a number for the fuel economy")
            elif mpg_input <= 0:
                print("Fuel economy given must be greater than 0")
            else:
                print("Fuel economy given must be less than 100")
        else:
            min_mpg = mpg_input
    print()
    
mpg()

input_file = None
while input_file is None:
    try:
        input_file = open(input("Enter the name of the input vehicle file ==> "),'r')
    except FileNotFoundError as e:
        print(f"Could not open file {e.filename}")
    except IOError as e:
        print(f"Could not open file {e.filename} for reading")
print()

output_file = None
while output_file is None:
    try:
        output_file = open(input("Enter the name of the file to output to ==> "),'w')
    except IOError as e:
        print(f"Could not open file {e.filename} for writing")
print()
for row in input_file.readlines()[1:]:
    words = row.split('\t')
    try:
        total = float(words[-3])
        if total > min_mpg:
            output_file.write(f"{words[0]:<5}{words[1]:<15}{words[2]:<20}{total:>10}\n")
    except ValueError:
        print(f"Could not convert value {words[-3]} for vehicle {words[0]} {words[1]} {words[2]}")
input_file.close
output_file.close()
