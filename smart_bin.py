#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 23:08:24 2021

@author: simeon
"""


from PyQt5 import QtWidgets, QtCore
from Libraries.main_window import Ui_MainWindow
import sys
import requests
import pprint
import cv2
from pyzbar import pyzbar

from ml.predict import SmartBinPredictor

PRODUCT_INFO = None


class Barcode_Scanner(QtCore.QObject):
    @staticmethod
    def _get_product_info(barcode):
        global PRODUCT_INFO
        url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

        response = requests.get(url)
        status = response.status_code
        if status == 200:
            result = response.json()

            try:
                print("Product information:")
                pprint.pprint(result['product']['packaging_text_en'])
                pprint.pprint(result['product']['code'])
                pprint.pprint(result['product']['product_name'])
                PRODUCT_INFO = result
            except:
                print("Information missing")

    def read_barcodes(self, frame, predictor):
        ai_barcode = predictor.predict(frame)
        if ai_barcode:
            self._get_product_info(ai_barcode)
            print(ai_barcode)
            return "Exit"

        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            barcode_info = barcode.data.decode('utf-8')
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)

            print(barcode_info)
            if barcode_info:
                self._get_product_info(barcode_info)
                return "Exit"

        return frame

    def start(self):
        predictor = SmartBinPredictor('ml/models/model1.pt')
        camera = cv2.VideoCapture(0)
        ret, frame = camera.read()
        while ret:
            ret, frame = camera.read()
            frame = self.read_barcodes(frame, predictor)
            if frame == "Exit":
                window.procuct_page()
                break
            frame = cv2.flip(frame, 1)
            cv2.imshow('Barcode/QR code reader', frame)
            if cv2.waitKey(1) & 0xFF == 27:
                break
        camera.release()
        cv2.destroyAllWindows()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.url = "sloji-url-tuk"

    def run_barcode(self):
        self.work = Barcode_Scanner()
        self.thread = QtCore.QThread(parent=self)

        self.thread.started.connect(self.work.start)
        self.thread.start()

    def procuct_page(self):
        global PRODUCT_INFO
        try:
            window.Next.clicked.disconnect(window.run_barcode)
        except:
            pass
        window.Next.clicked.connect(window.next_action)
        window.Next.setText("Next")
        self.stackedWidget.setCurrentIndex(1)
        self.Product_Name.setText(str(PRODUCT_INFO['product']['product_name']))
        self.Recycable_Name.setText(str("Yes"))
        split_text = PRODUCT_INFO['product']['packaging_text_en'].split("|")
        if "recyclable" in split_text[0] and "discard" in split_text[0]:
            self.Recycable_Name.setText(str("Partially"))
        elif "discard" in split_text:
            self.Recycable_Name.setText(str("No"))
        else:
            self.Recycable_Name.setText(str("Yes"))


        materials = split_text[0].replace(", ", "\n")
        self.instructions_list = split_text[1].split(", ")
        self.Materials.setText(materials)
        self.action_number = 0
        self.Current_Action.setText(self.instructions_list[self.action_number])
        # self.bin_request(self.instructions_list[self.action_number])

    def next_action(self):
        try:
            self.action_number += 1
            self.Current_Action.setText(self.instructions_list[self.action_number])
            # self.bin_request(self.instructions_list[self.action_number])
        except:
            self.Current_Action.setText("All Done! Next one?")
            try:
                window.Next.clicked.disconnect(window.next_action)
            except:
                pass
            window.Next.clicked.connect(window.run_barcode)
            window.Next.setText("New One")

    def bin_request(self, command):
        if "yellow" in command:
            r = requests.get(self.url, params="yellow")
        elif "blue" in command:
            r = requests.get(self.url, params="blue")
        elif "green" in command:
            r = requests.get(self.url, params="green")
        else:
            pass

    def main_page(self):
        self.stackedWidget.setCurrentIndex(0)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.Next.clicked.connect(window.run_barcode)
window.Video_Button.clicked.connect(window.run_barcode)
window.Exit.clicked.connect(window.main_page)
window.show()
app.exec()
