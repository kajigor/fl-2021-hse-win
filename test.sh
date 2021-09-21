find in/ -type f | xargs -n 1 ./lex.py
mv in/*.out out/
for i in {1..3}
do
    diff "out/$i.target" "out/$i.test.out"
done
