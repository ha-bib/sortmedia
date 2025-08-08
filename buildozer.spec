[app]
title = Sort Media
package.name = sortmedia
package.domain = org.example
source.dir = .
source.main = main.py
version = 1.0
requirements = python3
orientation = portrait
fullscreen = 0

# Python for android (p4a) specific
p4a.branch = master
p4a.bootstrap = sdl2

# Izin Android
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# Target
android.api = 31
android.minapi = 26
android.ndk = 25.2.9519653
android.build_tools = 30.0.3
android.archs = arm64-v8a

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
android.sdk_path = /usr/local/lib/android/sdk

# (str) python-for-android git clone directory (if empty, it will be automatically cloned from github)
p4a.source_dir = 

# (str) The directory in which python-for-android should look for your own build recipes (if any)
p4a.local_recipes = 

# (str) Filename to the hook for p4a
p4a.hook = 

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2

# (int) port number to specify an explicit --port= p4a argument (eg: --port=1234
# p4a.port =

# Control passing the --private-mp argument to p4a
# p4a.private_mp = True

# (str) extra command line arguments to pass when invoking pythonforandroid.toolchain
p4a.extra_args = --no-compile-pyo

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2
