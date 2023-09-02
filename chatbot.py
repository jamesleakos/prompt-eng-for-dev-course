from llm_interface import get_completion_from_messages

# Notable: you can add system level messages
# you can also add in chat history
messages =  [  
{'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
{'role':'user', 'content':'tell me a joke'},   
{'role':'assistant', 'content':'Why did the chicken cross the road'},   
{'role':'user', 'content':'I don\'t know'}  ]

response = get_completion_from_messages(messages)
print(response)

# You can continue adding messages to this context
# You can also add a lot of information to the system context - like a menu, whatever
