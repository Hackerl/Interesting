string='\x67,\x6e,\x62,\x63,\x7e,\x74,\x62,\x69,\x6d,\x55,\x6a,\x7f,\x60,\x51,\x66,\x63,\x4e,\x66,\x7b,\x71,\x4a,\x74,\x76,\x6b,\x70,\x79,\x66,\x1c'
string=string.split(',')
result=""
for j in range(1,29):
    data=bin(ord(string[j-1]))[2:]
    data1=bin(j)[2:]
    data2='0'*(len(data)-len(data1))+data1
    data3=''
    for n in range(len(data)):
        if(data[n]==data2[n]):
            data3+='0'
        else:
            data3+='1'
    result+=chr(int(data3,2))
print result

"""
int main(int argc, char const *argv[])
{
  char input[] = {0x0,  0x67, 0x6e, 0x62, 0x63, 0x7e, 0x74, 0x62, 0x69, 0x6d,
                  0x55, 0x6a, 0x7f, 0x60, 0x51, 0x66, 0x63, 0x4e, 0x66, 0x7b,
                  0x71, 0x4a, 0x74, 0x76, 0x6b, 0x70, 0x79, 0x66 , 0x1c};
  func(input, 28);
  printf("%s\n",input+1);
  return 0;
}


00000000004004e6 <func>:
  4004e6: 55                    push   rbp            //保存上次的rbp
  4004e7: 48 89 e5              mov    rbp,rsp        //使rbp指向rsp
  
  4004ea: 48 89 7d e8           mov    QWORD PTR [rbp-0x18],rdi     
  4004ee: 89 75 e4              mov    DWORD PTR [rbp-0x1c],esi
  4004f1: c7 45 fc 01 00 00 00  mov    DWORD PTR [rbp-0x4],0x1
  
  4004f8: eb 28                 jmp    400522 <func+0x3c>      --->跳转到400522
  
  4004fa: 8b 45 fc              mov    eax,DWORD PTR [rbp-0x4]                          跳转到此处 eax置于1
  
  4004fd: 48 63 d0              movsxd rdx,eax                                          带符号拓展传送    rdx=000000000000000000001
  
  400500: 48 8b 45 e8           mov    rax,QWORD PTR [rbp-0x18]                         rax置于rdi
  
  400504: 48 01 d0              add    rax,rdx                                          rax加rdx    rax=  rdi+1
  
  400507: 8b 55 fc              mov    edx,DWORD PTR [rbp-0x4]                          edx置于1
  
  40050a: 48 63 ca              movsxd rcx,edx                                          rcx置于edx    rcx=00000000000001
  
  40050d: 48 8b 55 e8           mov    rdx,QWORD PTR [rbp-0x18]                         rdx置于rdi
  
  400511: 48 01 ca              add    rdx,rcx                                          rdx加rcx=rdi   rdx= 1+rdi
  
  400514: 0f b6 0a              movzx  ecx,BYTE PTR [rdx]                               ecx 置于           ecx=[1+rdi]
  
  400517: 8b 55 fc              mov    edx,DWORD PTR [rbp-0x4]                          edx置于0x1         edx=1
  
  40051a: 31 ca                 xor    edx,ecx                                          1和ecx= [1+rdi]   抑或     1 [1+rdi] 抑或
  
  40051c: 88 10                 mov    BYTE PTR [rax],dl                                [rdi+1]  置于  1 [1+rdi] 抑或  将[1+rdi] 第一位翻转 1变0 0变1
  
  40051e: 83 45 fc 01           add    DWORD PTR [rbp-0x4],0x1                          [rbp-0x4]置为2
  
  
  400522: 8b 45 fc              mov    eax,DWORD PTR [rbp-0x4]         // eax置为1
  400525: 3b 45 e4              cmp    eax,DWORD PTR [rbp-0x1c]        // 1 与 esi 比较   小于或等于跳转4004fa
  400528: 7e d0                 jle    4004fa <func+0x14>
  40052a: 90                    nop
  40052b: 5d                    pop    rbp
  40052c: c3                    ret
"""

