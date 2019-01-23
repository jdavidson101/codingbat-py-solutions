#!/bin/sh

cd Warmup-1/unit_tests
echo "Warmup-1 Tests"
python3 -m unittest
cd ..
cd ..
cd String-1/unit_tests
echo "\nString-1 Tests"
python3 -m unittest