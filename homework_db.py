import argparse
import csv
import os
import sqlite3

# python homework_db.py -db D:\Python\Python101\TestDB.db -csv_projects D:\Python\Python101\Projects.csv -csv_tasks D:\Python\Python101\Tasks.csv -project Python101


def create_db(db_file):
    if os.path.isfile(db_file):
        os.remove(db_file)
    con = sqlite3.connect(db_file)
    return con


def create_tables(con, projects_file, tasks_file):
    cur = con.cursor()
    cur.execute('''CREATE TABLE Projects
                  ([Name] text,
                   [Description] text,
                   [Deadline] date)''')
    cur.execute('''CREATE TABLE Tasks
                  ([Id] number,
                   [Priority] integer,
                   [Details] text,
                   [Status] text,
                   [Deadline] date,
                   [Completed] date,
                   [Project] text)''')

    with open(projects_file,'r') as f:
        projects_data = csv.DictReader(f)
        to_db1 = [(i['Name'], i['Description'], i['Deadline'])
                  for i in projects_data]

    cur.executemany('''INSERT INTO Projects (Name, Description, Deadline)
                       VALUES (?, ?, ?);''', to_db1)

    with open(tasks_file,'r') as f:
        tasks_data = csv.DictReader(f)
        to_db2 = [(i['Id'], i['Priority'], i['Details'], i['Status'],
                   i['Deadline'], i['Completed'], i['Project'])
                  for i in tasks_data]

    cur.executemany('''INSERT INTO Tasks (Id, Priority, Details, Status, 
                                          Deadline, Completed, Project)
                       VALUES (?, ?, ?, ?, ?, ?, ?);''', to_db2)


def project_query(con, project):
    cur = con.cursor()
    cur.execute('''SELECT Name, Details, Status
                   FROM Projects
                   LEFT JOIN Tasks
                   ON Name = Project
                   WHERE Project = ?''', (project,))
    formatted_result = [f"{name:<13}{details:<13}{status:>6}"
                        for name, details, status in cur.fetchall()]
    name, details, status = "ProjectName", "TaskDetails", "Status"
    print('\n'.join([f"{name:<13}{details:<13}{status:>8}"]+formatted_result))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-db','--db_file', help='DB file', required=True)
    parser.add_argument('-csv_projects','--csv_projects', help='Projects.csv', required=True)
    parser.add_argument('-csv_tasks','--csv_tasks', help='Tasks.csv', required=True)
    parser.add_argument('-project','--project', help='Project name', required=True)
    args = vars(parser.parse_args())

    db_file = args['db_file']
    projects_file = args['csv_projects']
    tasks_file = args['csv_tasks']
    project = args['project']

    con = create_db(db_file)
    create_tables(con, projects_file, tasks_file)
    project_query(con, project)

    con.commit()
    con.close()


if __name__ == '__main__':
    main()
