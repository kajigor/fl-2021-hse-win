cmake .
make
for i in tests/*.in
do
	./main "$i"
done
