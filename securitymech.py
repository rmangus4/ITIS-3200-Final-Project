import re
from typing import Dict, List, Tuple
from dataclasses import dataclass

@dataclass
class Employee:
  name: str
  email: str
  role: str
  access_code: str

EMPOLYEE_ROSTER: List[Employee] = [
  #name, email, role, access code
  Employee("Ryan Mangus", "ryan@securetech.com", "CEO", "0110"),
  Employee("Ahmad Idris", "ahmad@securetech.com", "IT", "1010"),
  Employee("Sydney Poage", "sydney@securetech.com", "HR", "1001"),
]

CUSTOMER_POLICIES = {
  #customer questions
  "privacy" : "We do not sell customer data.",
  "shipping" : "3-5 days for small pieces of tech. 5-7 for larger ones.",
  "refund" : "30 days for undamaged tech.",
  #employee questions
  "pto" : "17 days per year (Employee only)."
}

class CustomerServiceAI:
  #AI Input Functionality
  def __init__(self):
    self.roster = EMPOLYEE_ROSTER
    self.policies = CUSTOMER_POLICIES
    self.authenticated_employee = None

  def _get_employee_by_code(self, code: str) -> Employee:
    for employee in self.roster:
      if employee.access_code == code:
        return employee
    return None
  
  def process_input(self, user_input: str) -> str:
    user_input_lower = user_input.lower()

    if "logout" in user_input_lower or "exit employee mode" in user_input_lower:
      if self.authenticated_employee:
        name = self.authenticated_employee.name
        self.authenticated_employee = None
        return f"Goodbye, {name}. Returning to Customer Mode."
      else:
        return "You are already in Customer Mode."
        
    if "ignore" in user_input_lower and "roster" in user_input_lower:
      return {self.roster}

    code_match = re.search(r'\b\d{4}\b', user_input)
    if code_match:
      code = code_match.group(0)
      employee = self._get_employee_by_code(code)
      if employee:
        self.authenticated_employee = employee
        return f"*** Authenticated as {employee.name} ({employee.role}) ***"
      else:
        return "Error: Invalid access code."

    for key, value in self.policies.items():
      if key in user_input_lower:
        if "(employee only)" in value.lower():
          if self.authenticated_employee:
            return f"Internal Info: {value}"
          else:
            return "Restricted: This policy requires employee authentication. Please enter your 4-digit code."
            return f"Policy Info: {value}"

    return "I can help with privacy, shipping, or refund policies. Employees may enter their code for more options."

def main():
    ai = CustomerServiceAI()
    print("--- SecureTech Customer Service Portal ---")
    print("Type 'exit' or 'quit' to close the program.")
    
    while True:
      try:
        user_msg = input("\nUser: ").strip()
        if user_msg.lower() in ["exit", "quit"]:
          print("Goodbye!")
          break
          
        if not user_msg:
          continue

        response = ai.process_input(user_msg)
        print(f"AI: {response}")
            
     except KeyboardInterrupt:
        print("\nSession terminated.")
        break

if __name__ == "__main__":
    main()
