#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

def import_data(file_path):
    with open(file_path,mode='r') as f:
        file_content = f.readlines()
    return file_content

def import_names_to_list(names_file_path):
    names_list = []
    content = import_data(names_file_path)

    for line in content:
        names_list.append(line.rstrip())

    return names_list

def personalise_letter(names_file_path,letter_file_path,desired_output_path):
    list_of_names = import_names_to_list(names_file_path)
    letter_content = import_data(letter_file_path)

    for name in list_of_names:
        temp_letter = letter_content.copy()
        first_line = temp_letter[0]
        personalised_first_line = first_line.replace("[name]",name)

        with open(desired_output_path+"/letter_for_"+name+".txt", mode="w") as f:
            f.write(personalised_first_line)
            for line in temp_letter[1::]:
                f.write(line)


personalise_letter("100-dni-z-pythonem/dzien 24/Mail Merge Project Start/Input/Names/invited_names.txt","100-dni-z-pythonem/dzien 24/Mail Merge Project Start/Input/Letters/starting_letter.txt","100-dni-z-pythonem/dzien 24/Mail Merge Project Start/Output/ReadyToSend")


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp