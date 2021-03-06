# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GetMaskParams.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GetMaskParams(object):
    def setupUi(self, GetMaskParams):
        GetMaskParams.setObjectName("GetMaskParams")
        GetMaskParams.resize(1161, 746)
        self.centralWidget = QtWidgets.QWidget(GetMaskParams)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_isLightBgnd = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_isLightBgnd.setChecked(True)
        self.checkBox_isLightBgnd.setObjectName("checkBox_isLightBgnd")
        self.gridLayout_3.addWidget(self.checkBox_isLightBgnd, 8, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)
        self.spinBox_buff_size = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_buff_size.setMinimum(1)
        self.spinBox_buff_size.setMaximum(1000)
        self.spinBox_buff_size.setProperty("value", 25)
        self.spinBox_buff_size.setObjectName("spinBox_buff_size")
        self.gridLayout_3.addWidget(self.spinBox_buff_size, 7, 1, 1, 1)
        self.label_fps = QtWidgets.QLabel(self.centralWidget)
        self.label_fps.setObjectName("label_fps")
        self.gridLayout_3.addWidget(self.label_fps, 6, 0, 1, 1)
        self.spinBox_fps = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.spinBox_fps.setProperty("value", 25.0)
        self.spinBox_fps.setObjectName("spinBox_fps")
        self.gridLayout_3.addWidget(self.spinBox_fps, 6, 1, 1, 1)
        self.spinBox_dilation_size = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_dilation_size.setMinimum(1)
        self.spinBox_dilation_size.setMaximum(999)
        self.spinBox_dilation_size.setProperty("value", 9)
        self.spinBox_dilation_size.setObjectName("spinBox_dilation_size")
        self.gridLayout_3.addWidget(self.spinBox_dilation_size, 4, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)
        self.dial_max_area = QtWidgets.QDial(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_max_area.sizePolicy().hasHeightForWidth())
        self.dial_max_area.setSizePolicy(sizePolicy)
        self.dial_max_area.setMinimum(100)
        self.dial_max_area.setMaximum(100000)
        self.dial_max_area.setProperty("value", 5000)
        self.dial_max_area.setObjectName("dial_max_area")
        self.gridLayout_3.addWidget(self.dial_max_area, 1, 1, 1, 1)
        self.dial_thresh_C = QtWidgets.QDial(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_thresh_C.sizePolicy().hasHeightForWidth())
        self.dial_thresh_C.setSizePolicy(sizePolicy)
        self.dial_thresh_C.setMinimum(5)
        self.dial_thresh_C.setMaximum(100)
        self.dial_thresh_C.setProperty("value", 15)
        self.dial_thresh_C.setObjectName("dial_thresh_C")
        self.gridLayout_3.addWidget(self.dial_thresh_C, 2, 1, 1, 1)
        self.dial_block_size = QtWidgets.QDial(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_block_size.sizePolicy().hasHeightForWidth())
        self.dial_block_size.setSizePolicy(sizePolicy)
        self.dial_block_size.setMinimum(5)
        self.dial_block_size.setMaximum(200)
        self.dial_block_size.setProperty("value", 61)
        self.dial_block_size.setObjectName("dial_block_size")
        self.gridLayout_3.addWidget(self.dial_block_size, 3, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.spinBox_block_size = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_block_size.setMinimum(5)
        self.spinBox_block_size.setMaximum(1000000)
        self.spinBox_block_size.setProperty("value", 61)
        self.spinBox_block_size.setObjectName("spinBox_block_size")
        self.verticalLayout_3.addWidget(self.spinBox_block_size)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 3, 0, 1, 1)
        self.checkBox_keepBorderData = QtWidgets.QCheckBox(self.centralWidget)
        self.checkBox_keepBorderData.setObjectName("checkBox_keepBorderData")
        self.gridLayout_3.addWidget(self.checkBox_keepBorderData, 9, 0, 1, 2)
        self.dial_min_area = QtWidgets.QDial(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dial_min_area.sizePolicy().hasHeightForWidth())
        self.dial_min_area.setSizePolicy(sizePolicy)
        self.dial_min_area.setMaximum(10000)
        self.dial_min_area.setProperty("value", 100)
        self.dial_min_area.setObjectName("dial_min_area")
        self.gridLayout_3.addWidget(self.dial_min_area, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.spinBox_thresh_C = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_thresh_C.setMinimum(-100)
        self.spinBox_thresh_C.setMaximum(100)
        self.spinBox_thresh_C.setProperty("value", 15)
        self.spinBox_thresh_C.setObjectName("spinBox_thresh_C")
        self.verticalLayout_4.addWidget(self.spinBox_thresh_C)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.spinBox_max_area = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_max_area.setMinimum(100)
        self.spinBox_max_area.setMaximum(10000000)
        self.spinBox_max_area.setProperty("value", 5000)
        self.spinBox_max_area.setObjectName("spinBox_max_area")
        self.verticalLayout_2.addWidget(self.spinBox_max_area)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spinBox_min_area = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox_min_area.setMaximum(10000000)
        self.spinBox_min_area.setProperty("value", 100)
        self.spinBox_min_area.setObjectName("spinBox_min_area")
        self.verticalLayout.addWidget(self.spinBox_min_area)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.pushButton_moreParams = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_moreParams.setObjectName("pushButton_moreParams")
        self.gridLayout_3.addWidget(self.pushButton_moreParams, 10, 0, 1, 2)
        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 17, 1)
        self.lineEdit_mask = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_mask.setReadOnly(False)
        self.lineEdit_mask.setObjectName("lineEdit_mask")
        self.gridLayout.addWidget(self.lineEdit_mask, 19, 3, 1, 3)
        self.pushButton_results = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_results.sizePolicy().hasHeightForWidth())
        self.pushButton_results.setSizePolicy(sizePolicy)
        self.pushButton_results.setObjectName("pushButton_results")
        self.gridLayout.addWidget(self.pushButton_results, 18, 2, 1, 1)
        self.lineEdit_results = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_results.setObjectName("lineEdit_results")
        self.gridLayout.addWidget(self.lineEdit_results, 18, 3, 1, 3)
        self.pushButton_mask = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_mask.sizePolicy().hasHeightForWidth())
        self.pushButton_mask.setSizePolicy(sizePolicy)
        self.pushButton_mask.setObjectName("pushButton_mask")
        self.gridLayout.addWidget(self.pushButton_mask, 19, 2, 1, 1)
        self.pushButton_paramFile = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_paramFile.sizePolicy().hasHeightForWidth())
        self.pushButton_paramFile.setSizePolicy(sizePolicy)
        self.pushButton_paramFile.setObjectName("pushButton_paramFile")
        self.gridLayout.addWidget(self.pushButton_paramFile, 17, 2, 1, 1)
        self.lineEdit_paramFile = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_paramFile.setObjectName("lineEdit_paramFile")
        self.gridLayout.addWidget(self.lineEdit_paramFile, 17, 3, 1, 3)
        self.pushButton_video = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_video.sizePolicy().hasHeightForWidth())
        self.pushButton_video.setSizePolicy(sizePolicy)
        self.pushButton_video.setObjectName("pushButton_video")
        self.gridLayout.addWidget(self.pushButton_video, 16, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 16, 6, 1, 1)
        self.lineEdit_video = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_video.setObjectName("lineEdit_video")
        self.gridLayout.addWidget(self.lineEdit_video, 16, 3, 1, 3)
        self.pushButton_saveParam = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_saveParam.sizePolicy().hasHeightForWidth())
        self.pushButton_saveParam.setSizePolicy(sizePolicy)
        self.pushButton_saveParam.setObjectName("pushButton_saveParam")
        self.gridLayout.addWidget(self.pushButton_saveParam, 17, 7, 1, 1)
        self.pushButton_next = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_next.sizePolicy().hasHeightForWidth())
        self.pushButton_next.setSizePolicy(sizePolicy)
        self.pushButton_next.setObjectName("pushButton_next")
        self.gridLayout.addWidget(self.pushButton_next, 16, 7, 1, 1)
        self.pushButton_start = QtWidgets.QPushButton(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setMouseTracking(False)
        self.pushButton_start.setAutoFillBackground(False)
        self.pushButton_start.setCheckable(False)
        self.pushButton_start.setAutoDefault(False)
        self.pushButton_start.setDefault(False)
        self.pushButton_start.setFlat(False)
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout.addWidget(self.pushButton_start, 18, 6, 2, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.graphicsView_full = QtWidgets.QGraphicsView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_full.sizePolicy().hasHeightForWidth())
        self.graphicsView_full.setSizePolicy(sizePolicy)
        self.graphicsView_full.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView_full.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView_full.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.graphicsView_full.setObjectName("graphicsView_full")
        self.horizontalLayout_2.addWidget(self.graphicsView_full)
        self.graphicsView_mask = QtWidgets.QGraphicsView(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_mask.sizePolicy().hasHeightForWidth())
        self.graphicsView_mask.setSizePolicy(sizePolicy)
        self.graphicsView_mask.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
        self.graphicsView_mask.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.graphicsView_mask.setResizeAnchor(QtWidgets.QGraphicsView.AnchorViewCenter)
        self.graphicsView_mask.setObjectName("graphicsView_mask")
        self.horizontalLayout_2.addWidget(self.graphicsView_mask)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 2, 13, 6)
        GetMaskParams.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(GetMaskParams)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1161, 22))
        self.menuBar.setObjectName("menuBar")
        GetMaskParams.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(GetMaskParams)
        self.mainToolBar.setObjectName("mainToolBar")
        GetMaskParams.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(GetMaskParams)
        self.statusBar.setObjectName("statusBar")
        GetMaskParams.setStatusBar(self.statusBar)

        self.retranslateUi(GetMaskParams)
        QtCore.QMetaObject.connectSlotsByName(GetMaskParams)

    def retranslateUi(self, GetMaskParams):
        _translate = QtCore.QCoreApplication.translate
        GetMaskParams.setWindowTitle(_translate("GetMaskParams", "GetMaskParams"))
        self.checkBox_isLightBgnd.setText(_translate("GetMaskParams", "is light background?"))
        self.label_5.setText(_translate("GetMaskParams", "Frames to average"))
        self.label_fps.setText(_translate("GetMaskParams", "Expected FPS"))
        self.label_6.setText(_translate("GetMaskParams", "Dilation"))
        self.label_3.setText(_translate("GetMaskParams", "Block Size"))
        self.checkBox_keepBorderData.setText(_translate("GetMaskParams", "keep border data?"))
        self.label_2.setText(_translate("GetMaskParams", "Thresh_C"))
        self.label_4.setText(_translate("GetMaskParams", "Max Area"))
        self.label.setText(_translate("GetMaskParams", "Min Area"))
        self.pushButton_moreParams.setText(_translate("GetMaskParams", "Edit more parameters"))
        self.pushButton_results.setText(_translate("GetMaskParams", "Results Dir"))
        self.pushButton_mask.setText(_translate("GetMaskParams", "Mask Dir"))
        self.pushButton_paramFile.setText(_translate("GetMaskParams", "Parameters File"))
        self.pushButton_video.setText(_translate("GetMaskParams", "Video File"))
        self.pushButton_saveParam.setText(_translate("GetMaskParams", "Save Parameters"))
        self.pushButton_next.setText(_translate("GetMaskParams", "Next Chunk"))
        self.pushButton_start.setText(_translate("GetMaskParams", "Start Analysis"))

