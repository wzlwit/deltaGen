"""deltaGen - Delta Table Generator GUI Application."""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QComboBox, QFileDialog,
    QGroupBox, QTextEdit, QStatusBar
)
from PyQt6.QtCore import QSettings


class MainWindow(QMainWindow):
    """Main application window for deltaGen."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("deltaGen - Delta Table Generator")
        self.setMinimumSize(600, 400)

        self.settings = QSettings(
            QSettings.Format.IniFormat,
            QSettings.Scope.UserScope,
            "deltaGen", "deltaGen"
        )

        self._setup_ui()
        self._load_settings()

    def _setup_ui(self):
        """Set up the main UI layout."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Input section
        input_group = QGroupBox("Input")
        input_layout = QVBoxLayout(input_group)

        input_row = QHBoxLayout()
        self.input_path = QLineEdit()
        self.input_path.setPlaceholderText("Select input file or folder...")
        input_browse = QPushButton("Browse...")
        input_browse.clicked.connect(self._browse_input)
        input_row.addWidget(self.input_path)
        input_row.addWidget(input_browse)
        input_layout.addLayout(input_row)

        format_row = QHBoxLayout()
        format_row.addWidget(QLabel("Format:"))
        self.input_format = QComboBox()
        self.input_format.addItems(["Auto-detect", "CSV", "Parquet", "Delta"])
        format_row.addWidget(self.input_format)
        format_row.addStretch()
        input_layout.addLayout(format_row)

        layout.addWidget(input_group)

        # Output section
        output_group = QGroupBox("Output")
        output_layout = QVBoxLayout(output_group)

        output_row = QHBoxLayout()
        self.output_path = QLineEdit()
        self.output_path.setPlaceholderText("Select output folder...")
        output_browse = QPushButton("Browse...")
        output_browse.clicked.connect(self._browse_output)
        output_row.addWidget(self.output_path)
        output_row.addWidget(output_browse)
        output_layout.addLayout(output_row)

        layout.addWidget(output_group)

        # Partitioning section
        partition_group = QGroupBox("Partitioning")
        partition_layout = QHBoxLayout(partition_group)

        partition_layout.addWidget(QLabel("Strategy:"))
        self.partition_strategy = QComboBox()
        self.partition_strategy.addItems(["None", "By Column", "By Date", "Custom"])
        partition_layout.addWidget(self.partition_strategy)

        partition_layout.addWidget(QLabel("Column:"))
        self.partition_column = QLineEdit()
        self.partition_column.setPlaceholderText("e.g., date, region")
        partition_layout.addWidget(self.partition_column)

        layout.addWidget(partition_group)

        # Log output
        log_group = QGroupBox("Log")
        log_layout = QVBoxLayout(log_group)
        self.log_output = QTextEdit()
        self.log_output.setReadOnly(True)
        self.log_output.setMaximumHeight(120)
        log_layout.addWidget(self.log_output)
        layout.addWidget(log_group)

        # Action buttons
        button_row = QHBoxLayout()
        button_row.addStretch()

        self.run_button = QPushButton("Generate Delta Table")
        self.run_button.clicked.connect(self._run_conversion)
        button_row.addWidget(self.run_button)

        layout.addLayout(button_row)

        # Status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")

    def _browse_input(self):
        """Open file dialog for input selection."""
        path, _ = QFileDialog.getOpenFileName(
            self, "Select Input File",
            self.settings.value("last_input_dir", ""),
            "Data Files (*.csv *.parquet);;All Files (*)"
        )
        if path:
            self.input_path.setText(path)
            self.settings.setValue("last_input_dir", path)

    def _browse_output(self):
        """Open folder dialog for output selection."""
        path = QFileDialog.getExistingDirectory(
            self, "Select Output Folder",
            self.settings.value("last_output_dir", "")
        )
        if path:
            self.output_path.setText(path)
            self.settings.setValue("last_output_dir", path)

    def _run_conversion(self):
        """Run the Delta table conversion."""
        input_path = self.input_path.text()
        output_path = self.output_path.text()

        if not input_path or not output_path:
            self.log_output.append("Error: Please specify input and output paths.")
            return

        self.log_output.append(f"Input: {input_path}")
        self.log_output.append(f"Output: {output_path}")
        self.log_output.append(f"Format: {self.input_format.currentText()}")
        self.log_output.append(f"Partition: {self.partition_strategy.currentText()}")

        # TODO: Integrate with PySpark/delta-spark backend
        self.log_output.append("Conversion started... (backend not implemented)")
        self.status_bar.showMessage("Conversion in progress...")

    def _load_settings(self):
        """Load saved settings."""
        self.input_path.setText(self.settings.value("input_path", ""))
        self.output_path.setText(self.settings.value("output_path", ""))
        self.input_format.setCurrentText(self.settings.value("input_format", "Auto-detect"))
        self.partition_strategy.setCurrentText(self.settings.value("partition_strategy", "None"))
        self.partition_column.setText(self.settings.value("partition_column", ""))

    def closeEvent(self, event):
        """Save settings on close."""
        self.settings.setValue("input_path", self.input_path.text())
        self.settings.setValue("output_path", self.output_path.text())
        self.settings.setValue("input_format", self.input_format.currentText())
        self.settings.setValue("partition_strategy", self.partition_strategy.currentText())
        self.settings.setValue("partition_column", self.partition_column.text())
        self.settings.sync()
        event.accept()


def main():
    """Application entry point."""
    app = QApplication(sys.argv)
    app.setApplicationName("deltaGen")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
