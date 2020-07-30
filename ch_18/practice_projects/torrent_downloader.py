#!/usr/bin/env python3

import getpass, imaplib, imapclient, pyzmail, subprocess, webbrowser

def check_torrents(email, password):
    imaplib._MAXLINE = 10000000
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(email, password)
    imap_obj.select_folder('INBOX', readonly=True)
    uids = imap_obj.search(['FROM ' + VERIFIED_EMAIL])

    links = []
    if uids:
        for idenitifier in uids:
            raw_messages = imap_obj.fetch([idenitifier], ['BODY[]', 'FLAGS'])
            message = pyzmail.PyzMessage.factory(raw_messages[idenitifier][b'BODY[]'])
            text = message.text_part.get_payload().decode(message.text_part.charset)

            if VERIFIED_PASS in text:
                html = message.html_part.get_payload().decode(message.html_part.charset)
                links.append(html)

        imap_obj.delete_messages(uids)
        imap_obj.expunge()
    
    imap_obj.logout()

    return links

if __name__ == '__main__':
    VERIFIED_EMAIL = 'verifiedemail@example.com'
    VERIFIED_PASS = 'thisverifiedpassword'

    torrent_client = 'ENTER PATH TO QBITTORENT HERE'
    email = input('Enter your email: ')
    password = getpass.getpass()

    links = check_torrents(email, password)

    for link in links:
        torrent_process = subprocess.Popen(torrent_client + ' ' + link)
        torrent_process.wait()

        
