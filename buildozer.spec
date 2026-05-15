[app]
title = Banknote AI
package.name = banknoteai
package.domain = org.ai
source.dir = .
source.include_exts = py,png,jpg,kv,tflite
version = 1.0

# FIX: eliminat tflite-runtime, adăugat tflite ca recipe separat
requirements = python3,kivy==2.3.0,numpy,pillow,android,tflite

orientation = portrait
fullscreen = 1

android.permissions = CAMERA,INTERNET,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a
android.features = android.hardware.camera

# FIX: adaugă recipe-ul custom pentru tflite
p4a.local_recipes = ./recipes

[buildozer]
log_level = 2
warn_on_root = 1
