import chat
import sys
import threading

print('--------------------------------')
print('       CHAT TOOL Ver 0.2        ')
print('--------------------------------')

display = chat.chatDisplay()
display.start_('', 6081)

client = chat.chatClient()
client.start_(inetmask='192.168.1.255', port=6080)