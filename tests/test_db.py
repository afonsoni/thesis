from src.embeddings.database import DB

def main():
    print("Testing database connection...")
    db = DB()
    
    if db.test_connection():
        print("✅ Database connection successful!")
        
    else:
        print("❌ Database connection failed!")
        print("Make sure your PostgreSQL Docker container is running:")
        print("docker ps | grep postgres")

if __name__ == "__main__":
    main()