#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def simple_chatbot(user_input):
    user_input = user_input.lower()

    # Predefined rules and responses
    rules = {
        r'.*(hi|hello|hey).*': 'Hello!',
        r'.*(can.*you.help.*me.*a.*little?).*': 'Yes Sure! Tell me how can i help you?',
        r'.*(good.*morning).*':'Good Morning',
         r'.*(good.*noon).*':'Good Noon',
         r'.*(good.*evening).*':'Good Evening',
         r'.*(good.*night).*':'Good Night',
        r'.*(who.*are.*you|what.*is.*your.*name.*?)\b.*': 'Hello!! This is Nelsa',
        r'.*(who.*is.*nelsa.*?)\b.*': 'Nelsa is a chatbot',
        r'.*(what.*is.*chatbot|how.*does.*it.*works.*?)\b.*': 'A chatbot is a software or computer program that simulates human conversation or chatter through text or voice interactions',
        r'.*(good).*':'Thanks',
        r'.*(bye|goodbye).*': 'Goodbye! Have a great day!',
        r'.*(ok.*tell.*me.*about.*your.*service)\b.*': 'We are Providing online Grocery service.',
        r'.*(do.*you.*have.*apples)\b.*': 'Yes Apples are available.',
        r'.*(and.* do.* your.* store.* provides.*home.* decor.* items.*?).*': 'Sory! we are not providing services for home decor itmes.',
        r'.*(please.* provide.* me.* a.* list.* of.* some.* items.* in your.* store).*' :'Yes Sure!Here is the list of some items,a)Food Items b)Kitchen Items.',
        
        
        r'.*\b(how.*are.*you|how.*going)\b.*': 'I am just a chatbot, but thanks for asking!',
        r'.*\b(thank you|thanks)\b.*': 'You are welcome!',
        r'.*': "I'm sorry, I didn't quite understand that. Can you please repeat or rephrase?"
    }

    for pattern, response in rules.items():
        if re.match(pattern, user_input):
            return response

    return "I'm sorry, I cannot answer that at the moment."

if __name__ == "__main__":
    print("MyBot: Hello! How can I assist you? (type 'exit' to end)")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("MyBot: Goodbye!")
            break

        response = simple_chatbot(user_input)
        print("MyBot:", response)


# In[ ]:





# In[ ]:




