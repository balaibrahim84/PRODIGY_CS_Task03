import re

def check_password_strength(password):
    # Initialize criteria flags
    length_ok = len(password) >= 8
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    
    # Check for common weak patterns
    common_patterns = [
        r'(.)\1{2,}',  # Repeated characters (e.g., aaa)
        r'(012|123|234|345|456|567|678|789|890)',  # Sequential numbers
        r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',  # Sequential letters
        r'(qwer|wert|erty|rtyu|tyui|yuio|uiop|asdf|sdfg|dfgh|fghj|ghjk|hjkl|zxcv|xcvb|cvbn|vbnm)'  # Keyboard patterns
    ]
    
    has_common_pattern = any(re.search(pattern, password.lower()) for pattern in common_patterns)
    
    # Calculate strength score
    score = sum([length_ok, has_upper, has_lower, has_digit, has_special])
    
    # Adjust score for common patterns
    if has_common_pattern:
        score = max(0, score - 2)
    
    # Provide feedback
    feedback = []
    if not length_ok:
        feedback.append("Password should be at least 8 characters long.")
    if not has_upper:
        feedback.append("Add uppercase letters.")
    if not has_lower:
        feedback.append("Add lowercase letters.")
    if not has_digit:
        feedback.append("Add numbers.")
    if not has_special:
        feedback.append("Add special characters (e.g., !@#$%^&*).")
    if has_common_pattern:
        feedback.append("Avoid common patterns like 'aaa' or '123'.")
    
    # Determine strength level
    if score < 3:
        strength = "Weak"
    elif score < 5:
        strength = "Moderate"
    else:
        strength = "Strong"
    
    return {
        "strength": strength,
        "score": f"{score}/5",
        "feedback": feedback if feedback else ["Password is strong!"]
    }

# Interactive section
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    print("Type a password to test (or type 'exit' to quit)\n")
    
    while True:
        password = input("Enter password: ").strip()
        if password.lower() == "exit":
            print("Goodbye! Stay secure. 🛡️")
            break
        
        result = check_password_strength(password)
        print(f"\nPassword Strength: {result['strength']} ({result['score']})")
        print("Feedback:")
        for item in result['feedback']:
            print(f"  - {item}")
        print("-" * 50)
