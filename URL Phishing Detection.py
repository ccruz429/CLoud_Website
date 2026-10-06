import re
def is_phishing(url):
    suspicious_patterns = ["@", "-login", "secure-", "http://"]
    for pattern in suspicious_patterns:
        if pattern in url:
            return True
        return False

url = input("Enter a URL to check for phishing: ")
print("Phishing Detected!" if is_phishing(url) else "No phishing detected.")