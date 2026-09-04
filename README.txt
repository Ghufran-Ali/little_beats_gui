# Little Beats - Streamlit GUI

## 1. Install

Open the PyCharm terminal:

```bash
pip install -r requirements.txt
```

## 2. Add your PNG graphs

Create these folders:

```text
data/
├── subject_01/
├── subject_02/
├── subject_03/
├── subject_04/
├── subject_05/
└── subject_06/
```

Inside each folder, put your graph files:

```text
fetal_heart_rate.png
maternal_heart_rate.png
sensor_signal.png
summary.png
```

If your filenames are different, edit `GRAPH_FILES` near the top of `app.py`.

## 3. Run

```bash
streamlit run app.py
```

Then open:

http://localhost:8501

## 4. Main navigation

The GUI includes:

- Home
- Subjects
- Results
- About
- How It Works
- Subject 01 to Subject 06 result pages

The design intentionally follows the clean AgroScan-style layout shown in the sample, but uses a Little Beats / fetal-monitoring theme.
