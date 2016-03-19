import demolib.API as API


@API.load
def wake_up():
    print "The cat starts to wake up..."


@API.speak
def meow():
    print "Meow!"


@API.unload
def back_to_sleep():
    print "The cat falls back asleep..."
