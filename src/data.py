"""HaluEval QA verisini yükleme ve soru bazlı bölme yardımcıları."""
import json
import os

import pandas as pd
import requests
from sklearn.model_selection import GroupShuffleSplit

HALUEVAL_QA_URL = "https://raw.githubusercontent.com/RUCAIBox/HaluEval/main/data/qa_data.json"
SEED = 42


def load_halueval_qa(cache_path: str = "data/qa_data.json") -> list[dict]:
    """HaluEval QA verisini indirir (bir kez) ve satır listesi olarak döndürür."""
    if not os.path.exists(cache_path):
        os.makedirs(os.path.dirname(cache_path) or ".", exist_ok=True)
        resp = requests.get(HALUEVAL_QA_URL, timeout=60)
        resp.raise_for_status()
        with open(cache_path, "w", encoding="utf-8") as f:
            f.write(resp.text)
    with open(cache_path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def to_binary_frame(rows: list[dict]) -> pd.DataFrame:
    """Her soruyu iki örneğe açar: doğru cevap (0) ve halüsinasyonlu cevap (1).

    `qid` sütunu aynı soruya ait iki örneği bağlar; bölmede grup olarak kullanılır.
    """
    data = []
    for qid, r in enumerate(rows):
        base = {"qid": qid, "knowledge": r["knowledge"], "question": r["question"]}
        data.append({**base, "answer": r["right_answer"], "label": 0})
        data.append({**base, "answer": r["hallucinated_answer"], "label": 1})
    return pd.DataFrame(data)


def group_split(df: pd.DataFrame, val_size: float = 0.15, test_size: float = 0.15,
                seed: int = SEED):
    """Soru bazlı eğitim/doğrulama/test bölmesi (veri sızıntısını önler)."""
    holdout = val_size + test_size
    gss = GroupShuffleSplit(n_splits=1, test_size=holdout, random_state=seed)
    train_idx, temp_idx = next(gss.split(df, groups=df["qid"]))
    train, temp = df.iloc[train_idx], df.iloc[temp_idx]

    gss2 = GroupShuffleSplit(n_splits=1, test_size=test_size / holdout, random_state=seed)
    val_idx, test_idx = next(gss2.split(temp, groups=temp["qid"]))
    val, test = temp.iloc[val_idx], temp.iloc[test_idx]

    # Sızıntı kontrolü: hiçbir soru iki kümede birden olmamalı
    s_tr, s_va, s_te = set(train.qid), set(val.qid), set(test.qid)
    assert not (s_tr & s_va) and not (s_tr & s_te) and not (s_va & s_te), "Veri sızıntısı!"

    return (train.reset_index(drop=True), val.reset_index(drop=True),
            test.reset_index(drop=True))
