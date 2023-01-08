for i in p262.py ; do
    echo "-------------------"
    echo "mypy checking $i..."
    mypy  $i
done
