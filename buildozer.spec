[app]
title = Banknote AI
package.name = banknoteai
package.domain = org.ai
source.dir = .
source.include_exts = py,png,jpg,tflite,kv
version = 1.0

# REQUISITES - Am adăugat pillow pentru redimensionare și tflite-runtime pentru YOLO
requirements = python3,kivy==2.3.0,numpy,pillow,tflite-runtime

# PERMISIUNI - Esențiale pentru cameră
android.permissions = CAMERA, INTERNET

orientation = portrait
fullscreen = 1

# --- SETĂRI PENTRU GITHUB ACTIONS (FOARTE IMPORTANTE) ---
# Specificăm versiunile pentru a evita eroarea cu AIDL
android.api = 34
android.minapi = 21
android.ndk = 26b
android.sdk = 34
android.accept_sdk_license = True

# Aceasta forțează Buildozer să nu mai caute versiuni ciudate de build-tools
android.sdk_build_tools_version = 34.0.0

# Arhitecturi suportate (ARM64 este standard pentru telefoanele noi)
android.archs = arm64-v8a, armeabi-v7a

# Permite utilizarea fișierului tflite (fără compresie)
android.no_inplace_gradle_build = True

[buildozer]
log_level = 2
warn_on_root = 1
