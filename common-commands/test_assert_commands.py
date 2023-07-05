# Assert always check if the condition's return is True
assert True

# assert numbers
waiting_number = 2
obtained_number = 1

# Using a message for errors
assert waiting_number == obtained_number, f"Expected: {waiting_number}, Obtained: {obtained_number}."

# assert text
waiting_text = "Selenium Webdriver"
obtained_text = "selenium Webdriver"

# # You can use string methods
assert waiting_text.lower() == obtained_text.lower(), f"Expected: {waiting_text}, Obtained: {obtained_text}."

text = "Selenium Webdriver"
present_text = "python"

# You can use string methods
assert present_text.lower() in text.lower(), f"{present_text} isn't in {text}."
