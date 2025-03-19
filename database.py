import mysql.connector

# Add your SQL password 
db_config = {
    'host': 'localhost',          
    'user': 'root',                
    'password': 'password',        
    'database': 'BankingSystem'    
}

def connect_to_db():
   
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def fetch_customer_data(connection):
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Customer LIMIT 5;")
    result = cursor.fetchall()
    print("Data from 'Customer' table:")
    for row in result:
        print(row)
    cursor.close()

def close_connection(connection):
    
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed.")

if __name__ == "__main__":
    
    connection = connect_to_db()

    if connection:
        
        fetch_customer_data(connection)

        
        close_connection(connection)



