from infi.systray import SysTrayIcon
import listenerFuncs


def on_quit_callback(systray):
    try:
        systray.shutdown()
    except RuntimeError:
        print('Runtime Error While Exiting')


def getMenu():
    options = []
    for func in [f for f in dir(listenerFuncs) if not f.startswith('_') and
                                                  'sendSignal' not in f and 'Client' not in f]:
        funcref = getattr(listenerFuncs, func)
        text, icon = funcref(None, True)
        options.append((text, icon, funcref))  # get function reference and call with None
    options = tuple(options)
    return options


def main():
    menu_options = getMenu()
    systray = SysTrayIcon("Copyright.ico", "Example tray icon", menu_options, on_quit=on_quit_callback)
    systray.start()


main()
