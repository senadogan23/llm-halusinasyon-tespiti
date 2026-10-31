# Görev Dağılımı ve Takvim

> Görevler rollere göre dağıtılmıştır; ancak tüm ekip üyeleri projenin her aşamasından sorumludur. Her hafta sonunda kısa bir ekip içi değerlendirme toplantısı yapılır.

## Roller

Sorumlular ekip toplantısında belirlenecek — isimleri aşağıya yazın.

| Rol | Sorumlu | Kapsam |
|---|---|---|
| **A – Veri ve Analiz** | ______ | Veri yükleme, ön işleme, soru bazlı bölme, EDA grafikleri, uzunluğu eşitlenmiş test kümesi |
| **B – Modeller** | ______ | Baseline'lar (uzunluk, TF-IDF, Sentence Transformer), BERT ve DeBERTa fine-tuning, hiperparametre tablosu |
| **C – Değerlendirme ve Demo** | ______ | Metrikler, confusion matrix, ROC/PR eğrileri, hata analizi, Gradio demo |
| **Ortak** | Herkes | Literatür (kişi başı en az 4 makale), öneri formu, rapor, sunum |

## Faz 1 — Ara Değerlendirmeye Hazırlık (31 Ekim – 8 Kasım)

Öneri formu ve ilerleme değerlendirmesi: **9–13 Kasım haftası** (sınav haftası 16 Kasım).

| # | Görev | Rol | Bitiş | Durum |
|---|---|---|---|---|
| 1 | GitHub reposunu kur, herkesi collaborator ekle | Sena | 31 Eki | ⬜ |
| 2 | `01_veri_inceleme.ipynb` çalıştır, grafikleri `results/` altına kaydet | A | 1 Kas | ⬜ |
| 3 | Herkes notebook 01'i kendi Colab'ında çalıştırıp anlasın | Herkes | 2 Kas | ⬜ |
| 4 | Literatür: kişi başı 4 makale oku, `docs/literatur.md`'ye not düş (IEEE formatında) | Herkes | 4 Kas | ⬜ |
| 5 | Uzunluk baseline + TF-IDF baseline (`02_baselines.ipynb`) | B | 4 Kas | ⬜ |
| 6 | Uzunluğu eşitlenmiş test kümesinin tasarımı | A | 5 Kas | ⬜ |
| 7 | Metrik fonksiyonları (`src/metrics.py`), confusion matrix çizimi | C | 5 Kas | ⬜ |
| 8 | Öneri formu taslağı: Özgün Değer + Amaç/Hedefler | Ortak | 6 Kas | ⬜ |
| 9 | Öneri formu taslağı: Yöntem + Kaynaklar | Ortak | 7 Kas | ⬜ |
| 10 | Özet yazımı, son kontrol, ekip içi prova | Ortak | 8 Kas | ⬜ |

## Faz 2 — Ana Modeller (ara sınavlardan sonra)

| # | Görev | Rol |
|---|---|---|
| 11 | BERT-base cross-encoder fine-tuning | B |
| 12 | DeBERTa-v3-base cross-encoder fine-tuning | B |
| 13 | Sentence Transformer + MLP baseline | B |
| 14 | Tüm modellerin orijinal ve eşitlenmiş testte karşılaştırılması | C |
| 15 | Hata analizi: modelin yanıldığı örneklerin incelenmesi | A + C |

## Faz 3 — Demo, Rapor, Sunum

| # | Görev | Rol |
|---|---|---|
| 16 | Gradio demo (cümle bazlı skor gösterimi) | C |
| 17 | Proje raporu (mazeret haftası) | Ortak |
| 18 | Sunum hazırlığı ve prova | Ortak |

## Çalışma Kuralları

- Her iş ayrı bir commit; mesajlar Türkçe ve açık: `EDA: cevap uzunluğu histogramı eklendi`
- Notebook'lar numaralı: `01_`, `02_` … — sırayla çalışır
- `random_state=42` her yerde aynı (tekrarlanabilirlik)
- **Test kümesine** model seçerken bakılmaz, sadece en sonda bakılır
- Commit edilen her kod ekip tarafından çalıştırılıp test edilir
