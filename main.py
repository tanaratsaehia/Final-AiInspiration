import streamlit as st
from roboflow import Roboflow
import time

# genText = False
testText = """โรคไหม้ (Rice Blast Disease) สาเหตุ: เกิดจากเชื้อรา Pyricularia grisea Sacc \n
ลักษณะอาการ: ระยะกล้า  ที่ใบมีแผลจุดสีน้ำตาล ลักษณะคล้ายรูปตา มีสีเทาอยู่ตรงกลางแผล มีขนาดแตกต่างกันตามสภาพแวดล้อมและพันธุ์ข้าว ความกว้างระหว่าง 2-5 มิลลิเมตร และความยาวประมาณ 15-20 มิลลิเมตร แผลนี้สามารถขยายลุกลามจนแผลรวมกันทั่วบริเวณใบ ในกรณีที่โรครุนแรง กล้าข้าวจะแห้ง และฟุบตาย อาการคล้ายถูกไฟไหม้ (blast)\n
ในระยะคอรวง เมื่อข้าวถูกเชื้อรานี้เข้าทำลาย จะทำให้คอรวงเสียหายเมล็ดลีบหมด แต่ถ้าเชื้อราเข้าทำลายตอนรวงข้าวแก่ใกล้เก็บเกี่ยว คอรวงจะปรากฎรอยแผลช้ำสีน้ำตาล ทำให้เปราะหักพับง่าย รวงข้าวร่วงหล่นเสียหายมาก
ในปัจจุบันในแหล่งที่มีการทำนามากกว่าปีละครั้งจะพบโรคนี้แพร่ระบาดเป็นประจำ โดยเฉพาะในแหลงที่ปลูกข้าวหนาแน่น อับลม ใส่ปุ๋ยอัตราสูง และมีสภาพร้อนในตอนกลางวัน อากาศชื้นในตอนกลางคืน\n
การป้องกันและกำจัด\n
1.เกษตรกรไม่ควรตกกล้าหรือหว่านข้าวหนาแน่นเกินไป อัตราที่เหมาะสมคือ 15 กก./ไร่  ในแปลงกล้าควรแบ่งแปลงย่อยให้มีพื้นที่พอเหมาะที่จะเข้าไปทำงานได้อย่างทั่วถึงและมีการถ่ายเทอากาศได้ดี\n
2.หมั่นตรวจดูแปลงเป็นประจำ  โดยเฉพาะแปลงที่มีประวัติการระบาดมาก่อน  ถ้าเกษตรกรพบโรคไหม้ในระยะแรกจำนวนไม่มากสามารถกำจัดโดยตัดใบหรือถอนต้นเป็นโรคออกจากแปลง\n
3.การคลุกเมล็ดพันธุ์ด้วยสารป้องกันกำจัดเชื้อราก่อนนำไปเพาะปลูก เช่น คาซูกามัยซิน ไตรไซคลาโซล คาร์เบนดาซิม  โพรคลอราซ  ตามอัตราที่แนะนำ\n
4.ถ้าเกษตรกรพบโรคไหม้ระบาด ให้ทำการฉีดพ่นสารกำจัดเชื้อรา เช่น คาซูกามัยซิน คาร์เบนดาซิม อีดิเฟนฟอส  ไตรไซคลาโซล  ไอโซโพรไทโอเลน ตามอัตราที่แนะนำ\n
5.เกษตรกรควรปฏิบัติตามแนวทางในการป้องกันโรคข้างต้นนี้ให้ได้มากที่สุด เพื่อการควบคุมโรคให้มีประสิทธิภาพสูงสุด"""

text2 = """สาเหตุของอาการปวดหลัง\n
อาการปวดหลังสามารถเกิดได้จากหลายปัจจัย เช่น การทำกิจกรรมในชีวิตประจำวัน การทำท่าทางที่ไม่ถูกต้องสะสมเป็นเวลานาน การเคล็ดขัดยอก การตึง การอักเสบของกล้ามเนื้อหรือเส้นเอ็นบริเวณหลัง ปัญหาของหมอนรองกระดูก ปัญหาของกระดูกสันหลังและเส้นประสาท ปัญหาจากโรค หรืออาจเกิดจากสาเหตุอื่น ๆ ซึ่งอาการปวดหลังจะส่งผลต่อการเคลื่อนไหวของร่างกายและการดำเนินชีวิตประจำวัน\n
การรักษาอาการปวดหลัง\n
การรักษาอาการปวดหลังมีหลายวิธี ขึ้นอยู่กับระดับความรุนแรงของอาการ หรือสาเหตุของการทำให้เกิดอาการปวดหลัง ถ้าเป็นอาการปวดในระยะสั้นคือเพิ่งปวดหรือปวดไม่มาก สามารถบรรเทาได้ด้วยตัวเองโดยการทาครีมบรรเทาอาการปวด หรือรับประทานยาแก้ปวดที่วางขายตามร้านขายยาทั่วไป\n
อย่างไรก็ตาม การใช้ยาแก้ปวดติดต่อกันเป็นเวลานานอาจส่งผลข้างเคียงต่อการทำงานของไตและเกิดการระคายเคืองต่อกระเพาะอาหารได้\n
ส่วนอาการปวดรุนแรงหรือเรื้อรัง แพทย์อาจแนะนำให้รับประทานยาแก้ปวดควบคู่ไปกับการรักษารูปแบบอื่น เช่น การทำกายภาพบำบัด การฝังเข็ม หรืออาจรวมไปถึงการตรวจจำพวกเอกซเรย์หรือ Magnetic Resonance Imaging (MRI) และการผ่าตัดร่วมด้วย\n
การป้องกันอาการปวดหลัง\n
การป้องกันอาการปวดหลังสามารถทำได้หลายวิธี โดยเริ่มจากการปรับเปลี่ยนพฤติกรรมการใช้หลัง การยืน การเดิน การนั่ง หรือการนอน รวมไปถึงการเลือกรับประทานอาหารที่มีประโยชน์ต่อร่างกาย ออกกำลังกายเพื่อเสริมสร้างให้กล้ามเนื้อหลังแข็งแรงขึ้น ทำให้ยากต่อการอักเสบหรืออ่อนล้าและไม่กลับไปสู่อาการปวดหลังอีก
"""

rf = Roboflow(api_key="xdQoU8d5CCV0aVq7bcxd")
project = rf.workspace().project("rice-disease-ahxc7")
model = project.version(1).model

#html title

def textGenerator(text):
    # global genText
    # global info_container
    displaytext = ""
    for i in text:
        displaytext += i
        info_container.info(displaytext)
        time.sleep(0.02)
    # genText = False

st.title("AgriTect")

with st.form('input_text'):
    text = st.empty()
    text.text_area('', placeholder='กรุณากรอกปัญหาของคุณที่ช่องนี้', value='', key='1')
    submitted = st.form_submit_button('Submit')

info_container = st.empty() 
if submitted:
    info_container = st.empty()
    textGenerator(text2)


# if submitted or genText:
#     print(genText)
#     textGenerator(testText)

uploaded_file = st.file_uploader("Upload rice images here")

colOriImage, colPreImage = st.columns(2)
if uploaded_file is not None:
    # text.text_area('', placeholder='กรุณากรอกปัญหาของคุณที่ช่องนี้', value='', key='2')
    colOriImage.image(uploaded_file, use_column_width=True, caption="Original")
    with open("uploaded_image.jpg", "wb") as f:
        f.write(uploaded_file.read())
        response = model.predict('./uploaded_image.jpg', confidence=50, overlap=30)
        response.save('predictions.jpg')
    colPreImage.image("./predictions.jpg", use_column_width=True, caption="Detected")
    classOfRes = response.json()
    print(classOfRes)
    if response is not None:
        st.write("<script>document.querySelector('textarea').value ='';</script>",unsafe_allow_html=True)
        textGenerator(testText)
    textGenerator(testText)
    # print(classOfRes)
    # print()
    # print(len(classOfRes['predictions']))
    # print()
    # print(classOfRes['predictions'][0]['class'])




styleEdit = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            
            div.stButton > button {
            float: right;
            }
            </style>
            """
st.markdown(styleEdit, unsafe_allow_html=True) 


# st.markdown(
#         """
#         <style>
#         div.stButton > button {
#             float: right;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )
# infer on a local image
# Start = 0
# i = 1
# while True:
#     print("START")
#     print()
#     Start = dt.datetime.now()
#     try :
#         x = model.predict(f"D:\\KKU_World\\1_1\\AiInspiration\\1\\FinalPrj\\Dataset\\RiceDiseases-DataSet-master\\Bacterial leaf blight\\orig\\blight_orig_00{i}.png", confidence=40, overlap=30).save()
#     except:
#         x = model.predict(f"D:\\KKU_World\\1_1\\AiInspiration\\1\\FinalPrj\\Dataset\\RiceDiseases-DataSet-master\\Bacterial leaf blight\\orig\\blight_orig_00{i}.jpg", confidence=40, overlap=30).save()
#     print(x)
#     print()
    
#     print(dt.datetime.now() - Start)
#     i+=1
#     if i >= 9:
#         break
#     time.sleep(2)

# visualize your prediction
# model.predict("your_image.jpg", confidence=40, overlap=30).save("prediction.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())