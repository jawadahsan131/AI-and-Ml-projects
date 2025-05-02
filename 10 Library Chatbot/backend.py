import nltk
from nltk.chat.util import Chat, reflections
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('vader_lexicon')

pairs = [
    # Greetings
    [r"(?i).*hello.*|.*hi.*|.*hey.*|.*hlo.*",
     ["Hello! How can I assist you with library-related information?",
     "Hi there! Do you need any help with library services?",
     "Hey! Welcome to the library information system. How may I help you?"]],
      
    # Library hours
    [r"(?i).*library hours.*|.*open.*|.*close.*|.*timing.*",
     ["The library is open from 8 AM to 8 PM, Monday to Saturday.",
      "Our library timings are 8 AM to 8 PM, and we're closed on Sundays.",
      "The library operates from 8 AM to 8 PM. Please let me know if you need further details!"]],
    
    # Book availability
    [r"(?i).*book availability.*|.*find books.*|.*check books.*",
     ["You can check book availability using the library catalog on our website or by visiting the library desk.",
      "To check if a book is available, use the online catalog or ask our librarians for assistance.",
      "Please visit our library website or contact the librarian desk to check the availability of books."]],
    
    # Borrow and return policies
    [r"(?i).*borrow books.*|.*return books.*|.*borrowing policy.*",
     ["Books can be borrowed for 14 days and renewed once. Late returns may incur fines.",
      "Borrowing is allowed for 14 days. Fines apply for overdue books, and you can renew once if needed.",
      "Books can be borrowed for a 2-week period. Check with the library for renewal options and late fees."]],
    
    # Membership
    [r"(?i).*membership.*|.*register.*|.*joining library.*",
     ["To become a member, fill out the registration form on our website or visit the library with a valid ID.",
      "Library membership is free for students and requires a valid ID. Visit our library or website for registration.",
      "To join the library, please provide your ID and fill out the membership form online or in person."]],
    
    # Digital resources
    [r"(?i).*digital resources.*|.*e-books.*|.*online materials.*",
     ["We provide access to e-books, journals, and research databases. Visit the library website to explore them.",
      "Digital resources like e-books and research papers are available through our library portal.",
      "You can access e-books, journals, and more through the online library system. Reach out for assistance if needed."]],
    
    # Late fees and fines
    [r"(?i).*late fees.*|.*fines.*|.*overdue books.*",
     ["The late fee is $1 per day per book. Please return or renew on time to avoid charges.",
      "For overdue books, a fine of $1 per day applies. Renew your books online or in person to avoid fines.",
      "Late fees are $1 per day. Contact the library staff for more information on overdue policies."]],
    
    # Library location
    [r"(?i).*library location.*|.*where is library.*|.*address.*",
     ["The library is located on the Main Campus, next to the Student Center.",
      "Our library is on the Main Campus, near the administration block.",
      "You can find the library at the Main Campus, adjacent to the Academic Hall."]],
    
    # Study spaces
    [r"(?i).*study spaces.*|.*study rooms.*|.*quiet areas.*",
     ["The library has dedicated quiet study rooms and collaborative workspaces for groups.",
      "We provide study spaces, including private rooms for quiet study and group work areas.",
      "You can reserve study rooms or use the quiet zones in the library. Ask our staff for assistance."]],
    
    # Printing and photocopying
    [r"(?i).*printing.*|.*photocopy.*|.*print services.*",
     ["Printing and photocopying services are available in the library at nominal charges.",
      "The library offers printing and photocopying services. Check with the help desk for rates and procedures.",
      "You can use our printing and photocopying services during library hours. Nominal charges apply."]],
    
    # Events and workshops
    [r"(?i).*library events.*|.*workshops.*|.*activities.*",
     ["The library hosts regular workshops and events. Check our website or noticeboard for upcoming activities.",
      "We organize workshops on research skills, citation styles, and more. Stay updated via our website.",
      "Library events and workshops are announced on our website and bulletin boards. Feel free to participate!"]],
    
    # Contact information
    [r"(?i).*contact information.*|.*library phone.*|.*email.*",
     ["You can reach the library at (555) 123-4567 or email us at library@university.edu.",
      "Contact us via phone at (555) 123-4567 or email at library@university.edu for any queries.",
      "Feel free to call (555) 123-4567 or email library@university.edu for assistance."]],
      
    # Library timing 
    [r"(?i).*library hours.*|.*open.*|.*close.*|.*timing.*|.*lib timing.*",
     ["The library is open from 8 AM to 8 PM, Monday to Saturday.",
     "Our library timings are 8 AM to 8 PM, and we're closed on Sundays.",
     "The library operates from 8 AM to 8 PM. Please let me know if you need further details!"]],
    
    # Goodbye
    [r"(?i).*bye.*|.*goodbye.*|.*see you later.*",
     ["Goodbye! Feel free to ask me anything about the library anytime.",
      "See you later! Let us know if you need more information.",
      "Alright, take care! Don’t hesitate to reach out for library assistance."]]

]

chatbot = Chat(pairs, reflections)
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
  sentiment_score = sia.polarity_scores(text)
  if sentiment_score['compound'] >= 0.05:
    return "Positive Sentence"
  elif sentiment_score['compound'] <= -0.05:
    return "Negative Sentence"
  else:
    return "Neutral Sentence"
  
def chatbot_app():
  print(" -- Welcome to BSAI-4A CHATBOT -- ")
  print(" -- Type 'Sentiment' to Analyze a Sentence ")
  print(" -- Type 'Exit' to exit ")

  while True:
    user_input = input("You: ")
    print(f"User input received: {user_input}")

    if user_input.lower() == "exit":
      print("ChatBot: Goodbye!")
      break
    elif user_input.lower() == "sentiment":
      print("ChatBot: Tell me a sentence to Analyze.")
      sentiment_input = input("You: ")
      print("ChatBot: Sentiment Analysis Report -", analyze_sentiment(sentiment_input))
    else:
      response = chatbot.respond(user_input.lower())
      if response:
        print("ChatBot:", response)
        if "bye" in user_input.lower():
          break
      else:
        print("ChatBot: I'm not sure how to respond to that.")


def get_chat_response(user_message):
    response = chatbot.respond(user_message)
    return response if response else "I'm not sure how to respond."

