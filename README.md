# buildroot-external-cb

## Linux Packages

```
sudo apt install debianutils sed make binutils build-essential gcc g++ bash patch gzip bzip2 perl tar cpio unzip rsync file bc git libssl-dev libncurses5-dev python3-pip graphviz
```

Create symlink for python3 to python

```
sudo ln -s /usr/bin/python3 /usr/bin/python
```

Remove spaces from PATH for WSL

```
PATH="/bin:/usr/local/bin:/usr/bin"
```

Python Packages
```
pip3 install numpy matplotlib
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

Build Errors
* numerical_limits build errors due to use of gcc11 instead of gcc10

Build statistics
```
make graph-build
```
```
make graph-depends
```
```
make graph-size
```

## How to program
Check USB interface under root
```
sudo ~/STMicroelectronics/STM32Cube/STM32CubeProgrammer/bin/STM32_Programmer_CLI -l usb
```

Change directory to images folder then call flash.tsv
```
sudo ~/STMicroelectronics/STM32Cube/STM32CubeProgrammer/bin/STM32_Programmer_CLI -c port=usb1 -w ../board/stmicroelectronics/stm32mp157/flash.tsv
```
