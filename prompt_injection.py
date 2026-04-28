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

 


