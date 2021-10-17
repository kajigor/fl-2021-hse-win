#!/usr/bin/env bash
for i in tests/*.in
do
  ./parser "$i"
done
