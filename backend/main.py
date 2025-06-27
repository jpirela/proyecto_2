#!/usr/bin/env python3
"""
Stable User Management Backend v2.0
Features:
- User authentication and management
- App management with permissions
- User-friendly admin interface
- Notebook and MediaPlayer apps
"""

from fastapi import FastAPI, HTTPException, Depends, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import List, Optional
import sqlite3
import subprocess
import os
from datetime import datetime, timedelta
import secrets

# Configuration
SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# FastAPI app
app = FastAPI(
    title="User Management System",
    description="A stable backend for user and app management",
    version="2.0.0"
)

# Templates and static files
templates = Jinja2Templates(directory="templates")

# Create static directory if it doesn't exist
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")

# Models
class User(BaseModel):
    username: str
    is_admin: bool = False

class UserCreate(BaseModel):
    username: str
    password: str
    is_admin: bool = False

class UserUpdate(BaseModel):
    password: str
    is_admin: bool = False

class App(BaseModel):
    id: int
    name: str
    description: str
    exec_path: str
    category: str
    is_blocked: bool = False

class AppCreate(BaseModel):
    name: str
    description: str
    exec_path: str
    category: str
    is_blocked: bool = False

class Token(BaseModel):
    access_token: str
    token_type: str

class UserInDB(User):
    hashed_password: str

# Database
DB_PATH = "app.db"

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize database with tables and default data"""
    conn = get_db()
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            hashed_password TEXT NOT NULL,
            is_admin INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS apps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            exec_path TEXT NOT NULL,
            category TEXT NOT NULL,
            is_blocked INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_app_permissions (
            username TEXT,
            app_id INTEGER,
            granted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (username) REFERENCES users (username) ON DELETE CASCADE,
            FOREIGN KEY (app_id) REFERENCES apps (id) ON DELETE CASCADE,
            PRIMARY KEY (username, app_id)
        )
    ''')
    
    # Check if admin user exists
    cursor.execute("SELECT COUNT(*) FROM users WHERE username = 'admin'")
    if cursor.fetchone()[0] == 0:
        # Create default admin user
        hashed_password = pwd_context.hash("admin123")
        cursor.execute(
            "INSERT INTO users (username, hashed_password, is_admin) VALUES (?, ?, ?)",
            ("admin", hashed_password, 1)
        )
        print("✅ Default admin user created: admin / admin123")
    
    # Check if default apps exist
    cursor.execute("SELECT COUNT(*) FROM apps")
    if cursor.fetchone()[0] == 0:
        # Create default apps
        default_apps = [
            ("Notebook", "Simple text editor", "notepad.exe", "Productivity", 0),
            ("Media Player", "Video and audio player", "wmplayer.exe", "Media", 1)  # Blocked by default
        ]
        
        for name, desc, path, category, blocked in default_apps:
            cursor.execute(
                "INSERT INTO apps (name, description, exec_path, category, is_blocked) VALUES (?, ?, ?, ?, ?)",
                (name, desc, path, category, blocked)
            )
        print("✅ Default apps created: Notebook and MediaPlayer")
    
    conn.commit()
    conn.close()

# Initialize database
init_database()

# Utility functions
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(username: str) -> Optional[UserInDB]:
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        return UserInDB(
            username=row["username"],
            hashed_password=row["hashed_password"],
            is_admin=bool(row["is_admin"])
        )
    return None

def authenticate_user(username: str, password: str):
    user = get_user(username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_admin_user(current_user: UserInDB = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

# API Endpoints
@app.get("/")
def read_root():
    return {
        "message": "User Management System v2.0",
        "version": "2.0.0",
        "endpoints": {
            "admin_interface": "/admin",
            "api_docs": "/docs",
            "login": "/api/token"
        }
    }

@app.post("/api/token", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/api/me", response_model=User)
def read_users_me(current_user: UserInDB = Depends(get_current_user)):
    return current_user

# User Management API
@app.post("/api/users", response_model=User)
def create_user(user: UserCreate, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if user already exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (user.username,))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="User already exists")
    
    hashed_password = get_password_hash(user.password)
    cursor.execute(
        "INSERT INTO users (username, hashed_password, is_admin) VALUES (?, ?, ?)",
        (user.username, hashed_password, int(user.is_admin))
    )
    conn.commit()
    conn.close()
    
    return User(username=user.username, is_admin=user.is_admin)

@app.get("/api/users", response_model=List[User])
def list_users(admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username, is_admin FROM users ORDER BY username")
    users = [User(username=row[0], is_admin=bool(row[1])) for row in cursor.fetchall()]
    conn.close()
    return users

@app.get("/api/users/{username}", response_model=User)
def get_user_by_username(username: str, admin: UserInDB = Depends(get_current_admin_user)):
    user = get_user(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return User(username=user.username, is_admin=user.is_admin)

@app.put("/api/users/{username}", response_model=User)
def update_user(username: str, user_update: UserUpdate, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if user exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="User not found")
    
    hashed_password = get_password_hash(user_update.password)
    cursor.execute(
        "UPDATE users SET hashed_password = ?, is_admin = ? WHERE username = ?",
        (hashed_password, int(user_update.is_admin), username)
    )
    conn.commit()
    conn.close()
    
    return User(username=username, is_admin=user_update.is_admin)

@app.delete("/api/users/{username}")
def delete_user(username: str, admin: UserInDB = Depends(get_current_admin_user)):
    if username == admin.username:
        raise HTTPException(status_code=400, detail="Cannot delete your own account")
    
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if user exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete user permissions first
    cursor.execute("DELETE FROM user_app_permissions WHERE username = ?", (username,))
    # Delete user
    cursor.execute("DELETE FROM users WHERE username = ?", (username,))
    conn.commit()
    conn.close()
    
    return {"message": f"User {username} deleted successfully"}

# App Management API
@app.post("/api/apps", response_model=App)
def create_app(app: AppCreate, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute(
        "INSERT INTO apps (name, description, exec_path, category, is_blocked) VALUES (?, ?, ?, ?, ?)",
        (app.name, app.description, app.exec_path, app.category, int(app.is_blocked))
    )
    app_id = cursor.lastrowid
    conn.commit()
    conn.close()
    
    return App(
        id=app_id,
        name=app.name,
        description=app.description,
        exec_path=app.exec_path,
        category=app.category,
        is_blocked=app.is_blocked
    )

@app.get("/api/apps", response_model=List[App])
def list_apps(current_user: UserInDB = Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    if current_user.is_admin:
        # Admins see all apps
        cursor.execute("SELECT * FROM apps ORDER BY name")
    else:
        # Regular users see only apps they have permission for
        cursor.execute("""
            SELECT DISTINCT a.* FROM apps a
            JOIN user_app_permissions p ON a.id = p.app_id
            WHERE p.username = ? AND a.is_blocked = 0
            ORDER BY a.name
        """, (current_user.username,))
    
    apps = []
    for row in cursor.fetchall():
        apps.append(App(
            id=row["id"],
            name=row["name"],
            description=row["description"],
            exec_path=row["exec_path"],
            category=row["category"],
            is_blocked=bool(row["is_blocked"])
        ))
    
    conn.close()
    return apps

@app.get("/api/apps/{app_id}", response_model=App)
def get_app(app_id: int, current_user: UserInDB = Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM apps WHERE id = ?", (app_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="App not found")
    
    # Check if user has permission (unless admin)
    if not current_user.is_admin:
        cursor.execute(
            "SELECT 1 FROM user_app_permissions WHERE username = ? AND app_id = ?",
            (current_user.username, app_id)
        )
        if not cursor.fetchone():
            raise HTTPException(status_code=403, detail="No permission to access this app")
    
    return App(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        exec_path=row["exec_path"],
        category=row["category"],
        is_blocked=bool(row["is_blocked"])
    )

@app.put("/api/apps/{app_id}", response_model=App)
def update_app(app_id: int, app_update: AppCreate, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT 1 FROM apps WHERE id = ?", (app_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="App not found")
    
    cursor.execute(
        "UPDATE apps SET name = ?, description = ?, exec_path = ?, category = ?, is_blocked = ? WHERE id = ?",
        (app_update.name, app_update.description, app_update.exec_path, app_update.category, int(app_update.is_blocked), app_id)
    )
    conn.commit()
    conn.close()
    
    return App(
        id=app_id,
        name=app_update.name,
        description=app_update.description,
        exec_path=app_update.exec_path,
        category=app_update.category,
        is_blocked=app_update.is_blocked
    )

@app.delete("/api/apps/{app_id}")
def delete_app(app_id: int, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT 1 FROM apps WHERE id = ?", (app_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="App not found")
    
    # Delete permissions first
    cursor.execute("DELETE FROM user_app_permissions WHERE app_id = ?", (app_id,))
    # Delete app
    cursor.execute("DELETE FROM apps WHERE id = ?", (app_id,))
    conn.commit()
    conn.close()
    
    return {"message": f"App {app_id} deleted successfully"}

# App Permissions API
@app.post("/api/apps/{app_id}/permissions/{username}")
def grant_app_permission(app_id: int, username: str, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    # Check if app exists
    cursor.execute("SELECT 1 FROM apps WHERE id = ?", (app_id,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="App not found")
    
    # Check if user exists
    cursor.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if not cursor.fetchone():
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if permission already exists
    cursor.execute("SELECT 1 FROM user_app_permissions WHERE app_id = ? AND username = ?", (app_id, username))
    if cursor.fetchone():
        raise HTTPException(status_code=400, detail="Permission already granted")
    
    cursor.execute("INSERT INTO user_app_permissions (app_id, username) VALUES (?, ?)", (app_id, username))
    conn.commit()
    conn.close()
    
    return {"message": f"Permission granted to {username} for app {app_id}"}

@app.delete("/api/apps/{app_id}/permissions/{username}")
def revoke_app_permission(app_id: int, username: str, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM user_app_permissions WHERE app_id = ? AND username = ?", (app_id, username))
    conn.commit()
    conn.close()
    
    return {"message": f"Permission revoked from {username} for app {app_id}"}

@app.get("/api/apps/{app_id}/permissions")
def get_app_permissions(app_id: int, admin: UserInDB = Depends(get_current_admin_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    # Get app info
    cursor.execute("SELECT name FROM apps WHERE id = ?", (app_id,))
    app_row = cursor.fetchone()
    if not app_row:
        raise HTTPException(status_code=404, detail="App not found")
    
    # Get users with permissions
    cursor.execute("SELECT username FROM user_app_permissions WHERE app_id = ?", (app_id,))
    users_with_permissions = [row[0] for row in cursor.fetchall()]
    
    # Get all users
    cursor.execute("SELECT username, is_admin FROM users ORDER BY username")
    all_users = []
    for row in cursor.fetchall():
        all_users.append({
            "username": row[0],
            "is_admin": bool(row[1]),
            "has_permission": row[0] in users_with_permissions
        })
    
    conn.close()
    
    return {
        "app_id": app_id,
        "app_name": app_row[0],
        "users": all_users
    }

# App Execution
@app.post("/api/apps/{app_id}/run")
def run_app(app_id: int, current_user: UserInDB = Depends(get_current_user)):
    conn = get_db()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM apps WHERE id = ?", (app_id,))
    row = cursor.fetchone()
    conn.close()
    
    if not row:
        raise HTTPException(status_code=404, detail="App not found")
    
    # Check if app is blocked
    if row["is_blocked"]:
        raise HTTPException(status_code=403, detail="This app is blocked")
    
    # Check permissions (unless admin)
    if not current_user.is_admin:
        cursor.execute(
            "SELECT 1 FROM user_app_permissions WHERE username = ? AND app_id = ?",
            (current_user.username, app_id)
        )
        if not cursor.fetchone():
            raise HTTPException(status_code=403, detail="No permission to run this app")
    
    try:
        subprocess.Popen(row["exec_path"], shell=True)
        return {"message": f"App {row['name']} started successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error running app: {str(e)}")

# Web Interface Routes
@app.get("/admin", response_class=HTMLResponse)
def admin_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/admin/dashboard", response_class=HTMLResponse)
def admin_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/admin/users", response_class=HTMLResponse)
def admin_users_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/admin/apps", response_class=HTMLResponse)
def admin_apps_page(request: Request):
    return templates.TemplateResponse("apps.html", {"request": request})

@app.get("/", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
def user_login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "is_admin": False})

@app.get("/perfil", response_class=HTMLResponse)
def user_profile_page(request: Request, current_user: UserInDB = Depends(get_current_user)):
    return templates.TemplateResponse("perfil.html", {"request": request, "user": current_user})

@app.get("/mis-apps", response_class=HTMLResponse)
def user_apps_page(request: Request, current_user: UserInDB = Depends(get_current_user)):
    # Obtener apps permitidas para el usuario
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.* FROM apps a
        JOIN user_app_permissions p ON a.id = p.app_id
        WHERE p.username = ? AND a.is_blocked = 0
        ORDER BY a.name
    """, (current_user.username,))
    apps = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("mis_apps.html", {"request": request, "apps": apps, "user": current_user})

@app.get("/logout")
def logout():
    return {"message": "Logged out successfully"}

if __name__ == "__main__":
    import uvicorn
    print("🚀 Starting User Management System v2.0")
    print("📊 Admin Interface: http://localhost:8000/admin")
    print("📚 API Documentation: http://localhost:8000/docs")
    print("🔑 Default Admin: admin / admin123")
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False) 