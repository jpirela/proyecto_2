#!/usr/bin/env python3
"""
Startup script for User Management System v2.0
This script initializes and starts the FastAPI server with proper configuration.
"""

import os
import sys
import uvicorn
from pathlib import Path

def main():
    """Main startup function"""
    print("🚀 Starting User Management System v2.0")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not Path("main.py").exists():
        print("❌ Error: main.py not found. Please run this script from the backend directory.")
        sys.exit(1)
    
    # Check if requirements are installed
    try:
        import fastapi
        import uvicorn
        import jinja2
        import jose
        import passlib
        print("✅ All dependencies are installed")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Please install requirements: pip install -r requirements.txt")
        sys.exit(1)
    
    # Create necessary directories
    os.makedirs("templates", exist_ok=True)
    os.makedirs("static", exist_ok=True)
    
    print("📊 Admin Interface: http://localhost:8000/admin")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔑 Default Admin: admin / admin123")
    print("=" * 50)
    
    # Start the server
    try:
        uvicorn.run(
            "main:app",
            host="127.0.0.1",
            port=8000,
            reload=False,
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 