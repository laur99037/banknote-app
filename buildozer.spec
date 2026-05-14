[app]
title = Banknote AI
package.name = banknoteai
package.domain = org.ai
source.dir = .
source.include_exts = py,png,jpg,tflite,kv
version = 1.0

# REQUIREMENTS: Am adăugat pachetele esențiale. 
# Dacă tflite-runtime continuă să dea eroare, se poate folosi versiunea specifică de mai jos.
requirements = python3,kivy==2.3.0,numpy,pillow,tflite-runtime

android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

orientation = portrait
fullscreen = 1

# SETĂRI SDK/NDK STABILE
android.api = 34
android.minapi = 21
android.ndk = 26b
android.sdk = 34
android.accept_sdk_license = True
android.sdk_build_tools_version = 34.0.0
android.archs = arm64-v8a

# Această opțiune previne compresia modelului .tflite, esențial pentru ca interpretorul să-l poată citi direct din APK
android.no_inplace_gradle_build = True
android.copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1
