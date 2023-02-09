from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from time import sleep

email_user_name = 'poobiat3@gmail.com'
email_user_pass = 'mifaglynnlmaunmm'

class Email:

    def __init__(self):
        try:
            self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            self.server.ehlo()

            # self.server.starttls(context=context)
            # Logando na conta utilizando os parametros
            self.server.login(email_user_name, email_user_pass)
            print("Login no e-mail, ok!")

        except Exception as e:
            print("ERRO AO LOGAR NO E-MAIL")
            print(e)


    def send(self, destinatario, titulo, mensagem, cc_recipients=None,  html = None, list_imgs_data = None):
        """
            list_imags_data = é uma lista de dicionários [{'data':image_data,'cid':'image1'}] onde: 
                    data: é os dados binarios da imagem
                    cid: é o content id (qualquer caractere para relacionar a imagem)
            para uasr, adicione no html:
                <img src="cid:_cid_" alt="img" /> # e substitua _cid_ pelo cid da imagem
        """


        # Criando uma instancia de objeto
        msg = MIMEMultipart()

        msg['From'] = email_user_name
        msg['To'] = destinatario
        msg['Subject'] = titulo

        if cc_recipients is not None:
            msg['Cc'] = ", ".join(cc_recipients)

        # Corpo da mensagem
        if not mensagem is None:
            msg.attach(MIMEText(mensagem,'plain'))

        if not html is None:
            msg.attach(MIMEText(html, 'html'))


        if not list_imgs_data is None:
            for img in list_imgs_data:
                img_attach = MIMEImage(img['data'])
                img_attach.add_header('Content-ID', '<'+str(img['cid'])+'>')
                msg.attach(img_attach)

        repetir = 0
        while repetir <= 1:
            try:
                self.server.sendmail(msg['From'], msg['To'], msg.as_string())
                print(f"Email enviado com sucesso para: {msg['To']}")
                repetir = 10
                break
            except Exception as e:
                print("ERRO AO ENVIAR E-MAIL")
                print(e)
                self.__init__()
                repetir += 1

    def __del__(self):
        try:
            self.server.quit()
        except Exception as e:
            print(e)




#def Exemplo_email_com_imagem():
#    import matplotlib.pyplot as plt
#    import io
#
#    plt.plot(range(100))
#    s = io.BytesIO()
#    plt.savefig(s, format='png', bbox_inches="tight")
#    plt.close()
#    image_data = s.getvalue() # pega os dados binarios da imagem
#
#    emails_dict = {
#        'destinatario':'daniel.fazzioni@gmail.com',
#        'titulo':'teste',
#        'mensagem' : None,
#        'html' : """\
#                <html>
#                    <head></head>
#                    <body>
#                        <p>Exemplo de e-mail com imagem!!</p>
#                        <img src="cid:image1" alt="img" />
#                    </body>
#                </html>    
#                """,
#        'list_imgs_data' : [{'data':image_data,'cid':'image1'}]
#        # cid = content id
#    }
#    e = Email()
#    e.send(**emails_dict)
#    emails_dict['destinatario'] = "ugarte_alex@discente.ufg.br"
#    e.send(**emails_dict)

if __name__ == '__main__':
    a = Email()
    a.send('daniel.fazzioni@gmail.com','tese','teste') 