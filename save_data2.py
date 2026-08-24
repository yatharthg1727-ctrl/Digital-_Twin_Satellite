import socket
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "port": 3306,
    "user": "root",
    "password": "yash1436@",
    "database": "satellite_twin",
    "connect_timeout": 5,
    "use_pure": True,
}

HOSTS_TO_TRY = ["127.0.0.1", "localhost"]


def test_tcp_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=3):
            return True
    except Exception as err:
        print(f"TCP check failed for {host}:{port}: {err}")
        return False


def get_db_connection(host):
    return mysql.connector.connect(host=host, **DB_CONFIG)


def fetch_latest_telemetry():
    for host in HOSTS_TO_TRY:
        print(f"Trying MySQL host: {host}:{DB_CONFIG['port']}")
        if not test_tcp_port(host, DB_CONFIG["port"]):
            continue

        conn = None
        try:
            conn = get_db_connection(host)
            print(f"Connected to MySQL on {host}:{DB_CONFIG['port']}")
            cursor = conn.cursor(dictionary=True)
            cursor.execute(
                "SELECT battery_level, fuel_level, signal_strength FROM telemetry ORDER BY telemetry_id DESC LIMIT 1"
            )
            return cursor.fetchone()
        except Error as err:
            print(f"MySQL connection failed for {host}: {err}")
        finally:
            if conn is not None and conn.is_connected():
                conn.close()

    return None


if __name__ == "__main__":
    data = fetch_latest_telemetry()
    if data:
        print("Latest telemetry:", data)
    else:
        print("Unable to read telemetry from MySQL. Make sure MySQL is running and the database 'satellite_twin' exists.")
