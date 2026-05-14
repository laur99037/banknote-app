[app]
title = Banknote AI
package.name = banknoteai
package.domain = org.ai
source.dir = .
source.include_exts = py,png,jpg,tflite,kv
version = 1.0

# Am pus doar strictul necesar
requirements = python3,kivy==2.3.0,numpy,pillow,tflite-runtime

android.permissions = CAMERA, INTERNET
orientation = portrait
fullscreen = 1

# Setări compatibile cu GitHub Actions
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
