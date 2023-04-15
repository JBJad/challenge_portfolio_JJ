# ZADANIE 1: konfiguracja oprogramowania.

## Podzadanie 1: Dlaczego zdecydowałem się wziąć udział w wyzwaniu Dare IT Challenge?"

Moim celem jest zapoznanie się z podstawami testowania automatycznego. Obecnie jako tester manualny temat ten pojawia się bardzo często, dlatego też chciałabym sprawdzić, jak bym sobie poradziła w tego typu zadaniach.

# ZADANIE 2: selektory

## Podzadanie 2: Wyszukiwanie selektorów na stronie logowania. 

- input login
  - //*[@id="login"]
  - /html/body/div/form/div/div[1]/div[1]/div/input
  - //input[@type='text']
- input password
  - //*[@id="password"]
  - //input[@type='password']
  - //input[@name='password']
- remind password hyperlink
  - //*[@id="__next"]/form/div/div[1]/a
  - //a[text()='Remind password']
  - //child::div/a
- language selection
  - //*[@id="__next"]/form/div/div[2]/div/div
- sign-in button
  - //*[@id="__next"]/form/div/div[2]/button/span[1]
  - //*[@id="__next"]/form/div/div[2]/button
  - //*[@type='submit']