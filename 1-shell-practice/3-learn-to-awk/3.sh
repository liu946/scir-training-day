awk 'BEGIN{RS=" "}{split($0, array, "_"); print array[1]}' 3.dat
