import psycopg 
from pymongo import MongoClient


def create_connection_sql():
    """Establish connection to the PostgreSQL database."""
    try:
        connection = psycopg.connect(
            dbname="sql_db", user="user", password="password", host="localhost", port="5432"
        )
        return connection
    except Exception as e:
        print(f"Error: Unable to connect to the database: {e}")
        return None

def create_connection_nosql():
    """Establish connection to the MongoDB database."""
    try:
        client = MongoClient('mongodb://root:password@localhost:27017/')
        return client
    except Exception as e:
        print(f"Error: Unable to connect to the database: {e}")
        return None

def join_data_from_both(locations,connection,table_name="locations"):
    """Fetch from both and output in one print"""
    try:
        cursor = connection.cursor()
        location_list = locations.find()
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
        if rows:
            column_names = [desc[0] for desc in cursor.description]
            print(f"{' | '.join(column_names)}")
            print("-" * 50)
            for row in rows:
                print(" | ".join(str(item) for item in row))
            for location in location_list:
                objectID = str(location['_id'])
                print(objectID+" | "+ location["name"]+" | "+location["city"]+" | "+location["country"])
        else:
            print(f"No data found in {table_name}.")
    except Exception as e:
        print(f"Error fetching data from {table_name}: {e}")
    finally:
        cursor.close()

def insert_data_to_both(locations,connection):

    name = input("Enter the location name: ")
    city = input("Enter the city: ")
    country = input("Enter the country: ")

    data = {
        'name': name,
        'city': city,
        'country': country
    }

    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO locations (name, city, country) VALUES (%s, %s, %s)", 
        (data['name'], data['city'], data['country'])
        )
        connection.commit()
        locations.insert_one(data)
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()

def delete_data_from_both(locations, connection):
    """Delete data based on the location name."""
    name = input("Enter the name of the location to delete: ")
    
    try:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM locations WHERE name = %s", (name))
        connection.commit()
        print(f"Data with name '{name}' deleted from PostgreSQL.")
        result = locations.delete_one({"name": name})
        if result.deleted_count > 0:
            print(f"Data with name '{name}' deleted from MongoDB.")
        else:
            print(f"No document found with name '{name}' in MongoDB.")
    except Exception as e:
        print(f"Error deleting data: {e}")
    finally:
        cursor.close()

def modify_data_in_both(locations, connection):
    """Modify data based on the location name."""
    name = input("Enter the name of the location to modify: ")
    
    new_name = input(f"Enter the new name for {name}: ")
    new_city = input(f"Enter the new city for {name}: ")
    new_country = input(f"Enter the new country for {name}: ")

    try:
        cursor = connection.cursor()
        
        cursor.execute("""
            UPDATE locations
            SET name = %s, city = %s, country = %s
            WHERE name = %s
        """, (new_name, new_city, new_country, name))
        connection.commit()
        print(f"Data with name '{name}' updated in PostgreSQL.")
        
        result = locations.update_one(
            {"name": name},
            {"$set": {"name": new_name, "city": new_city, "country": new_country}}
        )
        if result.modified_count > 0:
            print(f"Data with name '{name}' updated in MongoDB.")
        else:
            print(f"No document found with name '{name}' in MongoDB to update.")
    except Exception as e:
        print(f"Error modifying data: {e}")
    finally:
        cursor.close()

def menu(locations,connection):
    """Display the menu and prompt the user for action."""
    while True:
        print("\nSelect an action:")
        print("1. Print Data")
        print("2. Insert Data")
        print("3. Modify Data")
        print("4. Delete Data")
        print("5. Exit")

        action = input("Enter the number of the action: ")

        if action == '1':
            join_data_from_both(locations,connection)
        elif action == '2':
            insert_data_to_both(locations,connection)
        elif action == '3':
            modify_data_in_both(locations, connection)
        elif action == '4':
            delete_data_from_both(locations, connection)
        elif action == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please try again.")

def main():
    """Main function to run the menu-driven program."""

    while True:
        connection = create_connection_sql()
        client = create_connection_nosql()
        nosql_db = client['nosql_db']
        locations = nosql_db['locations']
        menu(locations,connection)
        connection.close()
        client.close()
        exit()

if __name__ == "__main__":
    main()