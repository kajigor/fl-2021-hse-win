#!/usr/bin/env bash

javac Main.java

for TEST in test-data/*.in; do
  TEST="$(basename "$TEST" .in)"
  java Main.java "test-data/$TEST.in" "test-data/$TEST.out"
  if [ -n "$(cmp "test-data/$TEST.out" "test-data/$TEST.expected")" ]; then
    echo "test #$TEST: FAILED"
  else
    echo "test #$TEST: OK"
  fi
done
