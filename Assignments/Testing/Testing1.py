def mpg():
    global min_mpg
    min_mpg = None
    while min_mpg is None:
        try:
            user_input = None
            user_input = int(input("Enter the minimum mpg ==> "))
            if user_input not in range(1,100):raise ValueError
        except ValueError:
            if user_input is None:
                print("You must enter a number for the fuel economy")
            elif user_input <= 0:
                print("Fuel economy given must be greater than 0")
            else:
                print("Fuel economy given must be less than 100")
        else:
            min_mpg = user_input
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
    entries = row.split('\t')
    try:
        combined_mpg = float(entries[-3])
        if combined_mpg > min_mpg:
            output_file.write(f"{entries[0]:<5}{entries[1]:<15}{entries[2]:<20}{combined_mpg:>10}\n")
    except ValueError:
        print(f"Could not convert value {entries[-3]} for vehicle {entries[0]} {entries[1]} {entries[2]}")
input_file.close
output_file.close()
