for i in p256.py p256-0.py; do
    echo "-------------------"
    echo "mypy checking $i..."
    mypy --disallow-untyped-defs $i
done
