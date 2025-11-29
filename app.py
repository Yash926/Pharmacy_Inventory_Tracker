from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)

# --- 1. DATABASE MANAGEMENT ---
def init_db():
    with sqlite3.connect("pharmacy.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS inventory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                stock INTEGER NOT NULL
            )
        """)
init_db()

# --- 2. FRONTEND ROUTE ---
@app.route('/')
def home():
    return render_template('index.html')

# --- 3. API ROUTES (BACKEND LOGIC) ---

@app.route('/add', methods=['POST'])
def add_medicine():
    data = request.get_json()
    name = data.get('name')
    stock = data.get('stock')

    if not name or stock is None:
        return jsonify({"error": "Name and Stock are required"}), 400
    
    if stock < 0:
        return jsonify({"error": "Stock cannot be negative"}), 400

    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO inventory (name, stock) VALUES (?, ?)", (name, stock))
        conn.commit()

    return jsonify({"message": f"{name} added successfully!"}), 201

@app.route('/inventory', methods=['GET'])
def get_inventory():
    with sqlite3.connect("pharmacy.db") as conn:
        conn.row_factory = sqlite3.Row  
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM inventory")
        rows = cursor.fetchall()
        
        items = [dict(row) for row in rows]
    
    return jsonify(items)

@app.route('/update/<int:item_id>', methods=['PUT'])
def update_stock(item_id):
    data = request.get_json()
    new_stock = data.get('stock')

    if new_stock is None:
        return jsonify({"error": "New stock value required"}), 400
        
    if new_stock < 0:
        return jsonify({"error": "Stock cannot be negative"}), 400

    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        
        # Check if the item exists
        cursor.execute("SELECT * FROM inventory WHERE id = ?", (item_id,))
        if cursor.fetchone() is None:
            return jsonify({"error": "Item not found"}), 404
            
        cursor.execute("UPDATE inventory SET stock = ? WHERE id = ?", (new_stock, item_id))
        conn.commit()

    return jsonify({"message": "Stock updated successfully!"})

@app.route('/delete/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    with sqlite3.connect("pharmacy.db") as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inventory WHERE id = ?", (item_id,))
        conn.commit()

    return jsonify({"message": "Item deleted successfully!"})

if __name__ == '__main__':
    app.run(debug=True)