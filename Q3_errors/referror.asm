section .data
  Array db "101","sff",10
  four dd 4
  msg db 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',10,0
  a dw 1
section .bss
  AA resb 1
  v resb 1
  c resd 1
  d resb 1
section .text
  mov ax,ecx
  mov ecx,eax
  mov eax,3
  mov eax, 3
  mov al, 128
  mov ah,128
lsd: mov al,ah
  mov al,ah
o: mov al,ah
mov dword[ecx],gf
mov a,dword[ecx]
mov dword[ecx+eax*4],ecx
g: mov dword[g+eax*4],ecx
mov dword[a],ecx
mov dword[ecx+ecx*8],ecx
mov dword[eax+esp*1],ecx
mov ecx,dword[eax+esp*1]
mov dword[ecx+a],a
mov dword[ecx+a],ecx
mov dword[a+ecx],a
mov ecx,dword[ecx+a]
mov dword[ecx+a],ecx
mov dword[a],ecx
mov dword[a+ecx],eax
mov ecx,dword[eax]
mov ecx,dword[eax*0]
mov ecx,dword[eax*10]
mov ecx,dword[eax*2]
mov ecx,[ecx*9]
mov [ecx],ecx
mov [a],cx
mov [a],ecx
push dword[ecx*8]
inc 3
inc a
dec ecx
jmp dword[ecx*8]
