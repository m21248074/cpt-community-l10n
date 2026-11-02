# Cisco Packet Tracer Community Localization Project 🚀

![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey?style=for-the-badge)

這是一個由社群發起的 **Cisco Packet Tracer (CPT)** 繁體中文翻譯計畫。我們的目標是提供準確、完整的繁體中文介面，讓學習網路技術不再受到語言隔閡的限制。

---

## 📢 參與翻譯 (How to Contribute)

翻譯檔為 Qt 的 `.ts` 格式，位於 [`zh-TW/Chinese Traditional.ts`](zh-TW/Chinese%20Traditional.ts)，原文範本為 `template.ts`。

1. Fork 本儲存庫。
2. 用 [Qt Linguist](https://doc.qt.io/qt-5/linguist-translators.html) 開啟 `zh-TW/Chinese Traditional.ts` 翻譯並標記為完成（也可直接編輯 XML 的 `<translation>`）。
3. 送出 Pull Request。

> [!TIP]
> 翻譯時請保留 `%1`、`&`、HTML 標籤等佔位符，並維持術語一致（盡量對齊 Cisco 官方繁中用語）。
> `tools/apply_duplicates.py` 可把已翻譯字串自動套用到原文相同的未翻項目。

---

## 🛠️ 安裝說明 (Installation)

如果你想在自己的 Packet Tracer 中使用目前的翻譯成果：

1. 前往本專案的 [Releases](../../releases) 頁面下載最新的 `.ptl` 檔案。
2. 將下載的檔案複製到 Packet Tracer 的安裝路徑：
   - **Windows:** `C:\Program Files\Cisco Packet Tracer X.X\languages`
   - **Linux:** `/opt/pt/languages`
3. 開啟 Packet Tracer，進入 **Options > Preferences > Interface**。
4. 在 **Languages** 清單中選擇該語言，並點擊 **Change Language**。
5. 重啟程式即可生效。

---

## 📅 更新維護

由於 CPT 版本更新頻繁，當官方發布新版本時：
1. 我們會將最新的 `template.ts` 上傳至此 Repo，並同步新增的字串到 `zh-TW` 翻譯檔。
2. 歡迎大家關注此專案以獲得最新進度。

---

## 🤝 貢獻者 (Contributors)

感謝所有參與翻譯的志工！

---

---

## 🧰 維護工具

- `tools/apply_duplicates.py`：把已翻譯字串套用到原文相同的未翻項目；`--prefer 原文=譯文` 可統一分歧譯名，`--dry-run` 只預覽。
- 術語與慣例請見 [docs/GLOSSARY.md](docs/GLOSSARY.md)。
- 本機編譯：`lrelease "zh-TW/Chinese Traditional.ts" -qm "Chinese Traditional.ptl"`。

## ⚖️ 免責聲明 (Disclaimer)

* 本專案為非官方發起，所有商標權歸 **Cisco Systems, Inc.** 所有。
* 翻譯內容僅供學習參考，不保證與官方術語完全一致。

---

**想協助我們改進翻譯？歡迎 Fork 後送出 Pull Request！**
