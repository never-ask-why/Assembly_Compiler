section .data
    msg db "Hello, World!", 0xA        ; string to print with newline
    len equ $ - msg                    ; length of the string

section .text
    global _start

_start:
    mov eax, 4                         ; syscall number for sys_write (4)
    mov ebx, 1                         ; file descriptor (1 = stdout)
    mov ecx, msg                       ; pointer to the message
    mov edx, len                       ; length of the message
    int 0x80                           ; trigger system call

    mov eax, 1                         ; syscall number for sys_exit (1)
    xor ebx, ebx                       ; exit code 0
    int 0x80                           ; trigger system call
