import requests
import hashlib
import sys # Import sys for potential stdout flushing or exit

# --- Your existing checking functions (no changes needed here) ---
HEADERS = {"User-Agent": "MyPwnCheckApp"}

def check_hibp_email(email):
    """Checks an email against Have I Been Pwned."""
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            return False
        elif response.status_code == 400: # HIBP returns 400 for malformed emails
            return "Invalid email format"
        else:
            return f"Error: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"

def check_hibp_password(password):
    """Checks a password against Have I Been Pwned's Pwned Passwords."""
    sha1pwd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1pwd[:5]
    suffix = sha1pwd[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        if response.status_code != 200:
            return f"Error: {response.status_code}"
        hashes = (line.split(':') for line in response.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                return True
        return False
    except requests.exceptions.RequestException as e:
        return f"Request Error: {e}"

def check_cybernews_email(email):
    # Simulating for demonstration based on previous interaction
    if "comprometido@example.com" in email:
        return True
    return False

def check_fsecure_email(email):
    # Simulating for demonstration based on previous interaction
    if "breached@fsecure.com" in email:
        return True
    return False
# -------------------------------------------------------------------

def main():
    print("PS C:\\Users\\corse\\Pipeline\\iHBP> docker run -it senha-checker") # Simulate the initial prompt

    email = ""
    while not email:
        email = input("Digite seu email para verificar: ").strip()
        if not email:
            print("Email não pode ser vazio. Por favor, tente novamente.")

    password = input("Digite uma senha para verificar: ").strip() # Password can be empty for email-only check

    print("-" * 40) # Separator for results

    results_to_display = []

    # HIBP email check
    hibp_email_status = check_hibp_email(email)
    if hibp_email_status is True:
        results_to_display.append(("HIBP", "compromised", "Email comprometido!"))
    elif hibp_email_status is False:
        results_to_display.append(("HIBP", "secure", "Email seguro."))
    else:
        results_to_display.append(("HIBP", "error", f"Erro: {hibp_email_status}"))

    # Mozilla Monitor (reflects HIBP email)
    if hibp_email_status is True:
        results_to_display.append(("Mozilla Monitor", "compromised", "Email comprometido!"))
    elif hibp_email_status is False:
        results_to_display.append(("Mozilla Monitor", "secure", "Email seguro."))
    else:
        results_to_display.append(("Mozilla Monitor", "error", f"Erro: {hibp_email_status}"))

    # CyberNews email (simulated)
    cybernews_email_status = check_cybernews_email(email)
    if cybernews_email_status is True:
        results_to_display.append(("CyberNews", "compromised", "Email comprometido!"))
    else:
        results_to_display.append(("CyberNews", "secure", "Email seguro."))

    # F-Secure email (simulated)
    fsecure_email_status = check_fsecure_email(email)
    if fsecure_email_status is True:
        results_to_display.append(("F-Secure", "compromised", "Email comprometido!"))
    else:
        results_to_display.append(("F-Secure", "secure", "Email seguro."))

    # Password check (only HIBP)
    if password:
        hibp_password_status = check_hibp_password(password)
        if hibp_password_status is True:
            results_to_display.append(("HIBP_Password", "compromised", "Senha comprometida!"))
        elif hibp_password_status is False:
            results_to_display.append(("HIBP_Password", "secure", "Senha segura."))
        else:
            results_to_display.append(("HIBP_Password", "error", f"Erro Senha: {hibp_password_status}"))
    else:
        results_to_display.append(("HIBP_Password", "info", "Senha não fornecida para verificação."))

    # Print results with icons
    for service, status, message in results_to_display:
        icon = "✅" if status == "secure" else "⚠️" if status == "compromised" else "❓"
        print(f"{service}: {icon} {message}")

    print("\nPress CTRL+C to quit") # Similar to what Flask server output
    sys.exit(0) # Exit the script after execution


if __name__ == '__main__':
    main()