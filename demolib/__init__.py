import demolib.plugins as plugins
from pydispatch import dispatcher


def run():
    print "Loading plugins..."
    plugins.load_plugins("plugin_dir")

    print "\nFiring \"load\" event..."
    dispatcher.send(plugins.LOAD_EVENT)

    print "\nFiring \"speak\" event..."
    dispatcher.send(plugins.SPEAK_EVENT)

    print "\nFiring \"unload\" event..."
    dispatcher.send(plugins.UNLOAD_EVENT)
