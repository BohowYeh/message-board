# 練習
建造一個網路留言板，後端使用python，將留言者的各項資料從db資料庫存入或取出顯示在前端。

Sub GenerateMyPresentation()
    Dim ppt As Presentation
    Dim slide As slide
    Set ppt = ActivePresentation
    
    ' 第1頁：標題
    Set slide = ppt.Slides.Add(1, ppLayoutTitle)
    slide.Shapes(1).TextFrame.TextRange.Text = "個人優勢與待強化領域評估"
    slide.Shapes(2).TextFrame.TextRange.Text = "軟體工程師 — [你的名字]"
    
    ' 第2頁：強項一
    Set slide = ppt.Slides.Add(2, ppLayoutText)
    slide.Shapes(1).TextFrame.TextRange.Text = "強項 (1)：系統化思維與高效執行力"
    slide.Shapes(2).TextFrame.TextRange.Text = "• 釐清核心：執行前先確認真正的商業邏輯與問題本質。" & vbCrLf & _
                                               "• 任務拆解 (Breakdown)：將大功能拆解為可控的小步驟並排定優先級。" & vbCrLf & _
                                               "• 高效產出：透過扎實的前期規劃，確保寫 Code 速度快且精準對焦。"
                                               
    ' 第3頁：強項二
    Set slide = ppt.Slides.Add(3, ppLayoutText)
    slide.Shapes(1).TextFrame.TextRange.Text = "強項 (2)：獨立解決問題與精準提問技巧"
    slide.Shapes(2).TextFrame.TextRange.Text = "• 前期研究：遇技術瓶頸時，先獨立查閱文件與測試。" & vbCrLf & _
                                               "• 收斂問題：將模糊的困難具體化，整理出清晰的癥結點。" & vbCrLf & _
                                               "• 帶著解法發問：備妥「初步想法」再尋求協助，極大化溝通效率。"
                                               
    ' 第4頁：弱項一
    Set slide = ppt.Slides.Add(4, ppLayoutText)
    slide.Shapes(1).TextFrame.TextRange.Text = "弱項 (1)：技術概念的口語轉譯（跨背景溝通）"
    slide.Shapes(2).TextFrame.TextRange.Text = "• 現況認知：具備「程式腦」，但在向非技術人員解釋時，易產生溝通落差。" & vbCrLf & _
                                               "• 改善行動：" & vbCrLf & _
                                               "  - 練習跳脫純技術視角。" & vbCrLf & _
                                               "  - 運用「視覺化流程圖」輔助說明。" & vbCrLf & _
                                               "  - 嘗試使用「生活化比喻」進行技術轉譯。"
                                               
    ' 第5頁：弱項二
    Set slide = ppt.Slides.Add(5, ppLayoutText)
    slide.Shapes(1).TextFrame.TextRange.Text = "弱項 (2)：對產出結果的預期焦慮"
    slide.Shapes(2).TextFrame.TextRange.Text = "• 現況認知：求好心切，容易因擔心「開發成果未達預期」而產生壓力。" & vbCrLf & _
                                               "• 改善行動：" & vbCrLf & _
                                               "  - 導入「敏捷對焦」思維。" & vbCrLf & _
                                               "  - 在半成品階段提早展示進度。" & vbCrLf & _
                                               "  - 以「提高確認頻率」取代「盲目焦慮」，確保開發方向正確。"
End Sub

# 說明
一般使用者可以在留言板留言，admin做為管理者可以登入後台刪除或更改留言。各個使用者的留言資料都會存進資料庫db

# 展示
https://github.com/BohowYeh/message-board/assets/151061264/f72544f8-8ee6-4cc2-944d-9633a01e3b60

↑↑↑ 主頁面

<img src="https://github.com/BohowYeh/message-board/assets/151061264/ba8985c6-89da-4ebf-b277-4e7228b976ea" alt="IMG_3373" width="500" height="290">
<img src="https://github.com/BohowYeh/message-board/assets/151061264/60e6b721-6500-40e1-98b0-49b913d2a32e" alt="IMG_3373" width="500" height="290">

↑↑↑ admin管理頁面，登錄後可以管理留言

<img src="https://github.com/BohowYeh/message-board/assets/151061264/1d056747-20f6-438b-9d9f-ba2bc182d810" alt="IMG_3373" width="500" height="250">
<img src="https://github.com/BohowYeh/message-board/assets/151061264/5ed6fe65-596b-41de-8556-d13d07e0c51e" alt="IMG_3373" width="500" height="250">
↑↑↑ 資料庫保存各項數據



