find data/in/ -type f | xargs -n 1 ./run.sh
mv data/in/*.out data/out/
for i in {1..2}
do
    diff "data/out/$i.target" "data/out/$i.in.out"
done
