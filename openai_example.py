from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_openai_instance():
    try:
        # Create an OpenAI client instance
        # The API key will be automatically read from the OPENAI_API_KEY environment variable
        client = OpenAI()
        
        # Test the client with a simple completion
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Say hello!"}
            ]
        )
        
        # Print the response
        print("Response from OpenAI:")
        print(response.choices[0].message.content)
        
        return client
        
    except Exception as e:
        print(f"Error creating OpenAI instance: {str(e)}")
        return None

if __name__ == "__main__":
    # Create and test the OpenAI instance
    client = create_openai_instance()
    
    if client:
        print("\nOpenAI client successfully created and tested!")
    else:
        print("\nFailed to create OpenAI client. Please check your API key and try again.")
