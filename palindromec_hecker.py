# Function to check if a string is palindrome
def is_palindrome(s):
    # Convert the string to lowercase and remove spaces
    s = s.replace(" ", "").lower()

    # Compare the string with its reverse
    return s == s[::-1]

# Driver code
if __name__ == "__main__":
    # Input from the user
    s = input("Enter a string: ")

    # Check if the string is palindrome
    if is_palindrome(s):
        print(f"'{s}' is a palindrome.")
    else:
        print(f"'{s}' is not a palindrome.")
