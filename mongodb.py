import csv
import pymongo


def main():
    tasks_csv = "D:\\Python\\Python101\\Tasks.csv"
    projects_csv = "D:\\Python\\Python101\\Projects.csv"

    conn = pymongo.MongoClient("mongodb://localhost:27017/")

    dbnames = conn.list_database_names()
    if "TestDB" in dbnames:
        conn.drop_database("TestDB")
    db = conn["TestDB"]

    projects_col = db["Projects"]
    with open(projects_csv, 'r') as p:
        csv_projects = csv.DictReader(p)
        projects_col.insert_many(csv_projects)

    tasks_col = db["Tasks"]
    with open(tasks_csv, 'r') as t:
        csv_tasks = csv.DictReader(t)
        tasks_col.insert_many(csv_tasks)

    query1 = tasks_col.find({"Status": "canceled"})
    for result in query1:
        project = result["Project"]

    query2 = projects_col.find({"Name": project}, {"Name": 1, "_id": 0})
    for result in query2:
        print(result)

    conn.close()


if __name__ == '__main__':
    main()


