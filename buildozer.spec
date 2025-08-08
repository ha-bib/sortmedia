[app]
title = Sort Media
package.name = sortmedia
package.domain = org.example
source.dir = .
source.main = main.py
version = 1.0
requirements = python3,pillow
orientation = portrait
fullscreen = 0

# Izin Android
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# Target
android.api = 31
android.minapi = 26
android.archs = armeabi-v7a, arm64-v8a

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
