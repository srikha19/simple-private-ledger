import sys
import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from ledger import Blockchain


class BlockchainApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.blockchain = Blockchain(difficulty=4)

        self.setWindowTitle("🚀 Advanced Blockchain Explorer (FINAL)")
        self.setGeometry(120, 60, 1200, 700)

        self.setStyleSheet("""
            QMainWindow { background-color: #0b1220; color: white; }
            QPushButton {
                background-color: #2563eb;
                color: white;
                padding: 7px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #1d4ed8; }
            QLineEdit {
                background-color: #1e293b;
                color: white;
                padding: 5px;
                border-radius: 5px;
            }
            QTableWidget {
                background-color: #111827;
                color: white;
            }
        """)

        self.init_ui()

    def init_ui(self):
        widget = QWidget()
        self.setCentralWidget(widget)

        layout = QVBoxLayout()

        # INPUTS
        input_layout = QHBoxLayout()

        self.from_input = QLineEdit()
        self.to_input = QLineEdit()
        self.amount_input = QLineEdit()
        self.node_input = QLineEdit()

        self.from_input.setPlaceholderText("From")
        self.to_input.setPlaceholderText("To")
        self.amount_input.setPlaceholderText("Amount")
        self.node_input.setPlaceholderText("Node name")

        input_layout.addWidget(self.from_input)
        input_layout.addWidget(self.to_input)
        input_layout.addWidget(self.amount_input)

        layout.addLayout(input_layout)

        # BUTTONS
        btn_layout = QHBoxLayout()

        self.add_btn = QPushButton("⛏️ Mine Block")
        self.save_btn = QPushButton("💾 Save")
        self.load_btn = QPushButton("📂 Load")
        self.valid_btn = QPushButton("🔍 Validate")
        self.node_btn = QPushButton("🌐 Add Node")

        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.save_btn)
        btn_layout.addWidget(self.load_btn)
        btn_layout.addWidget(self.valid_btn)
        btn_layout.addWidget(self.node_btn)

        layout.addLayout(btn_layout)

        layout.addWidget(self.node_input)

        # TABLE
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(
            ["Index", "Time", "Data", "Nonce", "Prev Hash", "Hash"]
        )

        layout.addWidget(self.table)

        widget.setLayout(layout)

        # EVENTS
        self.add_btn.clicked.connect(self.mine_block)
        self.save_btn.clicked.connect(self.save_chain)
        self.load_btn.clicked.connect(self.load_chain)
        self.valid_btn.clicked.connect(self.validate_chain)
        self.node_btn.clicked.connect(self.add_node)

    # ⛏️ MINE BLOCK
    def mine_block(self):
        data = {
            "from": self.from_input.text(),
            "to": self.to_input.text(),
            "amount": self.amount_input.text(),
            "time": str(datetime.datetime.now())
        }

        self.blockchain.add_block(data)

        QMessageBox.information(self, "Mining", "Block Mined Successfully ⛏️")

        self.from_input.clear()
        self.to_input.clear()
        self.amount_input.clear()

        self.load_chain()

    # 🌐 NODE SYSTEM
    def add_node(self):
        node = self.node_input.text()
        self.blockchain.add_node(node)

        QMessageBox.information(
            self,
            "Node Added",
            f"Node '{node}' connected 🌐\nTotal Nodes: {len(self.blockchain.get_nodes())}"
        )

        self.node_input.clear()

    # 📂 LOAD
    def load_chain(self):
        self.table.setRowCount(len(self.blockchain.chain))

        for i, b in enumerate(self.blockchain.chain):
            self.table.setItem(i, 0, QTableWidgetItem(str(b.index)))
            self.table.setItem(i, 1, QTableWidgetItem(b.timestamp))
            self.table.setItem(i, 2, QTableWidgetItem(str(b.data)))
            self.table.setItem(i, 3, QTableWidgetItem(str(b.nonce)))
            self.table.setItem(i, 4, QTableWidgetItem(b.previous_hash))
            self.table.setItem(i, 5, QTableWidgetItem(b.hash))

    # 💾 SAVE
    def save_chain(self):
        self.blockchain.save()
        QMessageBox.information(self, "Saved", "Blockchain saved successfully 💾")

    # 🔍 VALIDATE
    def validate_chain(self):
        if self.blockchain.is_valid():
            QMessageBox.information(self, "Valid", "Blockchain is VALID ✅")
        else:
            QMessageBox.critical(self, "Tampered", "Blockchain BROKEN ❌")


# RUN
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BlockchainApp()
    window.show()
    sys.exit(app.exec_())