section .data
    msg db "Hello, World!", 0xA        ; string to print with newline
    len equ $ - msg                    ; length of the string

section .text
    global _start

_start:
    mov rax, 1                         ; syscall number for sys_write (1)
    mov rdi, 1                         ; file descriptor (1 = stdout)
    mov rsi, msg                       ; pointer to the message
    mov rdx, len                       ; length of the message
    syscall                            ; trigger system call

    mov rax, 60                        ; syscall number for sys_exit (60)
    xor rdi, rdi                       ; exit code 0
    syscall                            ; trigger system call
