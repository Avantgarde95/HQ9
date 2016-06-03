import sys

def get_99bottles():
    lines = []

    for i in xrange(99, 0, -1):
        b = 'bottle' if i == 1 else 'bottles'
        
        lines.append(
            '%d %s of beer on the wall, %d %s of beer.\n'\
            'Take one down and pass it around, %d %s of beer on the wall.'
            % (i, b, i, b, i, b))

    lines.append('No more bottles of beer on the wall,'\
                 ' no more bottles of beer.\n'\
                 'Go to the store and buy some more,'\
                 ' 99 bottles of beer on the wall.')

    return '\n'.join(lines)

def interpret(source):
    _bottles = get_99bottles()
    
    list_insts = (c for c in source if c in ('H', 'Q', '9', '+'))
    buffer = []
    write = buffer.append

    for inst in list_insts:
        if inst == 'H':
            write('Hello, world!')
        elif inst == 'Q':
            write(source)
        elif inst == '9':
            write(_bottles)
        else:
            pass

    if len(buffer) == 0:
        pass
    else:
        print ''.join(buffer)

if __name__ == '__main__':
    argc, argv = len(sys.argv), sys.argv

    if argc < 2:
        print 'HQ9+ REPL'
        print '... Type \"exit\" to exit the program.\n'
        
        while 1:
            source = raw_input('> ')

            if source.strip() == 'exit':
                sys.exit(0)
            
            interpret(source)
    else:
        filename = argv[1]

        try:
            p = open(filename, 'r')
        except IOError:
            print 'Can\'t open the file [%s]!' % filename
            sys.exit(-1)

        source = p.read()
        interpret(source)
        p.close()

        sys.exit(0)
