import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from PySide6.QtCore import Qt
from helpers import absPath
from ui_tabla import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Configuración de la conexión a la base de datos SQLite
        conexion = QSqlDatabase.addDatabase("QSQLITE")
        conexion.setDatabaseName(absPath("Contactos.db"))
        
        # Verificación de la conexión a la base de datos
        if not conexion.open():
            print("No se puede conectar a la Base de Datos")
            sys.exit(True)
        
        # Configuración del modelo de la tabla
        self.modelo = QSqlTableModel()
        self.modelo.setTable("Contactos")
        self.modelo.select()
        
        # Configuración de los encabezados de la tabla
        self.modelo.setHeaderData(0, Qt.Horizontal, "Id")
        self.modelo.setHeaderData(1, Qt.Horizontal, "Nombres")
        self.modelo.setHeaderData(2, Qt.Horizontal, "Apellidos")
        self.modelo.setHeaderData(3, Qt.Horizontal, "Sexo")
        self.modelo.setHeaderData(4, Qt.Horizontal, "Edad")
        self.modelo.setHeaderData(5, Qt.Horizontal, "Empleo")
        self.modelo.setHeaderData(6, Qt.Horizontal, "Número")
        self.modelo.setHeaderData(7, Qt.Horizontal, "Email")

        # Configuración de la vista de la tabla
        self.tabla.setModel(self.modelo)
        self.tabla.setColumnHidden(0, True)
        self.tabla.resizeColumnsToContents()
        
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Conexión de señales a funciones
        self.tabla.selectionModel().selectionChanged.connect(self.selecionar_fila)
        self.boton_modificar.clicked.connect(self.modificar_fila)
        self.boton_nuevo.clicked.connect(self.nueva_fila)
        self.boton_borrar.clicked.connect(self.borrar_fila)
        
        # Variable para almacenar la fila seleccionada
        self.fila = -1

    def clear_fields(self):
        """Limpia los campos del formulario."""
        self.line_nombre.setText("")
        self.line_apellido.setText("")
        self.line_sexo.setText("")
        self.line_edad.setText("")
        self.line_empleo.setText("")
        self.line_telefono.setText("")
        self.line_email.setText("")

    def validar_campos(self):
        """Valida que todos los campos estén llenos."""
        if any(len(field) == 0 for field in [
            self.line_nombre.text(),
            self.line_apellido.text(),
            self.line_sexo.text(),
            self.line_edad.text(),
            self.line_empleo.text(),
            self.line_telefono.text(),
            self.line_email.text()
        ]):
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios.")
            return False
        return True

    def selecionar_fila(self, seleccion):
        """Selecciona una fila de la tabla y muestra los datos en el formulario."""
        if seleccion.indexes():
            self.fila = seleccion.indexes()[0].row()
            nombres = self.modelo.index(self.fila, 1).data()
            apellidos = self.modelo.index(self.fila, 2).data()
            sexo = self.modelo.index(self.fila, 3).data()
            edad = self.modelo.index(self.fila, 4).data()
            empleo = self.modelo.index(self.fila, 5).data()
            numero = self.modelo.index(self.fila, 6).data()
            email = self.modelo.index(self.fila, 7).data()
            self.line_nombre.setText(nombres)
            self.line_apellido.setText(apellidos)
            self.line_sexo.setText(sexo)
            self.line_edad.setText(str(edad))
            self.line_empleo.setText(empleo)
            self.line_telefono.setText(numero)
            self.line_email.setText(email)

    def modificar_fila(self):
        """Modifica la fila seleccionada en la tabla."""
        if self.fila >= 0 and self.validar_campos():
            nombres = self.line_nombre.text()
            apellidos = self.line_apellido.text()
            sexo = self.line_sexo.text()
            edad = self.line_edad.text()
            empleo = self.line_empleo.text()
            numero = self.line_telefono.text()
            email = self.line_email.text()

            # Validar si el número ya existe (excluyendo el propio registro que se está modificando)
            if self.modelo.match(self.modelo.index(self.fila, 6), Qt.DisplayRole, numero, 1, Qt.MatchExactly):
                pass  # No se realiza la validación en el caso de la modificación del propio registro
            elif self.modelo.match(self.modelo.index(0, 6), Qt.DisplayRole, numero, 1, Qt.MatchExactly):
                QMessageBox.warning(self, "Advertencia", "Número ya existe en la base de datos.")
                return

            # Validar si el correo ya existe (excluyendo el propio registro que se está modificando)
            if self.modelo.match(self.modelo.index(self.fila, 7), Qt.DisplayRole, email, 1, Qt.MatchExactly):
                pass  # No se realiza la validación en el caso de la modificación del propio registro
            elif self.modelo.match(self.modelo.index(0, 7), Qt.DisplayRole, email, 1, Qt.MatchExactly):
                QMessageBox.warning(self, "Advertencia", "Correo ya existe en la base de datos.")
                return

            # Actualizar los registros del modelo
            self.modelo.setData(self.modelo.index(self.fila, 1), nombres)
            self.modelo.setData(self.modelo.index(self.fila, 2), apellidos)
            self.modelo.setData(self.modelo.index(self.fila, 3), sexo)
            self.modelo.setData(self.modelo.index(self.fila, 4), edad)
            self.modelo.setData(self.modelo.index(self.fila, 5), empleo)
            self.modelo.setData(self.modelo.index(self.fila, 6), numero)
            self.modelo.setData(self.modelo.index(self.fila, 7), email)
            # Confirmar los cambios del modelo a la base de datos
            self.modelo.submitAll()
            self.clear_fields()


    def nueva_fila(self):
        """Agrega una nueva fila a la tabla."""
        if self.validar_campos():
            nombres = self.line_nombre.text()
            apellidos = self.line_apellido.text()
            sexo = self.line_sexo.text()
            edad = self.line_edad.text()
            empleo = self.line_empleo.text()
            numero = self.line_telefono.text()
            email = self.line_email.text()

            # Validar si el número y el email ya existen
            if self.modelo.match(self.modelo.index(0, 6), Qt.DisplayRole, numero, 1, Qt.MatchExactly) or \
               self.modelo.match(self.modelo.index(0, 7), Qt.DisplayRole, email, 1, Qt.MatchExactly):
                QMessageBox.warning(self, "Advertencia", "Número o Email ya existen en la base de datos.")
                return

            # Si todos los campos tienen algo
            nueva_fila = self.modelo.rowCount()
            self.modelo.insertRow(nueva_fila)
            # Definir los campos de la nueva fila
            self.modelo.setData(self.modelo.index(nueva_fila, 1), nombres)
            self.modelo.setData(self.modelo.index(nueva_fila, 2), apellidos)
            self.modelo.setData(self.modelo.index(nueva_fila, 3), sexo)
            self.modelo.setData(self.modelo.index(nueva_fila, 4), edad)
            self.modelo.setData(self.modelo.index(nueva_fila, 5), empleo)
            self.modelo.setData(self.modelo.index(nueva_fila, 6), numero)
            self.modelo.setData(self.modelo.index(nueva_fila, 7), email)
            # Confirmar los cambios del modelo
            self.modelo.submitAll()
            self.clear_fields()

    def borrar_fila(self):
        """Borra la fila seleccionada en la tabla."""
        if self.fila >= 0:
            # Confirmar con el usuario si realmente desea borrar la fila
            reply = QMessageBox.question(
                self, "Advertencia", "¿Estás seguro de borrar esta fila?",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                self.modelo.removeRow(self.fila)
                # Actualizar la tabla para mostrarla sin el registro borrado
                self.modelo.select()
                # Establecer la fila a -1
                self.fila = -1
                # Resetear los campos del formulario
                self.clear_fields()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())  # Inicializa la aplicación y muestra la ventana principal
