for i in p256-gra-typing.py p256-type-checking.py; do
    echo "-------------------"
    echo "mypy checking $i..."
    mypy --disallow-untyped-defs $i
done
