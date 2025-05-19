from dotenv import load_dotenv
from langchain.tools import tool
import mysql.connector
from mysql.connector import Error
import os

load_dotenv()
mysql_host = os.getenv("MYSQL_HOST")
mysql_user = os.getenv("MYSQL_USER")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_database = os.getenv("MYSQL_DATABASE")

connection = mysql.connector.connect(
    host=mysql_host,
    user=mysql_user,
    password=mysql_password,
    database=mysql_database
)


@tool
def find_name_percentage(reg_no: str) -> str:
    """Takes a registration number and returns the name and percentage of the student if found."""
    if connection is None:
        return "❌ No database connection."

    try:
        print("==>>> ", type(reg_no),reg_no)
        reg_no = reg_no.strip()
        print("==>>> ", type(reg_no))
        cursor = connection.cursor()
        query = "SELECT name, percentage FROM student WHERE regno =%s"
        cursor.execute(query, (reg_no,))
        result = cursor.fetchone()
        print(result)

        if result:
            name, percentage = result
            # print("Query executed -->> ", name, "==>> ", percentage)
            return f"Name: {name}, Percentage: {percentage}%"
        else:
            return "Oops! Student not found!"
    except Error as e:
        return f"❌ Error executing query: {e}"


@tool
def find_avg_of_total(class_id: int) -> str:
    """Takes student class as a integer input and returns the average of the totals of all students in a class ."""
    if connection is None:
        return "❌ No database connection."

    try:
        print("==>>. ", class_id)
        cursor = connection.cursor()
        cursor.execute("SELECT AVG(total) FROM student WHERE class = %s", (class_id,))
        avg_total = cursor.fetchone()[0]
        print("==>>. ", avg_total)

        if avg_total:
            print("==>>. ", avg_total)
            return f"Average of class: {class_id} is : {avg_total}"
        else:
            return "Oops! class not found!"
    except Error as e:
        return f"❌ Error executing query: {e}"


@tool
def grade_the_class_based_on_average(avg: float):
    """ Takes the average of total of a class as float input and finds the grade the class performance"""
    avg = float(avg)
    if avg > 500:
        return "The grade of the class is : 'A+' "
    elif avg > 400:
        return "The grade of the class is: 'B+' "
    else:
        return "The grade of the class is: C"


def close_connection():
    if connection and connection.is_connected():
        connection.close()
        print("🔒 MySQL connection closed.")
