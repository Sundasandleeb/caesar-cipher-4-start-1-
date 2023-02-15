alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #if user enters any character that is not included in alphabet list
    if char in alphabet: 
      
      position = alphabet.index(char)
      new_position = position + shift_amount
      new_letter = alphabet[new_position]
      end_text += new_letter
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)
#improving user experience by asking him if he wants to continue or exit
choice_yes = True
while choice_yes:
  
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
  
  #if user enters shift that is greater than alphabet length
    shift = shift % 26
  #calling method
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    x = input("Do you want to continue? If yes, type yes. If no, type no \n")
    if x == "no":
    
     choice_yes = False
     print("Goodbye \n. Replit exited")
    
    
    