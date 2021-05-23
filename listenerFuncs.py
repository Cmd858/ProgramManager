from multiprocessing.connection import Client


def sendSignal(port, msg='TERMINATE'):
    address = ('localhost', port)
    signal = f'{msg}'
    try:
        conn = Client(address, authkey=b'12321')
        conn.send(signal)
        conn.close()
    except ConnectionRefusedError as e:
        print(e)
        print('Connection Refused')

# Example formatting for new functions
# Worth noting that signals other than TERMINATE can be sent using the below functions
'''
def kill_test(systray, getinfo=False):
    if getinfo is True:
        displayText = 'Kill Test'
        icon = None
        return displayText, icon
    else:
        print('Terminating Test')
        sendSignal(50000)
'''

def kill_server(systray, getinfo=False):
    if getinfo is True:
        displayText = 'Kill Server'
        icon = None
        return displayText, icon
    else:
        print('Terminating Server_V2')
        sendSignal(54320)
