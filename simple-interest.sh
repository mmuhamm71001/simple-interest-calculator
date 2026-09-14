#!/bin/bash
#
# simple-interest.sh
# A simple Bash calculator that computes simple interest based on
# user input: principal, rate of interest, and time period.
#
# Formula:
#   Simple Interest (SI) = (P * R * T) / 100
#   Total Amount = P + SI
#

echo "=== Simple Interest Calculator ==="

read -p "Enter principal amount: " principal
read -p "Enter annual rate of interest (%): " rate
read -p "Enter time period (in years): " time

# Validate that inputs are numeric (integers or decimals)
number_re='^[0-9]+([.][0-9]+)?$'

if ! [[ $principal =~ $number_re ]] || ! [[ $rate =~ $number_re ]] || ! [[ $time =~ $number_re ]]; then
  echo "Error: Please enter valid non-negative numeric values."
  exit 1
fi

# Calculate simple interest and total amount using awk for floating point math
simple_interest=$(awk -v p="$principal" -v r="$rate" -v t="$time" 'BEGIN { printf "%.2f", (p * r * t) / 100 }')
total_amount=$(awk -v p="$principal" -v si="$simple_interest" 'BEGIN { printf "%.2f", p + si }')

echo ""
echo "Principal Amount : $principal"
echo "Rate of Interest : $rate%"
echo "Time Period      : $time year(s)"
echo "Simple Interest  : $simple_interest"
echo "Total Amount     : $total_amount"
