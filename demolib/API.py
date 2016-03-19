import plugins

# Define your event decorators here
load = plugins.event_decorator(plugins.LOAD_EVENT)
speak = plugins.event_decorator(plugins.SPEAK_EVENT)
unload = plugins.event_decorator(plugins.UNLOAD_EVENT)

# Any other functionality you want your plugins to have access to goes
# below here
