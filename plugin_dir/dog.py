import demolib.API as API


@API.load
def show_up():
    print "The dog runs to the door..."


@API.speak
def bark():
    print "Woof!"


@API.unload
def run_off():
    print "The dog runs off again..."
