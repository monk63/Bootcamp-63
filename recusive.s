int fact(int n ){
  if (n < 1) return (1):
 else return (n * fact(n-1)):
}

/*
dosseg
.model small
.stack 100h
.data
.code

main proc
mov dl,'5'
mov ah,2
int 21 h

mov ah,4ch
int 21ch
main endp
end main   
*/
