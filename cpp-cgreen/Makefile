SUT=Hiker

CFLAGS=-I/usr/local/include

all: $(SUT)Tests.so
	cgreen-runner $^

$(SUT)Tests.so: $(SUT)Tests.o $(SUT).o
	$(CXX) -shared -o $@ $^ -L/usr/local/lib -lcgreen

%.o: %.cpp
	$(CXX) $(CFLAGS) -fPIC -c -o $@ $^
