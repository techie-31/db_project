import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

class DatabaseViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Database Viewer")
        self.setGeometry(100, 100, 600, 400)

        # Initialize table widget
        self.table_widget = QTableWidget()
        self.setCentralWidget(self.table_widget)

        # Load data into the table
        self.load_data()

    def load_data(self):
        try:
            # Connect to the database
            conn = sqlite3.connect("tutorial.db")
            cur = conn.cursor()

            # Query the data
            cur.execute("SELECT * FROM User")
            rows = cur.fetchall()

            # Set table dimensions
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(rows[0]) if rows else 0)
            self.table_widget.setHorizontalHeaderLabels(["ID", "Password"])  # Adjust to match your columns

            # Populate the table
            for row_index, row_data in enumerate(rows):
                for col_index, data in enumerate(row_data):
                    self.table_widget.setItem(row_index, col_index, QTableWidgetItem(str(data)))

            # Close the connection
            conn.close()
        except sqlite3.Error as e:
            print(f"Error loading data: {e}")

# Run the application
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    viewer = DatabaseViewer()
    viewer.show()
    sys.exit(app.exec())
