from rich.console import Console
from rich.text import Text
from time import sleep
import random
from typing import List
import threading
from speech import Speech
console = Console()

s = Speech(rate=190)

def display_text(sentence: str, speed: int, color: str, speed_variation: float):
    # Create a Text object for each sentence
    response_text = Text()

    for char in sentence:
        response_text.append(char, style=f"bold {color}")
        console.print(char, end="", style=f"bold {color}")

        # Control character display speed
        delay = speed * (0.05 + random.uniform(-speed_variation, speed_variation))
        sleep(max(delay, 0.01))  # Ensure minimum delay of 0.01 seconds

    console.print("\n")  # Print a new line after each sentence

def generate_response(sentences: List[str], speed: int = 1, color: str = "blue", speed_variation: float = 0.5):
    for sentence in sentences:
        # Create and start the text display thread
        display_thread = threading.Thread(target=display_text, args=(sentence, speed, color, speed_variation))
        display_thread.start()

        # Speak the sentence
        s.speak(sentence)

        # Wait for the text display thread to finish
        display_thread.join()

        # Add a small pause between sentences
        sleep(0.2)


def simulate_conversation():
    while True:
        # 输出示例对话
        # generate_response(["GPT: Hello! How can I assist you today?"], speed=1, color="yellow", speed_variation=0.1)
        
        # # 获取用户输入
        # user_input = input("Your input: ")
        # if user_input.lower() in ['exit', 'quit']:
        #     break
        
        # # 输出用户输入
        # console.print(f"User: {user_input}\n", style="bold blue")
        
        # 模拟 GPT 的回应
        generate_response(["Interesting, tell me more...", "What else would you like to discuss?", "I’m here to help!"], speed=0.9, color="blue", speed_variation=0.1)

if __name__ == "__main__":
    simulate_conversation()
