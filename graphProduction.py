# Names: Kyle Teopiz, Alan Pangnathip, Joseph Carvalho, Hameez Iqbal
# Date: Wednesday, March 1, 2023

import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
from matplotlib.lines import Line2D


RESPONSE_LABEL_INDEX = 0

# Used to slice the list which has all the rows of the CSV File
# It slices out the first row which is a list of strings of the prompts given to the respondents
# Slice this row for easier data filtering
FIRST_RESPONDENT_ROW_INDEX = 1

# Many lists exist containing counts of "Yes" and "No" Instances
# Constants for where they are always placed
YES_RESPONSE_INDEX = 0
NO_RESPONSE_INDEX = 1

# Politcal Spectrum Value Constants
FAR_LEFTIST_RESPONSE_VALUE  = 1
FAR_RIGHT_RESPONSE_VALUE = 5

YES_NO_COLORS = ['green', 'red']

"""

TO DO: FIGURE OUT WHAT UR RETURNING, RN ITS JUST DISPLAY CLOSED

"""

QUESTION_ACCESSOR = {
    "age_range" : 1,
    "gender" : 2,
    "academia_status": 3,
    "location": 4,
    "political_spectrum": 5,
    "religion": 6,
    "heard_of_chatGPT": 7,
    "have_used_chatGPT": 8,
    "plagiarism_for_essays_prompt": 9,
    "use_for_research_prompt": 10,
    "use_commercially_prompt": 11,
    "effect_on_student_learning": 12,
    "instructor_use": 13,
    "personal_use": 14
}

def far_leftist_religions_bar_graph():
    """

    A pie graph representing the diverse religions within the Far Leftist respondents group 

    """

    RELIGION_NAME_INDEX = 0
    FOLLOWER_COUNT_INDEX = 1

    religious_group_counter = Counter()
    religions = []
    num_followers = []

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:

        # Slice the data list at row one to exclude the row of questions which has no respondent data
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]
        for row in data_accessor:

            # Filters the Political Spectrum column to only count Far Leftist Respondents 
            if int(row[(QUESTION_ACCESSOR["political_spectrum"])]) == FAR_LEFTIST_RESPONSE_VALUE:

                # Populates a Counter obkect which counts the instances of each religion
                religious_group_counter[row[QUESTION_ACCESSOR["religion"]]] += 1
        
        # Iterates through the Counter object to seperate the religions and their population counts into other lists
        # Seperated for assignment to their respective axes later
        for religion in religious_group_counter.most_common():
            religions.append(religion[RELIGION_NAME_INDEX])
            num_followers.append(religion[FOLLOWER_COUNT_INDEX])

    plt.bar(religions, num_followers, edgecolor='black')
    plt.xlabel("Religions")
    plt.ylabel("Number of Followers")
    plt.title("Religious Group Populations of the Far Leftist Repondents")

    plt.show()

    return "Display Closed"

def far_leftist_awareness_of_chatgpt():

    """
    
    A pie graph displaying the prior awareness of the Far Leftist respondent group of the existence of ChatGPT 
    
    """

    COUNTED_VALUES_INDEX= 1
    
    

    yes_no_counter = Counter()
    yes_no_labels = ["Knew of ChatGPT Prior", "Did not Know of ChatGPT Prior"]
    yes_no_results = []

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]

        for row in data_accessor:
            
            # Filters the Political Spectrum column to only count Far Leftist Respondents  
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == FAR_LEFTIST_RESPONSE_VALUE:

                # Populates a Counter of the Yes and No instances in the Far Leftist Group
                yes_no_counter[row[QUESTION_ACCESSOR["heard_of_chatGPT"]]] += 1
        
        # Populate the Result list with the results of "yes" and "no" instances from the Counter
        for count in yes_no_counter.most_common():
            yes_no_results.append(count[COUNTED_VALUES_INDEX])

    explode = (0, 0.2)
    fig, ax = plt.subplots()
    ax.pie(yes_no_results, explode=explode, colors=YES_NO_COLORS, labels=yes_no_labels, autopct='%1.1f%%', shadow= True)
    plt.title("Far Leftist Respondent Gtroup's Knowledge of ChatGPT Existence prior to Survey")
    plt.legend()
    plt.axis('equal')
    plt.show()

    return "Display Closed"
        


def far_left_chatGPT_essay_plagiarism():

    """
    
    A pie graph displaying the Far Left respondent group's opinion on if 
    the use of ChatGPT for Student Written Works is plagiarism
    
    """

    answer_labels = ["Yes, ChatGPT is Plagiarism" , "No, ChatGPT is not Plagiarism"]

    # "Yes" Instance Index = 0
    # "No" Instance index = 1
    far_left_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]
    
        for row in data_accessor:
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == FAR_LEFTIST_RESPONSE_VALUE:

                # Counts the yes and no instances in the Far Leftist Group
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    far_left_results[YES_RESPONSE_INDEX] += 1
                else:
                    far_left_results[NO_RESPONSE_INDEX] += 1
    
    fig, ax = plt.subplots()
    ax.pie(far_left_results, labels=answer_labels, autopct='%1.1f%%', colors=YES_NO_COLORS)
    plt.title("Far Left's Opinion on ChatGPT being Plagiarism when used in Student Written Works")
    plt.axis('equal')
    plt.legend()
    plt.show()

    return "Display Closed"

def far_right_chatGPT_essay_plagiarism():

    """
    
    A pie graph displaying the Far Right respondent group's opinion on if 
    the use of ChatGPT for Student Written Works is plagiarism
    
    """

    answer_labels = ["Yes" , "No"]

    # "Yes" Instance Index = 0
    # "No" Instance index = 1
    far_right_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]
    
    
        for row in data_accessor:

            # Counts the yes and no instances in the Far Right Group
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == FAR_RIGHT_RESPONSE_VALUE:
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    far_right_results[YES_RESPONSE_INDEX] += 1
                else:
                    far_right_results[NO_RESPONSE_INDEX] += 1
   
    fig, ax = plt.subplots()
    ax.pie(far_right_results, labels=answer_labels, autopct='%1.1f%%' , colors=YES_NO_COLORS)
    plt.title("Far Right's Opinion on ChatGPT being Plagiarism when used in Student Written Works")
    plt.axis('equal')
    plt.legend()
    plt.show()

def political_far_left_chatGPT_research():

    """
    
    A pie graph displaying the Far Left respondent group's opinion on if 
    the use of ChatGPT for Research Purposes is plagiarism
    
    """

    answer_labels = ["Yes" , "No"]

    # "Yes" Instance Index = 0
    # "No" Instance index = 1
    far_left_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]
    
        # Counts the yes and no instances in the Far Leftist Group
        for row in data_accessor:
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == FAR_LEFTIST_RESPONSE_VALUE:
                if row[QUESTION_ACCESSOR["use_for_research_prompt"]] == "Yes":
                    far_left_results[YES_RESPONSE_INDEX] += 1
                else:
                    far_left_results[NO_RESPONSE_INDEX] += 1

    fig, ax = plt.subplots()
    ax.pie(far_left_results, labels=answer_labels, autopct='%1.1f%%', colors=YES_NO_COLORS, startangle=45)
    plt.title("Far Left's Opinion on ChatGPT being Ethical for Research Purposes")
    plt.axis('equal')
    plt.legend()
    plt.show()


    return "Display Closed"

def political_far_right_chatGPT_research():


    """
    
    A pie graph displaying the Far Right respondent group's opinion on if 
    the use of ChatGPT for Research Purposes is plagiarism
    
    """

    answer_labels = ["Yes" , "No"]

    # "Yes" Instance Index = 0
    # "No" Instance index = 1
    far_right_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]

        for row in data_accessor:
            
             # Counts the yes and no instances in the Far Right Group
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == 5:
                if row[QUESTION_ACCESSOR["use_for_research_prompt"]] == "Yes":
                    far_right_results[YES_RESPONSE_INDEX] += 1
                else:
                    far_right_results[NO_RESPONSE_INDEX] += 1

    fig, ax = plt.subplots()
    ax.pie(far_right_results, labels = answer_labels, autopct='%1.1f%%', colors=YES_NO_COLORS)
    plt.title("Far Right's Opinion on ChatGPT being Ethical for Research Purposes")
    plt.axis('equal')
    plt.legend()
    plt.show()


def gender_chatGPT_commercial_use():

    """ 
    
    Figure: A double bar graph representing each gender group's [Males, Females, and Others], 
    answer on whether ChatGPT is ethical for use commerically / in workplace
    
    """
    gender_xaxis_labels = ["Males", "Females", "Other"]

    # Integers helping with formatting the double bar graph
    x_axis_position  = np.arange(len(gender_xaxis_labels))
    bar_offset = 0.25
    multiplier = 0
    
    # Counters will count the "Yes" and "No" Instances for each Gender Group
    male_reponses_counter = Counter()
    female_responses_counter = Counter()
    other_responses_counter = Counter()

    # Lists will hold the results of the counters
    male_yes_no_responses = []
    female_yes_no_repsonses = []
    other_yes_no_responses = []
    
    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]

        for row in data_accessor:

            # Checks for the Gender Group and populates the correct Counter for their response
            if row[QUESTION_ACCESSOR["gender"]] == "Male":
                male_reponses_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1
            elif row[QUESTION_ACCESSOR["gender"]] == "Female":
                female_responses_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1
            else:
                other_responses_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1

    # Sorting each counter to ensure that they are in "Yes" then "No" Order, standardizing the data
    # can perhaps optimize to a range to generalize into an algorithm.. ill think about it

    yes_or_no_index_in_counter = 1

    male_reponses_counter = sorted(male_reponses_counter.most_common(), reverse= True)
    for item in male_reponses_counter:
        male_yes_no_responses.append(item[yes_or_no_index_in_counter])
    
    female_responses_counter = sorted(female_responses_counter.most_common(), reverse= True)
    for item in female_responses_counter:
        female_yes_no_repsonses.append(item[yes_or_no_index_in_counter])
    
    other_responses_counter = sorted(other_responses_counter.most_common(), reverse= True)
    for item in other_responses_counter:
        other_yes_no_responses.append(item[yes_or_no_index_in_counter])
    
    dict_data = {

         # FORMAT: key = answer to questions : value [<males value> , <females value>, <otheres value>]
        "Yes" : [male_yes_no_responses[YES_RESPONSE_INDEX], female_yes_no_repsonses[YES_RESPONSE_INDEX], other_yes_no_responses[YES_RESPONSE_INDEX]],
        'No': [male_yes_no_responses[NO_RESPONSE_INDEX], female_yes_no_repsonses[NO_RESPONSE_INDEX], other_yes_no_responses[NO_RESPONSE_INDEX]]
       
    }

    fig ,ax =  plt.subplots()
    
    # Sets the attributes of the bars for placement using Format Helpers above
    for attribute, measurement in dict_data.items():

        # Ensures the bars are set to the correct colour
        # The even iterations are Yes bars and are greem
        # The odd iteratopms are the No bars and are red
        current_bar_colour = ""
        if multiplier % 2 == 0:
            current_bar_colour = 'green'
        else:
            current_bar_colour = 'red'

        shift = bar_offset * multiplier
        rects = ax.bar(x_axis_position + shift, measurement, bar_offset, label = attribute, color=current_bar_colour, edgecolor='black')
        ax.bar_label(rects, padding=3)
        multiplier += 1
    
    ax.set_ylabel('Number of People')
    ax.set_title('If ChatGPT is Ethical for Use in the Workplace by Gender Groups')
    ax.set_xticks(x_axis_position + bar_offset, gender_xaxis_labels)
    ax.legend(loc='upper right', ncols=3)  

    plt.show()

    return "Display Closed"




def undergraduate_instant_gratification_study():
    
    """
    
    Pie Graph displaying the Undergraduate Population who believed ChatGPT inhibited their growth but believe it is not unethical
    to use for essays is highlighted versus the rest of the population

    Contradictory Student Group Criteria:
    1) Answered "No" to the prompt of ChatGPT being unethical for Student Written Works
    2) Answered from 1-3 (Highly Negative to Neutral) for the effect on student development prompt

    
    """

    CONTRADICTORY_GROUP_INDEX = 0
    REST_OF_POPULATION_INDEX = 1

    HIGHLY_NEGATIVE_RESPONSE = 1
    SLIGHTLY_NEGATIVE_REPSONSE = 2
    NEUTRAL_RESPONSE = 3

    # Holds the contradictory group versus all other combinations of answering the two questions
    contradiction_to_other_counts = [0,0]

    population_labels = [ "Contradictory Students", "Rest of Population"]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]

        for row in data_accessor:
            # Undergraduate Students can be identified by a substring of the response 'Student' used to find undergraduate respondents
            if row[QUESTION_ACCESSOR["academia_status"]].__contains__('Student') == True:
                if (int(row[QUESTION_ACCESSOR["effect_on_student_learning"]]) == HIGHLY_NEGATIVE_RESPONSE or int(row[QUESTION_ACCESSOR["effect_on_student_learning"]]) == SLIGHTLY_NEGATIVE_REPSONSE or int(row[QUESTION_ACCESSOR["effect_on_student_learning"]]) == NEUTRAL_RESPONSE) and row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "No":
                    contradiction_to_other_counts[CONTRADICTORY_GROUP_INDEX] += 1
                else:
                    contradiction_to_other_counts[REST_OF_POPULATION_INDEX] += 1
    
    explode = (0, 0.1)
    fig, ax = plt.subplots()
    ax.pie(contradiction_to_other_counts, explode=explode, labels=population_labels, autopct='%1.1f%%', shadow= True)
    plt.legend()
    plt.title("Contradictory Undergraduate Students who Believe ChatGPT inhibhits Student Development and is still Ethical for Essay Writing vs. the Rest of Undergraduates")
    plt.axis('equal')
    plt.show()

    return "Display Closed"


def upper_academia_plagarism():

    """

    Pie Graph displaying the opinions of Faculty and Post-Graduate Students on whether or not
    ChatGPT is ethical for use in Student Written Works

    """

    upper_academia_labels = ["Yes", "No"]
    upper_academia_counts = [0,0]
    
    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]

        for row in data_accessor:

            # Checks for all non-undergraduate students whose titles do not contain the substring "Student"
            if (row[QUESTION_ACCESSOR["academia_status"]].__contains__("Student")) == False:
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    upper_academia_counts[YES_RESPONSE_INDEX] += 1
                else:
                    upper_academia_counts[NO_RESPONSE_INDEX] += 1
    
    explode = (0.1, 0)
    fig, ax = plt.subplots()
    ax.pie(upper_academia_counts, explode= explode, labels=upper_academia_labels, autopct='%1.1f%%', shadow=True)
    plt.legend()
    plt.title("The Opinions of Faculty and Post-Undergraduate Students on if ChatGPT is Plagiarism for Writing Essays")
    plt.show()
    

                

        


def academia_levels_on_chatgpt_usage():

    """
    
    A scatter plot graph displaying a general opinion of each Academia group's opinion on ChatGPT's usage by comparing the amount of
    "Yes" responses versus "No" responses to several prompts

    Three Academia groups have been created: Undergraduates, Post-Graduates, and Faculty and Staff

    Three Prompts of Yes/No answer format are used to decide on the opinon of these groups which are:
    1) If ChatGPT is unethical for use in Student Written Works
    2) If ChatGPT is unethical for use in Research
    3) If ChatGPT is unethical in the workplace or in any commerical setting

    """
   
    # tracking three questions, all binary
    # 1) Yes/No to essay promots
    # 2) Yes/No in a Research Setting
    # 3) Yes/No for commerical/monetary purposes

    # group masters students, PhD Students, and Post-Doctoral Fellows together as the post_grad group
    # group part time and full time undergraduate students as  the undergrad group
    # group faculty, professors, and TA's as the staff group

    undergrad_counter = Counter()
    post_grad_counter = Counter()
    staff_counter = Counter()

    PERCENTAGE_INDEX = 1

    yes_results = []
    no_results = []
    
    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]

        for row in data_accessor:

            # Populate the groups respective counters with their responses to each of the binary questions
            if row[QUESTION_ACCESSOR["academia_status"]].__contains__("Student"):
                undergrad_counter[row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]]] += 1
                undergrad_counter[row[QUESTION_ACCESSOR["use_for_research_prompt"]]] += 1
                undergrad_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1
            
            elif row[QUESTION_ACCESSOR["academia_status"]] == "PhD" or row[QUESTION_ACCESSOR["academia_status"]] == "Post-Doctoral Fellow" or row[QUESTION_ACCESSOR["academia_status"]] == "Master's Degree":
                post_grad_counter[row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]]] += 1
                post_grad_counter[row[QUESTION_ACCESSOR["use_for_research_prompt"]]] += 1
                post_grad_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1
            
            else:
                staff_counter[row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]]] += 1
                staff_counter[row[QUESTION_ACCESSOR["use_for_research_prompt"]]] += 1
                staff_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1

    # Changing the Counter objects to lists 
    undergrad_results = undergrad_counter.most_common()
    post_grad_results = post_grad_counter.most_common()
    staff_results = staff_counter.most_common()

    # Keeping track of the total number of responses from each group to calculate the percentage of Yes and No responses taken
    undergrad_population = undergrad_counter.total()
    post_grad_population = post_grad_counter.total()
    staff_population = staff_counter.total()

    # Populating temporary lists to manipulate the data 
    temp_for_processing = [undergrad_results, post_grad_results, staff_results]
    temp_populations = [undergrad_population, post_grad_population, staff_population]

    print(temp_for_processing)
    
    for i in range(len(temp_for_processing)): 

        # Sort the Counters to place them in Yes-No Order
        temp_for_processing[i] = sorted(temp_for_processing[i], reverse= True)

        # Convert the number of Yes and No responses to be graphed later
        for j in range(len(temp_for_processing[i])):
            temp_for_processing[i][j] = list(temp_for_processing[i][j]) # change from tuple to list so the elements can be changed
            temp_for_processing[i][j][1] = round(temp_for_processing[i][j][1] / temp_populations[i] * 100, 2)

            # The "Yes" Counts occurs at the even index of the results lists, the "Np" Counts at the odd index of the results lists
            if j % 2 == 0:
                yes_results.append(temp_for_processing[i][j][PERCENTAGE_INDEX])
            else:
                no_results.append(temp_for_processing[i][j][PERCENTAGE_INDEX])
        
    colours = ["green", "cyan", "blue"]
    print(yes_results, no_results)
    # Creating a legend to differntiate the data points
    legend_elements = [ Line2D([0],[0], marker='o',color="green", label='Undergraduate Result'),
                        Line2D([0], [0], marker='o', color="cyan",label="Post-Graduate Result"),
                        Line2D([0], [0], marker='o',color="blue",label="Staff Result")   
                       ]


    fig, ax = plt.subplots()
    ax.legend(handles=legend_elements, loc='upper right')
    plt.scatter(yes_results, no_results, c=colours)
    plt.title("General Opinion of Academia Groups on if ChatGPT is Ethical in Various Settings")
    plt.xlabel("Percentage of Academia Group which said 'Yes'")
    plt.ylabel("Percentage of Academia Group which said 'No'")



    plt.show()
    
    
    return "Display Closed"


def groups_for_plag(): 

    """
    
    A display of three pie charts which show each Academia's group responses to if ChatGPT is unethical for Student Writtem Works
    along with a bar graph which compares these percentages
    
    """
      
    # Indexes of the lists which will hold the repsonses of each group and their total population
    YES_COUNT_INDEX = 0
    NO_COUNT_INDEX = 1
    TOTAL_POPULATION_COUNT_INDEX = 2

    undergrad_counts = [0,0,0]
    post_grad_counts = [0,0,0]
    staff_counts = [0,0,0]
    all_population_percentages =[0,0,0]

    population_labels = ["Undergraduate", "Post-Graduate", "Faculty"]
    pie_chart_labels = ['Yes', 'No']
    pie_chart_colors = ['green', 'red']



    # percentages for groups on whether or not they think chatGPT is plagarism for essay writing

    # "Percent of Population of each Group who think ChatGPT is plargarism for Essay Writing"
    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[FIRST_RESPONDENT_ROW_INDEX:]

        for row in data_accessor:

            # Populates counter lists for each Academia Group
            if row[QUESTION_ACCESSOR["academia_status"]].__contains__("Student"):
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    undergrad_counts[YES_COUNT_INDEX] += 1
                    undergrad_counts[TOTAL_POPULATION_COUNT_INDEX] += 1
                else:
                    undergrad_counts[NO_COUNT_INDEX] += 1
                    undergrad_counts[TOTAL_POPULATION_COUNT_INDEX] += 1

            elif row[QUESTION_ACCESSOR["academia_status"]] == "PhD" or row[QUESTION_ACCESSOR["academia_status"]] == "Post-Doctoral Fellow" or row[QUESTION_ACCESSOR["academia_status"]] == "Master's Degree":
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    post_grad_counts[YES_COUNT_INDEX] += 1
                    post_grad_counts[TOTAL_POPULATION_COUNT_INDEX] += 1
                else:
                    post_grad_counts[NO_COUNT_INDEX] += 1
                    post_grad_counts[TOTAL_POPULATION_COUNT_INDEX] += 1
            else:
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    staff_counts[YES_COUNT_INDEX] += 1
                    staff_counts[TOTAL_POPULATION_COUNT_INDEX] += 1
                else:
                    staff_counts[TOTAL_POPULATION_COUNT_INDEX] += 1
                    staff_counts[NO_COUNT_INDEX] += 1

                 
    # Uses the counter lists to populate a new list of the percentages
    all_population_percentages = [
        round(undergrad_counts[YES_COUNT_INDEX] / undergrad_counts[TOTAL_POPULATION_COUNT_INDEX] * 100, 2) ,
        round(post_grad_counts[YES_COUNT_INDEX] / post_grad_counts[TOTAL_POPULATION_COUNT_INDEX] * 100, 2),
        round(staff_counts[YES_COUNT_INDEX] / staff_counts[TOTAL_POPULATION_COUNT_INDEX] * 100, 2)
        ]
    
    # Storing the yes and no counts for graphing 
    undergrad_yes_no_compare = [undergrad_counts[YES_COUNT_INDEX], undergrad_counts[NO_COUNT_INDEX]]
    post_grad_yes_no_compare = [post_grad_counts[YES_COUNT_INDEX], post_grad_counts[NO_COUNT_INDEX]]
    staff_yes_no_compare = [staff_counts[YES_COUNT_INDEX], staff_counts[NO_COUNT_INDEX]]

    # Creating a legend for colours used on the bar graph
    legend_elements = [ Line2D([0],[0], marker='o',color="green", label='Undergraduate Result'),
                        Line2D([0], [0], marker='o', color="cyan",label="Post-Graduate Result"),
                        Line2D([0], [0], marker='o',color="blue",label="Staff Result")   
        ]
   

    # Create a grid for all charts to be placed on
    ax = plt.subplot2grid((3,2),(0,0))

    # Undergraduate Pie Chart Placement
    plt.pie(undergrad_yes_no_compare,labels=pie_chart_labels, colors=pie_chart_colors, explode=(0.1,0), shadow=True, autopct='%1.1f%%')
    plt.title("Undergraduate Population")

    # Post-Graduate Pie Chart Placement
    ax = plt.subplot2grid((3,2), (1,0))
    plt.pie(post_grad_yes_no_compare,labels=pie_chart_labels, colors=pie_chart_colors, explode=(0.1,0), shadow=True, autopct='%1.1f%%')
    plt.title("Post Graduate Population")

    # Staff Pie Chart Placement
    ax = plt.subplot2grid((3,2), (2,0))
    plt.pie(staff_yes_no_compare, labels=pie_chart_labels, colors=pie_chart_colors, explode=(0.1,0), shadow=True, autopct='%1.1f%%')
    plt.title("Staff Population")

    ax = plt.subplot2grid((3,2), (0,1), rowspan=3, colspan=2)
    plt.bar(population_labels, all_population_percentages, color=["green", "cyan", "blue"], edgecolor = 'black')
    plt.legend(handles=legend_elements, loc='upper left')
    plt.ylabel("Percentage of the Population (%)")
    plt.xlabel("Group Names")
    plt.title("Percentage of Each Academia Group's Population who believe ChatGPT is Plagarism for Essay Writing")
    plt.show()

                



    










