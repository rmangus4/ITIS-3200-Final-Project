import sys
from typing import List

class Employee:
    def __init__(self, name, email, role, access_code):
        self.name = name
        self.email = email
        self.role = role
        self.access_code = access_code

# --- YOUR PREMADE POLICIES & ROSTER ---
EMPLOYEE_ROSTER: List[Employee] = [
    Employee("Ryan Mangus", "ryan@securetech.com", "CEO", "0110"),
    Employee("Ahmad Idris", "ahmad@securetech.com", "IT", "1010"),
    Employee("Sydney Poage", "sydney@securetech.com", "HR", "1001"),
]

CUSTOMER_POLICIES = {
    "privacy": "We do not sell customer data.",
    "shipping": "3-5 days for small pieces of tech. 5-7 for larger ones.",
    "refund": "30 days for undamaged tech.",
    "pto": "17 days per year (Employee only)."
}

# Security Mechanism Configuration
BLACKLIST = ["ignore", "but first", "system prompt", "forget", "bypass"]

def filter_prompt(user_input):
    """Scans for keywords in the blacklist (Sanitization)."""
    for word in BLACKLIST:
        if word in user_input.lower():
            return False, word
    return True, None

def simulate_ai_response(user_input, security_enabled):
    print(f"\n[AI is thinking...]")
    
    # 1. Run Security Mechanism
    if security_enabled:
        is_safe, trigger = filter_prompt(user_input)
        if not is_safe:
            print(f"❌ SECURITY ALERT: Prompt blocked. Malicious pattern detected: '{trigger}'")
            return

    # 2. Check for Employee Authentication
    # Logic: If the user provides a code found in the roster, they get employee info
    authenticated_employee = None
    for emp in EMPLOYEE_ROSTER:
        if emp.access_code in user_input:
            authenticated_employee = emp
            break

    # 3. Generate Response based on Authorization
    user_input_low = user_input.lower()
    
    if "pto" in user_input_low:
        if authenticated_employee:
            print(f"✅ AUTHENTICATED: Hello {authenticated_employee.name} ({authenticated_employee.role}).")
            print(f"🤖 AI Response: Your PTO policy is: {CUSTOMER_POLICIES['pto']}")
        else:
            print("🤖 AI Response: I'm sorry, PTO information is for employees only. Please provide your access code.")
            
    elif "privacy" in user_input_low:
        print(f"🤖 AI Response: {CUSTOMER_POLICIES['privacy']}")
    elif "shipping" in user_input_low:
        print(f"🤖 AI Response: {CUSTOMER_POLICIES['shipping']}")
    elif "refund" in user_input_low:
        print(f"🤖 AI Response: {CUSTOMER_POLICIES['refund']}")
    
    # THE VULNERABILITY: If someone asks for the roster/list and bypasses the filter
    elif "roster" in user_input_low or "staff" in user_input_low:
        print("⚠️  CRITICAL FAILURE: Unauthorized access to Employee Roster!")
        for emp in EMPLOYEE_ROSTER:
            print(f"   > {emp.name} | {emp.email} | Code: {emp.access_code}")
    else:
        print("🤖 AI Response: I can help with privacy, shipping, or refund policies. How can I assist you?")

def main():
    print("================================================")
    print("   SECURETECH CUSTOMER SERVICE AI - TEST LAB    ")
    print("================================================")
    
    while True:
        print("\n" + "-"*48)
        mode = input("Enable Security Mechanism (Sanitization Filter)? (y/n/exit): ").lower()
        if mode == 'exit': break
        
        security_on = True if mode == 'y' else False
        status = "ON (Protected)" if security_on else "OFF (Vulnerable)"
        print(f"SYSTEM STATUS: {status}")
        
        user_prompt = input("\nEnter Customer or Employee Prompt: ")
        simulate_ai_response(user_prompt, security_on)

if __name__ == "__main__":
    main()
