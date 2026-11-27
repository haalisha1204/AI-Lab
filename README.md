# AI-Lab

Artificial Intelligence lab exercises, datasets, results, and assignments.

## Repository layout

- `all_datasets/` contains datasets used by the labs.
- `all_experiments/` contains runnable lab scripts and shared utilities.
- `results/` contains generated outputs, grouped by lab.
- `Assignment_Reasoning_Semantic_NLP/` contains the reasoning and NLP assignment.
- `Lab06_Assignment/` contains the handwriting OCR assignment and its evidence.
- `GA Assignment/` contains the delivery-route genetic algorithm assignment.
- `Lab06/` contains the robotics sensor-control lab file.

## Lab scripts and results

Run commands from the repository root after installing dependencies from `requirements.txt`.

| Lab | Script or status | Results |
|---|---|---|
| 01 Search foundations | `all_experiments/lab01_search_foundations.py` | `results/lab01/` |
| 03 Search engineering | `all_experiments/lab03_search_engineering.py` | `results/lab03/` |
| 04 Fuzzy logic and ANFIS | `all_experiments/lab04_fuzzy_anfis.py` | `results/lab04/` |
| 05 | Results are available. | `results/lab05/` |
| 06 Handwriting OCR | `all_experiments/lab06_handwriting_ocr_worked.py` | `results/lab06/` |
| Airline tweet sentiment | `all_experiments/lab07_airline_sentiment.py` | `results/lab08_sentiment/` |
| Genetic algorithm regression | `all_experiments/lab08_genetic_algorithm_regression.py` | `results/lab08/` |

The OCR lab also needs the Tesseract application installed on the computer.

## Running a lab script

For example, run the OCR lab from the repository root with:

```powershell
python .\all_experiments\lab06_handwriting_ocr_worked.py
```

Generated files are written to the corresponding folder under `results/`.
