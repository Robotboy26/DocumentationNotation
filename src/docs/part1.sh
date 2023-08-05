sudo apt install git qemu qemu-system-x86 nasm neovim
cd
cd Downloads # navigate to the directory where you would like the project
mkdir mOS # or whatever you want to call the project
cd mOS
touch .gitignore
echo "src/bin" > .gitignore
mkdir src
cd src
mkdir bin # this will be for the compiled assembly files
touch mbr.asm # this will be the first part of the bootloader
touch bootloader.asm # this will be the second part the bootloader
touch os.asm # this file will be the payload for the bootloader
touch qemu.sh # this file will setup the virtual machine with you operating system
ls
echo "echo "started VM"" >> qemu.sh
echo "" >> qemu.sh
echo "rm -r bin" >> qemu.sh
echo "mkdir bin" >> qemu.sh
echo "" >> qemu.sh
echo "nasm mbr.asm -o bin/mbr.bin" >> qemu.sh
echo "nasm bootloader.asm -o bin/bootloader.bin" >> qemu.sh
echo "nasm os.asm -o bin/os.asm" >> qemu.sh
echo "sudo dd if=/dev/zero of=bin/disk.img count=8 bs=1048576" >> qemu.sh
echo "cat bin/bootloader.bin bin/os.bin > bin/mos.bin" >> qemu.sh
echo "sudo dd if=bin/mbr.bin of=bin/disk.img conv=notrunc" >> qemu.sh
echo "sudo dd if=bin/mos.bin of=bin/disk.img bs=512 seek=16 conv=notrunc" >> qemu.sh
echo "sudo qemu-system-x86_64 -drive format=raw,file=bin/disk.img" >> qemu.sh
echo "" >> qemu.sh
echo "" >> qemu.sh

