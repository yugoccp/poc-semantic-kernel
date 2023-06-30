from chatbot import ChatBot

chatbot = ChatBot()

input_text = input('Enter text (type "exit" to leave): ')

while(input_text != 'exit'):
    chatbot.chat(input_text)
    input_text = input('Enter text  (type "exit" to leave): ')
