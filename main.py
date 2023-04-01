from graphProduction import *

"""

Menu to easily display all availble graphs from Graph Production file

"""

MENU_IS_RUNNING = True
NUM_OPTIONS = 12


while MENU_IS_RUNNING:

    print("Graph Selection Menu:\n")

    # Option Menu in Terminal given to user
    print(
        " [1]: Religious Groups within the Far Left Respondent Group\n",
        "[2]: The prior knowledge of ChatGPT's existence within the Far Left Respondent Group\n",
        "[3]: Far Left respondent group's opinion on if the use of ChatGPT for Student Written Works is plagiarism \n",
        "[4]: Far Right respondent group's opinion on if the use of ChatGPT for Student Written Works is plagiarism\n",
        "[5]: Far Left respondent group's opinion on if the use of ChatGPT for Research Purposes is plagiarism\n",
        "[6]: Far Right respondent group's opinion on if the use of ChatGPT for Research Purposes is plagiarism\n",
        "[7]: The opinion of Gender Groups on if the use of ChatGPT is ethical in the Workplace or for Commercial Use\n",
        "[8]: Undergraduate Population who believed ChatGPT inhibited their growth but believe it is not unethical\n      to use for essays is highlighted versus the rest of the population \n",
        "[9]: opinions of Faculty and Post-Graduate Students on whether or not ChatGPT is ethical for use in Student Written Works \n",
        "[10]: A general opinion of each Academia group's opinion on ChatGPT's usage in various settings\n",
        "[11]: Academia's group responses to if ChatGPT is unethical for Student Written Works all compared on a bar graph\n",
        "[12]: Quit Menu\n"
    )

    user_input = 0
    waiting_valid_user_input = True

    # While loop to test that the user inputs a valid selection 
    while waiting_valid_user_input:
        try:
            user_input = int(input("Please Select a Graph by its Number: "))

            if (user_input == 0 or user_input > NUM_OPTIONS):
                raise ValueError()

            waiting_valid_user_input = not waiting_valid_user_input

        except ValueError:
            print("Please input a valid integer")
        
    match user_input:
        case 1:
            far_leftist_religions_bar_graph()
        case 2: 
            far_leftist_awareness_of_chatgpt()
        case 3:
            far_left_chatGPT_essay_plagiarism()
        case 4:
            far_right_chatGPT_essay_plagiarism()
        case 5:
            political_far_left_chatGPT_research()
        case 6:
            political_far_right_chatGPT_research()
        case 7:
            gender_chatGPT_commercial_use()
        case 8:
            undergraduate_instant_gratification_study()
        case 9:
            upper_academia_plagarism()
        case 10:
            academia_levels_on_chatgpt_usage()
        case 11:
            academia_groups_on_essay_prompt()
        case 12:
            MENU_IS_RUNNING = not MENU_IS_RUNNING
            print("Menu Closing")
    

    


  

   
