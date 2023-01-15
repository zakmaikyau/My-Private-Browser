import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets

class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Web Browser")
        self.setGeometry(50,50,800,600)

        # Create a web view and set the URL to Google
        self.webView = QtWebEngineWidgets.QWebEngineView(self)
        self.webView.setUrl(QtCore.QUrl("https://www.google.com"))
        self.setCentralWidget(self.webView)

        # Create a toolbar and add buttons for Back, Forward, and Refresh
        self.toolbar = self.addToolBar("Navigation")
        self.backBtn = QtWidgets.QAction("Back", self)
        self.backBtn.setShortcut("Alt+Left")
        self.backBtn.triggered.connect(self.webView.back)
        self.toolbar.addAction(self.backBtn)

        self.forwardBtn = QtWidgets.QAction("Forward", self)
        self.forwardBtn.setShortcut("Alt+Right")
        self.forwardBtn.triggered.connect(self.webView.forward)
        self.toolbar.addAction(self.forwardBtn)

        self.refreshBtn = QtWidgets.QAction("Refresh", self)
        self.refreshBtn.setShortcut("F5")
        self.refreshBtn.triggered.connect(self.webView.reload)
        self.toolbar.addAction(self.refreshBtn)
        
        # Create a URL bar
        self.urlBar = QtWidgets.QLineEdit(self)
        self.urlBar.returnPressed.connect(self.navigate_to_url)
        self.toolbar.addWidget(self.urlBar)
        
        # Create a history list
        self.history = []
        self.webView.urlChanged.connect(self.update_url)
        
        self.show()

    def navigate_to_url(self):
        url = self.urlBar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.webView.setUrl(QtCore.QUrl(url))

    def update_url(self, url):
        self.urlBar.setText(url.toString())
        self.history.append(url.toString())

app = QtWidgets.QApplication(sys.argv)
browser = Browser()
sys.exit(app.exec_())
