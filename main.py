import binascii

a = open('baseball','rb')
data = binascii.b2a_hex(a.read())

class Mainclass:
    def __init__(self, arg):
        self.arg = arg
        self.e_ident = []
        self.e_ident_EICLASS = []
        self.e_ident_EIDATA = []
        self.e_ident_VERSION = []
        self.e_ident_EIOSABI = []
        self.e_type = []
        self.e_version = []
        self.e_machine = []
        self.e_entry = []
        self.e_phoff = []
        self.e_shoff = []
        self.e_ehsize = []
        self.e_phentsize = []
        self.e_phnum = []
        self.e_shentsize = []
        self.e_shnum = []
        self.e_shstrndx = []

    def finder(self):
        result = [self.arg[i:i+2] for i in range(0, len(self.arg), 2)]
        self.e_ident = [result[i] for i in range(0,4)]
        self.e_ident_EICLASS = [result[i] for i in range(4,5)]
        self.e_ident_EIDATA = [result[i] for i in range(5,6)]
        self.e_ident_VERSION = [result[i] for i in range(6,7)]
        self.e_ident_EIOSABI = [result[i] for i in range(7,8)]
        # 8~16 don't used
        self.e_type = [result[i] for i in range(16,18)]
        self.e_machine = [result[i] for i in range(18,20)]
        self.e_version = [result[i] for i in range(20,24)]
        if b"".join(self.e_ident_EICLASS).decode() == '01': # 32 bits
            self.e_entry = [result[i] for i in range(24,28)]
            self.e_phoff = [result[i] for i in range(28,32)]
            self.e_shoff = [result[i] for i in range(32,36)]
            self.e_flags = [result[i] for i in range(36,40)]
            self.e_ehsize = [result[i] for i in range(40,42)]
            self.e_phentsize = [result[i] for i in range(42,44)]
            self.e_phnum = [result[i] for i in range(44,46)]
            self.e_shentsize = [result[i] for i in range(46,48)]
            self.e_shnum = [result[i] for i in range(48,50)]
            self.e_shstrndx = [result[i] for i in range(50,52)]
        else:                                               # 64 bits
            self.e_entry = [result[i] for i in range(24,32)]
            self.e_phoff = [result[i] for i in range(32,40)]
            self.e_shoff = [result[i] for i in range(40,48)]
            self.e_flags = [result[i] for i in range(48,52)]
            self.e_ehsize = [result[i] for i in range(52,54)]
            self.e_phentsize = [result[i] for i in range(54,56)]
            self.e_phnum = [result[i] for i in range(56,58)]
            self.e_shentsize = [result[i] for i in range(58,60)]
            self.e_shnum = [result[i] for i in range(60,62)]
            self.e_shstrndx = [result[i] for i in range(62,64)]

obj = Mainclass(data)
obj.finder()

if b"".join(obj.e_ident).decode() == '7f454c46':
    e_ident = 'ELF'

if b"".join(obj.e_ident_EICLASS).decode() == '01':
    e_ident_EICLASS = '32 bits'
else:
    e_ident_EICLASS = '64 bits'

if b"".join(obj.e_ident_EIDATA).decode() == '01':
    e_ident_EIDATA = 'Little endian'
else:
    e_ident_EIDATA = 'Big endian'

if b"".join(obj.e_ident_VERSION).decode() == '01':
    e_ident_VERSION = '1 (Current)'
else:
    e_ident_EIDATA = 'Big endian'

if b"".join(obj.e_ident_EIOSABI).decode() == '00':
    e_ident_EIOSABI = 'UNIX - System V'
elif b"".join(obj.e_ident_EIOSABI).decode() == '01':
    e_ident_EIDATA = 'HP-UX'
elif b"".join(obj.e_ident_EIOSABI).decode() == '02':
    e_ident_EIDATA = 'NetBDS'
elif b"".join(obj.e_ident_EIOSABI).decode() == '03':
    e_ident_EIDATA = 'linux'
elif b"".join(obj.e_ident_EIOSABI).decode() == '04':
    e_ident_EIDATA = 'solaris'      
elif b"".join(obj.e_ident_EIOSABI).decode() == '05':
    e_ident_EIDATA = 'AIX'        
elif b"".join(obj.e_ident_EIOSABI).decode() == '06':
    e_ident_EIDATA = 'IRIX'
elif b"".join(obj.e_ident_EIOSABI).decode() == '07':
    e_ident_EIDATA = 'FreeBSD'
elif b"".join(obj.e_ident_EIOSABI).decode() == '08':
    e_ident_EIDATA = 'OpenBSD'
elif b"".join(obj.e_ident_EIOSABI).decode() == '09':
    e_ident_EIDATA = 'OpenVMS'        

if b"".join(obj.e_type).decode() == '0100':
    e_type = 'relocate'
elif b"".join(obj.e_type).decode() == '0200':
    e_type = 'EXEC'
elif b"".join(obj.e_type).decode() == '0300':
    e_type = 'share'
elif b"".join(obj.e_type).decode() == '0400':
    e_type = 'core'

if b"".join(obj.e_machine).decode() == '0000':
    e_machine = 'null'
elif b"".join(obj.e_machine).decode() == '0200':
    e_machine = 'SPARC'
elif b"".join(obj.e_machine).decode() == '0300':
    e_machine = 'x86'
elif b"".join(obj.e_machine).decode() == '0800':
    e_machine = 'MIPS'
elif b"".join(obj.e_machine).decode() == '1400':
    e_machine = 'POWER_PC'
elif b"".join(obj.e_machine).decode() == '2800':
    e_machine = 'ARM'
elif b"".join(obj.e_machine).decode() == '2A00':
    e_machine = 'supar-h'
elif b"".join(obj.e_machine).decode() == '3200':
    e_machine = 'IA-64'
elif b"".join(obj.e_machine).decode() == '3E00':
    e_machine = 'x86-64'
elif b"".join(obj.e_machine).decode() == 'B700':
    e_machine = 'AArch64'
else:
    e_machine = b''.join(obj.e_machine).decode()

e_entry = b''.join(obj.e_entry).decode().replace('00','')
e_phoff = b''.join(obj.e_phoff).decode()
e_shoff = b''.join(obj.e_shoff).decode()
e_flags = b''.join(obj.e_flags).decode()
e_ehsize = int(b''.join(obj.e_ehsize).decode().replace('00',''),16)
e_phentsize = int(b''.join(obj.e_phentsize).decode().replace('00',''),16)
e_phnum = int(b''.join(obj.e_phnum).decode().replace('00',''),16)
e_shentsize = int(b''.join(obj.e_shentsize).decode().replace('00',''),16)
e_shnum = int(b''.join(obj.e_shnum).decode().replace('00',''),16)
e_shstrndx = int(b''.join(obj.e_shstrndx).decode().replace('00',''),16)

print("ELF header : \t{}\nClass: \t\t{}\nEndian : \t{}\nCurrent : \t{}\nOS ABI : \t{}\nELF type : \t{}\nISA type : \t{}\n".format(e_ident,e_ident_EICLASS,e_ident_EIDATA,e_ident_VERSION,e_ident_EIOSABI,e_type,e_machine),end='')
print("Entry point addr : \t\t0x{}\nStart of program headers : \tx{}\nStart of section headers : \tx{}\nFlags : \t\t\t0x{}\nSize of this header :\t\t{} (bytes)\nSize of program headers : \t{} (bytes)\nNumber of program headers : \t{}\nSize of section headers : \t{}\nNumber of section headers \t{}\nSection header string table index : \t{}\n" .format(e_entry,e_phoff,e_shoff,e_flags,e_ehsize,e_phentsize,e_phnum,e_shentsize,e_shnum,e_shstrndx))
