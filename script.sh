for FILE in *.in; do
python3 hash_code.py $FILE
echo "$FILE done!"
done
