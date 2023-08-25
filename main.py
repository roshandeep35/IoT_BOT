
from wakeword import WakeWordDetector
from command import CommandProcessor

def main():
    wake_word_detector = WakeWordDetector('hello bot', 'Roshan')
    command_processor = CommandProcessor()

    while True:
        result = wake_word_detector.listen_for_wake_word()
        listen = True
        if result is True:
                while listen:
                     command = command_processor.listen_for_command()
                     if command == False: 
                        listen=False
                     print(command)  # Prints the response from GPT-4 API
        elif isinstance(result, str):
                response = command_processor.process_command(result)
                print(response)


if __name__ == "__main__":
    main()
