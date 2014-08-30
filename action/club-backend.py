from bottle import error, post, run, request
import os

@error(404)
def error404(error):
    return "404"


@post('/interested')
def interested():
    """Add user information to our text file of interested users."""
    print("New interested user: " + request.forms.yourname + " email " + request.forms.wiscmail)
    statinfo = os.stat('interested.txt')
    if statinfo.st_size > 1024 * 1024 * 1024:
        return 'Something has gone wrong. Please send an email to akersten@wisc.edu telling him that the website is broken.'

    with open('interested.txt', 'a') as f:
        f.write('\n' + request.forms.wiscmail + ' ' + request.forms.yourname)

    return '<script type="text/javascript">alert("Thank you for your interest! Keep an eye out for an email announcement about our kickoff meeting within the next few days!"); window.location="http://enlight.club";</script>'


print("enlight.club backend server running.")
run(host='enlight.club', port=8081)