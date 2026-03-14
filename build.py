PROJECT_NAME = "gdextension_template"

if __name__ == "__main__":
    gdextension_file_content = """
[configuration]

entry_symbol = "init_gdextension"
compatibility_minimum = "26.1"
reloadable = true

[libraries]

macos.debug = "res://bin/lib{0}.macos.template_debug.framework"
macos.release = "res://bin/lib{0}.macos.template_release.framework"

ios.debug = "res://bin/lib{0}.ios.template_debug.xcframework"
ios.release = "res://bin/lib{0}.ios.template_release.xcframework"

windows.debug.x86_32 = "res://bin/lib{0}.windows.template_debug.x86_32.dll"
windows.release.x86_32 = "res://bin/lib{0}.windows.template_release.x86_32.dll"
windows.debug.x86_64 = "res://bin/lib{0}.windows.template_debug.x86_64.dll"
windows.release.x86_64 = "res://bin/lib{0}.windows.template_release.x86_64.dll"

linux.debug.x86_64 = "res://bin/lib{0}.linux.template_debug.x86_64.so"
linux.release.x86_64 = "res://bin/lib{0}.linux.template_release.x86_64.so"
linux.debug.arm64 = "res://bin/lib{0}.linux.template_debug.arm64.so"
linux.release.arm64 = "res://bin/lib{0}.linux.template_release.arm64.so"
linux.debug.rv64 = "res://bin/lib{0}.linux.template_debug.rv64.so"
linux.release.rv64 = "res://bin/lib{0}.linux.template_release.rv64.so"

android.debug.x86_64 = "res://bin/lib{0}.android.template_debug.x86_64.so"
android.release.x86_64 = "res://bin/lib{0}.android.template_release.x86_64.so"
android.debug.arm64 = "res://bin/lib{0}.android.template_debug.arm64.so"
android.release.arm64 = "res://bin/lib{0}.android.template_release.arm64.so"

[dependencies]
ios.debug = {{
    "res://bin/libgodot-cpp.ios.template_debug.xcframework": ""
}}
ios.release = {{
    "res://bin/libgodot-cpp.ios.template_release.xcframework": ""
}}
    """.format(PROJECT_NAME)

    gdextension_file_path = "demo/template.gdextension"

    with open(gdextension_file_path, "w") as gdextension_file:
        gdextension_file.write(gdextension_file_content)