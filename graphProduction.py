# Names: Kyle Teopiz, Alan Pangnathip, Joseph Carvalho, Hameez Iqbal
# Date: Wednesday, March 1, 2023

import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

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

    Figure 1: A pie graph representing the diverse religions within the Far Leftist respondents group (optional data about the far lefts)

    """

    religious_group_counter = Counter()
    religions = []
    num_followers = []

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]
        for row in data_accessor:
            if int(row[(QUESTION_ACCESSOR["political_spectrum"])]) == 1:
                religious_group_counter[row[QUESTION_ACCESSOR["religion"]]] += 1
        
        for item in religious_group_counter.most_common():
            religions.append(item[0])
            num_followers.append(item[1])

    plt.bar(religions, num_followers)
    plt.xlabel("Religions")
    plt.ylabel("Number of Followers")
    plt.title("Religious Groups of the Far Leftist Repondents")

    plt.show()

    return "Display Closed"

def far_leftist_awareness_of_chatgpt():

    """
    
    Figure: A pie graph displaying the prior awareness of the Far Leftist respondent group of the existence of ChatGPT 
    
    """

    yes_no_counter = Counter()
    yes_no_labels = []
    yes_no_results = []

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]

        for row in data_accessor:
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == 1:
                yes_no_counter[row[QUESTION_ACCESSOR["heard_of_chatGPT"]]] += 1
        
        for item in yes_no_counter.most_common():
            yes_no_labels.append(item[0])
            yes_no_results.append(item[1])

    explode = (0, 0.2)
    fig, ax = plt.subplots()
    ax.pie(yes_no_results, explode=explode, labels=yes_no_labels, autopct='%1.1f%%', shadow= True)
    plt.title("Far Leftist Respondent Gtroup's Knowledge of ChatGPT Existence prior to Survey")
    plt.axis('equal')
    plt.show()

    return "Display Closed"
        


def far_left_chatGPT_essay_plagiarism():

    answer_labels = ["Yes" , "No"]
    # Yes -> No for Indexes
    far_left_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]
    
    # far lefts are 1, # far rights are 5
        for row in data_accessor:
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == 1:
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    far_left_results[0] += 1
                else:
                    far_left_results[1] += 1
    
    print(far_left_results)

    fig, ax = plt.subplots()
    ax.pie(far_left_results, labels=answer_labels, autopct='%1.1f%%')
    plt.title("Far Left's Opinion on ChatGPT being Plagiarism when used in Student Written Works")
    plt.axis('equal')
    plt.legend()
    plt.show()


    return "Display Closed"

def far_right_chatGPT_essay_plagiarism():
    answer_labels = ["Yes" , "No"]
    # Yes -> No for Indexes
    far_right_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]
    
    # far lefts are 1, # far rights are 5
        for row in data_accessor:
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == 5:
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    far_right_results[0] += 1
                else:
                    far_right_results[1] += 1
    print(far_right_results)
    fig, ax = plt.subplots()
    ax.pie(far_right_results, labels=answer_labels, autopct='%1.1f%%')
    plt.title("Far Left's Opinion on ChatGPT being Plagiarism when used in Student Written Works")
    plt.axis('equal')
    plt.legend()
    plt.show()

def political_far_left_chatGPT_research():

    answer_labels = ["Yes" , "No"]
    # Yes -> No for Indexes
    far_left_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]
    
    # far lefts are 1, # far rights are 5
        for row in data_accessor:
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == 1:
                if row[QUESTION_ACCESSOR["use_for_research_prompt"]] == "Yes":
                    far_left_results[0] += 1
                else:
                    far_left_results[1] += 1

    fig, ax = plt.subplots()
    ax.pie(far_left_results, labels=answer_labels, autopct='%1.1f%%')
    plt.title("Far Left's Opinion on ChatGPT being Ethical for Research Purposes")
    plt.axis('equal')
    plt.legend()
    plt.show()


    return "Display Closed"

def political_far_right_chatGPT_research():

    answer_labels = ["Yes" , "No"]
    # Yes -> No for Indexes

    far_right_results = [0,0]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]

    # far lefts are 1, # far rights are 5
        for row in data_accessor:
    
            if int(row[QUESTION_ACCESSOR["political_spectrum"]]) == 5:
                if row[QUESTION_ACCESSOR["use_for_research_prompt"]] == "Yes":
                    far_right_results[0] += 1
                else:
                    far_right_results[1] += 1




    fig, ax = plt.subplots()
    ax.pie(far_right_results, labels = answer_labels, autopct='%1.1f%%')
    plt.title("Far Right's Opinion on ChatGPT being Ethical for Research Purposes")
    plt.axis('equal')
    plt.legend()
    plt.show()


    

    

    


def gender_chatGPT_commercial_use():

    """ 
    
    Figure: A double bar graph representing each gender group's [Males, Females, and Others], answer on whether ChatGPT is ethical for use commerically / in workplace
    
    """
    gender_xaxis_labels = ["Males", "Females", "Other"]
    x_axis_position  = np.arange(len(gender_xaxis_labels))
    bar_offset = 0.25
    multiplier = 0
    
    male_reponses_counter = Counter()
    female_responses_counter = Counter()
    other_responses_counter = Counter()

    male_yes_no_responses = []
    female_yes_no_repsonses = []
    other_yes_no_responses = []
    
    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]

        for row in data_accessor:
            if row[QUESTION_ACCESSOR["gender"]] == "Male":
                male_reponses_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1
            elif row[QUESTION_ACCESSOR["gender"]] == "Female":
                female_responses_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1
            else:
                other_responses_counter[row[QUESTION_ACCESSOR["use_commercially_prompt"]]] += 1

    # Sorting each counter to ensure that they are in "Yes" then "No" Order, standardizing the data
    # can perhaps optimize to a range to generalize into an algorithm.. ill think about it
    male_reponses_counter = sorted(male_reponses_counter.most_common(), reverse= True)
    for item in male_reponses_counter:
        male_yes_no_responses.append(item[1])
    
    female_responses_counter = sorted(female_responses_counter.most_common(), reverse= True)
    for item in female_responses_counter:
        female_yes_no_repsonses.append(item[1])
    
    other_responses_counter = sorted(other_responses_counter.most_common(), reverse= True)
    for item in other_responses_counter:
        other_yes_no_responses.append(item[1])
    
    dict_data = {

         # FORMAT: key = answer to questions : value [<males value> , <females value>, <otheres value>]
        "Yes" : [male_yes_no_responses[0], female_yes_no_repsonses[0], other_yes_no_responses[0]],
        'No': [male_yes_no_responses[1], female_yes_no_repsonses[1], other_yes_no_responses[1]]
       
    }

    fig ,ax =  plt.subplots()
    for attribute, measurement in dict_data.items():
        shift = bar_offset * multiplier
        rects = ax.bar(x_axis_position + shift, measurement, bar_offset, label = attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1
    
    ax.set_ylabel('Number of People')
    ax.set_title('If ChatGPT is Ethical for Use in the Workplace by Gender Groups')
    ax.set_xticks(x_axis_position + bar_offset, gender_xaxis_labels)
    ax.legend(loc='upper right', ncols=3)  

    plt.show()

    return "Display Closed"




def undergraduate_instant_gratification_study():
    

    # seraching for questions 9 and 12 in undergrad
    # really trying to show students dont really care by what cost a mark comes by, they are fine not doing the work
    # in order to get the mark.
    # writing papers -> not binary, need to see which students are at a 1 or 2 on the spectrum
    # education inhibitor -> also binary so this is a good double bar graph -> yes also for ethical inhibitor

    #comparing to what?
    # wrting papers : inhib
    # 1) yes to yes, ethical but detrimental -> contradictory
    # 2) yes to no, ethical but not detrimental
    # 3) no to yes, not ethical and detrimental
    # 4) no to no, not ethical and not detrimental

    contradiction_to_other_counts = [0,0]

    population_labels = [ "Contradictory Students", "Rest of Population"]

    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]

        for row in data_accessor:
            if row[QUESTION_ACCESSOR["academia_status"]].__contains__('Student') == True:
                if (int(row[QUESTION_ACCESSOR["effect_on_student_learning"]]) == 1 or int(row[QUESTION_ACCESSOR["effect_on_student_learning"]]) == 2 or int(row[QUESTION_ACCESSOR["effect_on_student_learning"]]) == 3) and row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "No":
                    contradiction_to_other_counts[0] += 1
                else:
                    contradiction_to_other_counts[1] += 1
    
    explode = (0, 0.1)
    fig, ax = plt.subplots()
    ax.pie(contradiction_to_other_counts, explode=explode, labels=population_labels, autopct='%1.1f%%', shadow= True)
    plt.legend()
    plt.title("Contradictory Undergraduate Students who Believe ChatGPT inhibhits Student Development and is still Ethical for Essay Writing vs. the Rest of Undergraduates")
    plt.axis('equal')
    plt.show()

    return "Display Closed"


def upper_academia_plagarism():

    # index 0 counts yes, index 1 counts no -> can make this constant later
    upper_academia_labels = ["Yes", "No"]
    upper_academia_counts = [0,0]
    
    with open('chatGPT_ethics_survey_responses.csv', newline='') as csv_file:
        data_accessor = list(csv.reader(csv_file))[1:]

        for row in data_accessor:
            if (row[QUESTION_ACCESSOR["academia_status"]].__contains__("Student")) == False:
                if row[QUESTION_ACCESSOR["plagiarism_for_essays_prompt"]] == "Yes":
                    upper_academia_counts[0] += 1
                else:
                    upper_academia_counts[1] += 1
    
    explode = (0.1, 0)
    fig, ax = plt.subplots()
    ax.pie(upper_academia_counts, explode= explode, labels=upper_academia_labels, autopct='%1.1f%%', shadow=True)
    plt.legend()
    plt.title("The Opinions of Faculty and Post-Undergraduate Students on if ChatGPT is Plagiarism for Writing Essays")
    print(upper_academia_counts)
    plt.show()
    

                

        


def academia_levels_on_chatgpt_usage():
    pass

# scatter plot for joseph, continue on the train :)

 










