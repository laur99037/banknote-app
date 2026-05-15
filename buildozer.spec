[app]
title = Banknote AI
package.name = banknoteai
package.domain = org.ai
source.dir = .
source.include_exts = py,png,jpg,kv,tflite
version = 1.0

# FIX: numpy fixat la versiune compatibila cu Android NDK
requirements = python3,kivy==2.3.0,numpy==1.26.4,pillow

orientation = portrait
fullscreen = 1
android.permissions = CAMERA,INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
