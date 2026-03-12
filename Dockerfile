# 使用輕量級 Python 映像檔 
FROM python:3.10-slim

# 設定容器內的工作目錄
WORKDIR /app

# 將本地的 api.py 複製到容器中
COPY api.py .

# 安裝必要的程式庫 [cite: 187]
RUN pip install requests

# 執行指令
CMD ["python", "api.py"]