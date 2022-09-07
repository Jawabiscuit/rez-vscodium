# Rez `vscodium` package for Windows

[Rez](https://github.com/AcademySoftwareFoundation/rez) package for VSCodium, the FLOSS binaries of VSCode.

## :memo: Requirements

- [rez](https://github.com/AcademySoftwareFoundation/rez)
    - :construction: At the time of writing, the rez experience on Windows while using `gitbash` as the default shell is still being tested. A [PR](https://github.com/AcademySoftwareFoundation/rez/pull/1364) exists that aims to improve it.

### Soft Requirements

__Windows__

- [gitbash](https://gitforwindows.org/)
    - If rez config `default_shell` is set to 'gitbash'

## :hammer: Building

- Fork this repo
- Download [vscodium](https://github.com/VSCodium/vscodium/releases/download/1.71.0.22245/VSCodium-win32-x64-1.71.0.22245.zip) zip archive for Windows from the internet and place in `rel/`
- Build
    - :construction: Building and installing a local version is recommended

```sh
rez build -i -p ~/packages
```

## :ship: Release

> :rotating_light: **Note:** Do not release this package until a local version can be symlinked.

- Set `SYSTEM_REZ_EXTERNAL_PACKAGES` in your environment or remove / edit the block below in package.py so that it points to the default or desired release path respectively.

```python
with scope('config') as config:
    config.release_packages_path = '${SYSTEM_REZ_EXTERNAL_PACKAGES}'
```

- If changing package.py is necessary then git commit and push that code before releasing, otherwise it's as simple as:

```sh
rez release -m "Initial release"
```
