
import pymongo
from flask import Flask, request, render_template, jsonify
import pandas as pd
from sqlalchemy import create_engine , text
import traceback
import os ,sys
import json
import pymongo as pm
from cassandra.cluster import  Cluster
from cassandra.auth import  PlainTextAuthProvider
from cassandra.concurrent import  execute_concurrent_with_args


app = Flask(__name__)


def parse_json_field(value, field_name):
    if value is None or value == "":
        return None
    if isinstance(value, dict):
        return value
    if isinstance(value, str):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in {field_name}")
    raise ValueError(f"{field_name} must be a JSON object")


def parse_cassandra_contact(host, port=None):
    host = (host or "").strip()
    if not host:
        raise ValueError("Cassandra host is required (e.g. 127.0.0.1 or localhost)")

    if ":" in host:
        host_part, _, port_part = host.rpartition(":")
        host = host_part.strip()
        if port_part.strip().isdigit():
            port = int(port_part.strip())

    if port is not None:
        port = int(port)
    else:
        port = 9042

    return host, port


@app.route("/" , methods=['POST' , 'GET'])
def home():
    return render_template("index.html")

#mysql
@app.route("/mysql" , methods=['POST'])
def mysql_operation():
    if request.method == 'POST':
        # Handle both JSON and multipart/form-data
        if request.content_type and 'multipart/form-data' in request.content_type:
            mysql_operation = request.form.get('mysql_operation')
            mysql_username = request.form.get('mysql_username')
            mysql_password = request.form.get('mysql_password')
            mysql_host = request.form.get('mysql_host')
            mysql_port = request.form.get('mysql_port')
            mysql_database_name = request.form.get('mysql_database_name')
            mysql_update_query = request.form.get('mysql_update_query')
            mysql_delete_query = request.form.get('mysql_delete_query')
            mysql_create_query = request.form.get('mysql_create_query')
            mysql_insert_query = request.form.get('mysql_insert_query')
            mysql_fetch_query = request.form.get('mysql_fetch_query')
            mysql_table_name = request.form.get('mysql_table_name')
           
        else:
            data = request.get_json()
            mysql_operation = data.get('mysql_operation')
            mysql_username = data.get('mysql_username')
            mysql_password = data.get('mysql_password')
            mysql_host = data.get('mysql_host')
            mysql_port = data.get('mysql_port')
            mysql_database_name = data.get('mysql_database_name')
            mysql_update_query = data.get('mysql_update_query')
            mysql_delete_query = data.get('mysql_delete_query')
            mysql_create_query = data.get('mysql_create_query')
            mysql_insert_query = data.get('mysql_insert_query')
            mysql_fetch_query = data.get('mysql_fetch_query')
            mysql_table_name = data.get('mysql_table_name')
          
        try:
            url = f"mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}"
            engine = create_engine(url)
            with engine.begin() as conn:
                conn.execute(text(f"CREATE DATABASE IF NOT EXISTS {mysql_database_name}"))
            url = f"mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_host}:{mysql_port}/{mysql_database_name}"
            engine = create_engine(url)

            if mysql_operation == "create":
                with engine.begin() as conn:
                    conn.execute(text(mysql_create_query))

                return  f"{mysql_table_name} created successfully"

            elif mysql_operation == "insert":
                with engine.begin() as conn:
                    conn.execute(text(mysql_insert_query))

                return f"Value inserted into {mysql_table_name} successfully"

            elif mysql_operation == "update":
                with engine.begin() as conn:
                    conn.execute(text(mysql_update_query))

                return f"{mysql_table_name} updated successfully"

            elif mysql_operation == "bulk":

                mysql_file = request.files.get('mysql_file')

                if mysql_file is None:
                    return "No file uploaded"
    
                df = pd.read_csv(mysql_file).dropna()

                df.to_sql(
                    mysql_table_name,
                    engine,
                    if_exists="append",
                    index=False
                )

                return f"Bulk insertion into {mysql_table_name} is successful"

            elif mysql_operation == "delete":
                with engine.begin() as conn:
                    conn.execute(text(mysql_delete_query))

                return  f"Deleted from {mysql_table_name} Successfull"

            elif mysql_operation == "download":
                # Save to project directory for easier access
                project_dir = os.path.dirname(os.path.abspath(__file__))
                download_dir = os.path.join(project_dir, "downloads")
                os.makedirs(download_dir, exist_ok=True)
                path = os.path.join(download_dir, mysql_table_name + '.csv')
                df = pd.read_sql(f"SELECT * FROM {mysql_table_name}", engine)
                df.to_csv(path, index=False)
                return f"Table successfully downloaded at: {path}"

        except Exception as e:
            return traceback.format_exc()

#mongodb
@app.route("/mongodb" , methods=['POST'])
def mongodb_mysql_mongodb_operation():
    # Handle both JSON and multipart/form-data
    if request.content_type and 'multipart/form-data' in request.content_type:
        mongo_url = request.form.get('mongo_url')
        mongodb_operation = request.form.get('mongodb_operation')
        mongodb_database_name = request.form.get('mongodb_database_name')
        mongodb_update_query1 = request.form.get('mongdb_update_query1')
        mongodb_update_query2 = request.form.get('mongodb_update_query2')
        mongodb_delete_query = request.form.get('mongodb_delete_query')
        mongodb_collection_name = request.form.get('mongodb_collection_name')
        mongodb_data = request.form.get('mongodb_data')
        mongodb_file = request.files.get('mongodb_file')
    else:
        data = request.get_json()
        mongo_url = data.get('mongo_url')
        mongodb_operation = data.get('mongodb_operation')
        mongodb_database_name = data.get('mongodb_database_name')
        mongodb_update_query1 = data.get('mongdb_update_query1')
        mongodb_update_query2 = data.get('mongodb_update_query2')
        mongodb_delete_query = data.get('mongodb_delete_query')
        mongodb_collection_name = data.get('mongodb_collection_name')
        mongodb_data = data.get('mongodb_data')
        mongodb_file = data.get('mongodb_file')


    try:
        client = pymongo.MongoClient(mongo_url)
        if mongodb_operation in ['create' , 'insert']:
            mongodb_data = parse_json_field(mongodb_data, "JSON Data")
            if not isinstance(mongodb_data, dict):
                return 'Data should be a dictionary'
            if mongodb_data:
                client[mongodb_database_name][mongodb_collection_name].insert_one(mongodb_data)
                return f"Data inserted successfully"
            else:
                return "Data should not be empty"

        elif mongodb_operation == "update":
            mongodb_update_query1 = parse_json_field(mongodb_update_query1, "Filter Query")
            mongodb_update_query2 = parse_json_field(mongodb_update_query2, "Update Query")
            client[mongodb_database_name][mongodb_collection_name].update_many(mongodb_update_query1 , mongodb_update_query2)
            return  f"Data updated successfully"

        elif mongodb_operation == 'bulk':
            mongodb_file = request.files.get('mongodb_file')

            if mongodb_file is None:
                return "No file uploaded"

            df = pd.read_csv(mongodb_file).dropna()
            mongodb_data_dict = df.to_dict(orient='records')
            client[mongodb_database_name][mongodb_collection_name].insert_many(mongodb_data_dict)
            return  f"Bulk insertion into {mongodb_collection_name} is successful"

        elif mongodb_operation == 'delete':
            mongodb_delete_query = parse_json_field(mongodb_delete_query, "Delete Query")
            client[mongodb_database_name][mongodb_collection_name].delete_many(mongodb_delete_query)
            return  f"Data successfully deleted"

        elif mongodb_operation == 'download':
            coll_data= list(client[mongodb_database_name][mongodb_collection_name].find())
            df = pd.DataFrame(coll_data)
            # Save to project directory for easier access
            project_dir = os.path.dirname(os.path.abspath(__file__))
            download_dir = os.path.join(project_dir, "downloads")
            os.makedirs(download_dir, exist_ok=True)
            path = os.path.join(download_dir, mongodb_collection_name + '.csv')
            df.to_csv(path, index=False)
            return f"Data successfully downloaded at: {path}"

    except ValueError as e:
        return str(e)
    except Exception as e:
        return traceback.format_exc()


#cassandra
@app.route("/cassandra" , methods=['POST'])
def cassandra_operation():
        # Handle both JSON and multipart/form-data
        if request.content_type and 'multipart/form-data' in request.content_type:
            cassandra_operation = request.form.get('cassandra_operation')
            cassandra_host = request.form.get('cassandra_host')
            cassandra_port = request.form.get('cassandra_port')
            cassandra_keyspace_name = request.form.get('cassandra_keyspace_name')
            cassandra_table_name = request.form.get('cassandra_table_name')
            cassandra_file = request.files.get('cassandra_file')
            cassandra_update_query = request.form.get('cassandra_update_query')
            cassandra_insert_query = request.form.get('cassandra_insert_query')
            cassandra_delete_query = request.form.get('cassandra_delete_query')
            cassandra_create_query = request.form.get('cassandra_create_query')
            cassandra_fetch_query = request.form.get('cassandra_fetch_query')
        else:
            data = request.get_json()
            cassandra_operation = data.get('cassandra_operation')
            cassandra_host = data.get('cassandra_host')
            cassandra_port = data.get('cassandra_port')
            cassandra_keyspace_name = data.get('cassandra_keyspace_name')
            cassandra_table_name = data.get('cassandra_table_name')
            cassandra_file = data.get('cassandra_file')
            cassandra_update_query = data.get('cassandra_update_query')
            cassandra_insert_query = data.get('cassandra_insert_query')
            cassandra_delete_query = data.get('cassandra_delete_query')
            cassandra_create_query = data.get('cassandra_create_query')
            cassandra_fetch_query = data.get('cassandra_fetch_query')

        try:
            contact_host, contact_port = parse_cassandra_contact(
                cassandra_host,
                cassandra_port,
            )
            cluster = Cluster([contact_host], port=contact_port)
            session = cluster.connect()

            if cassandra_operation == "create":
                query = (
                        "CREATE KEYSPACE IF NOT EXISTS " +
                        cassandra_keyspace_name +
                        " WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}"
                )

                session.execute(query)
                session.set_keyspace(cassandra_keyspace_name)
                session.execute(cassandra_create_query)
                return  f"{cassandra_table_name} created successfully"

            elif cassandra_operation == "insert":
                session.set_keyspace(cassandra_keyspace_name)
                session.execute(cassandra_insert_query)
                return f"Value inserted into {cassandra_table_name} successfully"

            elif cassandra_operation == "update":
              session.set_keyspace(cassandra_keyspace_name)
              session.execute(cassandra_update_query)
              return f"{cassandra_table_name} updated successfully"

            elif cassandra_operation == "bulk":
                cassandra_file = request.files.get('cassandra_file')

                if cassandra_file is None:
                    return "No file uploaded"
                print(cassandra_file)
                df = pd.read_csv(cassandra_file).dropna()
                print(df.columns)
               
                columns = list(df.columns)
                print(columns)
                query = (
                        "CREATE KEYSPACE IF NOT EXISTS " +
                        cassandra_keyspace_name +
                        " WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}"
                )
                print(df.info())
                session.execute(query)
                session.set_keyspace(cassandra_keyspace_name)
                print(cassandra_create_query)
                session.execute(cassandra_create_query)
                query = f"""
                                INSERT INTO {cassandra_table_name} ({','.join(columns)})
                                VALUES ({','.join(['?' for _ in columns])})
                                """
                
                prepared = session.prepare(query)
               
                args = [tuple(row) for row in df[columns].values]
                execute_concurrent_with_args(session, prepared, args)
                return f"Bulk insertion into {cassandra_table_name} is successful"


            elif cassandra_operation == "delete":
                session.set_keyspace(cassandra_keyspace_name)
                session.execute(cassandra_delete_query)
                return  f"Deleted from {cassandra_table_name} Successfull"

            elif cassandra_operation == "download":
                # Save to project directory for easier access
                project_dir = os.path.dirname(os.path.abspath(__file__))
                download_dir = os.path.join(project_dir, "downloads")
                os.makedirs(download_dir, exist_ok=True)
                path = os.path.join(download_dir, cassandra_table_name + '.csv')
                session.set_keyspace(cassandra_keyspace_name)
                rows =session.execute(f"SELECT * FROM {cassandra_table_name}")
                result = [row._asdict() for row in rows]
                df  = pd.DataFrame(result)
                df.to_csv(path, index=False)
                return f"Downloaded {cassandra_table_name} at path: {path}"

            elif cassandra_operation == "fetch":
                session.set_keyspace(cassandra_keyspace_name)
                rows = session.execute(cassandra_fetch_query)
                result = [row._asdict() for row in rows]

                return jsonify(result)

        except ValueError as e:
            return str(e)
        except Exception as e:
            return traceback.format_exc()
if __name__ == "__main__":
    app.run(debug=False , use_reloader=False)