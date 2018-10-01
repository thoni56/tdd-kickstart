SUT=hiker

all: $(SUT)_tests.so
	cgreen-runner $^

$(SUT)_tests.so: $(SUT)_tests.o $(SUT).o
	$(CC) -shared -o $@ $^ -L/usr/local/lib -lcgreen

%.o: %.c
	$(CC) $(CFLAGS) -fPIC -c -o $@ $^
