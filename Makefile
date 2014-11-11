#archivo makefile para creacion de ejecutables

#definicion de variables
PATH=/home/calc/Proyecto3/clantontoolchain/sysroots/i686-pokysdk-linux/usr/bin:/home/calc/Proyecto3/clantontoolchain/sysroots/i686-pokysdk-linux/usr/bin/i586-poky-linux:$PATH

CC=i586-poky-linux-gcc  -m32 -march=i586 --sysroot=/home/calc/Proyecto3/clantontoolchain/sysroots/i586-poky-linux
LD=i586-poky-linux-ld   --sysroot=/home/calc/Proyecto3/clantontoolchain/sysroots/i586-poky-linux
#HEADER=$(APP).h
SRC= hello.c
#INCLUDEDIR=../include
CFLAGS= -O #-L$(LIBDIR)#-I$(INCLUDEDIR) 
#LIBDIR=../lib
BINDIR=../bin
#DYNAMIC=libhello.so

# se incluye operaciones.h como dependencia
#_DEPS = $(HEADER)
#		DEPS = $(patsubst %,$(INCLUDEDIR)/%,$(_DEPS))

#se incluye el directorio de operaciones.o
#_OBJS=$(APP).o
	#	OBJS= $(patsubst %, $(LIBDIR)/%,$(_OBJS))

#se incluye el directorio de las librerias
#LIB_D= $(patsubst %, $(LIBDIR)/%,$(DYNAMIC))
	
#se crea la aplicacion calculadora_d en el directorio bin 
#calc2: $(OBJS)
	#	$(CC) -o $(BINDIR)/hola $(CFLAGS) $(SRC) -Bdynamic $(LIB_D)

hello: hello.o
			$(CC) -o $(BINDIR)/hola $(CFLAGS) $(SRC)

hello.o: hello.c 
			$(CC) -c $(SRC)
clean:
			rm hello \
			hello.o 
