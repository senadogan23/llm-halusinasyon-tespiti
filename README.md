# Büyük Dil Modellerinde Yanlış Bilgi Üretiminin Otomatik Tespiti

**YMÜ425 – Uygulamalı Sinir Ağları · Fırat Üniversitesi Yazılım Mühendisliği · 2026–2027 Güz**

| Öğrenci | Numara |
|---|---|
| Hüsna Nur Ulu | 230290023 |
| Sena Doğan | 230290024 |
| Sukeyna Söğütçü | 220290056 |

---

## Problem

Büyük dil modelleri (LLM), kendilerine verilen kaynak metinde **bulunmayan** bilgileri de akıcı ve kendinden emin bir dille üretebilir. Bu duruma **halüsinasyon** denir.

Bu projede şu soruya cevap veren bir sinir ağı sistemi geliştiriyoruz:

> Bir kaynak metin, bir soru ve bir LLM cevabı verildiğinde, **cevap kaynak tarafından destekleniyor mu, yoksa uydurma mı?**

- **Girdi:** `(kaynak metin, soru, cevap)`
- **Çıktı:** `0 = destekleniyor`, `1 = halüsinasyon` (ikili sınıflandırma)

## Araştırma Sorusu

İlk veri incelememizde, HaluEval QA kümesinde halüsinasyonlu cevapların doğru cevaplardan **belirgin şekilde daha uzun** olduğunu gördük (ortalama ~11 kelimeye karşı ~2 kelime; örneklerin ~%96'sında halüsinasyonlu cevap daha uzun). Bu, bir modelin anlamı öğrenmeden yalnızca uzunluğa bakarak yüksek başarı elde edebileceği anlamına gelir.

Bu yüzden projemizin temel sorusu:

> **Transformer tabanlı modeller kaynak–cevap tutarlılığını gerçekten mi öğreniyor, yoksa uzunluk gibi yüzeysel ipuçlarına mı dayanıyor?**

## Veri Seti

[HaluEval](https://github.com/RUCAIBox/HaluEval) – QA alt kümesi (10.000 soru → 20.000 ikili örnek).

- Bölme: **soru bazlı** (`GroupShuffleSplit`) %70 eğitim / %15 doğrulama / %15 test. Aynı sorunun doğru ve yanlış cevabı asla farklı kümelere düşmez (veri sızıntısı önlemi).
- Ek test kümesi: **uzunluğu eşitlenmiş** test kümesi (kısayolu ortadan kaldırmak için).

## Modeller (plan)

| Rol | Model |
|---|---|
| Kısayol baseline | Sadece cevap uzunluğu + Lojistik Regresyon |
| Klasik baseline | TF-IDF + Lojistik Regresyon |
| Embedding baseline | Sentence Transformer (kaynak, cevap) benzerliği + MLP |
| Karşılaştırma modeli | BERT-base (cross-encoder, fine-tune) |
| **Ana model** | **DeBERTa-v3-base** (cross-encoder, fine-tune) |

**Metrikler:** Precision, Recall, F1, ROC-AUC, PR-AUC, Confusion Matrix

**Demo:** Gradio arayüzü — kaynak metin ve cevap girilir, halüsinasyon olasılığı gösterilir.

## Klasör Yapısı

```
├── notebooks/        # Adım adım deney notebook'ları (01_, 02_, ...)
├── src/              # Tekrar kullanılan kodlar (veri yükleme, bölme, metrikler)
├── data/             # (git'e eklenmez) indirilen ve işlenen veri
├── results/          # Grafikler, tablolar, metrik çıktıları
├── docs/             # Görev dağılımı, literatür notları, öneri formu taslakları
└── app/              # Gradio demo uygulaması (ileride)
```

## Nasıl Çalıştırılır

```bash
pip install -r requirements.txt
jupyter notebook notebooks/01_veri_inceleme.ipynb
```

Veya Google Colab'da: notebook'u açıp **Runtime → Run all**.

## İlerleme

Ayrıntılı görev listesi ve takvim: [`docs/GOREVLER.md`](docs/GOREVLER.md)

- [x] Proje konusu ve kapsamın belirlenmesi
- [x] Veri setinin temini ve ilk inceleme (EDA)
- [ ] Literatür taraması (10+ kaynak)
- [ ] Baseline modeller
- [ ] Proje Öneri Formu
- [ ] BERT / DeBERTa fine-tuning
- [ ] Uzunluğu eşitlenmiş test deneyi
- [ ] Hata analizi
- [ ] Gradio demo
- [ ] Proje raporu ve sunum
