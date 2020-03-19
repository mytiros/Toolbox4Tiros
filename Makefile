FC = gfortran

SOURCE = main.f90
OBJS = $(SOURCE:.f90=.o)
TARGET = main.x

MODSOURCE = constant.f90 calculate.f90
MODOBJS = $(MODSOURCE:.f90=.o)
MODS = $(MODSOURCE:.f90=.mod)

$(TARGET) : $(OBJS) $(MODOBJS)
	$(FC) -o $(TARGET) $(OBJS) $(MODOBJS)

$(OBJS) : $(SOURCE) $(MODS)
	$(FC) -O -c $<

$(MODS) $(MODOBJS) : $(MODSOURCE)
	$(FC) -O -c $^ 

# Debug purpose
all:
	@echo $(OBJS)
	@echo $(MODOBJS)

run:
	$./$(TARGET)

clean:
	rm *.mod
	rm *.o
	rm *.x
