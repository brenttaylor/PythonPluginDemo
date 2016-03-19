# Python Plugin Demo

An MIT licensed demo showing off one approach to adding event driven plugins to a python application.

The system revolves around pyDispatch, a decorator generator and a custom python module loader.  The entire system is approximately 30 lines of code and the magic happens in demolib/plugins.py and demolib/API.py.  Example plugins can be found in "plugin_dir".
