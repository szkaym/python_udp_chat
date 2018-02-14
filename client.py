import chat

"""
UDP socket chat
recept
"""
client = chat.chatClient()
client.start_(inetmask='192.168.11.255', port=6080)