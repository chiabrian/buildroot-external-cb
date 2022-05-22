# buildroot-external-cb

## Linux Packages
```
sudo apt install debianutils sed make binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio unzip rsync file bc git libssl-dev libncurses5-dev
```
Create symlink for python3 to python
```
sudo ln -s /usr/bin/python3 /usr/bin/python
```

## Tools needed
STM32CubeProgrammer

## Buildroot
Buildroot Repository
```
git clone -b st/2021.02 https://github.com/bootlin/buildroot.git
```
Buildroot External Repository
```
git clone https://github.com/chiabrian/buildroot-external-cb.git
```

## How to Build
In Buildroot External Directory set configuration
```
make O=$(pwd) BR2_EXTERNAL=$(pwd) -C ../buildroot xxx_defconfig
```

## How to program
