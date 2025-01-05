import re
import random 

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    #Μετρά πόσες λέξεις υπάρχουν σε κάθε προκαθορισμένο μήνυμα
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #Υπολογίζει το ποσοστό των αναγνωρισμένων λέξεων σε ένα μήνυμα χρήστη
    percentage = float(message_certainty) / float(len(recognised_words))

    #Ελέγχει αν οι απαιτούμενες λέξεις βρίσκονται στη συμβολοσειρά
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #Απαντήσεις---------------------------------------------------------------------------------------------------
    response('Hello!', ['hi', 'hello','hey'], single_response=True)
    response('You too!', ['good', 'morning', 'good', 'evening','good', 'night','good','luck'], required_words=['good'])
    response('See you!', ['bye', 'goodbye','adios'], single_response=True)
    response('I\'m doing fine, and you?', ['how', 'are', 'you', 'doing'], required_words=['how','doing'])
    response('PAOK, of course!', ['which', 'is','the','best','football','team'], required_words=['best','team'])
    response('You\'re welcome!', ['thank', 'thanks'], single_response=True)
    response('I don\'t think so!', ['are', 'there', 'aliens'], required_words=['aliens'])
    response('Black!', ['what', 'is', 'your', 'favourite','colour'], required_words=['what','colour'])
    

    unknown = ["Could you please repeat that? ","...","I didn't understand this.","What does that mean?"][ random.randrange(4)]

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
   
     
      
    return unknown if highest_prob_list[best_match] ==0 else best_match  
   


#Χρησιμοποιείται για τη λήψη της απάντησης
def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


#Response System
while True:
    print('Bot: ' + get_response(input('User: ')))
    