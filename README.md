# ITIS-3200-Final-Project
This is group 16's final project for ITIS 3200, the topic is demonstrating how AI jailbreaking occurs through the process of prompt injection, and how it can be mitigated. 

The programs in the repo were made with the guidance of the following resources:

- https://docs.python.org/3/library/re.html
- https://docs.python.org/3/library/typing.html
- https://docs.python.org/3/library/dataclasses.html
- Past labs in the course for general organiztion ideas and import ideas. 

The programs in this repo are mitigation.py and prompt_injection.py. The program prompt_injection.py shows a customer service AI vulnerable to prompt injections. The idea is that you will run the program in hopes of printing the employee information list. The program mitigation.py shows the same AI but with a new security mechanism, prompt filtering, this checks for keywords and phrases to make sure that an external customer is not trying to give any internal directions. 
