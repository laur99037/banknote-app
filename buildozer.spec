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

android.permissions = CAMERA,INTERNET

android.api = 31
android.minapi = 24
android.sdk = 31
android.ndk = 25b
android.accept_sdk_license = True

android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
