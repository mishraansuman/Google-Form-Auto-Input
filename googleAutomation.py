from selenium import webdriver
import xlrd

def main():
    driver = webdriver.Chrome()
    # put your complete google form link down here
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScVP6ZjYUfvVCoz0ID_jrbI2fPXn0jxvPLvXiODG_bDboLutQ/viewform')
    # data import from col 1
    firstname=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(firstlist)
    # data import from col 2
    lastname=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(lastlist)
    # data import from col 3
    dob=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[5]/div/div[2]/div/div[2]/div[1]/div/div[1]/input').send_keys(doblist)
    # chooose item from drop down
    def engchoose():
        engoption=driver.find_element_by_xpath('//div[@role="presentation"]')
        engoption.click()
        driver.implicitly_wait(10)
        eng1=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[3]')
        eng2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[4]')
        eng3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[5]')
        eng4 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[6]')
        eng5 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[7]')
        eng6 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[8]')
        eng7 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[9]')
        eng8 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[10]')
        eng9 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[11]')
        eng10 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[6]/div/div[2]/div[2]/div[12]')
        e=[eng1,eng2,eng3,eng4,eng5,eng6,eng7,eng8,eng9,eng10]
        for i in e:
            if (englishlist == 1):
                eng1.click()
                break
            if (englishlist == 2):
                eng2.click()
                break
            if (englishlist == 3):
                eng3.click()
                break
            if (englishlist == 4):
                eng4.click()
                break
            if (englishlist == 5):
                eng5.click()
                break
            if (englishlist == 6):
                eng6.click()
                break
            if (englishlist == 7):
                eng7.click()
                break
            if (englishlist == 8):
                eng8.click()
                break
            if (englishlist == 9):
                eng9.click()
                break
            if (englishlist == 10):
                eng10.click()
                break
    engchoose()
    driver.implicitly_wait(10)
    school=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[7]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(schoollist)
    def classnum():
        cls1=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[2]')
        cls2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[3]')
        cls3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[4]')
        cls4 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[5]')
        cls5 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[6]')
        cls6 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[7]')
        cls7 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[8]')
        cls8 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[9]')
        cls9 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[10]')
        cls10 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[11]')
        cls11 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[12]')
        cls12 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[8]/div/div[2]/div/div[1]/div/div[2]/span/div[13]')
        c=[cls1,cls2,cls3,cls4,cls5,cls6,cls7,cls8,cls9,cls10,cls11,cls12]
        for i in c:
            if (classlist == 1):
                cls1.click()
                break
            if (classlist == 2):
                cls2.click()
                break
            if (classlist == 3):
                cls3.click()
                break
            if (classlist == 4):
                cls4.click()
                break
            if (classlist == 5):
                cls5.click()
                break
            if (classlist == 6):
                cls6.click()
                break
            if (classlist == 7):
                cls7.click()
                break
            if (classlist == 8):
                cls8.click()
                break
            if (classlist == 9):
                cls9.click()
                break
            if (classlist == 10):
                cls10.click()
                break
            if (classlist == 11):
                cls11.click()
                break
            if (classlist == 12):
                cls12.click()
                break
    classnum()
    def coursenum():
        course=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[1]')
        course.click()
        driver.implicitly_wait(10)
        crs1=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[3]')
        crs2=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[4]')
        crs3=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[5]')
        crs4=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[6]')
        crs5=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[7]')
        crs6=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[8]')
        crs7=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[9]')
        crs8=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[10]')
        crs9=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[11]')
        crs10=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[12]')
        crs11=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[13]')
        crs12=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[14]')
        crs13=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[15]')
        crs14=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[16]')
        crs15=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[17]')
        crs16=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[18]')
        crs17=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[19]')
        crs18=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[20]')
        crs19=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[21]')
        crs20=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[22]')
        crs21=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[23]')
        crs22=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[24]')
        crs23=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[25]')
        crs24=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[26]')
        crs25=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[27]')
        crs26=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[28]')
        crs27=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[29]')
        crs28=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[30]')
        crs29=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[31]')
        crs30=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[32]')
        crs31=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[33]')
        crs32=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[34]')
        crs33=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[35]')
        crs34=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[36]')
        crs35=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[37]')
        crs36=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[38]')
        crs37=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[9]/div/div[2]/div[2]/div[39]')
        crl = [crs1,crs2,crs3,crs4,crs5,crs6,crs7,crs8,crs9,crs10,crs11,crs12,crs13,crs14,crs15,crs16,crs17,crs18,crs19,crs20,crs21,crs22,crs23,crs24,crs25,crs26,crs27,crs28,crs29,crs30,crs31,crs32,crs33,crs34,crs35,crs36,crs37]
        for i in crl:
            if (courselist == 'Bank of America Student Leaders'):
                crs1.click()
                break
            if (courselist == 'Boston University – Research in Science & Engineering (RISE)'):
                crs2.click()
                break
            if (courselist == 'Canada/USA Mathcamp'):
                crs3.click()
                break
            if (courselist == 'Carnegie Mellon – Summer Academy for Math + Science (SAMS)'):
                crs4.click()
                break
            if (courselist == 'Cronkite Institute for High School Journalism: Summer Journalism Institute'):
                crs5.click()
                break
            if (courselist == 'Foundation for Teaching Economics – Economics for Leaders (EFL)'):
                crs6.click()
                break
            if (courselist == 'Garcia Scholars – Stony Brook University'):
                crs7.click()
                break
            if (courselist == 'Girls Who Code Summer Immersion Camp'):
                crs8.click()
                break
            if (courselist == 'Hampshire College Summer Studies in Mathematics (HCSSIM)'):
                crs9.click()
                break
            if (courselist == 'Indiana University – Young Women’s Institute'):
                crs10.click()
                break
            if (courselist == 'Jackson Laboratory – Summer Student Program'):
                crs11.click()
                break
            if (courselist == 'JCamp - For Journalism students'):
                crs12.click()
                break
            if (courselist == 'LaunchX'):
                crs13.click()
                break
            if (courselist == 'Massachusetts Institute of Technology – Minority Introduction to Science and Engineering (MITES)'):
                crs14.click()
                break
            if (courselist == 'MathILy – Bryn Mawr College'):
                crs15.click()
                break
            if (courselist == 'MDI Biological Laboratory Summer Research Fellowship'):
                crs16.click()
                break
            if (courselist == 'Michigan Math and Science Scholars'):
                crs17.click()
                break
            if (courselist == 'Michigan State University – High School Honors Science, Math and Engineering Program (HSHSP)'):
                crs18.click()
                break
            if (courselist == 'MIT Research Science Institute'):
                crs19.click()
                break
            if (courselist == 'Monell Center Science Apprenticeship Program'):
                crs20.click()
                break
            if (courselist == 'National Institutes of Health – Summer Internship in Biomedical Research (SIP)'):
                crs21.click()
                break
            if (courselist == 'Ohio State University – Ross Mathematics Program'):
                crs22.click()
                break
            if (courselist == 'Princeton University – Summer Journalism Program'):
                crs23.click()
                break
            if (courselist == 'Program in Mathematics for Young Scientists (PROMYS)'):
                crs24.click()
                break
            if (courselist == 'Simons Summer Research Program'):
                crs25.click()
                break
            if (courselist == 'Stanford Institutes of Medicine Summer Research Program (SIMR)'):
                crs26.click()
                break
            if (courselist == 'Stanford University Mathematics Camp (SUMaC)'):
                crs27.click()
                break
            if (courselist == 'Telluride Association Summer Program (TASP)'):
                crs28.click()
                break
            if (courselist == 'Texas Tech University – Clark Scholar'):
                crs29.click()
                break
            if (courselist == 'U.S. Air Force Academy – Summer Seminar'):
                crs30.click()
                break
            if (courselist == 'U.S. Coast Guard Academy – Academy Introduction Mission (AIM)'):
                crs31.click()
                break
            if (courselist == 'U.S. Military Academy – Summer Leaders Experience'):
                crs32.click()
                break
            if (courselist == 'U.S. Naval Academy – Summer Seminar'):
                crs33.click()
                break
            if (courselist == 'University of Iowa – Secondary Student Training Program (SSTP)'):
                crs34.click()
                break
            if (courselist == 'University of Notre Dame – Leadership Seminars'):
                crs35.click()
                break
            if (courselist == 'University of Pennsylvania – Leadership in the Business World'):
                crs36.click()
                break
            if (courselist == 'Yale Young Global Scholars'):
                crs37.click()
                break
    coursenum()

    email=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[11]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(emaillist)
    phone=driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[12]/div/div[2]/div/div[1]/div/div[1]/input').send_keys(phonelist)
    def choosefed():
        fed = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[13]/div/div[2]/div[1]/div[1]/div[1]')
        fed.click()
        driver.implicitly_wait(10)
        frd1 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[13]/div/div[2]/div[2]/div[3]')
        frd2 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[13]/div/div[2]/div[2]/div[4]')
        frd3 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[13]/div/div[2]/div[2]/div[5]')
        frd4 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[13]/div/div[2]/div[2]/div[6]')
        frd5 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[13]/div/div[2]/div[2]/div[7]')
        frd6 = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div/div/div[2]/div[13]/div/div[2]/div[2]/div[8]')
        f=[frd1,frd2,frd3,frd4,frd5,frd6]
        for i in f:
            if (feedbacklist=='Friends/ Word of mouth'):
                frd1.click()
                break
            if (feedbacklist == 'Social Media'):
                frd2.click()
                break
            if (feedbacklist == 'International School Advisor'):
                frd3.click()
                break
            if (feedbacklist == 'Other website/ Google'):
                frd4.click()
                break
            if (feedbacklist == 'Flyer/ Poster'):
                frd5.click()
                break
            if (feedbacklist == 'other'):
                frd6.click()
                break
    choosefed()
    
workbook = xlrd.open_workbook("svap2020dh-2-march.xlsx")
sheet = workbook.sheet_by_name("SVAP2020dh-march")
rowcount = sheet.nrows
colcount = sheet.ncols
print(rowcount)
print(colcount)

for i in range(2,6):
        firstlist = sheet.cell_value(i, 0)
        print(firstlist)
        lastlist = sheet.cell_value(i, 1)
        doblist = sheet.cell_value(i, 2)
        englishlist=sheet.cell_value(i, 3)   #for english level
        schoollist=sheet.cell_value(i, 4)
        classlist=sheet.cell_value(i, 5)     #for class standard
        courselist=sheet.cell_value(i, 6)
        emaillist=sheet.cell_value(i, 7)
        phonelist=sheet.cell_value(i, 8)
        feedbacklist=sheet.cell_value(i, 9) #for feedback
        main()
