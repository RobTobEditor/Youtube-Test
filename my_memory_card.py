from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QButtonGroup, QMessageBox
)
from random import shuffle
from random import randint

app = QApplication([])
widgets = QWidget()
widgets.setWindowTitle('RobTobEditor Youtube Contest')
widgets.resize(700, 500)

class Q_and_A():
    def __init__(self, question, rightAnswer, wrong1, wrong2, wrong3):
        self.Q = question
        self.rA = rightAnswer
        self.wA1 = wrong1
        self.wA2 = wrong2
        self.wA3 = wrong3

widgets.correctAnsCounter = 0
q = [
    Q_and_A('Are you subscibed to RobTobEditor?', 'Yes!', 'No', 'Who is he?', "I'm subscribing right now"),
    Q_and_A('Which is my skin?', 'Among Us', 'Bird', 'Robot', 'Steve'),
    Q_and_A('Which is my favorite color?', 'Green', 'Blue', 'Red', 'Black'),
    Q_and_A('How many subscribers I have?', '34', '33', '40', '30')
    ]
qEdit = [
    Q_and_A('Are you subscibed to RobTobEditor?', 'Yes!', 'No', 'Who is he?', "I'm subscribing right now"),
    Q_and_A('Which is my skin?', 'Among Us', 'Bird', 'Robot', 'Steve'),
    Q_and_A('Which is my favorite color?', 'Green', 'Blue', 'Red', 'Black'),
    Q_and_A('How many subscribers I have?', '46', '33', '40', '30')
    ]

questionText = QLabel('Are you subscibed to RobTobEditor?')
sendButton = QPushButton('Answer')
RadioGroupBox = QGroupBox('Answers')
rbtn1 = QRadioButton('1')
rbtn2 = QRadioButton('2')
rbtn3 = QRadioButton('3')
rbtn4 = QRadioButton('4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

h_ansLine = QHBoxLayout()
v_ansLine1 = QVBoxLayout()
v_ansLine2 = QVBoxLayout()

v_ansLine1.addWidget(rbtn1)
v_ansLine1.addWidget(rbtn2)
v_ansLine2.addWidget(rbtn3)
v_ansLine2.addWidget(rbtn4)

h_ansLine.addLayout(v_ansLine1)
h_ansLine.addLayout(v_ansLine2)

RadioGroupBox.setLayout(h_ansLine)

AnsGroupBox = QGroupBox('Results')
resultText = QLabel('True or False?')
correctText = QLabel('Correct answer')

v_resLine = QVBoxLayout()
v_resLine.addWidget(resultText, alignment = Qt.AlignTop)
v_resLine.addWidget(correctText, alignment = Qt.AlignHCenter, stretch = 2)
AnsGroupBox.setLayout(v_resLine)

h_questLine = QHBoxLayout()
h_ansLines = QHBoxLayout()
h_btnLine = QHBoxLayout()

h_questLine.addWidget(questionText, alignment = Qt.AlignCenter)
h_ansLines.addWidget(RadioGroupBox)
h_ansLines.addWidget(AnsGroupBox)
h_btnLine.addStretch(1)
h_btnLine.addWidget(sendButton, stretch = 2)
h_btnLine.addStretch(1)

AnsGroupBox.hide()


v_cardLine = QVBoxLayout()

v_cardLine.addLayout(h_questLine, stretch = 2)
v_cardLine.addLayout(h_ansLines, stretch = 8)
v_cardLine.addStretch(1)
v_cardLine.addLayout(h_btnLine, stretch = 1)
v_cardLine.addStretch(1)
v_cardLine.addSpacing(5)


def showResult():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    sendButton.setText('Next Question')
def showQuestion():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    sendButton.setText('Answer')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answer = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Q_and_A):
    shuffle(answer)
    answer[0].setText(q.rA)
    answer[1].setText(q.wA1)
    answer[2].setText(q.wA2)
    answer[3].setText(q.wA3)
    questionText.setText(q.Q)
    correctText.setText(q.rA)
    showQuestion()

def showCorrect(res):
    resultText.setText(res)
    showResult()

def checkAnswer():
    if answer[0].isChecked():
        if questionText.text() == 'Are you subscibed to RobTobEditor?':
            showCorrect('Yay!')
        elif questionText.text() == 'Which is my skin?':
            showCorrect('Correct!')
        elif questionText.text() == 'Which is my favorite color?':
            showCorrect('Correct!')
        elif questionText.text() == 'How many subscribers I have?':
            showCorrect('Correct!')
        widgets.correctAnsCounter += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            if questionText.text() == 'Are you subscibed to RobTobEditor?':
                showCorrect('Subscribe please!')
            elif questionText.text() == 'Which is my skin?':
                showCorrect('Incorrect!')
            elif questionText.text() == 'Which is my favorite color?':
                showCorrect('Incorrect!')
            elif questionText.text() == 'How many subscribers I have?':
                showCorrect('Incorrect!')
        else:
            showCorrect("Why you didn't answer?")

def statistic(CorrectAnswers, From):
    sendButton.setText('Close')
    prcent = (CorrectAnswers / From) * 100
    message = QMessageBox()
    text_prcent = 'You got ' + str(prcent) + '%\nYou are cool!'
    message.setText(text_prcent)
    message.exec_()

def nextQuestion():
    if len(qEdit) != 0:
        coorentQuestion = randint(0, len(qEdit)-1)
        coorentQ = qEdit[coorentQuestion]
    if len(qEdit) != 0:
        qEdit.remove(coorentQ)
        ask(coorentQ)
    else:
        statistic(widgets.correctAnsCounter, len(q))

def clickOK():
    if sendButton.text() == 'Answer':
        checkAnswer()
    elif sendButton.text() == 'Next Question':
        nextQuestion()
    elif sendButton.text() == 'Close':
        widgets.close()

sendButton.clicked.connect(clickOK)
nextQuestion()
widgets.setLayout(v_cardLine)
widgets.show()
app.exec_()