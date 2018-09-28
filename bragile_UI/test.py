import sys
from PyQt5.QtWidgets import *
import paramiko
from scp import SCPClient
from  PyQt5.Qt import *

class error(QDialog):
    def __init__(self,Mode):
        if Mode==0:
            super().__init__()
            self.setGeometry(1100, 200, 100, 200)
            self.setFixedSize(200, 100)
            self.setWindowTitle("Error")

            self.label2 =QLabel ("잘못된 입력",self)
            self.label2.move(60, 20)
        elif Mode==1:
            super().__init__()
            self.setGeometry(1100, 200, 100, 200)
            self.setFixedSize(200, 100)
            self.setWindowTitle("Success")

            self.label2 = QLabel("Success", self)
            self.label2.move(60, 20)


class setting(QDialog):
    def __init__(self,*args):
        super().__init__()
        self.ip = args[0]
        self.port = args[1]
        self.id = args[2]
        self.password =args[3]

        self.setupUI()


    def setupUI(self):
        self.setGeometry(1100, 200, 300, 400)
        self.setFixedSize(300, 300)
        self.setWindowTitle("Setting")
        self.setWindowIcon(QIcon('icon.png'))

        self.label1 = QLabel("IP: ")
        self.label2 = QLabel("PORT: ")
        self.label3 = QLabel("ID: ")
        self.label4 = QLabel("Password: ")
        self.label5 = QLineEdit(self.ip)
        self.label6 = QLineEdit(self.port)
        self.label7 = QLineEdit(self.id)
        self.label8 = QLineEdit(self.password)

        self.pushButton1= QPushButton("적용")
        self.pushButton1.clicked.connect(self.end)

        layout = QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.label3, 2, 0)
        layout.addWidget(self.label4, 3, 0)
        layout.addWidget(self.label5, 0, 1)
        layout.addWidget(self.label6, 1, 1)
        layout.addWidget(self.label7, 2, 1)
        layout.addWidget(self.label8, 3, 1)
        layout.addWidget(self.pushButton1, 4, 1)

        self.setLayout(layout)



    def end(self):
        self.ip = self.label5.text()
        self.port= self.label6.text()
        self.id = self.label7.text()
        self.password = self.label8.text()
        self.close()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.printer_ip="192.168.0.21";
        self.printer_port="22";
        self.printer_id="pi"
        self.printer_password="1234"
        self.file_dir=None
        self.remote_dir="~/test"

        self.setWindowTitle("SYR_Printing")
        self.setGeometry(40,40,600,400)
        self.setFixedSize(600,400)

        self.label1 =QLabel ("파일 명:",self)
        # self.label.setStyleSheet("background-color:#ffffff")
        self.label1.setFixedWidth(80)
        self.label1.setFixedHeight(30)
        # self.label.setAlignment(Qt.AlignCenter)
        # self.label.setFrameShape(QFrame.Panel)
        # self.label.setFrameShadow(QFrame.Sunken)
        self.label1.move(20,20)

        self.label2 =QLabel ("",self)
        self.label2.setStyleSheet("background-color:#ffffff")
        self.label2.setFixedWidth(330)
        self.label2.setFixedHeight(30)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setFrameShape(QFrame.Panel)
        self.label2.setFrameShadow(QFrame.Sunken)
        self.label2.move(100, 20)

        self.label3 =QPushButton("파일",self)
        self.label3.setStyleSheet("background-color:#ffffff")
        self.label3.move(450, 20)
        self.label3.clicked.connect(self.find_file)

        self.label4 =QPushButton("출력",self)
        self.label4.setStyleSheet("background-color:#ffffff")
        self.label4.move(450, 300)
        self.label4.clicked.connect(self.printing)

        self.label5 =QPushButton("취소",self)
        self.label5.setStyleSheet("background-color:#ffffff")
        self.label5.move(350, 300)

        self.label5 =QPushButton("설정",self)
        self.label5.setStyleSheet("background-color:#ffffff")
        self.label5.move(250, 300)
        self.label5.clicked.connect(self.setting)

        self.label6 = QLabel("Printer IP:"+self.printer_ip, self)
        self.label6.setFixedHeight(30)
        self.label6.move(20,100)

        self.label7 = QLabel("Printer Port:"+self.printer_port, self)
        self.label7.setFixedHeight(30)
        self.label7.move(20,140)

        self.label8 = QLabel("Remote Path:"+self.remote_dir, self)
        self.label8.setFixedHeight(30)
        self.label8.move(20,180)


    def find_file(self):
        fname=QFileDialog.getOpenFileName(self)
        self.file_dir=fname[0]
        self.label2.setText(fname[0])

    def setting(self):
        set=setting(self.printer_ip,self.printer_port,self.printer_id,self.printer_password)
        set.exec()

        self.printer_ip=set.ip
        self.printer_port=set.port
        self.printer_id=set.id
        self.printer_password=set.password
        self.label6.setText("Printer IP:"+self.printer_ip)
        self.label7.setText("Printer Port:"+self.printer_port)

    def printing(self):
        if self.file_dir== None or (self.file_dir[-3:] !='txt' and  self.file_dir[-3:] !='pdf'):
            get_error=error(0)
            get_error.exec()
        else:
            self.SSH_set()
            self.pull()

    def SSH_set(self):


        self.ssh = self.createSSHClient(self.printer_ip, self.printer_port, self.printer_id, self.printer_password)
        self.scp = SCPClient(self.ssh.get_transport())

    def createSSHClient(self,server, port, user, password):
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(server, port, user, password)
        return client
    def pull(self):
        self.scp.put(self.file_dir,self.remote_dir)
        get_error = error(1)
        get_error.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    first = MainWindow()
    first.show()
    app.exec_()