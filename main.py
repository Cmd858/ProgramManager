from infi.systray import SysTrayIcon
from multiprocessing.connection import Client


def sendSignal(port, msg='TERMINATE'):
    address = ('localhost', port)
    signal = f'{msg}'
    try:
        conn = Client(address, authkey=b'12321')
        conn.send(signal)
        conn.close()
    except ConnectionRefusedError:
        print()


def kill_test(systray):
    print('Terminating test')
    sendSignal(50000)

def kill_server(systray):
    print('Terminating Server_V2')
    sendSignal(54320)


def on_quit_callback(systray):
    systray.shutdown()


def main():
    menu_options = (("Kill Test", None, kill_test),
                    ('Kill Server_V2', None, kill_server))
    systray = SysTrayIcon("Copyright.ico", "Example tray icon", menu_options, on_quit=on_quit_callback)
    systray.start()

main()