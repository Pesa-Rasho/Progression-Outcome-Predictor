# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w2052935
# Date: 13/12/2023

import graphics

#Variable Declaration
user_preference = True
repeat_program = True
list_output = []
list_input = []
bar_1,bar_2,bar_3,bar_4 = 0,0,0,0
valid_marks = [0,20,40,60,80,100,120]

#Function to check user input is in range of 0,20,40,60,80,100,120 and the user input is an integer
def marks_input(prompt):
    try:
        value = int(input(prompt))
        if (value not in valid_marks):
            print("Out of range")
            return marks_input(prompt)
        return value
    except ValueError:
        print("Integer required")
        return marks_input(prompt)

#Function to check the total 
def check_total (total):
    if total != 120:
        print("Total incorrect\n")
    else:
        return True

#Function to draw the histogram
def draw_histogram(graph,x1,x2,x3,value,label,color):
    rectangle = graphics.Rectangle(graphics.Point(x1,600 - value * 20),graphics.Point(x2,600))
    graphics.Text(graphics.Point(x3,590 - value * 20),value).draw(graph)
    rectangle_text = graphics.Text(graphics.Point(x3,620),label)
    rectangle.setFill(color)
    rectangle_text.setStyle("bold")
    rectangle.draw(graph)
    rectangle_text.draw(graph)    

#Function to quit the program and write the outcomes to a file 
def quit_program():    
        with open("output.txt","w+") as fileOpen:    
            print("\nPart 2:") 
            for i in range(len(list_output)):   
                output = f"{list_output[i]} - {list_input[i]}\n"
                fileOpen.write(output.replace("[","").replace("]",""))  
                print(output.replace("[","").replace("]",""))  
            print("\nPart 3:")
            fileOpen.seek(0)
            print(fileOpen.read())

        #Drawing the histogram based on user inputs
        graph = graphics.GraphWin("Histogram", 700, 700)
        topic = graphics.Text(graphics.Point(100,100),"Histogram Results")
        topic.setStyle("bold")
        topic.draw(graph)

        draw_histogram(graph,150,30,100,bar_1,"Progress","palegreen")
        draw_histogram(graph,310,190,260,bar_2,"Trailer","yellowgreen")
        draw_histogram(graph,470,350,420,bar_3,"Retriever","olive")
        draw_histogram(graph,630,510,580,bar_4,"Exclude","lightpink") 

        graphics.Text(graphics.Point(100,650),f"{bar_1+bar_2+bar_3+bar_4} Outcomes in total").draw(graph)
        try:
            graph.getMouse()
        except graphics.GraphicsError:
            pass

#Checking if the user enters a valid user type
def user_type_input(prompt):
    try:
        user_type = input(prompt)
        if user_type.lower() == "s":
            return user_type
        elif user_type.lower() == "t":
            return user_type
        else:
            print("Please enter a valid input")
            return user_type_input(prompt)
    except ValueError:
        print("Please enter a valid input")
        return user_type_input(prompt)

#Main program to get the user input
user_type = user_type_input("Are you a student or a staff member?\nEnter 's' for student and 't' for staff: ")
while user_preference:  
    pass_value = marks_input("\nEnter your marks at pass: ")
    defer_value = marks_input("Enter your marks at defer: ")
    fail_value = marks_input("Enter your marks at fail: ")        

    total = pass_value + defer_value + fail_value
    
    #Checking the conditions
    if check_total(total):
        list_input.append([pass_value,defer_value,fail_value])
        if pass_value == 120:
            progression_state = "Progress"
            bar_1 += 1
            
        elif pass_value == 100:
            progression_state = "Progress (module trailer)"
            bar_2 += 1
            
        elif fail_value >=80:
            bar_4 += 1
            progression_state = "Exclude"
            
        else:
            progression_state = "Do not progress - module retriever"
            bar_3 += 1
        
        print(f"{progression_state}\n")
        list_output.append(progression_state)                

    #Checking if the staff wants to repeat the program again
    if user_type == "t":
        while repeat_program:
            new_set = input("Would you like to enter another set of data?\nEnter 'y' for yes and 'q' for quit and view results: ")
            if new_set == "q" or new_set == "Q":
                quit_program()  
                user_preference = False
                break
                
            elif new_set == "y" or new_set == "Y":
                break
                
            else:
                print("Invalid input")
                
    #Checking if the student wants to input another data when the total is incorrect
    elif user_type == "s":
        if total != 120:
            new_set = input("Would you like to enter another set of data?\nEnter 'y' for yes and 'q' for quit: ")
            if new_set == "q" or new_set == "Q":
                user_preference = False
                break
                
            elif new_set == "y" or new_set == "Y":
                pass

            else:
                print("Invalid input") 
        else:
            user_preference = False
                      
input("Press enter to exit")
