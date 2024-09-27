.global _start

.section .data
message:    .ascii "Hello, World!\n" 
len = . - message               

.section .text
_start:
    mov x8, #64              
    mov x0, #1                    
    ldr x1, =message            
    mov x2, #len
    svc 0                             
    mov x8, #93                        
    mov x0, #0                         
    svc 0                              
