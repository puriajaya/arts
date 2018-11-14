from __future__ import print_function

import sys
from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: wordcount <file>", file=sys.stderr)
        sys.exit(-1)

    spark = SparkSession\
        .builder\
        .appName("SparkTestBasic")\
        .getOrCreate()

    lines = spark.read.text(sys.argv[1])
    print("Number of rows:",lines.count())
    print("First five rows:\n",lines.take(5))

# Run Sript
# ./spark-submit --master spark://gov:7077\
#  /home/nepal/Documents/work/thesis-file/csv_read.py\
#   /home/nepal/Documents/work/todo/train.csv
