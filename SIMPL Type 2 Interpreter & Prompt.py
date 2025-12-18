#SIMPL Type 2 Interpreter & Prompt
#Copyright (c) 2025, Alexander Peat - All rights reserved
#Author: Alexander Peat
#Program written between: 09/08/2025 and 17/08/2025

#---Notes---

#Always write code in increments of ten

#Print Syntax:
#'P' for 'Print'
#P;S;Hello, World; <- prints a string called 'Hello, World'
#P;V;variable_one; <- prints the contents of a variable called 'variable_one'

#Input Syntax:
#'U' for 'inpUt'
#U;N;number_variable;Enter a number: ; <- outputs the prompt 'Enter a number' and stores the response in a variable called 'number_variable'
#U;S;string_variable;Enter a string: ; <- outputs the prompt 'Enter a string' and stores the response in a variable called 'string_variable'

#Initialisation Syntax:
#'I' for 'Initialise'
#I;N;number_variable;0; <- initialises a variable called 'number_variable' and assigns it the value of 0
#I;S;string_variable;Hello, World; <- initialises a variable called 'string-variable' and assigns it the value of 'Hello, World'

#Mathematical Syntax:
#'M' for 'Mathematics'
#M;answer_variable;operand1;+;operand2; <- adds the two variable ('operand1' and 'operand2') together and sets the value to the variable 'answer_variable'
#M;answer_variable;answer_variable;+;operand2; <- the variable set to the result of the operands can also be an operand
#M;answer_variable;operand1;(+/-/*///**);operand2; <- the operator can be either '+', '-', '*', '/', or '**'
#Also note that whilst the two operand variables have to have been initialised before the 'M'-line, the answer variable does not

#Go to Syntax:
#'G' for 'Go to'
#G;10; <- sets the line_counter variable to 10 thus executing the tenth line of code
#G;goto_variable; <- variables can also be used to specify the desired line number

#Conditional Syntax:
#'W' for 'When' as in 'When condition, then...'
#W;variable1;=;variable2;10; <- checks if variable1 is equal to variable2 and if it is, then it sets the line number to 10
#W;variable1;!;variable2;5; <- checks if variable1 is not equal to variable2 and if so, it then sets the line number to 5
#W;variable1;(=/!/</>);variable2;15; <- the logical operator can be either '=', '!', '<', or '>'
#W;variable_one;=;variable_two;goto_variable; <- the goto number can also be a variable

#String Concatenation Syntax:
#'C' for 'Concatenation'
#C;concatenated_string;V;variable_one;V;variable_two; <- concatenates the two variables, 'variable_one' and 'variable_two' together and sets the value to the variable 'concatenated_string'
#C;concatenated_string;S;Hello, ;S;World; <- non variable strings can also be concatenated
#C;concatenated_string;S;Hello, ;V;variable_world; <- non variable strings and variables can be concatenated, too

#Comment Syntax:
#-This is a comment <- comments are written on their own lines and all start with '-' to tell the interpreter to ignore them

#Time Syntax:
#'T' for 'Time'
#T;time_variable; <- assigns the variable 'time_variable' a string with the format dd/mm/yyyy xx:yy UTC+1

#Number <--> String Conversion Syntax:
#'B' for 'Become' as in 'Become a string' or 'Become a number'
#B;S;variable_in_question; <- changes the variable 'variable_in_question' from a number to a string
#B;N;variable_in_question; <- changes the variable 'variable_in_question' from a number to a number

#Splicing Syntax:
#'L' for 'spLicing'
#I;S;slice_that_variable;Hello, World!;
#L;slice_that_variable;0;5; <- sets the variable 'slice_that_variable' to equal only the characters from the start to, but not including, the fifth place
#P;V;slice_that_variable; <- prints 'Hello'

#Re-initialisation Syntax:
#'R' for 'Re-initialisation'
#R;copied_var;N;original_var; <- sets the variable 'copied_var' to have the same value as the variable 'original_var'
#R;copied_var;S;original_var; <- sets the variable 'copied_var' to have the same value as the string variable 'original_var'

#Sleeping Syntax:
#'S' for 'Sleep'
#S;10; <- that pauses (i.e. sleeps) the program for 10 seconds
#S;pause_time; <- variables can also be used to specify the desired pause length

#Ending Programs:
#the last line of any program should always be 'END'

import time

running = True
command = ""
code_list = [""] * 1000
load_list = [""] * 1000
directory_list = [""] * 1000

line_counter = 0
variable_dictionary = {}

def do_math(opand1, opand2, oper, ans_var): #Some guilty, bad quality code right here - I honestly don't know what to do here, though
    global variable_dictionary
    
    opand1_is_num = False
    opand2_is_num = False
    
    if opand1.isnumeric() == True:
        opand1 = int(opand1)
        opand1_is_num = True
            
    if opand2.isnumeric() == True:
        opand2 = int(opand2)
        opand2_is_num = True
        
    #10 What I've got here is essentially a 2-bit number
    #20 And the highest 2-bit number is 4, so that's a lot of repeating code...
    #30 Shut up.
    #40 When I can be arsed or it becomes a real problem - whichever comes first - then I'll fix it.
    #50 At the moment, though, G;30;
    
    if opand1_is_num == True and opand2_is_num == True:
        if oper == "+":
            variable_dictionary.update({ans_var: (opand1 + opand2)})
        elif oper == "-":
            variable_dictionary.update({ans_var: (opand1 - opand2)})
        elif oper == "*":
            variable_dictionary.update({ans_var: (opand1 * opand2)})
        elif oper == "/":
            variable_dictionary.update({ans_var: (opand1 / opand2)})
        elif oper == "**":
            variable_dictionary.update({ans_var: (opand1 ** opand2)})
    elif opand1_is_num == False and opand2_is_num == True:
        if oper == "+":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] + opand2)})
        elif oper == "-":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] - opand2)})
        elif oper == "*":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] * opand2)})
        elif oper == "/":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] / opand2)})
        elif oper == "**":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] ** opand2)})
    elif opand1_is_num == True and opand2_is_num == False:
        if oper == "+":
            variable_dictionary.update({ans_var: (opand1 + variable_dictionary[opand2])})
        elif oper == "-":
            variable_dictionary.update({ans_var: (opand1 - variable_dictionary[opand2])})
        elif oper == "*":
            variable_dictionary.update({ans_var: (opand1 * variable_dictionary[opand2])})
        elif oper == "/":
            variable_dictionary.update({ans_var: (opand1 / variable_dictionary[opand2])})
        elif oper == "**":
            variable_dictionary.update({ans_var: (opand1 ** variable_dictionary[opand2])})
    elif opand1_is_num == False and opand2_is_num == False:
        if oper == "+":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] + variable_dictionary[opand2])})
        elif oper == "-":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] - variable_dictionary[opand2])})
        elif oper == "*":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] * variable_dictionary[opand2])})
        elif oper == "/":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] / variable_dictionary[opand2])})
        elif oper == "**":
            variable_dictionary.update({ans_var: (variable_dictionary[opand1] ** variable_dictionary[opand2])})
            
def do_logic(log_oper1, log_oper2, log_opera):
    global variable_dictionary
            
    log_oper1_is_num = False
    log_oper2_is_num = False
            
    tot_bool = False
            
    if log_oper1.isnumeric() == True:
        log_oper1 = int(log_oper1)
        log_oper1_is_num = True
                
    if log_oper2.isnumeric() == True:
        log_oper2 = int(log_oper2)
        log_oper2_is_num = True
                
    if log_oper1_is_num == True and log_oper2_is_num == True:
        if log_opera == "=":
            if log_oper1 == log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "!":
            if log_oper1 != log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "<":
            if log_oper1 < log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == ">":
            if log_oper1 > log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
    elif log_oper1_is_num == True and log_oper2_is_num == False:
        if log_opera == "=":
            if log_oper1 == variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "!":
            if log_oper1 != variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "<":
            if log_oper1 < variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == ">":
            if log_oper1 > variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
    elif log_oper1_is_num == False and log_oper2_is_num == True:
        if log_opera == "=":
            if variable_dictionary[log_oper1] == log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "!":
            if variable_dictionary[log_oper1] != log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "<":
            if variable_dictionary[log_oper1] < log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == ">":
            if variable_dictionary[log_oper1] > log_oper2:
                tot_bool = True
            else:
                tot_bool = False
                        
    elif log_oper1_is_num == False and log_oper2_is_num == False:
        if log_opera == "=":
            if variable_dictionary[log_oper1] == variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "!":
            if variable_dictionary[log_oper1] != variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == "<":
            if variable_dictionary[log_oper1] < variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
        elif log_opera == ">":
            if variable_dictionary[log_oper1] > variable_dictionary[log_oper2]:
                tot_bool = True
            else:
                tot_bool = False
                        
    return tot_bool

def line_reader(line):
    global variable_dictionary
    global line_counter
    
    if line[0] == "P":
        line = line[2:]
        
        is_print_var = False
        
        if line[0] == "S":
            is_print_var = False
        elif line[0] == "V":
            is_print_var = True
            
        line = line[2:]
        
        print_contents = ""
        
        while line[0] != ";":
            print_contents = print_contents + line[0]
            line = line[1:]
            
        if is_print_var == False:
            print(print_contents)
        elif is_print_var == True:
            print(variable_dictionary[print_contents])
                
    elif line[0] == "U":
        line = line[2:]
        
        is_input_var_num = False
        
        if line[0] == "S":
            is_input_var_num = False
        elif line[0] == "N":
            is_input_var_num = True
            
        line = line[2:]
        
        input_variable = ""
        
        while line[0] != ";":
            input_variable = input_variable + line[0]
            line = line[1:]
            
        line = line[1:]
        
        input_prompt = ""
        
        while line[0] != ";":
            input_prompt = input_prompt + line[0]
            line = line[1:]
            
        line = line[1:]
        
        if is_input_var_num == True:
            variable_dictionary.update({input_variable: int(input(input_prompt))})
        elif is_input_var_num == False:
            variable_dictionary.update({input_variable: str(input(input_prompt))})
            
    elif line[0] == "I":
        line = line[2:]
        
        init_var_is_num = False
        
        if line[0] == "S":
            init_var_is_num = False
        elif line[0] == "N":
            init_var_is_num = True
            
        line = line[2:]
        
        init_var_name = ""
        
        while line[0] != ";":
            init_var_name = init_var_name + line[0]
            line = line[1:]
            
        line = line[1:]
            
        init_var_value = ""
        
        while line[0] != ";":
            init_var_value = init_var_value + line[0]
            line = line[1:]
            
        line = line[1:]
        
        if init_var_is_num == True:
            init_var_value = int(init_var_value)
        elif init_var_is_num == False:
            init_var_value = str(init_var_value)
            
        variable_dictionary.update({init_var_name: init_var_value})
        
    elif line[0] == "M":
        line = line[2:]
        
        answer_variable = ""
        
        while line[0] != ";":
            answer_variable = answer_variable + line[0]
            line = line[1:]
            
        line = line[1:]
        
        operand1_var = ""
        
        while line[0] != ";":
            operand1_var = operand1_var + line[0]
            line = line[1:]
            
        line = line[1:]                 #I like the movies 'Terminator' and 'Terminator 2'
                        
        operator = ""                   
        
        while line[0] != ";":
            operator = operator + line[0]
            line = line[1:]
            
        line = line[1:]
        
        operand2_var = ""
        
        while line[0] != ";":
            operand2_var = operand2_var + line[0]
            line = line[1:]
        
        line = line[1:]
        
        do_math(operand1_var, operand2_var, operator, answer_variable)
            
    elif line[0] == "G":
        line = line[2:]
        
        set_line = ""
        
        while line[0] != ";":
            set_line = set_line + line[0]
            line = line[1:]
            
        line = line[1:]

        set_line_actuall = 0

        if set_line.isnumeric() == True:
            set_line_actuall = int(set_line)
        else:
            set_line_actuall = variable_dictionary[set_line]
        
        line_counter = set_line_actuall - 2
        
    elif line[0] == "W":
        line = line[2:]
        
        logical_operand_1 = ""
        
        while line[0] != ";":
            logical_operand_1 = logical_operand_1 + line[0]
            line = line[1:]
        
        line = line[1:]
        
        logical_operator = ""
        
        while line[0] != ";":
            logical_operator = logical_operator + line[0]
            line = line[1:]
            
        line = line[1:]
        
        logical_operand_2 = ""
        
        while line[0] != ";":
            logical_operand_2 = logical_operand_2 + line[0]
            line = line[1:]
            
        line = line[1:]
        
        boolean_state = do_logic(logical_operand_1, logical_operand_2, logical_operator)
                
        goto_number = ""
        
        while line[0] != ";":
            goto_number = goto_number + line[0]
            line = line[1:]
            
        line = line[1:]

        goto_number_actuall = 0
        
        if goto_number.isnumeric() == True:
            goto_number_actuall = int(goto_number)
        else:
            goto_number_actuall = variable_dictionary[goto_number]
        
        if boolean_state == True:
            line_counter = goto_number_actuall - 2

    elif line[0] == "C":
        line = line[2:]

        concatenated_variable = ""

        while line[0] != ";":
            concatenated_variable = concatenated_variable + line[0]
            line = line[1:]

        line = line[1:]

        con1_is_var = False

        if line[0] == "V":
            con1_is_var = True
        else:
            con1_is_var = False

        line = line[2:]

        con1 = ""

        while line[0] != ";":
            con1 = con1 + line[0]
            line = line[1:]

        line = line[1:]

        con2_is_var = False

        if line[0] == "V":
            con2_is_var = True
        else:
            con2_is_var = False

        line = line[2:]

        con2 = ""

        while line[0] != ";":
            con2 = con2 + line[0]
            line = line[1:]

        line = line[1:]

        con1_placeholder = ""
        con2_placeholder = ""

        if con1_is_var == False:
            con1_placeholder = con1
        else:
            con1_placeholder = variable_dictionary[con1]

        if con2_is_var == False:
            con2_placeholder = con2
        else:
            con2_placeholder = variable_dictionary[con2]

        total_con = ""
        total_con = con1_placeholder + con2_placeholder
        
        variable_dictionary.update({concatenated_variable: total_con})

    elif line[0] == "T":
        line = line[2:]

        time_set_variable = ""

        while line[0] != ";":
            time_set_variable = time_set_variable + line[0]
            line = line[1:]
        
        line = line[1:]

        given_time = get_time()
        
        variable_dictionary.update({time_set_variable: given_time})

    elif line[0] == "B":
        #Number <--> String Conversion Syntax:
        #'B' for 'Become' as in 'Become a string' or 'Become a number'
        #B;S;variable_in_question; <- changes the variable 'variable_in_question' from a number to a string
        #B;N;variable_in_question; <- changes the variable 'variable_in_question' from a number to a number

        line = line[2:]
        
        convert_to_number = False

        if line[0] == "N":
            convert_to_number = True
        else:
            convert_to_number = False

        line = line[2:]

        variable_to_convert = ""

        while line[0] != ";":
            variable_to_convert = variable_to_convert + line[0]
            line = line[1:]

        line = line[1:]

        variable_value_to_convert = ""

        variable_value_to_convert = variable_dictionary[variable_to_convert]

        if convert_to_number == False:
            variable_value_to_convert = str(variable_value_to_convert)
        elif convert_to_number == True:
            variable_value_to_convert = int(variable_value_to_convert)

        variable_dictionary.update({variable_to_convert: variable_value_to_convert})

    elif line[0] == "L":
        #I;S;slice_that_variable;Hello, World!;
        #L;slice_that_variable;0;5; <- sets the variable 'slice_that_variable' to equal only the characters from the start to, but not including, the fifth place
        #P;V;slice_that_variable; <- prints 'Hello'

        line = line[2:]

        variable_to_slice = ""

        while line[0] != ";":
            variable_to_slice = variable_to_slice + line[0]
            line = line[1:]

        line = line[1:]
        
        starting_slice_pos = ""

        while line[0] != ";":
            starting_slice_pos = starting_slice_pos + line[0]
            line = line[1:]

        line = line[1:]

        ending_slice_pos = ""

        while line[0] != ";":
            ending_slice_pos = ending_slice_pos + line[0]
            line = line[1:]

        line = line[1:]

        starting_slice_pos = int(starting_slice_pos)
        ending_slice_pos = int(ending_slice_pos)

        if ending_slice_pos < starting_slice_pos:
            ending_slice_pos = -ending_slice_pos
        
        sliced_variable_value = variable_dictionary[variable_to_slice]

        variable_dictionary.update({variable_to_slice: sliced_variable_value[starting_slice_pos:ending_slice_pos]})

    elif line[0] == "R":
        #Initialising variables with the values of other variables?
        #R;copied_var;N;original_var; <- sets the variable 'copied_var' to have the same value as the number variable 'original_var'
        #R;copied_var;S;original_var; <- sets the variable 'copied_var' to have the same value as the string variable 'original_var'

        line = line[2:]

        copied_variable = ""

        while line[0] != ";":
            copied_variable = copied_variable + line[0]
            line = line[1:]

        line = line[1:]

        is_original_variable_a_number_question_mark = False #Yeah, yeah, yeah... but is it? Is the original variable a number? Life's deepest questions.

        if line[0] == "N":
            is_original_variable_a_number_question_mark = True
        else:
            is_original_variable_a_number_question_mark = False

        line = line[2:]

        original_variable = ""

        while line[0] != ";":
            original_variable = original_variable + line[0]
            line= line[1:]

        line = line[1:]

        original_variable_value = ""

        original_variable_value = variable_dictionary[original_variable]

        if is_original_variable_a_number_question_mark == True:
            original_variable_value = int(original_variable_value)
        elif is_original_variable_a_number_question_mark == False:
            original_variable_value = str(original_variable_value)

        variable_dictionary.update({copied_variable: original_variable_value})

    elif line[0] == "S":
        line = line[2:]

        sleeping_time = ""

        while line[0] != ";":
            sleeping_time = sleeping_time + line[0]
            line = line[1:]

        line = line[1:]

        sleeping_time_actuall = 0
        
        if sleeping_time.isnumeric() == True:
            sleeping_time_actuall = sleeping_time = int(sleeping_time)
        else:
            sleeping_time_actuall = variable_dictionary[sleeping_time]
        
        time.sleep(sleeping_time_actuall)
        
    elif line[0] == "-":
        pass
            
def find_end(list_of_things):
    counter = len(list_of_things) - 1
    while list_of_things[counter] != "END":
        if counter == 0:
            return True
        else:
            counter = counter - 1
    else:
        return False

def remove_whitespace(text):
    if text == "":
        pass
    elif text[0] == " ":
        text = text[1:]
    
    return text

def code_line_reader(code):
    global code_list
    
    current_line = 0
    line_number = ""
    
    while code[0].isnumeric() == True or code[0] == "0":
        line_number = line_number + code[0]
        current_line = current_line + 1
        code = code[1:]
        if len(code) < 1:
            current_line = current_line + 1
            code = code[1:]
            break
        
    code = remove_whitespace(code)
    #line_number = str(line_number)
    #print(int(line_number))
    if int(line_number) > 1000 or int(line_number) < 0:
        print("line number (" + str(line_number) + ") out of range")
    elif code == "":
        code_list[int(line_number) - 1] = ""
    else:
        code_list[int(line_number) - 1] = code
            
def list_code(array_of_code):
    for loop in range(len(array_of_code)):
        if array_of_code[loop] == "":
            pass
        else:
            print(loop + 1, array_of_code[loop])
            
def clear_code(big_ol_array):
    for loop in range(len(big_ol_array)):
        if big_ol_array[loop] == "":
            pass
        else:
            big_ol_array[loop] = ""

def append_directory(intended_name):
    directory = open("compiler_directory.txt", "r")
    found = False
    
    while found == False:
        test_variable = (directory.readline())[:-1]
        if test_variable == intended_name:
            found = True
            directory.close()
        elif test_variable == "":
            break
    
    if found == False:
        directory = open("compiler_directory.txt", "a")
        directory.write(intended_name + "\n")
        directory.close()

def save_code(script, fname):
    file = open(fname, "w")
    
    for loop in range(len(script)):
        if script[loop] == "":
            pass
        else:
            file.write(str(loop + 1) + " " + script[loop] + "\n")
            
    file.close()
    
    append_directory(fname)
    
    print("file successflly saved")

def unpack_numbers():
    global code_list
    
    code_line_reader = 0
    
    for loop in range(len(code_list)):
        if (code_list[loop])[0].isnumeric() == True:
            code_list[loop] = (code_list[loop])[1:-1] 

def load_code(name_of_file):
    global code_list
    
    try:
        file = open(name_of_file, "r")
        
        for loop in range(len(code_list)):
            if code_list[loop] == "":
                pass
            else:
                code_list[loop] = ""
                
        load_list = file.readlines()
        file.close()
        
        for loop in range(len(code_list)):
            if code_list[loop] == "":
                pass
            else:
                code_list[loop] = ""
        
        for loop in range(len(load_list)):
            load_list[loop] = (load_list[loop])[:-1]
        
        for loop in range(len(load_list)):
            code_line_reader(load_list[loop])
        
        print("file successfully read to compiler")
    except:
        print("file '" + name_of_file + "' does not exist")
        
def directory_reader():
    global directory_list
    
    directory = open("compiler_directory.txt", "r")
    
    for loop in range(len(directory_list)):
        if directory_list[loop] == "":
            pass
        else:
            directory_list[loop] = ""
    
    directory_list = directory.readlines()
    directory.close()
    
    for loop in range(len(directory_list)):
        directory_list[loop] = (directory_list[loop])[:-1]
            
    print("file directory:")
    
    for loop in range(len(directory_list)):
        print(str(loop + 1) + ". " + directory_list[loop])
        
def get_time():
    current_time = time.time()

    def is_leap_year(year):
        if year % 100 == 0 and year % 400 == 0:
            #print(year, "is a leap year")
            return "Y"
        elif year % 100 == 0:
            #print(year, "is not a leap year")
            return "N"
        elif year % 4 == 0:
            #print(year, "is a leap year")
            return "Y"
        elif year % 4 != 0:
            #print(year, "is not a leap year")
            return "N"
    
    plus_days = current_time / 86400
    year_counter = 1970

    current_day_time = plus_days - int(float(plus_days))
    current_day_time_hours = (current_day_time * 24) + 1
    current_day_time_minutes = (current_day_time_hours - int(current_day_time_hours)) * 60

    plus_days = int(float(plus_days))

    #print("There are", plus_days, "days since 1970")

    while plus_days > 364:    
        if is_leap_year(year_counter + 1) == "N":
            year_counter += 1
            plus_days -= 365
        elif is_leap_year(year_counter + 1) == "Y":
            year_counter += 1
            plus_days -= 366
    
    def day_and_month_getter(days_n_stuff, leapy):
        month_counter = 0
        if leapy == "N":
            while days_n_stuff > 28:
                if month_counter == 0:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 1:
                    days_n_stuff -= 28
                    month_counter += 1
                elif month_counter == 2:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 3:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 4:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 5:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 6:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 7:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 8:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 9:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 10:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 11:
                    days_n_stuff -= 31
                    month_counter += 1
            
            return (days_n_stuff + 1), month_counter
    
        elif leapy == "Y":
            while days_n_stuff > 28:
                if month_counter == 0:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 1:
                    days_n_stuff -= 29
                    month_counter += 1
                elif month_counter == 2:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 3:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 4:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 5:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 6:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 7:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 8:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 9:
                    days_n_stuff -= 31
                    month_counter += 1
                elif month_counter == 10:
                    days_n_stuff -= 30
                    month_counter += 1
                elif month_counter == 11:
                    days_n_stuff -= 31
                    month_counter += 1
            
            return (days_n_stuff + 1), month_counter

        
    d, m = day_and_month_getter(plus_days, is_leap_year(year_counter))

    #print("Days:", d)
    #print("Months:", m)
    
    def date_constructor(years, months, days, hours, minutes):
        if hours == 24:
            hours = 0
            days += 1
    
        final_date = ""
    
        if days < 10:
            final_date += "0"
            final_date += str(days)
        else:
            final_date += str(days)
        
        final_date += "/"
        
        if months < 10:
            final_date += "0"
            final_date += str(months + 1)
        else:
            final_date += str(months + 1)
        
        final_date += "/"
    
        final_date += str(years)
        
        final_date += " "
    
        if hours < 10:
            final_date += "0"
            final_date += str(hours)
        else:
            final_date += str(hours)
        
        final_date += ":"
    
        if minutes < 10:
            final_date += "0"
            final_date += str(minutes)
        else:
            final_date += str(minutes)
        
        return final_date

    #print(date_constructor(year_counter, m, d, int(current_day_time_hours), int(current_day_time_minutes)) + " UTC+1")#, int(current_day_time_hours), int(current_day_time_minutes)

    return (date_constructor(year_counter, m, d, int(current_day_time_hours), int(current_day_time_minutes)) + " UTC+1")
    
def spec_list(start, stop, array_of_code):
    for loop in range((start - 1), stop):
        if array_of_code[loop] == "":
            pass
        else:
            print(loop + 1, array_of_code[loop])

def renum(): #This took embarrassingly long to write
    global code_list

    code_instance = 0

    for loop in range(len(code_list)):
        if code_list[loop] != "":
            code_instance = code_instance + 1

    #print("non empty code_list instances:", code_instance)

    if code_instance >= 1000:
        print("too many lines of code for renum")
    else:
        temp_list = code_list
        code_list = [""] * 1000
        renumbered_line_number = 9

        #print(code_list)
    
        for loop in range(len(temp_list)):
            if temp_list[loop] != "":
                #print(temp_list[loop] + " -> " + str(renumbered_line_number + 1))
                code_list[renumbered_line_number] = temp_list[loop]
                renumbered_line_number = renumbered_line_number + 10

        temp_list = [""]
        

#print("""Minecraft Computer Assembly Language Compiler Example (MCALCE)
#Copyright (c) Alexico Software Corporation, 2025 - All rights reserved
#Enter 'help' for command list
#""")
        
print("""Single-letter Interpreted Machine Programming Language (SIMPL) Interpreter and Prompt
Copyright (c) 2025, Alexander Peat - All rights reserved
SIMPL Type 2
""")

while running == True:
    command = ""
    
    try:
        command = str(input(">"))
    except KeyboardInterrupt:
        print("escape")
    except:
        print("mistake")
    
    if command == "help" or command == "HELP":
        print("""command list:
1. 'help' - prints command list
2. 'helpcode' - prints guide on code formatting
3. 'list' - lists inputted code
4. 'renum' - renumbers every line of code in intervals of ten
5. 'speclist' - lists inputted code with line numbers in the specified range
6. 'run' - runs inputted code
7. 'debug' - prints all the stored variables and lines of code in the interpreter
8. 'clear' - clears all lines of code
9. 'save' - saves current code to specified file ------- note: both the 'save' and 'load' commands may not work
10. 'load' - loads code to compiler --------------------- due to differences in file organisation; be careful
11. 'dir' - prints a directory to all the saved files
12. 'time' - prints out the time in UTC+1 to the terminal
13. 'exit' - exits compiler""")
        
    elif command == "helpcode" or command == "HELPCODE":
        print("""code formatting guide:
1. always start code line with its line number, a space, and then the actuall code itself
2. to delete a line in the code, rewrite its line number along with the space specified in rule (1) and then enter nothing
3. to review already written code, enter 'list' and the code will be printed out
4. to run the code, enter 'run'
5. this compiler supports up to 1,000 lines of code""")
        
    elif command == "exit" or command == "EXIT":
        print("exiting interpreter")
        #print(code_list)
        running = False

    elif command == "terminate" or command == "TERMINATE":
        print("i'll be back")
        running = False
    
    elif command == "list" or command == "LIST":
        list_code(code_list)
    
    elif command == "run" or command == "RUN":
        variable_dictionary = {}
        line_counter = 0
        
        if find_end(code_list) == True:
            print("missing 'END' at end of program");
        else:
            while True:
                if code_list[line_counter] == "END":
                    break
                elif code_list[line_counter] == "":
                    line_counter = line_counter + 1
                else:
                    try:
                        line_reader(code_list[line_counter])
                        line_counter = line_counter + 1
                    except KeyboardInterrupt:
                        print("escape at line " + str(line_counter + 1))
                        break
                    except:
                        print("error at line " + str(line_counter + 1))
                        #print(error)
                        break
   
    elif command == "clear" or command == "CLEAR":
        clear_code(code_list)
        
    elif command == "save" or command == "SAVE":
        print("note: always succeed file names with '.txt'")
        save_filename = str(input("enter filename to save code as: "))
        save_code(code_list, save_filename)
        
    elif command == "load" or command == "LOAD":
        print("warning: opening a file will overwrite code currently in compiler")
        print("note: end file querys with '.txt'")
        load_filename = str(input("enter the name of the file to open: "))
        load_code(load_filename)
        
    elif command == "dir" or command == "DIR":
        try:
            directory_reader()
        except:
            print("directory file not found")
        
    elif command == "time" or command == "TIME":
        print(get_time())
        
    elif command == "speclist" or command == "SPECLIST":
        low_range = int(input("input the low line number "))
        high_range = int(input("input the high line number "))
        
        spec_list(low_range, high_range, code_list)
        
    elif command == "debug" or command == "DEBUG":
        print("---interpreter information---")
        print("code_list contents:")
        print(code_list)
        print("variable_dictionary contents:")
        print(variable_dictionary)
        print("line counter:")
        print(line_counter)

    elif command == "renum" or command == "RENUM":
        renum()
        
    elif command == "hey mate" or command == "HEY MATE":
        print("bro im just a computer you cant talk to me")
        
    elif command == "":
        pass
    
    else:
        if command[0].isnumeric() == False:
            print("entered command '" + command + "' unrecognised")
        else:
            code_line_reader(command)
