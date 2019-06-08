#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#


from tools.utilities import initialize_directories_and_settings

if __name__ == "__main__":
    initialize_directories_and_settings()
    from dvha_app import MainApp
    app = MainApp(0)
    app.MainLoop()
