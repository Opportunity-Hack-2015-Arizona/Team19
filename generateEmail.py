__author__ = 'saipc'

def generateEmail(name, message, image):
    email = """
<!DOCTYPE html><html><head lang="en"><meta charset="UTF-8"><title></title></head><body>
<div class="body" width="600" style="color: #000088; font-size: 20px"><table cellpadding="5"><tbody style="padding: 12px;">
<tr><th colspan="4"><img src="header.jpg" width="600"></th></tr>
<tr><td colspan="2" style="padding: 12px;"><p>Dear Mr. """ + name + """</p>
<p>""" + message + """</p></td><td colspan='1'><img src='""" + image + """'></td></tr>
<tr><td colspan="4"><img src="footer.jpg" width="600"></td></tr></tbody></table></div></body></html>
"""