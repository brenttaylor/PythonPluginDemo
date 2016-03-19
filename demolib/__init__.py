import demolib.plugins as plugins
from pydispatch import dispatcher


def run():
    print "Loading plugins..."
    print "\nFiring \"load\" event..."
    plugins.load_plugins("plugin_dir")

    print "\nFiring \"speak\" event..."
    dispatcher.send(plugins.SPEAK_EVENT)

    print "\nFiring \"unload\" event..."
    plugins.unload_all()
