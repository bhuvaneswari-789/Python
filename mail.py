import yagmail

def suretrust_mail():
    # Compose your HTML newsletter content
    html_content = """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> Wonderful SURETRUST Internship Offer.. </title>
</head>
<body style="background-color: #FFFFFF; font-family: Arial, sans-serif;">
  <div style=" background-color: #FFFFFF;">
    <h1 style="color: #333333;">Heartly Welcoming Sure Trust Organization!..</h1>
    <p style="color: #666666;">Dear Coders,</p>
    <p style="color: #666666;">We're proudly announcing the offer for an exclusive internship in suretrust organisation!</p>
   <form action="https://script.google.com/macros/s/AKfycbwq2xCBh_IeyzfWr8FF9jetRn68sY0dDI90NGTutQGvt84lvZxsBSIchAQos2FoWOiB/exec" method="get" style="background-color:#FFC0CB; padding: 20px; border-radius: 5px;">
      <label for="name" style="font-weight: bold;">Name:</label>
      <input type="text" id="name" name="name" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
      <label for="email" style="font-weight: bold;">Email:</label>
      <input type="email" id="email" name="email" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">

      <label for="how" style="font-weight: bold;">What is your role ?</label>
      <select id="how" name="how" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
        <option value="">Select</option>
        <option value="student">Student</option>
        <option value="developer">Developer</option>
        <option value="dataanalyst">DataAnalyst</option>
        <option value="productmanager">Product Manager</option>
        <option value="Other">Other</option>
      </select>

      <label for="why" style="font-weight: bold;">Select your course:</label>
      <select id="why" name="why" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
        <option value="">Select</option>
        <option value="JAVA">JAVA</option>
        <option value="PYTHON">PYTHON</option>
        <option value="DATA SCIENCE">DATA SCIENCE</option>
        <option value="DATA STRUCTURE">DATA STRUCTURE</option>
        <option value="Other">Other</option>
      </select>
       <label for="duration">How long  you intrested to work with suretrust family?</label><br>
       <select id="duration" name="duration" required style="width: 100%; padding: 10px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;">
    <option value="">Select</option>
    <option value="1_month"> 1 month</option>
    <option value="3_months">1 to 3 months</option>
    <option value="5_months">3 to 5 months</option>
    <option value="6_months">More than 5 months</option>
    <option value="indefinitely">Indefinitely</option>
  </select>
<label for="phone">Phone Number:</label><br>
<input type="tel" id="phone" name="phone" pattern="[0-9]{3}-[0-9]{3}-[0-9]{4}" required>
<small>Format: xxx-xxx-xxxx</small>


      <input type="submit" value="Submit" style="background-color: #4CAF50; color: white; padding: 15px 25px; text-align: center; text-decoration: none; display: inline-block; border: none; border-radius: 5px; cursor: pointer;">
    </form>
    <p style="color: #666666;">Best regards,<br>Your Organisation</p>
  </div>
</body>
</html>

    """
    return html_content
    
def send_suretrustmail(html_content):
    # Initialize Yagmail with your Gmail credentials
    yag = yagmail.SMTP('bhuvaneswarisiddamreddy@gmail.com', 'iast rfax npva amgy')


    # Send the newsletter to your subscribers
    yag.send(
        to=['pharika9390@gmail.com','induendluri@gmail.com','bhopibhavitha@gmail.com','r190583@rguktrkv.ac.in','invitha@gmail.com','devipriyagadi99@gmail.com'],
        subject='GREETINGS FROM SURE TRUST',
        contents=html_content
    )

    # Close the Yagmail connection
    yag.close()

if __name__ == "__main__":
    mail_content = suretrust_mail()
    send_suretrustmail(mail_content)



