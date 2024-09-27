#About this program
''' 
This program is an compilation helper for assembly code which compiles assembly code of arm and x86
-x option capable of compiling 32 and 64 bit versions
-a option will compile arm assembly
-d is enabled it will start debugging the program after compiling and executing

'''

import argparse
import subprocess
import os
import sys
import time
import atexit
import signal

class ARM:
    def __init__(self, input_file):
        self.input_file = input_file  # Attribute

    def arm_32(self):
        """Assembles and links the given input file for arm-32 Bit architecture."""
        nasm_cmd = f"arm-linux-gnueabihf-as {self.input_file}"
        before_dot, _ = self.input_file.split('.', 1)
        print("[+] Object File Generated\n")
        
        ld_cmd = f"arm-linux-gnueabihf-ld a.out -o {before_dot}"
        print("[+] Running The Program:\n")
        
        run_cmd = f"qemu-arm ./{before_dot}"
        debug_cmd = f"qemu-arm -g 1234 ./{before_dot} &"
        debug_cmd2 = f'gdb-multiarch -q -nx -ex "set architecture arm" -ex "file nop" -ex "target remote 127.0.0.1:1234"'
    
        try:
            subprocess.run(nasm_cmd, shell=True, check=True)
            subprocess.run(ld_cmd, shell=True, check=True)
            subprocess.run(run_cmd, shell=True)
    
            if args.debug:
                print("\n[+] Starting Debugger in:")
                for i in range(5, 0, -1):
                    sys.stdout.write(f"   {i} seconds... (CTRL+C to stop)\r")
                    sys.stdout.flush()
                    time.sleep(1)
                subprocess.run(debug_cmd, shell=True)
                subprocess.run(debug_cmd2, shell=True)
    
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.cmd}")
            exit(1)

    def arm_64(self):
        """Assembles and links the given input file for arm-64 Bit architecture."""
        nasm_cmd = f"aarch64-linux-gnu-as {self.input_file}"
        before_dot, _ = self.input_file.split('.', 1)
        print("[+] Object File Generated\n")
        
        ld_cmd = f"aarch64-linux-gnu-ld a.out -o {before_dot}"
        print("[+] Running The Program:\n")
        
        run_cmd = f"qemu-aarch64 ./{before_dot}"
        debug_cmd = f"qemu-aarch64 -g 1234 ./{before_dot} &"
        debug_cmd2 = f'gdb-multiarch -q -nx -ex "set architecture aarch64" -ex "file nop" -ex "target remote 127.0.0.1:1234"'
    
        try:
            subprocess.run(nasm_cmd, shell=True, check=True)
            subprocess.run(ld_cmd, shell=True, check=True)
            subprocess.run(run_cmd, shell=True)
    
            if args.debug:
                print("\n[+] Starting Debugger in:")
                for i in range(5, 0, -1):
                    sys.stdout.write(f"   {i} seconds... (CTRL+C to stop)\r")
                    sys.stdout.flush()
                    time.sleep(1)
                subprocess.run(debug_cmd, shell=True)
                subprocess.run(debug_cmd2, shell=True)
    
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.cmd}")
            exit(1)

class X86:
    def __init__(self, input_file):
        self.input_file = input_file  # Attribute

    def x86_32(self):
        """Assembles and links the given input file for x86-32 Bit architecture."""
        nasm_cmd = f"nasm -f elf32 {self.input_file}"
        before_dot, _ = self.input_file.split('.', 1)
        print("[+] Object File Generated\n")
        
        ld_cmd = f"ld -m elf_i386 {before_dot}.o -o {before_dot}"
        print("[+] Running The Program:\n")
        
        run_cmd = f"./{before_dot}"
        debug_cmd = f"gdb {before_dot}"
    
        try:
            subprocess.run(nasm_cmd, shell=True, check=True)
            subprocess.run(ld_cmd, shell=True, check=True)
            subprocess.run(run_cmd, shell=True)
    
            if args.debug:
                print("\n[+] Starting Debugger in:")
                for i in range(5, 0, -1):
                    sys.stdout.write(f"   {i} seconds... (CTRL+C to stop)\r")
                    sys.stdout.flush()
                    time.sleep(1)
                subprocess.run(debug_cmd, shell=True)
    
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.cmd}")
            exit(1)
    
    def x86_64(self):
        """Assembles and links the given input file for x86-64 Bit architecture."""
        nasm_cmd = f"nasm -f elf64 {self.input_file}"
        before_dot, _ = self.input_file.split('.', 1)
        print("[+] Object File Generated\n")
        
        ld_cmd = f"ld {before_dot}.o -o {before_dot}"
        print("[+] Running The Program:\n")
        
        run_cmd = f"./{before_dot}"
        debug_cmd = f"gdb {before_dot}"
    
        try:
            subprocess.run(nasm_cmd, shell=True, check=True)
            subprocess.run(ld_cmd, shell=True, check=True)
            subprocess.run(run_cmd, shell=True)
    
            if args.debug:
                print("\n[+] Starting Debugger in:")
                for i in range(5, 0, -1):
                    sys.stdout.write(f"   {i} seconds... (CTRL+C to stop)\r")
                    sys.stdout.flush()
                    time.sleep(1)
                subprocess.run(debug_cmd, shell=True)
    
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.cmd}")
            exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assemble and link assembly files.")
    parser.add_argument("input_file", help="Input file path")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debugging")
    parser.add_argument("-x", "--x64", action="store_true", help="Enables 64bit architecture")
    parser.add_argument("-a", "--arm", action="store_true", help="ARM architecture Default is intel x86")
    args = parser.parse_args()

    def arm_compiler():
        if args.x64:
            print("[+] ARM64 Architecture is selected.\n")
            arm = ARM(args.input_file)
            arm.arm_64()
        else:
            print("[+] Default Architecture set to ARM32.\n")
            arm = ARM(args.input_file)
            arm.arm_32()

    def x86_compiler():
        if args.x64:
            print("[+] x86-64 Architecture is selected.\n")
            x86 = X86(args.input_file)
            x86.x86_64()
        else:
            print("[+] Default Architecture set to x86-32.\n")
            x86 = X86(args.input_file)
            x86.x86_32()
    def kill_port_1234():
    #Kill any process using port 1234.
        try:
            # Find the process ID (PID) using port 1234
            #Apt install lsof
            result = subprocess.check_output("lsof -t -i:1234", shell=True)
            pid = result.decode().strip().split('\n')
            # Kill the process using the PID
            # os.kill(pid[0], signal.SIGTERM)
            # os.kill(pid[1], signal.SIGTERM)
            subprocess.run(f"kill {pid[0]}", shell=True)
            subprocess.run(f"kill {pid[1]}", shell=True)
            print(f"[+] Port 1234 closed. Process {pid} killed.")
        except subprocess.CalledProcessError:
            #print("[-] No process is using port 1234.")
            pass
        except Exception as e:
            print(f"Error while killing process on port 1234: {str(e)}")
    
        # Register the function to be called on exit
    atexit.register(kill_port_1234)


    ############################################
    #             Execution Logic              #
    ############################################
    if args.debug:
        print("[+] Debugging is enabled.\n")
    else:
        print("[-] Debugging is disabled. Use \"-d\" argument to enable it.\n")

    if args.arm:
        arm_compiler()
    else:
        x86_compiler()
