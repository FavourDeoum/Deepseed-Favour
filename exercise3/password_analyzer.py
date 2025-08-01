import string

# List of common passwords
common_passwords = [
    "123456", "password", "12345678", "qwerty", "123456789",
    "12345", "1234", "111111", "1234567", "dragon",
    "letmein", "baseball", "abc123", "iloveyou", "123123",
    "admin", "welcome", "monkey", "login", "football"
]

def analyze_password(password):
    score = 0
    suggestions = []

    """Check length"""
    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters.")

    """Check uppercase"""
    if any(c.isupper() for c in password):
        score += 20
    else:
        suggestions.append("Add at least one uppercase letter.")

    """Check lowercase"""
    if any(c.islower() for c in password):
        score += 20
    else:
        suggestions.append("Add at least one lowercase letter.")

    """Check digits"""
    if any(c.isdigit() for c in password):
        score += 20
    else:
        suggestions.append("Include at least one number.")

    """ Check special characters"""
    special_chars = "!@#$%^&*"
    if any(c in special_chars for c in password):
        score += 20
    else:
        suggestions.append(f"Include at least one special character ({special_chars}).")

    """Check common passwords"""
    if password.lower() not in common_passwords:
        score += 20
    else:
        suggestions.append("Avoid common passwords (e.g., '123456', 'password').")

    """Determine strength level"""
    if score <= 40:
        strength = "Weak"
    elif score <= 60:
        strength = "Fair"
    elif score <= 80:
        strength = "Good"
    elif score <= 100:
        strength = "Strong"
    else:
        strength = "Excellent"

    """Output"""
    print(f"\n🔐 Password Analysis:")
    print(f"Score: {score}/120")
    print(f"Strength: {strength}")

    if suggestions:
        print("\n💡 Suggestions to Improve:")
        for s in suggestions:
            print(f"❌ {s}")
    else:
        print("\n✅ Your password meets all criteria!")

"""Example usage"""
print("\n === PASSWORD SECURITY ANALYZER ===")
password_input = input("Enter a password to analyze: ")
analyze_password(password_input)
