# authority-test-app

Disposable application used to qualify Authority's GitHub integration.
It is a tiny refund calculator with one deliberate defect (ticket PAY-1):
refund amounts with more than two decimals are truncated instead of rounded.
