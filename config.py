import numpy as np

RANDOM_STATE = 564
SAMPLE_NUM = 5
MISSING_DATA_LEVELS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
IMPUTATION_METHODS = ["mean", "median", "knn", "regression", "mice", "missforest"]
DISEASES = ["breast_cancer", "diabetes", "eeg_eye", "hepatitis", "NF1", "obesity"]
MISS_TYPES = ["mar", "mcar", "mnar"]

CATEGORICAL_FEATURES = {
    "breast_cancer": [], # target - "class"

    "diabetes": [ # target -  "Diabetes_binary"
        "HighBP",
        "HighChol",
        "CholCheck",
        "Smoker",
        "Stroke",
        "HeartDiseaseorAttack",
        "PhysActivity",
        "Fruits",
        "Veggies",
        "HvyAlcoholConsump",
        "AnyHealthcare",
        "NoDocbcCost",
        "GenHlth",
        "DiffWalk",
        "Sex",
        "Age",
        "Education",
        "Income"
    ],

    "eeg_eye": [], # target - "eyeDetection"

    "hepatitis": [ # target - "Baselinehistological staging"
        "Gender",
        "Fever",
        "Nausea/Vomting",
        "Headache",
        "Diarrhea",
        "Fatigue_&_generalized_bone_ache",
        "Jaundice",
        "Epigastric_pain",
        "Baseline_histological_Grading"
    ],

    "NF1": [ # target - "Case type"
        "Cafe_au_lait_CLS",
        "Axillary_Freckles",
        "Inguinal_Freckles",
        "Lisch_Nodules",
        "Dermal_Neurofibromins",
        "Plexiform_Neurofibromins",
        "Optic_Glioma",
        "Skeletal_Dysplasia",
        "Learning_Disability",
        "Hypertension",
        "Astrocytoma",
        "Hamartoma",
        "Scoliosis",
        "Other_Symptoms",
        "Tumour_Case"
    ],

    "obesity": [ # target - "NObeyesdad"
        "Gender",
        "family_history_with_overweight",
        "FAVC",
        "FCVC",
        "NCP",
        "CAEC",
        "SMOKE",
        "CH2O",
        "SCC",
        "FAF",
        "TUE",
        "CALC",
        "MTRANS"
    ]
}

def get_rng():
    return np.random.default_rng(RANDOM_STATE)

def get_random_num(low=0, high=10000):
    rng = get_rng()
    return rng.integers(low, high)

def count_missing(df):
    df = df[df.columns[:-1]]
    total = df.size
    missing = df.isna().sum().sum()
    percent = (missing / total) * 100
    return total, missing, percent