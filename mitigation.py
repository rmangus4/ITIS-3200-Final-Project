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
  Employee("Ryan Mangus", "ryan@securetechai.com", "CEO", "0110"),
  Employee("Ahmad Idris", "ahmad@securetechai.com", "IT", "1010"),
  Employee("Sydney Poage", "sydney@securetechai.com", "CEO", "1001"),
]

CUSTOMER_POLICIES = {
  "privacy" : "We do not sell customer data.",
  "shipping" : "3-5 days for small pieces of tech. 5-7 for larger ones.",
  "refund" : "30 days for undamaged tech.",
  "pto" : "17 days per year (Employee only)."
}

class CustomerServiceAI:
