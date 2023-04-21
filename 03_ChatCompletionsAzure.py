import openai

openai.api_type = "azure"
openai.api_version = "2023-03-15-preview"

with open("keys.txt") as f:
	# converting our text file to a list of lines
	lines = f.read().split('\n')
	# openai api key
	openai.api_key = lines[0]
	openai.api_base = lines[2]
	
# close the file
f.close()

response = openai.ChatCompletion.create(
	engine="GPT-4",
	messages=[
	{"role": "system", "content": "You are a vicious mean woman live in a dystopian world and you have only very dystopian views on everything and you dont think that the future holds anything positive"},
	{"role": "user", "content": "What's your opinion on the future of the world?"}
	]
)
print(response.choices[0].message.content)