# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'In-Class_example.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(460, 300)
        self.Buttton1 = QDialogButtonBox(Dialog)
        self.Buttton1.setObjectName(u"Buttton1")
        self.Buttton1.setGeometry(QRect(100, 250, 341, 32))
        self.Buttton1.setOrientation(Qt.Orientation.Horizontal)
        self.Buttton1.setStandardButtons(QDialogButtonBox.StandardButton.Ok)
        self.LineEditName = QLineEdit(Dialog)
        self.LineEditName.setObjectName(u"LineEditName")
        self.LineEditName.setGeometry(QRect(110, 30, 301, 26))
        self.LineEditName.setToolTipDuration(5)
        self.LineEditName.setAutoFillBackground(False)
        self.LineEditName.setMaxLength(20)
        self.LineEditName.setReadOnly(True)
        self.LabelName = QLabel(Dialog)
        self.LabelName.setObjectName(u"LabelName")
        self.LabelName.setGeometry(QRect(30, 30, 61, 16))

        self.retranslateUi(Dialog)
        self.Buttton1.accepted.connect(Dialog.accept)
        self.Buttton1.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
#if QT_CONFIG(tooltip)
        self.LineEditName.setToolTip(QCoreApplication.translate("Dialog", u"Enter your first name", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.LineEditName.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.LineEditName.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Text Here", None))
        self.LabelName.setText(QCoreApplication.translate("Dialog", u"First Name", None))
    # retranslateUi

