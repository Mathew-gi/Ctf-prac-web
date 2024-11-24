import random

def vm(bytecode, user_input):
    stack = []
    pc = 0
    flag = ""

    key = 0x5A
    bytecode = [b ^ key for b in bytecode]

    while pc < len(bytecode):
        instr = bytecode[pc]
        
        if instr == 0x01:
            pc += 1
            stack.append(bytecode[pc])
        
        elif instr == 0x02:
            a = stack.pop()
            b = stack.pop() 
            stack.append(a + b)
        
        elif instr == 0x03:
            pc += 1
            expected_len = bytecode[pc]
            expected = "".join(chr(bytecode[pc + 1 + i]) for i in range(expected_len))
            if user_input != expected:
                print("Wrong input!")
                return
            pc += expected_len
        
        elif instr == 0x04:
            pc += 1
            pc = bytecode[pc] - 1
        
        elif instr == 0x05:
            word = "".join(chr(stack.pop(0)) for _ in range(bytecode[pc + 1]))
            flag += word
            pc += 1
        
        elif instr == 0x07:
            pass
        
        elif instr == 0x08:
            a = stack.pop()
            b = stack.pop()
            stack.append(a ^ b)
        
        elif instr == 0x09:
            print(f"FLAG: {flag}")
            return
        
        pc += 1

def encrypt_bytecode(bytecode, key):
    return [b ^ key for b in bytecode]

original_bytecode = [
    0x03, 6,
    0x61, 0x63, 0x63, 0x65, 0x73, 0x73,
    0x01, 99, 0x01, 116, 0x01, 102, 0x01, 123,
    0x05, 4,
    0x01, 118, 0x01, 109, 0x01, 95, 0x01, 112,
    0x05, 4,
    0x01, 117, 0x01, 122, 0x01, 122, 0x01, 108,
    0x05, 4,
    0x01, 101, 0x01, 95, 0x01, 109, 0x01, 97,
    0x05, 4,
    0x01, 99, 0x01, 104, 0x01, 49, 0x01, 110,
    0x05, 4,
    0x01, 51, 0x01, 125,
    0x05, 2,
    0x09
]

key = 0x5A
encrypted_bytecode = encrypt_bytecode(original_bytecode, key)

print("Input the secret key to unlock the flag:")
user_input = input()
vm(encrypted_bytecode, user_input)
