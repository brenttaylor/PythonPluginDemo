import demolib.API as API


@API.load
def wake_up():
    print "The bear wakes up from hibernation..."


@API.speak
def roar():
    print "ROAR!"


@API.unload
def back_to_sleep():
    print "The beark starts to hibernate..."
