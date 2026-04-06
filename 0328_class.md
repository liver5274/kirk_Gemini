# Filter 類別說明文件

## 概述

這是一個用於 Open WebUI 的過濾器（Filter）類別，主要功能是限制對話輪次數量，防止對話過長。

## 基本資訊

- **標題**: Example Filter
- **作者**: open-webui
- **版本**: 0.1
- **作者網址**: https://github.com/open-webui

## 類別結構

### Valves（系統級設定）

系統級別的配置參數：

- `priority` (int): 過濾器操作的優先級，預設值為 0
- `max_turns` (int): 系統允許的最大對話輪次，預設值為 8

### UserValves（使用者級設定）

使用者級別的配置參數：

- `max_turns` (int): 使用者允許的最大對話輪次，預設值為 4

## 主要方法

### `__init__()`

初始化方法，建立 Valves 實例來管理設定。

### `inlet(body: dict, __user__: Optional[dict] = None) -> dict`

**前處理器方法** - 在請求發送到 API 之前執行

**功能**:
- 驗證和修改請求內容
- 檢查對話輪次是否超過限制
- 記錄請求資訊（body 和 user）

**邏輯**:
1. 檢查使用者角色是否為 "user" 或 "admin"
2. 取得對話訊息列表
3. 計算有效的最大輪次（取使用者設定和系統設定的較小值）
4. 如果訊息數量超過限制，拋出例外

**參數**:
- `body`: 請求主體，包含對話訊息
- `__user__`: 使用者資訊，包含角色和個人設定

**回傳**: 修改後的請求主體

**例外**: 當對話輪次超過限制時，拋出 Exception

### `outlet(body: dict, __user__: Optional[dict] = None) -> dict`

**後處理器方法** - 在 API 回應後執行

**功能**:
- 分析或修改 API 回應
- 記錄回應資訊（body 和 user）
- 執行額外的檢查和分析

**參數**:
- `body`: 回應主體
- `__user__`: 使用者資訊

**回傳**: 修改後的回應主體

## 使用範例

### 對話輪次限制機制

系統會取使用者設定和系統設定中較小的值作為實際限制：

```python
max_turns = min(__user__["valves"].max_turns, self.valves.max_turns)
# 如果使用者設定 = 4，系統設定 = 8，則實際限制 = 4
```

### 錯誤訊息

當超過限制時，會顯示：
```
Conversation turn limit exceeded. Max turns: {max_turns}
```

## 注意事項

1. **檔案處理**: 程式碼中包含 `file_handler` 的註解說明，可以啟用自訂檔案處理邏輯
2. **權限控制**: 目前只對 "user" 和 "admin" 角色進行輪次限制
3. **除錯輸出**: inlet 和 outlet 方法都會印出詳細的請求/回應資訊，方便除錯

## 擴展建議

- 可以根據不同使用者角色設定不同的輪次限制
- 可以加入更多驗證邏輯，如內容過濾、敏感詞檢測等
- 可以在 outlet 方法中加入回應內容的後處理邏輯
