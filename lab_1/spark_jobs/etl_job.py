from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper

def main():
    spark = SparkSession.builder \
        .appName('ETL Job') \
        .getOrCreate()

    # Загрузка данных из CSV-файла
    input_filepath = "/path_to_your_directory/people.csv"  # Укажите путь до вашего CSV-файла
    people_df = spark.read.csv(input_filepath, header=True, inferSchema=True)

    # Преобразование данных: приведение имен к верхнему регистру
    transformed_people_df = people_df.withColumn("name", upper(col("name")))

    # Сохранение преобразованных данных в новый CSV-файл
    output_filepath = "/path_to_your_directory/people_transformed.csv"  # Укажите, куда сохранить результат
    transformed_people_df.write.csv(output_filepath, header=True, mode="overwrite")

    spark.stop()

if __name__ == "__main__":
    main()
