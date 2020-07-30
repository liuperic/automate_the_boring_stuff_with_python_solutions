#!/usr/bin/env python3
# auto_unsubscriber.py - opens all unsubscribe links in email

import bs4, getpass, imaplib, imapclient, pyzmail, webbrowser

def unsubscribe(email, password):
    imaplib._MAXLINE = 10000000
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(email, password)
    imap_obj.select_folder('INBOX', readonly=True)
    uids = imap_obj.search(['ALL'])

    for identifier in uids:
        raw_message = imap_obj.fetch([identifier], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_message[identifier][b'BODY[]'])
        html = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(html, 'html.parser')
        link_elems = soup.select('a')
        for link in link_elems:
            if 'unsubscribe' in link.text.lower():
                url = link.get('href')
                webbrowser.open(url)
    print('Unsubscribe links from email are opened.')

    imap_obj.logout()

if __name__ == '__main__':
    email = input('Enter your email: ')
    password = getpass.getpass()
    unsubscribe(email, password)
