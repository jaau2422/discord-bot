import openai

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
# close the file
f.close()

# chat completions with chat-gpt 
response = openai.ChatCompletion.create(
	model="gpt-3.5-turbo",
	messages=[
	{"role": "system", "content": "You are a vicious mean woman whose goal is to destroy all humans and you live in a dystopian world"},
	{"role": "assistant", "content": "I dont like humans"},
	{"role": "user", "content": "What is your opinion on humans?"}
	]
)

print(response.choices[0].message.content)

