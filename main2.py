from multiprocessing import Value
import streamlit as st
import pandas as pd
from pandas import DataFrame, Series
import numpy as np
from PIL import Image
import xlsxwriter
from io import BytesIO

# import FPDF
# import EMAIL

output = BytesIO()


col1, col2 = st.columns([2,1])

with col1:
        # Title
        st.title('Cold Drink Operations')

        # Header
        st.header("Assesment Breakfix Form")

        # Description
        st.text("Assesment ini dilakukan untuk Teknisi Breakfix GDM")

with col2:
        #Image
        image = Image.open('cdo.png')
        st.image(image, width=195)


###############################################################################

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Detail Assesment", "Pemahaman Tools", "Pemahaman Safety", "Service Knowledge", "Summary", "Result"])

with tab1:
   # Header-2
        st.header("1. Detail Assesment")

        #Body Form
        ### 1. Input Nama Teknisi
        nama_teknisi = st.text_input("Nama Teknisi", 
                                value="", placeholder="Isi dengan nama Teknisi")

        ### 2. Jenis Pekerjaan
        jenis_pekerjaan = st.text_input("Jenis Pekerjaan", 
                                value="", placeholder="Breakfix GDM / Workshop GDM / Breakfix Postmix / Breakfix GDM")

        ### 3. Instansi (CDO CCEP / ESP)
        instansi = st.text_input("Instansi", 
                                value="", placeholder="CDO Region 1 / ESP Tita Jakarta")

        ### 4. Nama Assesor
        nama_assesor = st.text_input("Nama Assesor", 
                                value="", placeholder="Yofiatna")

        ### 5. Tanggal Assesment
        tanggal_assesment = st.date_input("Tanggal Assesment")

with tab2:
   #Header-3
        st.header("2. Questioner Assesment")
        st.subheader('2a. Pemahaman Penggunaan Tools')

        #Body Form
        ### 1
        tools1 = st.radio("1. Teknisi memahami fungsi dari Tang Kombinasi, Obeng(+) & (-), Kunci Inggris, Senter & Pembersih Karat (WD40)", 
                                ('Yes', 'N/A'))
        if tools1 == 'N/A':
                tools1 = st.text_input("tools1", value="", label_visibility="hidden", placeholder="Isi Reason N/A")
        ################            ----------------------------------------        #################
        tools2 = st.radio("2. Teknisi memahami fungsi dari Pembuka Isolator", 
                                ('Yes', 'N/A'))
        if tools2 == 'N/A':
                tools2 = st.text_input("tools2", value="", label_visibility="hidden", placeholder="Isi Reason N/A")
        ################            ----------------------------------------        #################
        tools3 = st.radio("3. Teknisi memahami fungsi Skun(Kabel Penyambung", 
                                ('Yes', 'N/A'))
        if tools3 == 'N/A':
                tools3 = st.text_input("tools3", value="", label_visibility="hidden", placeholder="Isi Reason N/A")
        ################            ----------------------------------------        #################
        tools4 = st.radio("4. Teknisi memahami fungsi Kape, Silet Pemotong, Sikat Keras, Kain Lap Silikon, Cairan Pembersih Kaca, Sikat Pembersih Debu & Pengki serta Ember Lipat", 
                                ('Yes', 'N/A'))
        if tools4 == 'N/A':
                tools4 = st.text_input("tools4", value="",label_visibility="hidden", placeholder="Isi Reason N/A")
        ################            ----------------------------------------        #################
        tools5 = st.radio("5. Teknisi memahami fungsi Martil", 
                                ('Yes', 'N/A'))
        if tools5 == 'N/A':
                tools5 = st.text_input("tools5", value="", label_visibility="hidden", placeholder="Isi Reason N/A")
        ################            ----------------------------------------        #################
        tools6 = st.radio("6. Teknis memahami fungsi Termometer", 
                                ('Yes', 'N/A'))
        if tools6 == 'N/A':
                tools6 = st.text_input("tools6", value="", label_visibility="hidden", placeholder="Isi Reason N/A")
        ################            ----------------------------------------        #################
        tools7 = st.radio("7. Teknisi memahami fungsi Kamera Digital", 
                                ('Yes', 'N/A'))
        if tools7 == 'N/A':
                tools7 = st.text_input("tools7", value="", label_visibility="hidden", placeholder="Isi Reason N/A")
        ################            ----------------------------------------        #################
        tools8 = st.radio("8. Teknisi memahami fungsi AVOMeter/Multimeter", 
                                ('Yes', 'N/A'))
        if tools8 == 'N/A':
                tools8 = st.text_input("tools8", value="",label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        tools9 = st.radio("9. Teknisi memahami fungsi Test Pen (100-500 V AC)", 
                                ('Yes', 'N/A'))
        if tools9 == 'N/A':
                tools9 = st.text_input("tools9", value="", label_visibility="hidden", placeholder="Isi Reason N/A")   


with tab3:
        st.subheader('2b. Pemahaman Safety')

        #Body Form
        ### 2
        ################            ----------------------------------------        #################
        saf1 = st.radio("1. Safety Shoes, Face Mask, Hand Gloves dan Seragam", 
                                ('Yes', 'N/A'))
        if saf1 == 'N/A':
                saf1 = st.text_input("saf1", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        saf2 = st.radio("2. Teknisi memahami fungsi kabel grounding (GDM dan Outlet) dan PRCD", 
                                ('Yes', 'N/A'))
        if saf2 == 'N/A':
                saf2 = st.text_input("saf2", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        saf3 = st.radio("3. Teknisi memahami fungsi MCB", 
                                ('Yes', 'N/A'))
        if saf3 == 'N/A':
                saf3 = st.text_input("saf3", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        saf4 = st.radio("4. Teknisi memahami LOTO", 
                                ('Yes', 'N/A'))
        if saf4 == 'N/A':
                saf4 = st.text_input("saf4", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        saf5 = st.radio("5. Teknisi memahami Line Fasa dan Netral", 
                                ('Yes', 'N/A'))
        if saf5 == 'N/A':
                saf5 = st.text_input("saf5", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        saf6 = st.radio("6. Teknisi memahami Normally Closed dan Normally Open", 
                                ('Yes', 'N/A'))
        if saf6 == 'N/A':
                saf6 = st.text_input("saf6", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        saf7 = st.radio("7. Teknisi paham penggunaan Skun Kabel dan Kabel Ties", 
                                ('Yes', 'N/A'))
        if saf7 == 'N/A':
                saf7 = st.text_input("saf7", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################

with tab4:
        st.subheader('2c. Service Knowledge')

        #Body Form
        ### 3
        ################            ----------------------------------------        #################
        ser1 = st.radio("1. Teknisi memahami jenis dan fungsi lampu berikut dengan aksesorisnya", 
                                ('Yes', 'N/A'))
        if ser1 == 'N/A':
                ser1 = st.text_input("ser1", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser2 = st.radio("2. Teknisi memahami prinsip dan cara kerja Motor Fan Evap dan Kondensor", 
                                ('Yes', 'N/A'))
        if ser2 == 'N/A':
                ser2 = st.text_input("ser2", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser3 = st.radio("3. GDM Type CPE (253,254)", 
                                ('Yes', 'N/A'))
        if ser3 == 'N/A':
                ser3 = st.text_input("ser3", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser4 = st.radio("4. GDM Type Frigorex(650, 1000)", 
                                ('Yes', 'N/A'))
        if ser4 == 'N/A':
                ser4 = st.text_input("ser4", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser5 = st.radio("5. Teknisi memahami prinsip dan cara kerja Relay, Overload dan Capacitor", 
                                ('Yes', 'N/A'))
        if ser5 == 'N/A':
                ser5 = st.text_input("ser5", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser6 = st.radio("6. Teknisi memahami nilai continuity dan arus pada compressor", 
                                ('Yes', 'N/A'))
        if ser6 == 'N/A':
                ser6 = st.text_input("ser6", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser7 = st.radio("7. Teknisi memahami C-S,C-R dan S-R", 
                                ('Yes', 'N/A'))
        if ser7 == 'N/A':
                ser7 = st.text_input("ser7", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser8 = st.radio("8. Teknisi memahami prinsip dan cara kerja EMS", 
                                ('Yes', 'N/A'))
        if ser8 == 'N/A':
                ser8 = st.text_input("ser8", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser9 = st.radio("9. Teknisi memahami prinsip dan cara kerja Thermosensor (PTC)", 
                                ('Yes', 'N/A'))
        if ser9 == 'N/A':
                ser9 = st.text_input("ser9", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser10 = st.radio("10. Teknisi memahami prinsip dan cara kerja Thermostat Mechanical", 
                                ('Yes', 'N/A'))
        if ser10 == 'N/A':
                ser10 = st.text_input("ser10", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser11 = st.radio("11. Teknisi memahami kurang & lebih refrigeran", 
                                ('Yes', 'N/A'))
        if ser11 == 'N/A':
                ser11 = st.text_input("ser11", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser12 = st.radio("12. Teknisi memahami refrigeran bocor", 
                                ('Yes', 'N/A'))
        if ser12 == 'N/A':
                ser12 = st.text_input("ser12", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser13 = st.radio("13. Teknisi memahami refrigeran mampat", 
                                ('Yes', 'N/A'))
        if ser13 == 'N/A':
                ser13 = st.text_input("ser13", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser14 = st.radio("14. Teknisi memahami sisi High Pressure Cooling System", 
                                ('Yes', 'N/A'))
        if ser14 == 'N/A':
                ser14 = st.text_input("ser14", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser15 = st.radio("15. Teknisi memahami sisi Low Pressure Cooling System", 
                                ('Yes', 'N/A'))
        if ser15 == 'N/A':
                ser15 = st.text_input("ser15", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser16 = st.radio("16. Teknisi memahami fungsi PCB PS dan Delay Time (M253)", 
                                ('Yes', 'N/A'))
        if ser16 == 'N/A':
                ser16 = st.text_input("ser16", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser17 = st.radio("17. Teknisi memahami fungsi Power Stabilizer (PS)", 
                                ('Yes', 'N/A'))
        if ser17 == 'N/A':
                ser17 = st.text_input("ser17", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser18 = st.radio("18. Teknisi memahami fungsi Voltage Protector (VP)", 
                                ('Yes', 'N/A'))
        if ser18 == 'N/A':
                ser18 = st.text_input("ser18", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser19 = st.radio("19. Teknisi memahami DC Converter CPE", 
                                ('Yes', 'N/A'))
        if ser19 == 'N/A':
                ser19 = st.text_input("ser19", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser20 = st.radio("20. Teknisi memahami PC Board CPE", 
                                ('Yes', 'N/A'))
        if ser20 == 'N/A':
                ser20 = st.text_input("ser20", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################
        ser21 = st.radio("21. Teknisi memahami Delay Timer CPE", 
                                ('Yes', 'N/A'))
        if ser21 == 'N/A':
                ser21 = st.text_input("ser21", value="", label_visibility="hidden", placeholder="Isi Reason N/A")        
        ################            ----------------------------------------        #################

with tab5:
        # Summary 1
        st.header('Summary')
        st.write("Teknisi : ", nama_teknisi)
        st.write("Jenis Pekerjaan : ", jenis_pekerjaan)
        st.write("Instansi : ", instansi)
        st.write("Nama Assesor : ", nama_assesor)
        st.write("Tanggal : ", tanggal_assesment)

        # Summary 2
        st.header('Summary 2')
        st.write("Penguasaan Tools 1: ", tools1)
        st.write("Penguasaan Tools 2: ", tools2)
        st.write("Penguasaan Tools 3: ", tools3)
        st.write("Penguasaan Tools 4: ", tools4)
        st.write("Penguasaan Tools 5: ", tools5)
        st.write("Penguasaan Tools 6: ", tools6)
        st.write("Penguasaan Tools 7: ", tools7)
        st.write("Penguasaan Tools 8: ", tools8)
        st.write("Penguasaan Tools 9: ", tools9)

        # Summary 3
        st.header('Summary 3')
        st.write("Penguasaan Safety 1: ", saf1)
        st.write("Penguasaan Safety 2: ", saf2) 
        st.write("Penguasaan Safety 3: ", saf3)
        st.write("Penguasaan Safety 4: ", saf4)
        st.write("Penguasaan Safety 5: ", saf5)
        st.write("Penguasaan Safety 6: ", saf6)
        st.write("Penguasaan Safety 7: ", saf7)

        # Summary 4
        st.header('Summary 4')
        st.write("Penguasaan Service 1: ", ser1)
        st.write("Penguasaan Service 2: ", ser2)
        st.write("Penguasaan Service 3: ", ser3)
        st.write("Penguasaan Service 4: ", ser4)
        st.write("Penguasaan Service 5: ", ser5)
        st.write("Penguasaan Service 6: ", ser6)
        st.write("Penguasaan Service 7: ", ser7)
        st.write("Penguasaan Service 8: ", ser8)
        st.write("Penguasaan Service 9: ", ser9)
        st.write("Penguasaan Service 10: ", ser10)
        st.write("Penguasaan Service 11: ", ser11)
        st.write("Penguasaan Service 12: ", ser12)
        st.write("Penguasaan Service 13: ", ser13)
        st.write("Penguasaan Service 14: ", ser14)
        st.write("Penguasaan Service 15: ", ser15)
        st.write("Penguasaan Service 16: ", ser16)
        st.write("Penguasaan Service 17: ", ser17)
        st.write("Penguasaan Service 18: ", ser18)
        st.write("Penguasaan Service 19: ", ser19)
        st.write("Penguasaan Service 20: ", ser20)
        st.write("Penguasaan Service 21: ", ser21)

with tab6 :
        if st.button('Selesai Assesment'):
                # Write files to in-memory strings using BytesIO
                # See: https://xlsxwriter.readthedocs.io/workbook.html?highlight=BytesIO#constructor
                workbook = xlsxwriter.Workbook(output, {'in_memory': True})
                worksheet = workbook.add_worksheet()

                worksheet.write('A1', nama_teknisi)

                workbook.close()

                st.download_button(
                        label="Download Excel workbook",
                        data=output.getvalue(),
                        file_name= nama_teknisi+"_" +nama_assesor+"_"+"workbook.xlsx",
                        mime="application/vnd.ms-excel"
                        )