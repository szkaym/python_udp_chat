import chat
import sys

print('--------------------------------')
print('       CHAT TOOL Ver 0.1        ')
print('--------------------------------')

password = input('input secret code. require when shutdown: ')

print('start chat tool.')

display = chat.chatDisplay(password_=password)
display.start_('', 6081)