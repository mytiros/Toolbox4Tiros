FC = gfortran 

SUBROUTINE = Nonequilib.f Thermo.f Evaprate.f Liquiddistrib.f Molweight.f  VLE.f
SUBOBJS = $(SUBROUTINE:.f=.o)

SOURCE = main.f 
OBJS = $(SOURCE:.f=.o)
TARGET = main.x

MODSOURCE = Modcom.f 
MODOBJS = $(MODSOURCE:.f=.o)
MODS = $(MODSOURCE:.f=.mod)

$(TARGET) : $(OBJS) $(SUBOBJS) $(MODOBJS)
	$(FC) -o $(TARGET) $(OBJS) $(SUBOBJS) $(MODOBJS)

$(OBJS) : $(SOURCE) $(MODS)
	$(FC) -O -c $<

$(MODS) $(MODOBJS) : $(MODSOURCE)
	$(FC) -O -c $^ 

$(SUBOBJS) : $(SUBROUTINE)
	$(FC) -c $^

# Debug purpose
all:
	@echo $(OBJS)
	@echo $(MODOBJS)
	@echo $(SUBOBJS)

run:
	./$(TARGET)

clean:
	rm *.mod
	rm *.o
	rm *.x
