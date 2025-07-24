#  [Python] Simple Strings to L33t
Convert your regular strings into **L33t Speak** easily with this simple Python script.

---

## 🔧 Description

This script transforms your input string into **L33t Speak** (a.k.a. hacker speak).  
It’s a lightweight and straightforward tool — just run and type!

**Note:**  
By default, both `'i'` and `'l'` are converted into `'1'`.  
Feel free to modify the script if you want a different behavior.

---

## ▶️ Usage

Run the script:

```bash
python string2l33t.py
```
You will be prompted with:
```
Enter:
```
Type your string, for example:
```
This is the test string.
```
Then you'll be asked:
```
Do you want to change space to _ ? (y/n):
```
You can choose:

y(Y) → Replace spaces with underscores (_)

n(N) → Keep spaces as-is

If you enter anything else, the script will exit with an error:
```
Error! Only 'y' and 'n' are allowed
```
💡 Example
Input:
```
This is the test string.
```
Output (if you enter y):
```
Leet: 7h15_15_7h3_7357_57r1n9.
```
Output (if you enter n):
```
Leet: 7h15 15 7h3 7357 57r1n9.
```
