CC=gcc
FORTRAN=gfortran
FFLAGS= -O3 -fPIC
CFLAGS= -std=c99 -O3 -fPIC

SOURCES= moid_v4_fun.f
OBJECTS=$(SOURCES:.f=.o)

all: $(SOURCES) libmoid.so

%.o: %.f
	@echo "Compiling source file $< ..."
	$(FORTRAN) -c $(FFLAGS) -o $@ $<

libmoid.so: $(OBJECTS)
	@echo ""
	@echo "Linking shared library $@ ..."
	$(FORTRAN) $(FFLAGS) -shared $(OBJECTS) -o $@

	@echo ""
	@echo "The shared library $< has been created successfully."

clean:
	@echo "Removing object files *.o ..."
	@-rm -f *.o
	@echo "Removing shared library libmoid.so ..."
	@-rm -f *.so
