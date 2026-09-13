from mssql_python import connect

# 接続文字列（SQL認証の例）
connection_string = (
    "Server=your_server_name;"
    "Database=your_database_name;"
    "Trusted_Connection=yes;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"  # 開発環境などで必要に応じて設定
)

sql_string = """
SELECT TOP 10 * 
FROM YourTableName
"""

try:
    conn = connect(connection_string)
    cursor = conn.cursor()

    cursor.execute(sql_string)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(f"エラーが発生しました: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()