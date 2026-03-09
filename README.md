# Package Classification System

## Overview

This project implements a function that classifies packages for a robotic dispatch system based on **size** and **mass**.

The system determines whether a package should be sent to:

* **STANDARD stack**
* **SPECIAL stack**
* **REJECTED stack**

## Classification Rules

A package is classified using the following criteria:

### Bulky Package

A package is considered **bulky** if:

* Volume ≥ **1,000,000 cm³**

OR

* Any dimension ≥ **150 cm**

### Heavy Package

A package is considered **heavy** if:

* Mass ≥ **20 kg**

### Final Classification

| Condition       | Result   |
| --------------- | -------- |
| Bulky AND Heavy | REJECTED |
| Bulky OR Heavy  | SPECIAL  |
| Neither         | STANDARD |

---

## Function Signature

```python
sort(width, height, length, mass)
```

Parameters:

* `width` (cm)
* `height` (cm)
* `length` (cm)
* `mass` (kg)

Returns:

```
STANDARD
SPECIAL
REJECTED
```

---

## How to Run

1. Clone the repository

```
git clone https://github.com/yourusername/package-classifier.git
```

2. Navigate to the project folder

```
cd package-classifier
```

3. Run the script

```
python main.py
```

---

## Example Test Cases

```
sort(10, 10, 10, 1)      → STANDARD
sort(100, 100, 100, 5)   → SPECIAL
sort(150, 10, 10, 5)     → SPECIAL
sort(10, 10, 10, 20)     → SPECIAL
sort(200, 200, 200, 25)  → REJECTED
```

---

## Online Execution

You can run the solution directly using Replit:

```
https://replit.com/@yourusername/package-classifier
```

Simply open the link and click **Run**.

---

## Author

Animashaun Afolabi
