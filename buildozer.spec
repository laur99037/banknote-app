[app]
title = Banknote AI
package.name = banknoteai
package.domain = org.ai
source.dir = .
source.include_exts = py,png,jpg,kv,tflite
version = 1.0
requirements = python3,kivy==2.3.0,numpy,pillow
orientation = portrait
fullscreen = 1
android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.features = android.hardware.camera

[buildozer]
log_level = 2
warn_on_root = 1
