# -*- coding: utf-8 -*-

name = "vscodium"

version = "1.71"

authors = ["VSCodium"]

description = """\
    FLOSS binaries of VSCode. Microsoft VSCode available for download is not FLOSS and contains telemetry/tracking. 
"""

help = "https://vscodium.com/"

tools = [
    "VSCodium",
    "codium"
]

variants = [
    ["os-Windows-10"]
]

private_build_requires = []

with scope('config') as config:
    config.release_packages_path = '${SYSTEM_REZ_EXTERNAL_PACKAGES}'

build_command = """\
    set -e

    source_archive=`/usr/bin/find "$REZ_BUILD_SOURCE_PATH/rel" -type f -name '*.zip'`
    unzip -u "$source_archive" -d "$REZ_BUILD_PATH"

    if [ $REZ_BUILD_INSTALL == 1 ]
    then
        echo -e "\e[1m\e[32mInstalling...\e[0m"
        for item in "$REZ_BUILD_PATH"/*
        do
            if [ -d "$item" ]
            then
                printf '.'
                cp -r "$item" "$REZ_BUILD_INSTALL_PATH"
            fi
        done

        source_files=`/usr/bin/find "$REZ_BUILD_PATH" \
            -maxdepth 1 \
            -type f \
            -name '*.exe' \
            -o -name '*.dll' \
            -o -name '*.pak' \
            -o -name '*.dat' \
            -o -name '*.bin' \
            -o -name '*.json' \
            -o -name '*.xml'`

        for item in $source_files
        do
            if [ -f "$item" ]
            then
                printf '.'
                cp -r "$item" "$REZ_BUILD_INSTALL_PATH"
            fi
        done
    else
        echo -e "\e[1m\e[33mNothing more to do. Run ""rez-build -i"" to install\e[0m"
    fi
"""


def commands():
    import os

    env.PATH.append(os.path.join(this.root, "bin"))
