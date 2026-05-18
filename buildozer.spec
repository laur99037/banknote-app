[app]
title = Banknote AI
package.name = banknoteai
package.domain = org.ai
source.dir = .
source.include_exts = py,png,jpg,kv,tflite
version = 1.0
requirements = python3,kivy==2.2.1,numpy,pillow
android.ndk = 23b
android.api = 31
orientation = portrait
fullscreen = 1
android.permissions = CAMERA,INTERNET
android.minapi = 24
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 0
