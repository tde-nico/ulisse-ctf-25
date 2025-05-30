from Crypto.Util.number import bytes_to_long

with open('delirivm_bytecode', 'rb') as f:
	bytecode = f.read()

DEBUG = 0

def dbg():
	while (opt := input('>> ')):
		if opt == 'r':
			for r in regs:
				print(hex(r), end=' ')
			print()
		elif opt == 'm':
			print(mem)
		elif opt == 's':
			print(stack[:rsp+1])
		elif opt == 'i':
			print('i', hex(regs[0]), 'op', op, 'mode1', mode1, 'mode2', mode2, 'reg1', reg1, 'reg2', reg2)

def r(mode, reg):
	if mode == 1:
		return regs[reg]
	elif mode == 2:
		return mem[regs[reg]]
	return reg

def w(mode, reg, val):
	if mode == 1:
		regs[reg] = val % (256*256)
		return
	mem[regs[reg]] = val % 256


def check(flag):
	global mem, regs, stack, rsp, op, mode1, mode2, reg1, reg2

	regs = [0] * 5
	mem = bytearray(bytecode)
	stack = [0] * 0x400
	rsp = 100
	for i in range(len(flag)):
		stack[rsp-i] = ord(flag[i])
	correct = 0

	i = 0
	while i < len(mem):
		mode1 = (mem[i] >> 2) & 3
		mode2 = mem[i] & 3
		op = mem[i] >> 4
		reg1 = bytes_to_long(mem[i+1:i+3][::-1])
		reg2 = bytes_to_long(mem[i+3:i+5][::-1])
		i += 5

		if DEBUG: print(hex(regs[0]), end=' ')
		if op == 0:
			tmp = r(mode2, reg2)
			if DEBUG: print('mov', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			w(mode1, reg1, tmp)
		elif op == 1:
			tmp = r(mode1, reg1) + r(mode2, reg2)
			if DEBUG: print('add', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			w(mode1, reg1, tmp)
		elif op == 2:
			tmp = r(mode1, reg1) - r(mode2, reg2)
			if DEBUG: print('sub', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			w(mode1, reg1, tmp)
		elif op == 3:
			tmp = r(mode1, reg1) ^ r(mode2, reg2)
			if DEBUG: print('xor', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			w(mode1, reg1, tmp)
		elif op == 4:
			tmp = r(mode1, reg1) & r(mode2, reg2)
			if DEBUG: print('and', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			if mode1 == 1 and reg1 == 4 and mode2 == 1:
				if tmp == 1:
					correct += 1
				else:
					return correct
			w(mode1, reg1, tmp)
		elif op == 5:
			tmp = r(mode1, reg1) | r(mode2, reg2)
			if DEBUG: print('or', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			w(mode1, reg1, tmp)
		elif op == 6:
			tmp = r(mode1, reg1) << r(mode2, reg2)
			if DEBUG: print('shl', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			w(mode1, reg1, tmp)
		elif op == 7:
			tmp = r(mode1, reg1) >> r(mode2, reg2)
			if DEBUG: print('shr', ['const', 'reg', 'mem'][mode1], reg1, ['const', 'reg', 'mem'][mode2], tmp)
			w(mode1, reg1, tmp)
		elif op == 8:
			if DEBUG: print('exit')
			break
		elif op == 9:
			tmp = r(mode1, reg1)
			if DEBUG: print('call', tmp)
			ret_addr = i
			i = tmp
		elif op == 10:
			if DEBUG: print('ret', ret_addr)
			i = ret_addr
		elif op == 11:
			r1, r2 = r(mode1, reg1), r(mode2, reg2)
			if DEBUG: print('cmp', reg1, reg2, r1, r2, r1 == r2)
			w(mode1, reg1, r1 == r2)
		elif op == 12:
			tmp = r(mode1, reg1)
			if DEBUG: print('jmp', tmp)
			i = tmp
		elif op == 13:
			r1, r2 = r(mode2, reg1), r(mode1, reg2)
			if DEBUG: print('jz', r2==0, r1)
			if r2 == 0:
				i = r1
		elif op == 14:
			tmp = r(mode1, reg1)
			if DEBUG: print('push', ['const', 'reg', 'mem'][mode1], tmp)
			rsp += 1
			stack[rsp] = tmp
		elif op == 15:
			if DEBUG: print('pop', ['const', 'reg', 'mem'][mode1], reg1, stack[rsp])
			w(mode1, reg1, stack[rsp])
			rsp -= 1

		else:
			print('Not Implemented', op, mode1, mode2, reg1, reg2)
			exit(1)

		regs[0] = i
	
	print('END')
	return correct


from string import printable
flag = ''
for i in range(40):
	for char in printable:
		print(flag + char)
		num = check(flag + char)
		if num == len(flag)+1:
			flag += char
			break

# UlisseCTF{d1d_y0u_r34lly_und3rst4nd_1t?}
