import signal
import time
from time import gmtime, strftime
import gtk
import appindicator

APPINDICATOR_ID = 'timemanager'
indicator = appindicator.Indicator(APPINDICATOR_ID, gtk.STOCK_REFRESH, appindicator.CATEGORY_APPLICATION_STATUS)
start_time = 0;

def main():
    global indicator, start_time

    indicator.set_status(appindicator.STATUS_ACTIVE)
    indicator.set_label(strftime("%H:%M:%S",time.gmtime(0)), 'test')
    indicator.set_menu(build_menu())
    
    start_time = time.time()
    gtk.timeout_add(1000, on_timer)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_reset = gtk.MenuItem('Reset')
    item_reset.connect('activate', reset)
    menu.append(item_reset)

    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)

    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()

def reset(source):
    global start_time
    start_time = time.time()
    on_timer()
    return True    

def on_timer(args=None):
    global indicator, start_time

    indicator.set_label(strftime("%H:%M:%S", time.gmtime(time.time() - start_time)), 'test')
    return True

if __name__ == '__main__':
    main()