import copy
# This script creates a list of messages and sends them.

message_list = [
    [0, "Hello, how are you?"],
    [1, "I'm doing fine, how are you?"],
    [2, "I'm doing well, thank you."],
]

sent_messages = []


def send_message(message):
    """Print a simple greeting to each user in the list."""
    print(message)


def send_messages(messages):
    """Print a simple greeting to each user in the list."""
    for message_num, message in messages:
        sent_messages.append(message)
        print(f"Sending message: {message}")
        send_message(message)
        # Mark the message as sent.
        message_list.remove([message_num, message])


send_messages(copy.copy(message_list))


print("\nSent messages:")
for message in sent_messages:
    print(message)

print("\nRemaining messages:")
for message in message_list:
    print(message)
