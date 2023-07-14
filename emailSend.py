import smtplib
from email.mime.multipart import MIMEMultipart #메일의 Data 영역의 메시지를 만드는 모듈
from email.mime.text import MIMEText # 메일의 본문 내용을 만드는 모듈
from email.mime.application import MIMEApplication # 메일의 첨부 파일을 base64 형식으로 변환

from email.mime.base import MIMEBase
from email import encoders
from email.encoders import encode_base64
import zipfile
import os
import glob



#파일이 생성될 때까지 대기
path=os.path.dirname(os.path.realpath(__file__))
count = 1
while not glob.glob(os.path.join(path, 'report*.html')):
    count += 1
    time.sleep(1)


file_path = 'C:\\git\\test\\Report'
zip_file = zipfile.ZipFile(file_path + "\\report.zip", "w")  # "w": write 모드
for file in os.listdir(file_path):
if file.endswith('.html'):
        zip_file.write(os.path.join(file_path, file), compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()



# smpt 서버와 연결
gmail_smtp = "smtp.gmail.com"
gmail_port = 465
smtp = smtplib.SMTP_SSL(gmail_smtp, gmail_port)
print(smtp)

# 로그인
my_id = "bbrosqa2022@gmail.com"
my_password = "nsxlcwljvpiosvdl"
smtp.login(my_id, my_password)

# 메일 기본 정보 설정
msg = MIMEMultipart()
msg["Subject"] = "테스트 결과 전달드립니다."
msg["From"] = "TEST"
msg["To"] = "QA"


# 메일 내용 쓰기
content = "안녕하세요. \n\n\
똑닥 테스트 결과 전송드립니다. \n\n\
감사합니다."

content_part = MIMEText(content, "plain")
msg.attach(content_part)

# 데이터 파일 첨부하기
filename = 'C:\\git\\test\\Report\\report.zip'  # 첨부 파일 이름 이처럼 이름만쓰려면 같은 경로에 파일있어야됨 아니면 절대경로입력
attachment = open(filename, 'rb')
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= " + filename)
msg.attach(part)
encode_base64(part)

# 메일 보내고 서버 끄기
to_mail = "mgpark@bbros.kr"
smtp.sendmail(my_id, to_mail, msg.as_string())
smtp.quit()

