import openai
import pyttsx3

# Replace YOUR_API_KEY with your actual OpenAI API key
print("Enter OpenAI API Key")
openai.api_key = input()

# Create a TTS engine using pyttsx3
engine = pyttsx3.init()

# Create a loop to continue the conversation until the user explicitly tells the program to exit
while True:
  # Prompt the user to enter a message
  message = input("Enter a message (press Alt+X to exit): ")

  # Check if the user wants to exit the program
  if message.lower() == "alt+x":
    break

  # Use GPT-3 to generate a response to the user's message
  response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=message,
      max_tokens=128,
      temperature=0.5,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  ).get("choices")[0].get("text")

  # Use the eSpeak program to speak the response
  engine.say(response)
  engine.runAndWait()
