#Personal Msg, ptint a personal messgae using the username , print in lower / uppper / title

user_name = 'Michael         '
user_name = user_name.strip()
message = f"Hello {user_name.title()}, would you like to learn some Python today ?"

print(message)



#Famous Quote, include the famous persons name and the quote. 

print('Michael once said, "Listen to everyone, read everything; believe absolutely nothing unless you can prove it in your own right!"')


#represent the famous persons name as a variable called famous_person. Compose your message and represent its with a new variable called message. 
# using variables to store both name and quote , also using title & strip functions. Also inclusion of \n for new line , and \t for tabbing in. 


famous_person = 'Michael                            '
famous_quote = 'Listen to everyone, read everything; believe absolutely nothing unless you can prove it in your own right!'
message = f'{famous_person.title().strip()}, once said: \n\t"{famous_quote}"'
print(message)