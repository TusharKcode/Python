import random
import string

def generate_password(length,uppercase,lowercase,numbers,symbols):
    characters=''
    if uppercase:
        characters+=string.ascii_uppercase
    if lowercase:
        characters+=string.ascii_lowercase
    if numbers:
        characters+=string.digits
    if symbols:
        characters+=string.punctuation

    if not any([uppercase,lowercase,numbers,symbols]):
        print("Please select at least one character  type.")
        return None
    password=''.join(random.choice(characters) for _ in range(length))
    return password
def password_strength_meter(password):
    strength=0
    if len(password)>=8:
        strength+=1
    if any(c.isupper() for c in password):
        strength+=1
    if any(c.islower() for c in password):
        strength+=1
    if any(c.isdigit() for c in password):
        strength+=1
    if any(c in string.punctuation for c in password):
        strength+=1

    if strength==0:
        return print("Very Weak")
    elif strength==1:
        return print("Weak")
    elif strength==2:
        return print("Medium")
    elif strength==3:
        return print("Strong")
    else:
        return print("Very Strong")

if __name__=='__main__':
        length=int(input("Enter desired password length: "))
        uppercase=input("Include uppercase letters? (y/n): ").lower()=='y'
        lowercase=input("Include lowercase letters? (y/n): ").lower()=='y'
        numbers=input("Include numbers? (y/n): ").lower()=='y'
        symbols=input("Include symbols? (y/n): ").lower()=='y'

password=generate_password(length,uppercase,lowercase,numbers,symbols)

if password:
        print("Generated Password: ",password)
        








